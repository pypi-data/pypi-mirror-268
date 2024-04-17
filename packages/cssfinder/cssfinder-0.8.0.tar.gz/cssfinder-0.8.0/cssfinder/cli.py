# Copyright 2023 Krzysztof Wiśniewski <argmaster.world@gmail.com>
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the “Software”), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""Module contains implementation of CSSFinder command line interface."""

from __future__ import annotations

import logging
import shutil
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Callable, Optional, TypeVar

import click

import cssfinder
from cssfinder.cssfproject import project_file_path

if TYPE_CHECKING:
    from cssfinder import examples

VERBOSITY_INFO: int = 2


@dataclass
class Ctx:
    """Command line context wrapper class."""

    is_debug: bool = False
    is_rich: bool = True
    project_path: Path | None = None


@click.group(invoke_without_command=True, no_args_is_help=True)
@click.pass_context
@click.version_option(cssfinder.__version__, "-V", "--version", prog_name="cssfinder")
@click.option(
    "-v",
    "--verbose",
    default=0,
    count=True,
    help="Control verbosity of logging, by default+ critical only, use "
    "-v, -vv, -vvv to gradually increase it.",
)
@click.option(
    "--numpy-thread-count",
    type=int,
    default=1,
    required=False,
    help="NumPy thread count override. Use '-1' to disable override and use defaults.",
)
@click.option(
    "--seed",
    type=int,
    default=None,
    required=False,
    help="NumPy random generator seed override.",
)
@click.option("--debug", is_flag=True, default=False)
@click.option("--rich", "--no-rich", "is_rich", is_flag=True, default=True)
@click.option("--perf-log", is_flag=True, default=False)
def main(
    ctx: click.Context,
    verbose: int,
    seed: Optional[int],
    numpy_thread_count: int,
    *,
    debug: bool,
    is_rich: bool,
    perf_log: bool,
) -> None:
    """CSSFinder is a script for finding closest separable states."""
    import os
    from pprint import pformat

    import pendulum
    import rich
    from threadpoolctl import threadpool_info

    if numpy_thread_count != -1:
        numpy_thread_count_str = str(numpy_thread_count)

        os.environ["OMP_NUM_THREADS"] = numpy_thread_count_str
        os.environ["OPENBLAS_NUM_THREADS"] = numpy_thread_count_str
        os.environ["MKL_NUM_THREADS"] = numpy_thread_count_str
        os.environ["VECLIB_MAXIMUM_THREADS"] = numpy_thread_count_str
        os.environ["NUMEXPR_NUM_THREADS"] = numpy_thread_count_str

    import numpy as np

    from cssfinder.log import configure_logger, enable_performance_logging

    configure_logger(verbosity=verbose, logger_name="cssfinder", use_rich=is_rich)
    ctx.obj = Ctx(is_debug=debug, is_rich=is_rich)

    if seed is not None:
        logging.debug("NumPy random number generator seed set to %d", seed)
        np.random.seed(seed)  # noqa: NPY002

    logging.debug("\n%s", pformat(threadpool_info(), indent=4))

    logging.getLogger("numba").setLevel(logging.ERROR)
    logging.info("CSSFinder started at %s", pendulum.now().isoformat(sep=" "))

    if perf_log:
        enable_performance_logging()

    if verbose >= VERBOSITY_INFO:
        rich.print(
            f"""{'[blue]' if is_rich else ''}
  ██████╗███████╗███████╗███████╗██╗███╗   ██╗██████╗ ███████╗██████╗
 ██╔════╝██╔════╝██╔════╝██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
 ██║     ███████╗███████╗█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
 ██║     ╚════██║╚════██║██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
 ╚██████╗███████║███████║██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
  ╚═════╝╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
