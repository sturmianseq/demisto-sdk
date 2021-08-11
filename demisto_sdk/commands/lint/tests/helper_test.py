import json
import logging
import os

import pytest
from freezegun import freeze_time

from demisto_sdk.commands.lint.helpers import (export_report, get_coverage,
                                               get_coverage_summery_file,
                                               split_warnings_errors)


def test_validate_env(mocker) -> None:
    from demisto_sdk.commands.lint import helpers
    mocker.patch.object(helpers, 'run_command_os')
    helpers.run_command_os.side_effect = [('python2', '', ''), ('flake8, mypy, vultue', '', '')]
    helpers.validate_env()

    assert helpers.run_command_os.call_count == 2


EXIT_CODES = {
    "flake8": 0b1,
    "xsoar_linter": 0b1000000000,
    "bandit": 0b10,
    "mypy": 0b100,
    "vulture": 0b1000,
    "pytest": 0b10000,
    "pylint": 0b100000,
    "pwsh_analyze": 0b1000000,
    "pwsh_test": 0b10000000,
    "image": 0b100000000,
}


@pytest.mark.parametrize(
    argnames="no_flake8, no_xsoar_linter, no_bandit, no_mypy, no_pylint, no_vulture, no_test, no_pwsh_analyze, "
             "no_pwsh_test, docker_engine, expected_value",
    argvalues=[(True, False, True, True, True, True, True, True, True, True, 0b11111111),
               (True, False, False, True, True, True, True, True, True, True, 0b11111101),
               (True, False, False, True, True, True, True, False, True, True, 0b10111101)])
def test_build_skipped_exit_code(no_flake8: bool, no_xsoar_linter: bool, no_bandit: bool, no_mypy: bool,
                                 no_pylint: bool, no_vulture: bool,
                                 no_test: bool, no_pwsh_analyze: bool, no_pwsh_test: bool, docker_engine: bool,
                                 expected_value: int):
    from demisto_sdk.commands.lint.helpers import build_skipped_exit_code
    env_var = os.environ.get('CI')
    # On you local env
    if not env_var:
        assert expected_value == build_skipped_exit_code(no_flake8, no_bandit, no_mypy, no_pylint, no_vulture,
                                                         no_xsoar_linter, no_test,
                                                         no_pwsh_analyze, no_pwsh_test, docker_engine)
    # On circle runs
    else:
        assert 0 == build_skipped_exit_code(no_flake8, no_bandit, no_mypy, no_pylint, no_vulture, no_xsoar_linter,
                                            no_test,
                                            no_pwsh_analyze, no_pwsh_test, docker_engine)


@pytest.mark.parametrize(argnames="image, output, expected", argvalues=[('alpine', b'3.7\n', 3.7),
                                                                        ('alpine-3', b'2.7\n', 2.7)])
def test_get_python_version_from_image(image: str, output: bytes, expected: float, mocker):
    from demisto_sdk.commands.lint import helpers
    mocker.patch.object(helpers, 'docker')
    helpers.docker.from_env().containers.run().logs.return_value = output
    assert expected == helpers.get_python_version_from_image(image)


@pytest.mark.parametrize(argnames="archive_response, expected_count, expected_exception",
                         argvalues=[
                             ([False, True], 2, False),
                             ([True], 1, False),
                             ([False, False], 2, True)
                         ])
def test_copy_dir_to_container(mocker, archive_response: bool, expected_count: int, expected_exception: bool):
    from demisto_sdk.commands.lint import helpers
    mocker.patch.object(helpers, 'docker')
    mocker.patch.object(helpers, 'tarfile')
    mocker.patch.object(helpers, 'os')
    mock_container = mocker.MagicMock()
    mock_container_path = mocker.MagicMock()
    mock_host_path = mocker.MagicMock()
    mock_container.put_archive.side_effect = archive_response
    if expected_exception:
        with pytest.raises(Exception):
            helpers.copy_dir_to_container(mock_container, mock_container_path, mock_host_path)
    else:
        helpers.copy_dir_to_container(mock_container, mock_container_path, mock_host_path)

    assert mock_container.put_archive.call_count == expected_count


