---
title: generate-docs
---


::: mkdocs-click
    :module: demisto_sdk.__main__
    :command: generate_docs

### Notes

* If `command_permissions` wil not be given, a generic message regarding the need of permissions will be given.
* If no `output` given, the README.md file will be generated in the `input` file repository.

### Use-Cases

This command is used to create a documentation file for Cortex XSOAR content files.

### Examples

```bash
demisto-sdk generate-docs -i Packs/MyPack/Integrations/MyInt/MyInt.yml -e Packs/MyPack/Integrations/MyInt/command_exmaple.txt
```

This will generate a documentation for the MyInt integration using the command examples found in the .txt file in the MyInt integration.

```bash
demisto-sdk generate-docs -i Packs/MyPack/Integrations/MyInt/MyInt_v2.yml --old-version Packs/MyPack/Integrations/MyInt/MyInt.yml
```

This will generate a documentation for MyInt_v2 integration including a section about changes compared the MyInt integration.
The command will automatically detect if the given integration is a v2 using the integration's display name and create the changes section.
If no '--old-version' is supplied a prompt will appear asking for the path to the old integration.
