# itkwasm-morphological-contour-interpolation-emscripten

[![PyPI version](https://badge.fury.io/py/itkwasm-morphological-contour-interpolation-emscripten.svg)](https://badge.fury.io/py/itkwasm-morphological-contour-interpolation-emscripten)

Morphology-based approach for interslice interpolation of anatomical slices from volumetric images. Emscripten implementation.

This package provides the Emscripten WebAssembly implementation. It is usually not called directly. Please use the [`itkwasm-morphological-contour-interpolation`](https://pypi.org/project/itkwasm-morphological-contour-interpolation/) instead.


## Installation

```sh
import micropip
await micropip.install('itkwasm-morphological-contour-interpolation-emscripten')
```

## Development

```sh
pip install hatch
hatch run download-pyodide
hatch run test
```
