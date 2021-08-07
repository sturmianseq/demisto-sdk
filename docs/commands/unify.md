---
title: unify
---

::: mkdocs-click
    :module: demisto_sdk.__main__
    :prog_name: demisto-sdk unify
    :command: unify

## Upload a content entity to Cortex XSOAR

In order to run the command, `DEMISTO_BASE_URL` environment variable should contain the Demisto base URL, and `DEMISTO_API_KEY` environment variable should contain a valid Demisto API Key.
To set the environment variables, run the following shell commands:

```bash
export DEMISTO_BASE_URL=<YOUR_DESMISTO_BASE_URL>
export DEMISTO_API_KEY=<YOUR_DEMISTO_API_KEY>
```

### Use Cases

This command is used in order to upload content entities to a remote Demisto instance.
Supported content entities:

- Integrations
- Playbooks
- Scripts
- Widgets
- Dashboards
- Incident Types
- Incident Fields
- Indicator Fields
- Indicator Types
- Layouts
- Layouts Container
- Classifiers
- Packs
- Zipped packs
- Reports

#### Limitation

Uploading classifiers to Cortex XSOAR is available from version 6.0.0 and up.

### Examples

```bash
demisto-sdk upload -i Packs/HelloWorld/Integrations/HelloWorld/
```

This will create a unified **integration** YML file and will upload it to the Cortex XSOAR instance.

```bash
demisto-sdk upload -i Packs/HelloWorld/Scripts/HelloWorldScript
```

This will create a temporary unified file of the `HelloWorldScript` **script** which will be uploaded to the Cortex XSOAR instance.

```bash
demisto-sdk upload -i Packs/HelloWorld/Scripts
```

This will iterate over the **scripts** folder under the `HelloWorld` pack and in turn will create a temporary unified file for each script and upload it to the Cortex XSOAR instance.

```bash
demisto-sdk upload -i Packs/HelloWorld
```

This will iterate over **all content entities** under the pack `HelloWorld` and will and in turn will upload each entity to the Cortex XSOAR instance.

```bash
demisto-sdk upload -i Packs/HelloWorld -z
```

This will zip the pack `HelloWorld` and will upload the zip file `uploadable_packs.zip` to the Cortex XSOAR instance.

```bash
demisto-sdk upload -i Packs/HelloWorld -z --keep-zip some/directory
```

This will zip the pack `HelloWorld` in `some/directory/uploadable_packs.zip` directory and will upload the zip file to the Cortex XSOAR instance.

```bash
demisto-sdk upload -i path/to/HelloWorld.zip
```

This will upload the zipped pack `HelloWorld.zip` to the Cortex XSOAR instance.

```bash
demisto-sdk upload -i Integrations/GoogleCloudTranslate/integration-GoogleCloudTranslate.yml --insecure
```

This will upload the integration YML file `integration-GoogleCloudTranslate.yml` to the Cortex XSOAR instance, **without a certificate validation**.

```bash
demisto-sdk upload -i Integrations/GoogleCloudTranslate/integration-GoogleCloudTranslate.yml --verbose
```

This will upload the integration YML file `integration-GoogleCloudTranslate.yml` to the Cortex XSOAR instance and **print the response returned from the API**.
