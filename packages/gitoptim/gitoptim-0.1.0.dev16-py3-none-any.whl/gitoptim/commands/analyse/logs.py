import time
from typing import Annotated, Optional

import httpx
import regex
import typer

from gitoptim.schemas.workflows import AnalyseLogsSchema
from gitoptim.services.gitlab import GitlabAPI
from gitoptim.services.workflows import workflow_service
from gitoptim.utils import validator
from gitoptim.utils.cli import console, error_console
from gitoptim.utils.tag import EndTag, StartTag, TagFactory

PROMPT_TEMPLATE = (
    "{input}\n\nAbove are displayed logs from Gitlab CI/CD job. Analyse them. If there are no errors and warning "
    "don't do anything. If there are any errors or warning summarize them. If you know how to fix some "
    "errors/warnings or fix is described in the logs include it in your answer. Group errors, warnings and fixes by "
    "command. Commands are prefixed with $ sign.")

AFTER_LAST_SECTION_HELP = "Include only the logs that appear after the end of the last section. If there are no " \
                          "sections it will include all the logs."
LAST_SECTION_HELP = "Include only the logs from the last section. If there are no sections it will throw an error. " \
                    "Section does not need to be closed that is it can only have a start tag. In that case it will " \
                    "include all the logs starting from the start tag."
NAME_HELP = "Works like --last-section but includes only the logs from the section with the given name."


def extract_relevant_logs(api: GitlabAPI, last_section: bool, after_last_section: bool, section_name: str):
    retries = 0
    logs = api.get_job_logs()
    start_tag = TagFactory.create_start_tag()
    start_tag_index = logs.rfind(str(start_tag))

    while start_tag_index == -1:
        retries += 1

        if retries > 18:
            error_console.print("Cannot synchronize with Gitlab logs")
            raise typer.Exit(code=1)

        time.sleep(10)
        logs = api.get_job_logs()
        start_tag_index = logs.rfind(str(start_tag))

    logs_before_command = remove_command_echo(logs[:start_tag_index])

    if after_last_section:
        extracted_logs = extract_after_last_section(logs_before_command)
    elif last_section:
        extracted_logs = extract_section(logs_before_command)
    elif section_name is not None:
        extracted_logs = extract_section(logs_before_command, section_name)
    else:
        extracted_logs = logs_before_command

    return f"{extracted_logs.strip()}\n"


def remove_command_echo(logs: str):
    pattern = regex.compile(r"^\$ gitoptim .*$", regex.REVERSE | regex.MULTILINE)
    match = pattern.search(logs)

    # If there is match it must be the last line in the logs
    if match is None or match.end() != len(logs) - 1:
        return logs

    return logs[:match.start()]


def extract_section(logs: str, section_name: Optional[str] = None):
    pattern = regex.compile(StartTag.generate_regex_pattern(name=section_name), regex.REVERSE)
    match = pattern.search(logs)

    if match is None:
        error_console.print(
            f"Tag with name: {section_name} not found." if section_name is not None else "No tags found.")
        raise typer.Exit(code=1)

    logs_after_start_tag = logs[match.end():]

    pattern = regex.compile(EndTag.generate_regex_pattern(name=section_name))
    match = pattern.search(logs_after_start_tag)
    end_index = match.start() if match is not None else len(logs_after_start_tag)

    return remove_command_echo(logs_after_start_tag[:end_index])


def extract_after_last_section(logs):
    pattern = regex.compile(EndTag.generate_regex_pattern(), regex.REVERSE)
    match = pattern.search(logs)
    return logs if match is None else remove_command_echo(logs[match.end():])


def run_workflow_task(logs: str):
    data = AnalyseLogsSchema(input=PROMPT_TEMPLATE.format(input=logs))
    workflow_service.trigger_log_analysis(data)


def validate(last_section, after_last_section, section_name):
    if [after_last_section is True, last_section is True, section_name is not None].count(True) > 1:
        error_console.print("Options to this command are mutually exclusive.")
        raise typer.Exit(code=1)


def command(
        last_section: Annotated[bool, typer.Option("--last-section", help=LAST_SECTION_HELP)] = False,
        after_last_section: Annotated[bool, typer.Option("--after-last-section", help=AFTER_LAST_SECTION_HELP)] = False,
        name: Annotated[str, typer.Option(help=NAME_HELP, callback=validator.validate_name)] = None,
):
    """
    Analyse logs from the current job.

    Includes only the logs that appear before execution of this command.

    Example:
    $ npm install
    $ gitoptim analyse
    $ npm run test
    $ gitoptim analyse logs --after-last-section
    $ gitoptim analyse

    In the example above first `gitoptim` command will analyse logs from `npm install`. Second `gitoptim` command will
    analyse only the logs from `npm run test`. Last command will analyse all the logs.

    Term `section` refers to the part of the logs that is marked with special tags. Whenever gitoptim command
    (except `gitoptim tag`) starts execution it marks the current location in the logs with special START
    tag and when it finishes execution it marks the current location in the logs with special END tag. Everything
    between START and END tags is considered a section. While the sections created automatically by gitoptim commands
     are not that useful, it becomes powerful when you create your own sections with `gitoptim tag` command.


    See:
    `gitoptim tag`
    """

    validate(last_section, after_last_section, name)

    console.print("Running job logs analysis command")
    gitlab_api = GitlabAPI()

    console.print("Synchronizing with Gitlab logs... (it may take up to 3 minutes)")
    relevant_logs = extract_relevant_logs(gitlab_api, last_section, after_last_section, name)

    console.print("Starting analysis...")
    run_workflow_task(relevant_logs)

    console.print("Logs analysis started. See [url] for more details.")
