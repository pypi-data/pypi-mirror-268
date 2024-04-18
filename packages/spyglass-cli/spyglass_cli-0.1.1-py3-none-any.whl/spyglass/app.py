import os
from pathlib import Path
import subprocess

import inquirer
import typer
from icecream import ic

from database import Shelf
from utils import die, Project


app = typer.Typer()
project_subcommand = typer.Typer()
app.add_typer(project_subcommand, name='project')

entries: list[Project] = []


@app.command('run')
def project_run(editor: str = None):
    with Shelf('spyglass') as shelf:
        projects = {
            project.name: project
            for project in shelf.fetch()
        }

        menu = [inquirer.List('selection', message="Select a string", choices=projects.keys()),]
        answer = inquirer.prompt(menu).get('selection', 'None')

        subprocess_command = create_command(projects.get(answer), editor)

        print(f'Running {answer} ...\nCommand run:\n{subprocess_command}')
        subprocess.run(subprocess_command)




@project_subcommand.command('add')
def project_add(
    path: Path,
    name: str = None,
    runner: str = None,
    editor: str = 'nvim',
    multi: bool = False
):

    global entries

    if multi:
        die('Cannot specify name for a dir', 2) if name else None

        for dir in os.listdir(path):

            entry = create_entry(path.resolve()/dir, dir, runner, editor, True)

            ic(path/dir)
            entries.append(entry)

    else:
        entry = create_entry(path.resolve(), name, runner, editor, False)
        ic(entry)
        entries.append(entry)

    with Shelf('spyglass') as shelf:
        shelf.update(entries)


@project_subcommand.command('remove')
def project_remove(names: str = None, path: Path = None, multi: bool = False):

    global entries

    if multi:
        die('Cannot specify name for a dir', 2) if names else None
        die('No path provided', 2) if not path else None

        for dir in os.listdir(path):

            entry = create_entry(path.resolve()/dir, dir, None, None, True)

            ic(path/dir)
            entries.append(entry)

    else:
        for name in names.split(','):
            entry = create_entry(path.resolve() if path else None, name, None, None, False)
            ic(entry)
            entries.append(entry)

    with Shelf('spyglass') as shelf:
        shelf.remove(entries)



@project_subcommand.command('list')
def project_list():

    with Shelf('spyglass') as shelf:
        shelf.list()


def create_command(project: Project, editor: str) -> list[str]:
    if project.runner:
        return [project.runner]

    command: list(str) = []
    ed = editor if editor else project.editor

    if ed:
        command.append(ed)
    else:
        command.append('nvim')

    command.append(str(project.dir.resolve()))

    return command


def create_entry(path: Path, name: str, runner: str, editor: str, multi: bool) -> Project:

    proj: Project = Project(
        path,
        name if name else os.path.dirname(path),
        str(path/runner) if runner else None,
        editor if editor else 'nvim',
        multi
    )

    return proj



def main():
    app()


if __name__ == '__main__':
    main()
