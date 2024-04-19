# How to publish to PyPI

1) Update the version number in `xmipy/__init__.py`.

2) Make a new commit with the updated version number,
and push to remote

3) Make a new github release

4) Publish to PyPI:
```
pixi run publish-build
```
