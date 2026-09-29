import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tools" / "skill_sync_manifest.yaml"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def yaml_version(path: Path) -> str | None:
    """Best-effort read of a top-level 'version' key, for a friendlier error
    message on taxonomy.yaml specifically. Returns None for non-YAML files
    or files without a version key — callers must not treat None as a match."""
    if path.suffix not in (".yaml", ".yml"):
        return None
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError:
        return None
    return data.get("version") if isinstance(data, dict) else None


def main() -> int:
    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    problems: list[str] = []
    checked = 0

    for pair in manifest["pairs"]:
        canonical = ROOT / pair["canonical"]
        if not canonical.is_file():
            problems.append(f"canonical file missing: {pair['canonical']}")
            continue

        canonical_hash = sha256(canonical)
        canonical_version = yaml_version(canonical)

        for bundled_rel in pair["bundled"]:
            checked += 1
            bundled = ROOT / bundled_rel
            if not bundled.is_file():
                problems.append(f"bundled file missing: {bundled_rel}")
                continue

            if sha256(bundled) == canonical_hash:
                continue

            # Drifted — give the most specific message we can.
            bundled_version = yaml_version(bundled)
            if canonical_version is not None and bundled_version is not None and canonical_version != bundled_version:
                problems.append(
                    f"{bundled_rel} is out of sync with {pair['canonical']} "
                    f"(bundled version '{bundled_version}' != canonical version '{canonical_version}')"
                )
            else:
                problems.append(
                    f"{bundled_rel} is out of sync with {pair['canonical']} (content differs)"
                )

    if problems:
        print(f"❌ Skill bundle sync check failed ({len(problems)} of {checked} bundled files out of sync):")
        for p in problems:
            print(f" - {p}")
        print("\nFix: copy the canonical file over each listed bundled file, or update the manifest")
        print("if the drift is intentional. See skills/README.md and tools/skill_sync_manifest.yaml.")
        return 1

    print(f"✅ Skill bundle sync check passed ({checked} bundled files match their canonical source).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
