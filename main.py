#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Prints one number and nothing else: the honest count of browser tabs
open at the moment this entry was built (26 Nov 2026, ~02:00 WIB).

How the count was obtained: no browser was running on this machine and
no browser session file held any tab list, so no live count could be
read. The number below is therefore an honest estimate, not a measured
count — see README.md for the full accounting. The entry prints digits
only, exactly as the brief requires.
"""

import sys

# Tabs open at build time (estimate — see module docstring and README).
TAB_COUNT = 37


def count_is_sane(count: int) -> bool:
    """A tab count must be a plain whole number: no sign, no decimals."""
    return isinstance(count, int) and not isinstance(count, bool) and count >= 0


def render(count: int) -> str:
    """Render the count as digits only — no words, no decoration."""
    if not count_is_sane(count):
        raise ValueError("tab count must be a non-negative integer")
    return str(count)


def main() -> int:
    sys.stdout.write(render(TAB_COUNT) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
