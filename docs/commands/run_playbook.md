---
title: run-playbook
---


:: mkdocs-click
    :module: demisto_sdk.__main__
    :command: run_playbook
    :prog_name: demisto-sdk run-playbook

## Notes

* In order to run the command, `DEMISTO_API_KEY` environment variable should contain a valid Demisto API Key.
* You can either specify a URL as an environment variable named: `DEMISTO_BASE_URL`, or enter it as an argument.

To set the environment variables, run the following shell commands:

```bash
export DEMISTO_BASE_URL=<YOUR_DESMISTO_BASE_URL>
export DEMISTO_API_KEY=<YOUR_DEMISTO_API_KEY>
```

## Examples

```bash
demisto-sdk run-playbook -p 'playbook_name'
```

This will run the playbook `playbook_name` in Demisto instance `https://demisto.local` and will wait for the playbook to finish its run.
If the run is taking more than 90 seconds (the default timeout), the command will stop while the playbook will keep running in Demisto.

```bash
demisto-sdk run-playbook -p 'playbook_name' -n
```

This will run the playbook `playbook_name` in Demisto instance `https://demisto.local` and will not wait to see the response.
The playbook will keep running in Demisto.

```bash
demisto-sdk run-playbook -p 'playbook_name' -t 300
```

This will run the playbook 'playbook_name' in Demisto instance `https://demisto.local` and will wait for the playbook to finish its run.
If the playbook is running for more than 5 minutes (300 seconds), the command will stop while the playbook will keep running in Demisto.
If you have a long running playbook, consider increasing the timeout argument respectively.
