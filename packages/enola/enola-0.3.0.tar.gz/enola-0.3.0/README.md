# enola-ai-python
Librería en python para instalar en python


para construir:
py -m build

para publicar:
https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-your-project-to-pypi

py -m pip --version
py -m pip install twine

frecuente:
py -m pip install build

twine upload dist/*

--para testing
py -m twine upload --repository testpypi dist/*

--para desarrollo
py -m twine upload --repository pypi dist/*