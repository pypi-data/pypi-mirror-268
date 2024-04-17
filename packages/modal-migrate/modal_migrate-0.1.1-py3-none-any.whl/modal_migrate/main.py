from pathlib import Path
from typing import Annotated, Iterator, Sequence

import libcst as cst
import rich.progress
import typer

# Common excluded directories.
exclude: set[str] = {
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pyenv",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".vscode",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
}


def list_files(src: Path) -> Iterator[Path]:
    if src.is_file():
        if src.name.endswith(".py"):
            yield src
    elif src.is_dir():
        for p in src.iterdir():
            if p.name not in exclude:
                yield from list_files(p)


class StubToAppTransformer(cst.CSTTransformer):
    def __init__(self) -> None:
        super().__init__()
        self.changes = 0

    def leave_ImportFrom(self, original_node, updated_node):
        if updated_node.module is not None and updated_node.module.value == "modal":
            if isinstance(updated_node.names, Sequence):
                new_aliases = []
                has_changes = False
                for alias in updated_node.names:
                    if alias.name.value == "Stub":
                        has_changes = True
                        new_aliases.append(alias.with_changes(name=cst.Name("App")))
                    else:
                        new_aliases.append(alias)
                if has_changes:
                    self.changes += 1
                    return updated_node.with_changes(names=new_aliases)
        return original_node

    def leave_Attribute(self, original_node, updated_node):
        # Check if the value is an attribute with name 'modal' and the attribute itself is 'Stub'
        if (
            isinstance(updated_node.value, cst.Name)
            and updated_node.value.value == "modal"
            and updated_node.attr.value == "Stub"
        ):
            # Return a new attribute with the name 'App' instead of 'Stub'
            self.changes += 1
            return updated_node.with_changes(attr=cst.Name("App"))
        return original_node


def fix_file(src: Path, apply: bool) -> bool:
    module = cst.parse_module(src.read_text())
    transformer = StubToAppTransformer()
    new_module = module.visit(transformer)
    if transformer.changes:
        rich.print(
            f"{transformer.changes} change{'s' if transformer.changes > 1 else ''} in [underline]{src}[/underline]"
        )
        if apply:
            src.write_text(new_module.code)
        return True
    return False


def show_warning(message: str) -> None:
    rich.print("[bold][yellow]Warning:[/yellow] " + message + "[/bold]")


def show_error(message: str) -> None:
    rich.print("[bold][red]Error:[/red] " + message + "[/bold]")


def main(
    src: Annotated[
        Path, typer.Argument(..., help="The path to the file or directory to process.")
    ],
    apply: Annotated[
        bool, typer.Option(help="Apply changes to your code in place.")
    ] = False,
) -> None:
    if not src.exists():
        show_error("File not found, the given path does not exist")
        raise typer.Exit(code=1)

    files = list(list_files(src))
    if not files:
        show_warning("No Python files found under the given path")
        raise typer.Exit()

    files_changed = 0
    with rich.progress.Progress(
        rich.progress.MofNCompleteColumn(),
        rich.progress.BarColumn(),
        rich.progress.TaskProgressColumn(),
        rich.progress.TimeRemainingColumn(),
        rich.progress.TextColumn("[progress.description]{task.description}"),
        refresh_per_second=60,
    ) as progress:
        task = progress.add_task("Processing...", total=len(files))
        for f in files:
            progress.update(task, description=str(f))
            try:
                files_changed += fix_file(f, apply=apply)
            except Exception as exc:
                print("Error while processing file", f)
                print(exc)
            progress.update(task, advance=1)

    if files_changed:
        rich.print(f"[blue]Updated [bold]{files_changed}[/bold] files![/blue]")
        if not apply:
            show_warning("Rerun with --apply to apply changes to your code in place.")
    else:
        rich.print("[blue]No changes needed.[/blue]")


def entrypoint():
    typer.run(main)


if __name__ == "__main__":
    entrypoint()