""",
        )


@main.command(name="show-command-tree")
@click.pass_context
def tree(ctx: click.Context) -> None:
    """Show the command tree of your CLI."""
    root_cmd = _build_command_tree(ctx.find_root().command)
    _print_tree(root_cmd)


class _CommandWrapper:
    """Command tree printing based on `https://github.com/whwright/click-command-
    tree`.
    """

    def __init__(
        self,
        command: Optional[click.Command] = None,
        _children: Optional[list[click.Command]] = None,
    ) -> None:
        self.command = command
        self.children: list[_CommandWrapper] = []

    @property
    def name(self) -> str:
        if self.command is None:
            msg = "Command is not set."
            raise TypeError(msg)

        if self.command.name is None:
            msg = "Command name is not set."
            raise TypeError(msg)

        return self.command.name

    def __repr__(self) -> str:
        return f"{{_CommandWrapper {self.name}}}"


def _build_command_tree(click_command: click.Command) -> _CommandWrapper:
    wrapper = _CommandWrapper(click_command)

    if isinstance(click_command, click.core.Group):
        for cmd in click_command.commands.values():
            if not getattr(cmd, "hidden", False):
                wrapper.children.append(_build_command_tree(cmd))

    return wrapper


def _print_tree(
    command: _CommandWrapper,
    depth: int = 0,
    *,
    is_last_item: bool = False,
    is_last_parent: bool = False,
) -> None:
    if depth == 0:
        prefix = ""
        tree_item = ""
    else:
        prefix = "    " if is_last_parent else "│   "
        tree_item = "└── " if is_last_item else "├── "

    doc = command.command.__doc__
    first_line = " - " + doc.split("\n")[0] if doc else ""

    line = f"{prefix * (depth - 1) + tree_item + command.name:<30}{first_line}"

    click.echo(line)

    for i, child in enumerate(sorted(command.children, key=lambda x: x.name)):
        _print_tree(
            child,
            depth=(depth + 1),
            is_last_item=(i == (len(command.children) - 1)),
            is_last_parent=is_last_item,
        )


@main.command("create-new-json-project")
@click.option("--author", default=None, help="Author metadata field value.")
@click.option("--email", default=None, help="Email metadata field value.")
@click.option("--name", default=None, help="Name metadata field value.")
@click.option("--description", default=None, help="Description metadata field value.")
@click.option("--project-version", default=None, help="Version metadata field value.")
@click.option(
    "--no-interactive",
    is_flag=True,
    default=False,
    help="Make prompt not interactive at all.",
)
@click.option(
    "--override-existing",
    is_flag=True,
    default=False,
    help="Override existing project if exists.",
)
def _create_new_json_project(
    author: Optional[str],
    email: Optional[str],
    name: Optional[str],
    description: Optional[str],
    project_version: Optional[str],
    *,
    no_interactive: bool,
    override_existing: bool,
) -> None:
    """Create new JSON based project directory `<name>` in current working directory."""
    from cssfinder.interactive import create_new_project

    project = create_new_project(
        author,
        email,
        name,
        description,
        project_version,
        no_interactive=no_interactive,
        override_existing=override_existing,
    )

    serialized = project.json(indent=4, ensure_ascii=False)
    project.project_file.write_text(serialized)


@main.command("create-new-python-project")
@click.option("--author", default=None, help="Author metadata field value.")
@click.option("--email", default=None, help="Email metadata field value.")
@click.option("--name", default=None, help="Name metadata field value.")
@click.option("--description", default=None, help="Description metadata field value.")
@click.option("--project-version", default=None, help="Version metadata field value.")
@click.option(
    "--no-interactive",
    is_flag=True,
    default=False,
    help="Make prompt not interactive at all.",
)
@click.option(
    "--override-existing",
    is_flag=True,
    default=False,
    help="Override existing project if exists.",
)
def _create_new_python_project(
    author: Optional[str],
    email: Optional[str],
    name: Optional[str],
    description: Optional[str],
    project_version: Optional[str],
    *,
    no_interactive: bool,
    override_existing: bool,
) -> None:
    """Create new Python based project directory `<name>` in current working
    directory.
    """
    from cssfinder.interactive import create_new_project

    project = create_new_project(
        author,
        email,
        name,
        description,
        project_version,
        no_interactive=no_interactive,
        override_existing=override_existing,
    )

    serialized = project.to_python_project_template()
    project.project_file.with_suffix(".py").write_text(serialized)


@main.group("project")
def _project() -> None:
    """Group of commands for interaction with projects."""


def _project_path_validator(param: str) -> Path:
    """Check if provided path is a valid project path."""
    from cssfinder.cssfproject import CSSFProject

    project_path = Path(param).expanduser().resolve()

    if not CSSFProject.is_project_path(project_path):
        msg = "Provided path is not a valid project path."
        raise click.BadParameter(msg)

    return project_file_path(project_path)


def _json_project_path_validator(param: str) -> Path:
    """Check if provided path is a valid project path."""
    path = _project_path_validator(param)
    if path.suffix != ".json":
        msg = "Provided path is not a valid JSON project path."
        raise click.BadParameter(msg)
    return path


CallableT = TypeVar("CallableT", bound=Callable)


def _add_project_path_argument(
    param_name: str = "project_path",
    validator: Callable[[str], Path] = _project_path_validator,
) -> Callable[[CallableT], CallableT]:
    def _(function: CallableT) -> CallableT:
        return click.argument(param_name, type=validator)(function)

    return _


@_project.command("inspect")
@_add_project_path_argument()
def _inspect(project_path: Path) -> None:
    """Load project from PROJECT_PATH and display its contents.

    This command allows for inspection of task list and project metadata from command
    line.

    """
    import rich

    from cssfinder.cssfproject import CSSFProject

    project = CSSFProject.load_project(project_path)
    rich.print_json(project.json(indent=4))


@_project.command("list-tasks")
@_add_project_path_argument()
@click.option("--long", "-l", is_flag=True, default=False, help="Show more details.")
def _list_tasks(project_path: Path, *, long: bool) -> None:
    """Load project from PROJECT_PATH and list names of all tasks defined."""
    from cssfinder.cssfproject import CSSFProject

    project = CSSFProject.load_project(project_path)
    for name, details in project.tasks.items():
        if long and details.gilbert is not None:
            print(
                name,
                f"mode={details.gilbert.mode.value}",
                (
                    f"backend={details.gilbert.backend.name}"
                    if details.gilbert.backend is not None
                    else "backend=<undefined>"
                ),
            )
            continue
        print(name)


@_project.command("inspect-tasks")
@_add_project_path_argument()
@click.argument("task_pattern")
@click.pass_obj
def _inspect_tasks(ctx: Ctx, project_path: Path, task_pattern: str) -> None:
    """Load project from PROJECT_PATH and inspect configuration of tasks specified by
    TASK_PATTERN.
    """
    import json

    import rich

    from cssfinder.cssfproject import CSSFProject

    project = CSSFProject.load_project(project_path)
    tasks = project.select_tasks([task_pattern])

    for task in tasks:
        if task.gilbert is not None:
            content = json.dumps(
                {task.task_name: {"gilbert": json.loads(task.gilbert.json())}},
                indent=4,
            )
            if ctx.is_rich:
                rich.print_json(content)
            else:
                print(content)


@_project.command("inspect-output")
@_add_project_path_argument()
@click.argument("task_pattern")
def _inspect_output(project_path: Path, task_pattern: str) -> None:
    """Load project from PROJECT_PATH and display output of task specified by
    TASK_PATTERN.
    """
    import json

    from cssfinder.cssfproject import CSSFProject

    project = CSSFProject.load_project(project_path)
    tasks = project.select_tasks([task_pattern])
    for i, task in enumerate(tasks):
        corrections = json.loads(
            task.output_corrections_file.read_text(encoding="utf-8"),
        )
        print("First correction: ", corrections[0])
        print("Middle correction:", corrections[len(corrections) // 2 - 1])
        print("Last correction:  ", corrections[-1])

        if i < (len(tasks) - 1):
            print("-" * 70)


@_project.command("add-gilbert-task")
@_add_project_path_argument()
@click.option("--name", default=None, help="Name for the task.")
@click.option("--mode", default=None, help="Algorithm mode.")
@click.option(
    "--backend-name",
    default=None,
    help="Name of backend. Use `cssfinder backend list` to show installed backends.",
)
@click.option("--precision", default=None, help="Precision of calculations.")
@click.option(
    "--state",
    default=None,
    help="Path to matrix file containing initial system state.",
)
@click.option(
    "--depth",
    default=None,
    help="Depth of system, ie. number of dimensions in qu(D)it. (d)",
)
@click.option(
    "--quantity",
    default=None,
    help="Quantity of systems. ie. number of qu(D)its in state. (n)",
)
@click.option(
    "--visibility",
    default=None,
    help="Visibility against white noise, Between 0 and 1.",
)
@click.option(
    "--max-epochs",
    default=None,
    help="Maximal number of algorithm epochs to perform.",
)
@click.option(
    "--iters-per-epoch",
    default=None,
    help="Number of iterations per single epoch.",
)
@click.option(
    "--max-corrections",
    default=None,
    help="Maximal number of corrections to collect. Because halt condition is checked "
    "once per epoch, number of total corrections might exceed this limit for long "
    "epochs. Use -1 to disable this limit.",
)
@click.option(
    "--derive",
    default=None,
    help="Declare name of other existing task to derive missing field values from.",
)
@click.option(
    "--symmetries",
    default=None,
    help="List of lists of files containing symmetries matrices as valid JSON literal.",
)
@click.option(
    "--projection",
    default=None,
    help="Path to file containing projection matrix.",
)
@click.option(
    "--no-interactive",
    is_flag=True,
    default=False,
    help="Make prompt not interactive at all.",
)
@click.option(
    "--override-existing",
    is_flag=True,
    default=False,
    help="Override existing task with the same name.",
)
def _add_gilbert_task(  # noqa: PLR0913
    project_path: Path,
    name: Optional[str],
    mode: Optional[str],
    backend_name: Optional[str],
    precision: Optional[str],
    state: Optional[str],
    depth: Optional[str],
    quantity: Optional[str],
    visibility: Optional[str],
    max_epochs: Optional[str],
    iters_per_epoch: Optional[str],
    max_corrections: Optional[str],
    symmetries: Optional[str],
    projection: Optional[str],
    derive: Optional[str],
    *,
    no_interactive: bool,
    override_existing: bool,
) -> None:
    """Add new gilbert algorithm task.

    Task options can either be given by command line parameters or later interactively.

    """
    from cssfinder.cssfproject import CSSFProject
    from cssfinder.interactive import GilbertTaskSpec, add_task_gilbert

    project = CSSFProject.load_project(project_path)

    add_task_gilbert(  # type: ignore[misc]
        project,
        GilbertTaskSpec(
            name or f"task_{len(project.tasks)}",
            mode or "FSnQd",
            backend_name or "numpy_jit",
            precision or "single",
            state,
            depth,
            quantity,
            visibility or "0.4",
            max_epochs or "100",
            iters_per_epoch or "10000",
            max_corrections or "1000",
            symmetries or "[]",
            projection,
            derive,
        ),
        no_interactive=no_interactive,
        override_existing=override_existing,
    )


@_project.command("run-tasks")
@_add_project_path_argument()
@click.option(
    "--match",
    "-m",
    "match_",
    multiple=True,
    help="Use to specify names of tasks to run. When omitted, all tasks are executed.",
)
@click.option(
    "--force-sequential",
    is_flag=True,
    default=False,
    help="Enforce sequential execution. As opposed to --max-parallel set to 1, "
    "this causes code to execute only in main thread.",
)
@click.option(
    "--max-parallel",
    "-p",
    type=int,
    default=-1,
    help="Limit maximal number of tasks executed in parallel. Note that this never "
    "changes execution scheme, thus code won't be executed in main thread.",
)
@click.pass_obj
def _run_tasks(
    ctx: Ctx,
    project_path: Path,
    match_: list[str] | None,
    *,
    force_sequential: bool,
    max_parallel: int,
) -> None:
    """Run tasks from the project."""
    from cssfinder.algorithm.gilbert import SaveCorrectionsHookError, SaveStateHookError
    from cssfinder.api import run_project_from
    from cssfinder.cssfproject import (
        InvalidCSSFProjectContentError,
        MalformedProjectFileError,
        ProjectFileNotFoundError,
    )

    if not match_:
        match_ = None

    try:
        run_project_from(
            project_path,
            match_,
            is_debug=ctx.is_debug,
            is_rich=ctx.is_rich,
            force_sequential=force_sequential,
            max_parallel=max_parallel,
        )

    except ProjectFileNotFoundError as exc:
        logging.critical("Project file not found. %s", exc.args[0])
        raise SystemExit(300_000) from exc

    except MalformedProjectFileError as exc:
        logging.critical("Couldn't parse `cssfproject.json` file.")
        logging.critical(exc)
        raise SystemExit(301_000) from exc

    except InvalidCSSFProjectContentError as exc:
        logging.critical("Project file doesn't contain valid project configuration.")
        logging.critical("Fix it and try again.")
        raise SystemExit(302_000) from exc

    except SaveStateHookError:
        _log_exit(303_000)

    except SaveCorrectionsHookError:
        _log_exit(304_000)

    raise SystemExit(0)


@_project.command("create-task-report")
@_add_project_path_argument()
@click.argument(
    "task",
)
@click.option(
    "--html",
    "--no-html",
    is_flag=True,
    default=False,
    help="Include HTML report.",
)
@click.option(
    "--pdf",
    "--no-pdf",
    is_flag=True,
    default=False,
    help="Include PDF report.",
)
@click.option(
    "--json",
    "--no-json",
    is_flag=True,
    default=False,
    help="Include JSON report.",
)
@click.option(
    "--open",
    "--no-open",
    "open_",
    is_flag=True,
    default=False,
    help="Automatically open report in web browser.",
)
def _create_task_report(
    project_path: Path,
    task: str,
    *,
    html: bool,
    pdf: bool,
    json: bool,
    open_: bool,
) -> None:
    """Create short report for task.

    TASK - name pattern matching exactly one task, for which report should be created.

    """
    from cssfinder.api import AmbiguousTaskKeyError, create_report_from
    from cssfinder.reports.renderer import ReportType

    include_report_types = []

    if html:
        include_report_types.append(ReportType.HTML)

    if pdf:
        include_report_types.append(ReportType.PDF)

    if json:
        include_report_types.append(ReportType.JSON)

    if len(include_report_types) == 0:
        logging.critical(
            "No report type was selected therefore nothing will be calculated, "
            "exiting.",
        )
        raise SystemExit(0)

    try:
        for report in create_report_from(project_path, task, include_report_types):
            report.save_default()
            if open_:
                report.get_default_dest()
                import webbrowser

                webbrowser.open(url=report.get_default_dest().as_uri())

    except AmbiguousTaskKeyError as exc:
        logging.critical(exc.args[0])
        raise SystemExit(304_00) from exc


def _log_exit(code: int) -> None:
    logging.exception("Exit with code %d.", code)
    raise SystemExit(code)


@_project.command("create-json-summary")
@_add_project_path_argument()
@click.argument("task_pattern")
def _create_json_summary(project_path: Path, task_pattern: str) -> None:
    """Load and display project."""
    import json

    from cssfinder.api import create_report_from
    from cssfinder.reports.renderer import ReportType

    output = []

    for report in create_report_from(
        project_path,
        task=task_pattern,
        reports=[ReportType.JSON],
    ):
        content = json.loads(report.content)
        output.append(content)

    dest = Path(project_path) / "output" / "summary.json"
    dest.write_text(json.dumps(output, indent=4))


@_project.command("to-python")
@_add_project_path_argument("json_project_path", _json_project_path_validator)
@click.option("--override-existing", is_flag=True, default=False)
def _to_python(json_project_path: Path, *, override_existing: bool) -> None:
    """Load project from JSON_PROJECT_PATH and convert it to Python based project."""
    from cssfinder.cssfproject import CSSFProject

    project = CSSFProject.load_project(json_project_path)
    project_file_path = project.project_file.with_suffix(".py")

    if (
        not override_existing
        and project_file_path.exists()
        and (
            input("`cssfinder.py` already exists, override? (y/n) ").casefold()
            != "Y".casefold()
        )
    ):
        print("Aborted.")
        raise SystemExit(1)

    project_file_path.write_text(
        project.to_python_project_template(),
    )


@main.command("list-backends")
def _list_backends() -> None:
    """List available backends."""
    import rich

    from cssfinder.algorithm.backend.loader import Loader

    rich.get_console().print(Loader.new().get_rich_table())


@main.command("list-examples")
def _list_examples() -> None:
    """Show list of all available example projects."""
    import rich

    from cssfinder import examples

    console = rich.get_console()
    table = examples.Example.get_info_table()
    console.print()
    console.print(table)


def validate_mutually_exclusive(
    this: str,
    other: str,
) -> Callable[[click.Context, dict[str, str], str], Optional[str]]:
    """Return callback checking for mutually exclusive options."""

    def _(
        ctx: click.Context,
        param: dict[str, str],  # noqa: ARG001
        value: Optional[str],
    ) -> Optional[str]:
        if value is not None and ctx.params.get(other) is not None:
            msg = f"{this!r} and {other!r} options are mutually exclusive."
            raise click.BadParameter(msg)

        return value

    return _


@main.command("clone-example")
@click.argument(
    "sha_or_name",
)
@click.option(
    "-o",
    "--out",
    default=None,
    help="Path to destination directory, where project folder should be placed.",
)
@click.option(
    "-f",
    "--force",
    "force_overwrite",
    is_flag=True,
    help="Remove and recreate project folder in destination if one already exists.",
)
@click.option(
    "-t",
    "--terminal",
    "do_open_terminal",
    is_flag=True,
    help="When set, automatically open new terminal window in example directory.",
)
@click.option(
    "-e",
    "--explorer",
    "do_open_explorer",
    is_flag=True,
    help="When set, automatically open new explorer window in example directory.",
)
def _examples_clone(
    sha_or_name: str,
    out: Optional[str],
    *,
    force_overwrite: bool,
    do_open_terminal: bool,
    do_open_explorer: bool,
) -> None:
    """Clone one of examples to specific location.

    SHA_OR_NAME - or name of example. to select by sha, use 'sha:000000', otherwise this
                    parameter will be considered a example name.

    """
    import rich

    from cssfinder.crossplatform import open_file_explorer, open_terminal
    from cssfinder.cssfproject import ProjectFileNotFoundError
    from cssfinder.enums import ExitCode

    destination = Path.cwd() if out is None else Path(out).expanduser().resolve()

    example = _select_example(sha_or_name)
    try:
        project = example.get_project()
    except ProjectFileNotFoundError as exc:
        logging.debug(traceback.format_exc())
        logging.critical(
            "Sorry but example is broken. (%s)",
            exc.__class__.__qualname__,
        )
        raise SystemExit(ExitCode.BROKEN_EXAMPLE) from exc

    rich.print(
        f"Found example {example.name!r}, {project.meta.author!r}, "
        f"{example.get_sha256().hexdigest()[:8]!r}",
    )

    destination_project_folder = _get_validated_destination(
        destination,
        example,
        force_overwrite=force_overwrite,
    )
    try:
        example.clone(destination)
        rich.print(f"Cloned example to {destination.as_posix()!r}")

    except FileNotFoundError as exc:
        logging.critical(str(exc))
        raise SystemExit(ExitCode.PROJECT_NOT_FOUND) from exc

    if do_open_explorer:
        open_file_explorer(destination_project_folder)
    if do_open_terminal:
        open_terminal(destination_project_folder)


def _get_validated_destination(
    destination: Path,
    example: examples.Example,
    *,
    force_overwrite: bool,
) -> Path:
    from cssfinder.enums import ExitCode

    destination_project_folder = destination / example.folder_name
    is_destination_exists = destination_project_folder.exists()

    try:
        is_destination_non_empty = len(list(destination_project_folder.iterdir())) > 0
    except FileNotFoundError:
        is_destination_non_empty = False

    if is_destination_exists and is_destination_non_empty:
        if force_overwrite:
            shutil.rmtree(destination_project_folder.as_posix())

        else:
            logging.critical(
                "Output directory already contains folder %r, change destination "
                "folder. Remove existing folder or use `--force` flag to remove it "
                "automatically.",
                example.folder_name,
            )
            raise SystemExit(ExitCode.EXAMPLE_DESTINATION_ALREADY_EXISTS)

    return destination_project_folder


def _select_example(sha_or_name: str) -> examples.Example:
    from cssfinder import examples
    from cssfinder.enums import ExitCode

    if sha_or_name.startswith("sha:"):
        sha_or_name = sha_or_name[4:]
        try:
            example = examples.Example.select_by_sha256(sha_or_name)
        except examples.ExampleNotFoundError as exc:
            logging.critical("%s", exc)
            raise SystemExit(ExitCode.EXAMPLE_WITH_SHA_NOT_FOUND) from exc

    else:
        try:
            example = examples.Example.select_by_name(sha_or_name)
        except examples.ExampleNotFoundError as exc:
            logging.critical("%s", exc)
            raise SystemExit(ExitCode.EXAMPLE_WITH_NAME_NOT_FOUND) from exc

    return example
