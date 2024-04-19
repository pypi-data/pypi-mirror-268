# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tensorcat']

package_data = \
{'': ['*']}

install_requires = \
['iPython>=8.4.0,<9.0.0', 'numpy>=1.22.4,<2.0.0', 'pillow>=9.5.0,<10.0.0']

entry_points = \
{'console_scripts': ['tensorcat = tensorcat.cli:main']}

setup_kwargs = {
    'name': 'tensorcat',
    'version': '0.1.1',
    'description': '',
    'long_description': '# TensorCat\n\nThis utility provides a unified interface to display an image/tensor/array in terminal, notebook and python debugger (pdb, ipdb). It utilizes the iTerm2 Inline Images Protocol to display an image inline. This protocol is also implemented by VSCode. To display image inside terminal, you need to use iTerm2 or the VSCode terminal with `terminal.integrated.enableImages` setting enabled.\n\n## Usage\n\n### Terminal (CLI)\n```\npython -m tensorcat.cli /path/to/img.png\ntensorcat /path/to/img.png\n```\n\n### Python API (Can be used in Python Debugger or iPython Notebook)\n```\nfrom tensorcat import tensorcat\nimport torch\n \nimg = th.randn(4, 3, 32, 32)\ntensorcat(img)\n```\n',
    'author': 'Zhengyu Yang',
    'author_email': '25852061+zhengyu-yang@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
