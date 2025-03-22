clear
python3 -m venv .venv --clear
source .venv/bin/activate
pip install -U setuptools wheel mypy pytest pytest-cov pylint black
pip install -U .