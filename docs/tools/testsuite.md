
# TestSuite

This module helps the developer to create unit-tests and end-to-end tests with ease.
It fixtures mocks the Content repository and creates a valid clean repository and methods to work on.

## Available fixtures

::: conftest
    selection:
        members:
            - repo
            - pack
            - integration
            - playbook
    rendering:
        show_source: true
        heading_level: 3

Use those fixture to auto-create a temporary repository.
When creating a repo, It will create a clean content directory.
**pack** will create a clean repository with a pack in it and **integration** will also create an integration in it.

Use the lowest needed entity to use in your unit-test.

## Examples

Those examples are good unit-tests that demonstrate both use of the TestSuite.

::: demisto_sdk.commands.validate.tests.validators_test
    selection:
        members:
            - test_is_mapping_fields_command_exist
    rendering:
        show_source: true
        heading_level: 3

---

::: demisto_sdk.commands.common.tests.readme_test
    selection:
        members:
            - test_demisto_not_in_readme
    rendering:
        show_source: true
        heading_level: 3
