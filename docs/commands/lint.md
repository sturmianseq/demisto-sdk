---
title: lint
---

::: mkdocs-click
    :module: demisto_sdk.__main__
    :command: lint
    :prog_name: demisto-sdk lint

### Use Cases

1. Package in host checks - flake8, bandit, mypy, vulture.
2. Package in docker image checks -  pylint, pytest, powershell - test, powershell - analyze.
Meant to be used with integrations/scripts that use the folder (package) structure.
Will lookup up what docker image to use and will setup the dev dependencies and file in the target folder.
If no additional flags specifying the packs are given,will lint only changed files.

### Examples

---

```bash
demisto-sdk lint -i Integrations/PaloAltoNetworks_XDR,Scripts/HellowWorldScript --no-mypy
```

Details:

1. lint and test check will execute on Packages `Integrations/PaloAltoNetworks_XDR,Scripts/HellowWorldScript`
2. Mypy check will not be execute.
3. coverage report will be printed.

---

```bash
demisto-sdk lint -g -p 2
```

1. lint and test check will execute on all Packages which are changed from `origin/master` and from in staging.
2. 2 Threads will be used inorder to preform the lint.
3. coverage report will be printed.

---

```bash
demisto-sdk lint -i Integrations/PaloAltoNetworks_XDR,Scripts/HellowWorldScript --coverage-report coverage_report
```

Details:

1. lint and test check will execute on Packages `Integrations/PaloAltoNetworks_XDR,Scripts/HellowWorldScript`
2. coverage report will be printed.
3. coverage report files will be exported to coverage_report dir.

---
