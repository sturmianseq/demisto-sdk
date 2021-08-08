[![PyPI version](https://badge.fury.io/py/demisto-sdk.svg)](https://badge.fury.io/py/demisto-sdk)
[![CircleCI](https://circleci.com/gh/demisto/demisto-sdk/tree/master.svg?style=svg)](https://circleci.com/gh/demisto/demisto-sdk/tree/master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/ppwwyyxx/OpenPano.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/demisto/demisto-sdk/context:python)
[![Coverage Status](https://coveralls.io/repos/github/demisto/demisto-sdk/badge.svg)](https://coveralls.io/github/demisto/demisto-sdk)

# Demisto SDK

The Demisto SDK library can be used to manage your Demisto content with ease and efficiency.
The library uses python 3.7+.

## Usage

### Installation

* **Install** - `pip3 install demisto-sdk`

* **Upgrade** - `pip3 install --upgrade demisto-sdk`

* **Demisto server demisto-sdk integration**

In order that demisto-sdk and Demisto server communicate, perfrom the following steps:

* Get an API key for Demisto-server - `Settings` -> `Integrations` -> `API keys` -> `Get your Key` (copy it, you will be to copy it once)

* Add the following parameters to `~/.zshrc` and `~/.bash_profile`:

   ```bash
   export DEMISTO_BASE_URL=<http or https>://<demisto-server url or ip>:<port>
   export DEMISTO_API_KEY=<API key>
   ```

* Reload your terminal before continue.

---

### CLI usage

You can use the SDK in the CLI as follows:

```bash
demisto-sdk <command> <args>
```

For more information, run `demisto-sdk -h`.
For more information on a specific command execute `demisto-sdk <command> -h`.

### Version Check

`demisto-sdk` will check against the GitHub repository releases for a new version every time it runs and will issue a warning if you are not using the latest and greatest. If you wish to skip this check you can set the environment variable: `DEMISTO_SDK_SKIP_VERSION_CHECK`. For example:

```bash
export DEMISTO_SDK_SKIP_VERSION_CHECK=yes
```

---

### Customizable command configuration

You can create your own configuration for the `demisto-sdk` commands by creating a file named `.demisto-sdk-conf` within the directory from which you run the commands.
This file will enable you to set a default value to the existing command flags that will take effect whenever the command is run.
This can be done by entering the following structure into the file:

```buildoutcfg
[command_name]
flag_name=flag_default_value
```

Note: Make sure to use the flag's full name and input `_` instead of a `-` if it exists in the flag name (e.g. instead of `no-docker-checks` use `no_docker_checks`).

Here are a few examples:

* As a user, I would like to not use the `mypy` linter in my environment when using the `lint` command. In the `.demisto-sdk-conf` file I'll enter:

```toml
[lint]
no_mypy=true
```

* As a user, I would like to include untracked git files in my validation when running the `validate` command. In the `.demisto-sdk-conf` file I'll enter:

```toml
[validate]
include_untracked=true
```

* As a user, I would like to automatically use minor version changes when running the `update-release-notes` command. In the `.demisto-sdk-conf` file I'll enter:

```toml
[update-release-notes]
update_type=minor
```

---

### How to setup development environment?

Follow the guide found [here](CONTRIBUTION#2-install-demisto-sdk-dev-environment) to setup your `demisto-sdk-dev` virtual environment.
The development environment is connected to the branch you are currently using in the SDK repository.

Simply activate it by running `workon demisto-sdk-dev`.
The virtual environment can be deactivated at all times by running `deactivate`.

---

### Autocomplete

Our CLI supports autocomplete for Linux/MacOS machines, you can turn this feature on by running one of the following:
for zsh users run in the terminal

```bash
eval "$(_DEMISTO_SDK_COMPLETE=source_zsh demisto-sdk)"
```

for regular bashrc users run in the terminal

```bash
eval "$(_DEMISTO_SDK_COMPLETE=source demisto-sdk)"
```

---

## License

MIT - See [LICENSE](LICENSE) for more information.

---

## Contributions

Contributions are welcome and appreciated.\
For information regarding contributing, press [here](CONTRIBUTION).
For release guide, press [here](release_guide.md)