MSG = [('flake8',
        "/Users/test_user/dev/demisto/content/Packs/Maltiverse/Integrations/Maltiverse/Maltiverse.py:6:1: F401 "
        "'typing.Tuple' imported but unused\n/Users/test_user/dev/demisto/content/Packs/Maltiverse/Integrations"
        "/Maltiverse/Maltiverse.py:6:1: F401 'typing.Dict' imported but "
        "unused\n/Users/test_user/dev/demisto/content/Packs/Maltiverse/Integrations/Maltiverse/Maltiverse.py:6:1: F401 "
        "'typing.Any' imported but unused",
        [], [], [
            "/Users/test_user/dev/demisto/content/Packs/Maltiverse/Integrations/Maltiverse/Maltiverse.py:6:1: F401 "
            "'typing.Tuple' imported but unused",
            "/Users/test_user/dev/demisto/content/Packs/Maltiverse/Integrations/Maltiverse/Maltiverse.py:6:1: F401 "
            "'typing.Dict' imported but unused",
            "/Users/test_user/dev/demisto/content/Packs/Maltiverse/Integrations/Maltiverse/Maltiverse.py:6:1: F401 "
            "'typing.Any' imported but unused"]),
       ('xsoar_linter',
        "************* Module Maltiverse\nMaltiverse.py:509:0: W9010: try and except statements were not found in "
        "main function. Please add them (try-except-main-doesnt-exists)\nMaltiverse.py:509:0: W9012: return_error "
        "should be used in main function. Please add it. (return-error-does-not-exist-in-main)\nMaltiverse.py:511:4: "
        "E9002: Print is found, Please remove all prints from the code. (print-exists)",
        ["Maltiverse.py:511:4: E9002: Print is found, Please remove all prints from the code. (print-exists)"], [
            "Maltiverse.py:509:0: W9010: try and except statements were not found in main function. Please add them ("
            "try-except-main-doesnt-exists)",
            "Maltiverse.py:509:0: W9012: return_error should be used in main function. Please add it. ("
            "return-error-does-not-exist-in-main)"],
        ["************* Module Maltiverse"]),
       ('xsoar_linter',
        "************* Module VirusTotal-Private_API\nW: 20,10: Initialize of params was found outside of main"
        " function. Please use demisto.params() only inside mainfunc (init-params-outside-main)",
        [], ["W: 20,10: Initialize of params was found outside of main function. Please use demisto.params()"
             " only inside mainfunc (init-params-outside-main)"],
        ["************* Module VirusTotal-Private_API"]),
       ('mypy',
        "Maltiverse.py:31:12: error: Incompatible return value type (got\nDict[Any, Any]', expected 'str')["
        "return-value]     \nreturn params^\n    Found 1 error in 1 file (checked 1 source file)",
        [], [], ["Maltiverse.py:31:12: error: Incompatible return value type (got",
                 "Dict[Any, Any]', expected 'str')[return-value]     ", "return params^",
                 "    Found 1 error in 1 file (checked 1 source file)"]),
       ('mypy',
        "Ebox.py:31:12: error: Incompatible return value type (got\nDict[Any, Any]', expected 'str')["
        "return-value]     \nreturn params^\n    Found 1 error in 1 file (checked 1 source file)",
        [], [], ["Ebox.py:31:12: error: Incompatible return value type (got",
                 "Dict[Any, Any]', expected 'str')[return-value]     ", "return params^",
                 "    Found 1 error in 1 file (checked 1 source file)"]),

       ]


@pytest.mark.parametrize('linter_name, input_msg, output_error, output_warning, output_other', MSG)
def test_split_warnings_errors(linter_name, input_msg, output_error, output_warning, output_other):
    """
        Given:
            - linter name releated to input_msg which was returned from this specific linter.

        When:
            - Running split_warnings_errors on the given inupt.

        Then:
            - Ensure that the error, warning, other return values equal to expected.
        """
    error, warning, other = split_warnings_errors(input_msg)
    assert error == output_error
    assert warning == output_warning
    assert other == output_other


