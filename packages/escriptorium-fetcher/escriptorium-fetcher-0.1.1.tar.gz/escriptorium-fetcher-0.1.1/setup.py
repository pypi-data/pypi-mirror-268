# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['escriptorium_fetcher']

package_data = \
{'': ['*']}

install_requires = \
['escriptorium-connector>=0.2.6,<0.3.0',
 'rich>=13.7.0,<14.0.0',
 'srsly>=2.4.8,<3.0.0',
 'typer[all]>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['fetcher = escriptorium_fetcher.main:app']}

setup_kwargs = {
    'name': 'escriptorium-fetcher',
    'version': '0.1.1',
    'description': '',
    'long_description': '# 🐕 escriptorium-fetcher 🐕\nA CLI for downloading data from an eScriptorium server.\n\n\n### Installation\n```bash\npip install escriptorium-fetcher\n```\n\n### Usage\n```bash\n$ fetcher\n```\nYou will be prompted to select a project to fetch. Enter the number next to the project that you would like to fetch and press enter. For example, if you would like to fetch the first project, enter the following and press enter:\n```bash\n0 initial_batch-2024-02-21\n1 another_project-2024-02-21\n🐾 Select a project to fetch: 0\n```\nBy default, fetcher downloads images and transcriptions. You need to select which transcription you want to download. Enter the number next to the transcription that you would like to fetch and press enter. For example, if you would like to fetch the first transcription, enter the following and press enter:\n```bash\n0 vision\n1 manual\nPlease select a transcription to fetch: 0\n```\n\nThe first time that you run the script you will be prompted to enter:\n- the url of the eScriptorium server\n- your username for the eScriptorium server\n- your password for the eScriptorium server\n- a local path to save the image files\n- a local path to save the transcription files (ALTO xml)\n\nTo clear  your settings and start over, run:\n```bash\n$ fetcher --clear-secrets\n```\nIf you do not want to download images or transcriptions, you can use the `--no-images` or `--no-transcriptions` flags. For example:\n```bash\n$ fetcher --no-images\n```',
    'author': 'apjanco',
    'author_email': 'apjanco@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
