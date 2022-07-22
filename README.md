# ape-is-array-error-repro

Covers a bug with ape. The regex pattern used for checking if a returned data type is array or not does not cover `uint256[20]` at least (and maybe more?).

To install:

```
python -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
```

To reproduce this issue:

```
ape test
```

All tests should pass, which means you reproduced the issue.
