python -m pip install --quiet --no-input --disable-pip-version-check --upgrade pip
pip install --quiet --no-input --disable-pip-version-check --upgrade --upgrade-strategy eager setuptools wheel
pip install --quiet --no-input --disable-pip-version-check --upgrade --upgrade-strategy eager .[dev,test]
