<a href="https://www.islas.org.mx/"><img src="https://www.islas.org.mx/img/logo.svg" align="right" width="256" /></a>
# Container runner

![example branch
parameter](https://github.com/IslasGECI/container_runner/actions/workflows/actions.yml/badge.svg)
![licencia](https://img.shields.io/github/license/IslasGECI/container_runner)
![languages](https://img.shields.io/github/languages/top/IslasGECI/container_runner)
![commits](https://img.shields.io/github/commit-activity/y/IslasGECI/container_runner)
![PyPI - Version](https://img.shields.io/pypi/v/container_runner)

Para usar este repo como plantilla debemos hacer lo siguiente:

1. Presiona el botón verde que dice _Use this template_
1. Selecciona como dueño a la organización IslasGECI
1. Agrega el nombre del nuevo módulo de python
1. Presiona el botón _Create repository from template_
1. Reemplaza `container_runner` por el nombre del nuevo módulo en:
    - `Makefile`
    - `pyproject.toml`
    - `tests\test_transformations.py`
1. Renombra el archivo `container_runner\transformations.py` al nombre del primer archivo del
   nuevo módulo
1. Cambia la descripción del archivo `container_runner\__init__.py`
1. Renombra el directorio `container_runner` al nombre del nuevo módulo
1. Cambia el `codecov_token` del archivo `Makefile`

Los archivos del nuevo módulo los agregarás en la carpeta que antes se llamaba
`container_runner` y las pruebas en la carpeta `tests`.
