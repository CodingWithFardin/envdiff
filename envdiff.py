#!/usr/bin/env python3
"""envdiff - compare two dotenv files, reporting key-level changes."""
import argparse
import sys


def load(path):
    values = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key = key.strip()
            if key.startswith("export "):
                key = key[7:].strip()
            val = val.strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            values[key] = val
    return values


def diff(old, new):
    return {
        "added": sorted(set(new) - set(old)),
        "removed": sorted(set(old) - set(new)),
        "changed": sorted(k for k in set(old) & set(new) if old[k] != new[k]),
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="envdiff", description=__doc__)
    ap.add_argument("old")
    ap.add_argument("new")
    ap.add_argument("--show-values", action="store_true")
    args = ap.parse_args(argv)
    old, new = load(args.old), load(args.new)
    d = diff(old, new)
    for key in d["added"]:
        print("+ %s%s" % (key, ("=" + new[key]) if args.show_values else ""))
    for key in d["removed"]:
        print("- %s" % key)
    for key in d["changed"]:
        if args.show_values:
            print("~ %s: %r -> %r" % (key, old[key], new[key]))
        else:
            print("~ %s" % key)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
