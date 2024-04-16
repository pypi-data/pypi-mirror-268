# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['core']

package_data = \
{'': ['*']}

install_requires = \
['netmiko>=4.3.0,<5.0.0', 'typer-slim>=0.12.3,<0.13.0']

entry_points = \
{'console_scripts': ['nt = core.main:create_app']}

setup_kwargs = {
    'name': 'netswitcher',
    'version': '0.2.0',
    'description': '',
    'long_description': '# netswitcher (nt)\n\n```console\nUsage: nt [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n  --help                          Show this message and exit.\n\nCommands:\n  acl\n  lacp\n  speed\n  state\n  status\n```\n\n## Installation\n```console\npip install nt\n```\n\nor\n\n```console\ngit clone https://github.com/Fearkin/netswitcher/tree/master\n\npoetry install\n```\n## Usage:\n**`nt acl` [action]** - команда для работы с ACL\n\nName of interface should be ge-(0-9)/(0-9)/(0-9)\n\n- add     *ACL_name* *interface_name* - Adds ACL rule with given name to interface\n\n- create  *name* IP - Creates ACL rule with given name\n\n- delete  *name* IP - Deletes IP from ACL with given name\n\n- find    *name* - Shows ACL with given name\n\n- prune   *name* - Deletes ACL rule with given name\n\n- remove  *ACL_name* *interface_name* - Removes ACL rule with given name from interface\n\n\n**`nt status` [action]** - команда для проверки интерфейсов\n\n- int   *name* - Shows current state of interface\n\n- lacp  *name* - Shows active LACP with given name and all created LACP\n\n- show  *name* OR show --mac *MAC* - Shows current configuration of interface\n\n\n**`nt speed` [action]** - команда для изменения скорости\n\n- desc  *name* *description* - Set description for interface\n\n- set   *name* *speed* (10m|100m|1g) - Set speed for interface\n\n**`nt lacp` [action]** - команда для работы с LACP\n\n\n- create  *port (0-9)* *description* *interface1* *interface2* - Creates LACP\n\n- delete  *port (0-9)* - Deletes LACP\n\n- remove  *name* - Removes interface from LACP\n\n**`nt state` on/off *name*** - включить/выключить интерфейс\n',
    'author': 'Fearkin',
    'author_email': 'aloneWorker@yandex.ru',
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
