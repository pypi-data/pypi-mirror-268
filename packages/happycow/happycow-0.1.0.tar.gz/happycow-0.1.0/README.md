# happycow

This is a demo project for poetry, upload to PyPI, github action, etc

```python
conda create --name happycow python=3.10
conda activate happycow
# conda install pipx
# pipx install poetry
poetry new happycow
cd happycow
git init
# .gitignore copy from https://github.com/github/gitignore/blob/main/Python.gitignore
git add .gitignore
git commit -m "add gitignore"
# modify code
git add .
git commit -m "add code"
poetry install
poetry run pytest
```