class TestGenerateCoverageReport:
    def test_get_coverage(self):
        cov_obj = get_coverage()
        assert cov_obj.config.data_file == 'coverage_report/.coverage'
        assert cov_obj.config.html_dir == 'coverage_report/html'
        assert cov_obj.config.xml_output == 'coverage_report/coverage.xml'
        assert cov_obj.config.json_output == 'coverage_report/coverage.json'

    class TestExportReport:
        def nothing(self):
            from coverage.misc import CoverageException
            raise CoverageException('some coverage exception')

        def test_export_report_logger(self, mocker):
            logger_info = mocker.patch.object(logging.getLogger('demisto-sdk'), 'info')
            export_report(lambda: None, 'format', 'dest')
            logger_info.assert_called_once_with('exporting format coverage report to dest')

        def test_export_report_error(self, mocker):
            logger_warning = mocker.patch.object(logging.getLogger('demisto-sdk'), 'warning')

            export_report(self.nothing, 'format', 'dest')
            logger_warning.assert_called_once_with('some coverage exception')

        def test_export_report_called(self, mocker):
            mocker.patch.object(self, 'nothing')
            export_report(self.nothing, 'format', 'dest')
            self.nothing.assert_called_once()


class TestGetCoverageSummeryFile:

    cov_url = "https://storage.googleapis.com/marketplace-dist-dev/code-coverage/coverage_data.json"

    def test_without_file(self, requests_mock, tmpdir):
        requests_mock.get(self.cov_url, json={'files': {'Packs/Lastline/Integrations/Lastline_v2/Lastline_v2.py': 40.0},
                          'last_updated': '2021-08-10T00:00:00Z'})
        files = get_coverage_summery_file(os.path.join(tmpdir, 'test.json'))
        assert files == {'Packs/Lastline/Integrations/Lastline_v2/Lastline_v2.py': 40.0}

    def test_without_dir(self, requests_mock, tmpdir):

        requests_mock.get(self.cov_url, json={'files': {'Packs/Lastline/Integrations/Lastline_v2/Lastline_v2.py': 40.0},
                          'last_updated': '2021-08-10T00:00:00Z'})
        files = get_coverage_summery_file(os.path.join(tmpdir, 'test/test.json'))
        assert files == {'Packs/Lastline/Integrations/Lastline_v2/Lastline_v2.py': 40.0}

    @freeze_time('2021-08-10T01:00:00Z')
    def test_with_updated_file(self, requests_mock, tmpdir):
        file_path = os.path.join(tmpdir, 'test.json')
        with open(file_path, 'w') as _file:
            _file.write(json.dumps({'files': {'Packs/Lastline/Integrations/Lastline_v2/Lastline_v2.py': 40.0},
                                    'last_updated': '2021-08-10T00:00:00Z'}))
        requests_mock.get(self.cov_url, status_code=500)
        files = get_coverage_summery_file(file_path)
        assert files == {'Packs/Lastline/Integrations/Lastline_v2/Lastline_v2.py': 40.0}

    @freeze_time('2021-08-10T01:00:00Z')
    def test_with_old_file(self, requests_mock, tmpdir):
        file_path = os.path.join(tmpdir, 'test.json')
        with open(file_path, 'w') as _file:
            _file.write(json.dumps({'files': {'Packs/Lastline/Integrations/Lastline_v2/Lastline_v2.py': 40.0},
                                    'last_updated': '2021-08-09T00:00:00Z'}))
        requests_mock.get(self.cov_url, json={'files': {'Packs/Lastline/Integrations/Lastline_v2/Lastline_v2.py': 50.0},
                          'last_updated': '2021-08-10T00:00:00Z'})
        files = get_coverage_summery_file(file_path)
        assert files == {'Packs/Lastline/Integrations/Lastline_v2/Lastline_v2.py': 50.0}
