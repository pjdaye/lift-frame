# FRAME

FRAME is a practical lens for defining correctness in non-deterministic systems.

## Core idea

A system is correct if it produces an outcome that lies within an allowed set under stated constraints **and** can provide evidence that the constraints were met.

In deterministic software, the allowed set may be a singleton. In non-deterministic systems, it is a region.
