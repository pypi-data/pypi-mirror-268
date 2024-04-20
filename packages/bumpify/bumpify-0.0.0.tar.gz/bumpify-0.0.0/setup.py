# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bumpify',
 'bumpify.core',
 'bumpify.core.api',
 'bumpify.core.config',
 'bumpify.core.console',
 'bumpify.core.filesystem',
 'bumpify.core.semver',
 'bumpify.core.vcs',
 'bumpify.core.vcs.implementation',
 'bumpify.delivery',
 'bumpify.delivery.cli',
 'bumpify.di']

package_data = \
{'': ['*']}

install_requires = \
['click-help-colors>=0.9.4,<0.10.0',
 'click>=8.1.7,<9.0.0',
 'colorama>=0.4.6,<0.5.0',
 'pydantic>=2.6.3,<3.0.0',
 'pydio>=0.4.1,<0.5.0',
 'tomlkit>=0.12.4,<0.13.0']

entry_points = \
{'console_scripts': ['bumpify = bumpify.delivery.cli.__main__:main']}

setup_kwargs = {
    'name': 'bumpify',
    'version': '0.0.0',
    'description': 'Semantic versioning automation tool for software projects',
    'long_description': "# Bumpify\n\nSemantic versioning automation tool for software projects.\n\n## About\n\nBumpify is a CLI tool that analyzes VCS changelog of your project and generates\nnext semantic version of it. Despite the fact that the tool is written in\nPython, it can be used to automate versioning of any project, written in any\nlanguage, and any technology.\n\nBumpify works with conventional commits, as defined here:\n\nhttps://www.conventionalcommits.org/en/v1.0.0/\n\nAnd follows semantic versioning rules that can be found here:\n\nhttps://semver.org/\n\n## Installation\n\n### Using ``pip``\n\nThis is recommended option if you want to use this tool only inside your\nvirtual Python environment as a development dependency of the project you work\non:\n\n```\n$ pip install bumpify\n```\n\n### Using ``pipx``\n\nThis is recommended option if you want this tool to be available system wide:\n\n```\n$ pipx install bumpify\n```\n\n## Usage\n\n### Creating initial configuration\n\nBumpify reads its configuration from a configuration file, that by default will\nbe created inside project's root directory and named ``.bumpify.toml``.\n\nTo create initial configuration for your project, proceed to the root directory\nof your project and type:\n\n```\n$ bumpify init\n```\n\nThat command will interactively guide you through the process of creating\ninitial configuration file.\n\nAlternatively, you can also take a look at config file that Bumpify itself is\nusing:\n\nhttps://github.com/mwiatrzyk/bumpify/blob/main/.bumpify.toml\n\nYes, Bumpify is also versioned with Bumpify :-)\n\n### Create a new version\n\nOnce the project is configured, you can start using the tool. To bump the\nversion and create new release just run following command:\n\n```\n$ bumpify bump\n```\n\nThe ``bump`` command will, among other things, do following:\n\n1. Check if version tags are present.\n2. Create initial version in no version tags are found.\n3. Create next version if version tags are found. The new version is calculated\n   by analyzing VCS changelog between last version and VCS repository HEAD.\n   Only **conventional commits** are currently taken into account, all other\n   formats are ignored.\n4. Write new version to all configured **version files**.\n5. Create or update all configured **changelog files**.\n6. Create so called **bump commit** and add all modified files to it.\n7. Tag the bump commit with a **version tag**.\n\nBumpify will not push the commit and the tag to the upstream; you will have to\ndo it on your own, as this is out of scope of Bumpify.\n\nI strongly recommend calling ``bumpify bump`` from one of the final CI steps of\nyour project.\n\n## Glossary\n\n### Conventional commit\n\nA normalized format of a commit message that can be later parsed by tools like\nBumpify and interpreted accordingly.\n\nHere's an example:\n\n    feat: add support for Markdown changelog\n\nThanks to conventional commits Bumpify knows what changes are breaking changes,\nwhat are new features, and what are bug fixes. Based on that the tool can\ncalculate next version and generate changelog.\n\nCheck here for more details:\n\nhttps://www.conventionalcommits.org/en/v1.0.0/\n\n### Version file\n\nProject's file containing project's version string. Version files are used to\nstore project's version value, which must be adjusted on each version bump.\nThere can be several such files inside a project and all should be known to\nBumpify to avoid version integrity problems.\n\n### Changelog file\n\nThe file with release history of the project.\n\nIt is automatically created or updated on each version bump. Bumpify can create\nseveral changelog files, with different formats.\n\nCurrently supported changelog file formats are Markdown and JSON.\n\n### Bump commit\n\nA commit created once version was bumped with message containing information\nabout previous and new version. For example:\n\n```\nbump: 0.1.0 -> 0.2.0\n```\n\nThe format of a bump commit can be changed in the config file.\n\n### Version tag\n\nEach bump commit is tagged with a version tag. For example:\n\n```\nv1.2.3\n```\n\nThe format of this tag can be changed in the config file.\n\n## License\n\nThe project is licensed under the terms of the MIT license.\n\n## Author\n\nMaciej Wiatrzyk <maciej.wiatrzyk@gmail.com>\n",
    'author': 'Maciej Wiatrzyk',
    'author_email': 'maciej.wiatrzyk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mwiatrzyk/bumpify',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
