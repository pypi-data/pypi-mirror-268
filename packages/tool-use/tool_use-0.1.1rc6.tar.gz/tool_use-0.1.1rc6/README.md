# Promptflow-Tool-Use

- promptflow custom llm tool package for function calling mode and newer version of openai/azure deployment

## Pypi Installation

```bash
pip install tool-use
```

link : https://pypi.org/project/tool-use/0.1.0/

## Contribution Guideline

```bash
make pre-commit
pip install wheel twine
python setup.py sdist bdist_wheel
twine upload dist/*
```
