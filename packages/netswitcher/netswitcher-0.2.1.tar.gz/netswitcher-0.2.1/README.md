# netswitcher (nt)

```console
Usage: nt [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  acl
  lacp
  speed
  state
  status
```

## Installation
```console
git clone https://github.com/Fearkin/netswitcher

poetry install
```
## Usage:
**`nt acl` [action]** - команда для работы с ACL

Name of interface should be ge-(0-9)/(0-9)/(0-9)

- add     *ACL_name* *interface_name* - Adds ACL rule with given name to interface

- create  *name* IP - Creates ACL rule with given name

- delete  *name* IP - Deletes IP from ACL with given name

- find    *name* - Shows ACL with given name

- prune   *name* - Deletes ACL rule with given name

- remove  *ACL_name* *interface_name* - Removes ACL rule with given name from interface


**`nt status` [action]** - команда для проверки интерфейсов

- int   *name* - Shows current state of interface

- lacp  *name* - Shows active LACP with given name and all created LACP

- show  *name* OR show --mac *MAC* - Shows current configuration of interface


**`nt speed` [action]** - команда для изменения скорости

- desc  *name* *description* - Set description for interface

- set   *name* *speed* (10m|100m|1g) - Set speed for interface

**`nt lacp` [action]** - команда для работы с LACP


- create  *port (0-9)* *description* *interface1* *interface2* - Creates LACP

- delete  *port (0-9)* - Deletes LACP

- remove  *name* - Removes interface from LACP

**`nt state` on/off *name*** - включить/выключить интерфейс
