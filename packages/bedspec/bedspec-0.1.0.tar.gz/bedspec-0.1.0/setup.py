# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bedspec', 'cgranges', 'cgranges.test']

package_data = \
{'': ['*'],
 'cgranges': ['cpp/*', 'python/*'],
 'cgranges.test': ['3rd-party/*',
                   '3rd-party/AIList/*',
                   '3rd-party/AITree/*',
                   '3rd-party/NCList/*']}

setup_kwargs = {
    'name': 'bedspec',
    'version': '0.1.0',
    'description': 'An HTS-specs compliant BED toolkit.',
    'long_description': '# bedspec\n\n[![PyPi Release](https://badge.fury.io/py/bedspec.svg)](https://badge.fury.io/py/bedspec)\n[![CI](https://github.com/clintval/bedspec/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/clintval/bedspec/actions/workflows/tests.yml?query=branch%3Amain)\n[![Python Versions](https://img.shields.io/badge/python-3.12-blue)](https://github.com/clintval/bedspec)\n[![MyPy Checked](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)\n[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://docs.astral.sh/ruff/)\n\nAn HTS-specs compliant BED toolkit.\n\n## Installation\n\nThe package can be installed with `pip`:\n\n```console\npip install bedspec\n```\n\n## Quickstart\n\n### Writing\n\n```python\nfrom bedspec import BedWriter, Bed3\n\nbed = Bed3("chr1", start=2, end=8)\n\nwith BedWriter(open("test.bed", "w")) as writer:\n    writer.write(bed)\n```\n\n### Reading\n\n```python\nfrom bedspec import BedReader, Bed3\n\nwith BedReader[Bed3](open("test.bed")) as reader:\n    for bed in reader:\n        print(bed)\n```\n```console\nBed3(contig="chr1", start=2, start=8)\n```\n\n### BED Types\n\nThis package provides pre-defined classes for the following BED formats:\n\n```python\nfrom bedspec import Bed2\nfrom bedspec import Bed3\nfrom bedspec import Bed4\nfrom bedspec import Bed5\nfrom bedspec import Bed6\nfrom bedspec import BedPE\n```\n\n### Custom BED Types\n\nCreating custom records is as simple as inheriting from the relevent BED-type:\n\n| Type        | Description                                         |\n| ---         | ---                                                 |\n| `PointBed`  | BED ecords that are a single point (1-length) only. |\n| `SimpleBed` | BED ecords that are a single interval.              |\n| `PairBed`   | BED ecords that are a pair of intervals.            |\n\nFor example, to create a custom BED3+1 class:\n\n```python\nfrom dataclasses import dataclass\n\nfrom bedspec import SimpleBed\n\n@dataclass\nclass MyCustomBed(SimpleBed):\n    contig: str\n    start: int\n    end: int\n    my_custom_field: float\n```\n\n## Development and Testing\n\nSee the [contributing guide](./CONTRIBUTING.md) for more information.\n',
    'author': 'Clint Valentine',
    'author_email': 'valentine.clint@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/clintval/bedspec',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.12,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
