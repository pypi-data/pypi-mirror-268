import re

from jira import JIRA, Issue, JIRAError
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.validation import ValidationError, Validator
from rich.table import Table

from inni.modules.base import BaseModule

TICKET_RE = re.compile(r"\w+-\d+")


class WorkTimeValidator(Validator):
    regex = re.compile(r"(\d+w\s*)?(\d+d\s*)?(\d+h\s*)?(\d+s\s*)?")

    def validate(self, document):
        if not self.regex.fullmatch(document.text):
            raise ValidationError(
                0,
                "Use the format: 2w 4d 6h 45m."
                " w = weeks, d = days, h = hours, m = minutes",
            )


class Module(BaseModule):
    def setUp(self):
        self.jira = JIRA(
            self.config["instance_url"],
            basic_auth=(self.config["username"], self.config["password"]),
        )

    def print_issues(self, issues: list[Issue], title="Jira Tickets"):
        table = Table(title=title)
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("Creator", style="green")
        table.add_column("Status", style="cyan")
        table.add_column("Priority", style="blue")

        for issue in issues:
            table.add_row(
                issue.key,
                issue.fields.summary,
                issue.fields.creator.displayName,
                issue.fields.status.name,
                issue.fields.priority.name,
            )
        self.out.print(table)

    def update_workhours(self):
        issue_session = PromptSession()
        worktime_session = PromptSession(validator=WorkTimeValidator())

        def blue(text):
            return FormattedText([("ansiblue", text)])

        jql = self.config.get("jql", "assignee = currentUser()")
        search = True
        keys = []
        while True:
            if search:
                with self.out.status(f"[blue]Searching issues: {jql}"):
                    issues: list[Issue] = self.jira.search_issues(jql)
                    self.print_issues(issues, jql)
                    keys = [issue.key for issue in issues]
                search = False
            self.out.print(
                "[blue]Select issue to update. Leave blank to finish."
                " To enter a new search, prefix with ?"
            )
            response = issue_session.prompt(
                blue("> "), completer=FuzzyWordCompleter(keys)
            )
            if not response:
                break
            elif response.startswith("?"):
                jql = response[1:]
                search = True
            elif TICKET_RE.fullmatch(response):
                try:
                    self.jira.issue(response)
                except JIRAError:
                    self.err.print(
                        "[red]Error fetching issue {response}."
                        " Most likely, it either doesn't exist"
                    )

                time = worktime_session.prompt(
                    blue(f"Enter time to add to {response}: ")
                )
                if not time:
                    self.out.print(f"[yellow]Skipping adding time to {response}")
                    continue
                self.jira.add_worklog(response, time)
                self.out.print("[green]Time Added!")
            else:
                self.err.print("[red]Invalid Response")

    def login(self, responses):
        self.update_workhours()

    def logout(self, responses):
        self.update_workhours()
