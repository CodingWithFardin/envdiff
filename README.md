# envdiff

Compare two .env files and report added, removed, changed keys.

```
python envdiff.py .env.old .env.new
```

## layout

- `envdiff.py`
- `tests/test_envdiff.py`  — tests

## use

Runs on 3.11 and newer.

```
git clone https://github.com/CodingWithFardin/envdiff.git
cd envdiff
```

Tests: `tests/test_envdiff.py`. A change that breaks one is usually the wrong change.

MIT, 2026.
