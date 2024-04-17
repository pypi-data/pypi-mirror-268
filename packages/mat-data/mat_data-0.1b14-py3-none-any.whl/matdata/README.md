# MAT-data: Data Preprocessing for Multiple Aspect Trajectory Data Mining \[MAT-Tools Framework\]
---

\[[Publication](#)\] \[[citation.bib](citation.bib)\] \[[GitHub](https://github.com/ttportela/mat-data)\] \[[PyPi](https://pypi.org/project/mat-data/)\]


The present package offers a tool, to support the user in the task of data preprocessing of multiple aspect trajectories, or to generating synthetic datasets. It integrates into a unique framework for multiple aspects trajectories and in general for multidimensional sequence data mining methods.

Created on Dec, 2023
Copyright (C) 2023, License GPL Version 3 or superior (see LICENSE file)

### Main Modules

- [proprocess](/proprocess.py): Methods for trajectory preprocessing;
- [generator](/generator.py): Methods for trajectory datasets generation;
- [datasets](/datasets.py): Methods for loading trajectory datasets.


### Installation

Install directly from PyPi repository, or, download from github. (python >= 3.7 required)

```bash
    pip install mat-data
```

### Getting Started

On how to use this package, see [MAT-data-Tutorial.ipynb](https://github.com/ttportela/mat-data/blob/main/MAT-data-Tutorial.ipynb) (or the HTML [MAT-data-Tutorial.html](https://github.com/ttportela/mat-data/blob/main/MAT-data-Tutorial.html))

### Citing

If you use `mat-data` please cite the following paper (this package is fragmented from `automatize` realease):

    Portela, Tarlis Tortelli; Bogorny, Vania; Bernasconi, Anna; Renso, Chiara. AutoMATise: Multiple Aspect Trajectory Data Mining Tool Library. 2022 23rd IEEE International Conference on Mobile Data Management (MDM), 2022, pp. 282-285, doi: 10.1109/MDM55031.2022.00060.

Bibtex:
```bash
@inproceedings{Portela2022automatise,
    title={AutoMATise: Multiple Aspect Trajectory Data Mining Tool Library},
    author={Portela, Tarlis Tortelli and Bogorny, Vania and Bernasconi, Anna and Renso, Chiara},
    booktitle = {2022 23rd IEEE International Conference on Mobile Data Management (MDM)},
    volume={},
    number={},
    address = {Online},
    year={2022},
    pages = {282--285},
    doi={10.1109/MDM55031.2022.00060}
}
```

### Collaborate with us

Any contribution is welcome. This is an active project and if you would like to include your code, feel free to fork the project, open an issue and contact us.

Feel free to contribute in any form, such as scientific publications referencing this package, teaching material and workshop videos.

### Related packages

This package is part of _MAT-Tools Framework_ for Multiple Aspect Trajectory Data Mining:

- [automatize](https://github.com/ttportela/automatize): automatize for experimental evaluation of MAT classification
- [movelets](https://github.com/ttportela/movelets): movelets for MAT classification methods (based on movelets)
- [mat-data](https://github.com/ttportela/mat-data): mat-data is a preprocessing library for MAT data
- [mat-analysis](https://github.com/ttportela/mat-analysis): mat-analysis for MAT classification methods
- [mat-view](https://github.com/ttportela/mat-view): mat-view for MAT and movelets visualization, and interpratation tools

### Change Log

This is a package under construction, see [CHANGELOG.md](./CHANGELOG.md)
