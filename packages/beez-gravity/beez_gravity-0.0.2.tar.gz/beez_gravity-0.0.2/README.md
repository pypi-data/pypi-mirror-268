# GRAVITY

(General-purpose Runtime for Application Virtualization and IT Yield)

## Requirements

- loguru (for logging)
- pytest (for tests)
- twine (to publish on Pypi)

## Tests

```bash
pytest -s test/gravity_test.py
```

## Commands

```bash
gcc -shared -o add.so add.c
```

```bash
python3 setup.py sdist
```

```bash
twine upload dist/gravity-0.0.1.tar.gz
```
