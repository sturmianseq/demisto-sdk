---
title: json-to-outputs
---

::: mkdocs-click
    :module: demisto_sdk.__main__
    :command: json_to_outputs_command
    :prog_name: demisto-sdk json-to-outputs

## Examples

```bash
demisto-sdk json-to-outputs -c jira-get-ticket -p Jira.Ticket -i path/to/valid.json
```

if valid.json looks like

```json
{
    "id": 100,
    "title": "do something title",
    "created_at": "2019-01-01T00:00:00"
}
```

This command will print to the stdout the following:

```yaml
arguments: []
name: jira-get-ticket
outputs:
- contextPath: Jira.Ticket.id
  description: ''
  type: Number
- contextPath: Jira.Ticket.title
  description: ''
  type: String
- contextPath: Jira.Ticket.created_at
  description: ''
  type: Date
```
