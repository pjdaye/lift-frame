import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "taxonomy" / "lift.yaml"
SCHEMA = ROOT / "taxonomy" / "schemas" / "lift.schema.json"

def main() -> int:
    data = yaml.safe_load(TAXONOMY.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

    if errors:
        print("❌ LIFT taxonomy validation failed:")
        for e in errors:
            path = ".".join([str(p) for p in e.path]) or "<root>"
            print(f" - {path}: {e.message}")
        return 1

    print("✅ LIFT taxonomy validation passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
