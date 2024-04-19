Python wrappers for Ordinals
============================

This project provides Python wrappers for [ord](https://github.com/ordinals/ord) internals.

The project is very much WIP. Currently, only wrappers for structs and functions related to Runes are provided.

The philosophy is to wrap `ord` internal structs as thinly as possible inside pyo3-compatible Rust, and to
provide sane methods on top of them to enable use in Python.

## Development

```bash
# python3.10 needs to be in PATH
make develop  # creates a venv and installs `pyord` inside it
make test  # test using pytest
```

## Building wheels

```bash
make build
```
