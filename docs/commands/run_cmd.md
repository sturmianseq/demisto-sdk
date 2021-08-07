---
id: run-cmd
title: run-cmd
---

::: mkdocs-click
    :module: demisto_sdk.__main__
    :command: run
    :prog_name: demisto-sdk run

In order to run the command, `DEMISTO_BASE_URL` environment variable should contain the Cortex XSOAR base URL, and `DEMISTO_API_KEY` environment variable should contain a valid Demisto API Key.
To set the environment variables, run the following shell commands:

```bash
export DEMISTO_BASE_URL=<YOUR_DESMISTO_BASE_URL>
export DEMISTO_API_KEY=<YOUR_DEMISTO_API_KEY>
```

### Use Cases

This command is used in order to run integration or script commands of a remote Cortex XSOAR instance. This is useful especially when developing new commands or fixing bugs, so that while working on the code the developer can debug it directly from the CLI and optimize the development process flow.

### Examples

Note that `!` is not mandatory, as we add it if needed. You can also use double quotes `"` or single quotes `'` to wrap the query.

```bash
demisto-sdk run -q 'ip ip="8.8.8.8"'
```

This will run the query `!ip ip="8.8.8.8"` on the playground of the Cortex XSOAR instance and print the output.

```bash
demisto-sdk run -q "panorama-list-address-groups"
```

This will run the query `!panorama-list-address-groups` on the playground of the Cortex XSOAR instance and print the output.

```bash
demisto-sdk run -q '!gct-translate-text text="ciao" target="iw"'
```

This will run the query `!gct-translate-text text="ciao" target="iw"` on the playground of the Cortex XSOAR instance and print the output.

```bash
demisto-sdk run -q '!gct-translate-text text="ciao" target="iw"' -k
```

This will run the query `!gct-translate-text text="ciao" target="iw"` on the playground of the Cortex XSOAR instance without a certificate validation, and print the output.

```bash
demisto-sdk run -q '!gct-translate-text text="ciao" target="iw"' -v
```

This will run the query `!gct-translate-text text="ciao" target="iw"` on the playground of the Cortex XSOAR instance, print the output and additional meta-data.

```bash
demisto-sdk run -q '!gct-translate-text text="ciao" target="iw"' -D
```

This will run the query `!gct-translate-text text="ciao" target="iw"` in debug mode (with `debug-mode="true"`) on the playground of the Cortex XSOAR instance, print the output, retrieve the debug log file and pretty print it.

```bash
demisto-sdk run -q '!gct-translate-text text="ciao" target="iw"' -D --debug-path output.log
```

This will run the query `!gct-translate-text text="ciao" target="iw"` in debug mode (with `debug-mode="true"`) on the playground of the Cortex XSOAR instance, print the output and creates `output.log` file that contains the command debug logs.
