::: mkdocs-click
    :module: demisto_sdk.__main__
    :command: validate

Makes sure your content repository files are in order and have valid yml file scheme.

### Notes

In order to run the README validator:

- Node should be installed on you machine
- The modules '@mdx-js/mdx', 'fs-extra', 'commander' should be installed in node-modules folder.
    If not installed, the validator will print a warning with the relevant module that is missing.
    please install it using "npm install *missing_module_name*"
- 'DEMISTO_README_VALIDATION' environment variable should be set to True.
    To set the environment variables, run the following shell commands:
    export DEMISTO_README_VALIDATION=True

In case of a private repo and an un-configured 'DEMISTO_SDK_GITHUB_TOKEN' validation of version bumps in files will be done with the local remote git branch.

### Use cases

This command is used to make sure that the content repo files are valid and are able to be processed by Demisto.
This is used in our validation process both locally and in Circle CI.

### Examples

`demisto-sdk validate -g --no-backwards-comp`
This will validate only changed files from content origin/master branch and will exclude backwards
compatibility checks.

`demisto-sdk validate -j`
This will validate all content repo files and including conf.json file.

`demisto-sdk validate --prev-ver SHA1-HASH`
This will validate only changed files from the branch given (SHA1).

`demisto-sdk validate --post-commit`
This indicates that the command runs post commit.

`demisto-sdk validate -i Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.yml`
This will validate the file Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.yml only.

`demisto-sdk validate -a`
This will validate all files under `Packs` directory

`demisto-sdk validate -i Packs/HelloWorld`
This will validate all files under the content pack `HelloWorld`

### Error Codes and Ignoring Them

Starting in version 1.0.9 of Demisto-SDK, each error found by validate (excluding `pykwalify` errors) has an error
code attached to it - the code can be found in brackets preceding the error itself.
For example: `path/to/file: [IN103] - The type field of the proxy parameter should be 8`

The first 2 letters indicate the error type and can be used to easily identify the cause of the error.
| Code | Type |
| --- | --- |
| BA | Basic error |
| BC | Backwards compatibility error |
| CJ | Conf json error |
| CL | Classifier error |
| DA | Dashboard error |
| DB | DBootScore error |
| DO | Docker error |
| DS | Description error |
| ID | Id set error |
| IF | Incident field or type error |
| IM | Image error |
| IN | Integration or script error |
| IT | Incident type error |
| MA | Mapper error |
| PA | Pack files error (pack-metadata, pack-secrets, pack-ignore) |
| PB | Playbook error |
| RM | Readme error |
| RN | Release notes error |
| RP | Reputation error |
| SC | Script error |
| ST | Structure error |
| WD | Widget error |

If you wish to ignore errors for a specific file in the pack insert the following to the `pack-ignore` file.

```buildoutcfg
[file:FILE_NAME]
ignore=BA101
```

*Note*: Currently only `BA101` is ignorable.
