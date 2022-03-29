# Python középhaladó oktatás

* Hozzuk létre a `venv` könyvtárat:

```shell
python -m venv venv
```

```shell
pip install -r requirements.txt
```

```shell
git init
```

```shell
pytest  --cov . --cov-report=html
```

```shell
mypy .
```

```shell
autopep8 -a -i type_hint_demo.py
```

## Docker

```shell
docker build -t hello-python .
docker run hello-python
```