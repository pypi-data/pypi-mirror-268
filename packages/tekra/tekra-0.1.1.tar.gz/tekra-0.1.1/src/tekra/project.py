"""
Handler tekra project
"""
import os
from pathlib import Path

import yaml
from pydantic import BaseModel

from jinja2 import Template


TEKRA_CONFIG_FILE_NAME = 'tekra.yaml'


class _Templates:
    project_main_py = Template("""
import tekra


def main():
    engine = tekra.Engine()
    engine.run()


def __main__():
    main()

    """)

    requirements_txt = Template("""
tekra
    """)


class Project(BaseModel):
    name: str
    description: str
    version: str
    author: str
    path: Path


def find_current_project_path(path: Path):

    while path != Path('/'):
        if (path / TEKRA_CONFIG_FILE_NAME).exists():
            return path
        path = path.parent
    return None


def open_project(path: Path):
    project_path = find_current_project_path(path)
    if not project_path:
        raise Exception('Project not found')
    with open(project_path / TEKRA_CONFIG_FILE_NAME, 'r') as f:
        project = yaml.safe_load(f)
    return Project(**project, path=project_path)


def create_virtual_environment(path: Path):
    os.system(f'python -m venv {path}')


def create_project(path: Path, name: str, description: str, version: str, author: str):
    project_path = find_current_project_path(path)
    if project_path:
        raise Exception('Project already exists')
    project_path = path / name
    project_path.mkdir()
    with open(project_path / TEKRA_CONFIG_FILE_NAME, 'w') as f:
        yaml.dump({
            'name': name,
            'description': description,
            'version': version,
            'author': author
        }, f)
    (project_path/'src').mkdir()
    (project_path/'dist').mkdir()
    (project_path/'data').mkdir()
    with open(project_path/'src'/'main.py', 'w') as f:
        f.write(_Templates.project_main_py.render())
    with open(project_path/'requirements.txt', 'w') as f:
        f.write(_Templates.requirements_txt.render())
    create_virtual_environment(project_path/'venv')
    os.system(f'{project_path}/venv/bin/pip install -r {project_path}/requirements.txt')
    return Project(name=name, description=description, version=version, author=author, path=project_path)


def update_project(path: Path, name: str, description: str, version: str, author: str):
    project = open_project(path)
    with open(project.path / TEKRA_CONFIG_FILE_NAME, 'w') as f:
        yaml.dump({
            'name': name,
            'description': description,
            'version': version,
            'author': author
        }, f)
    return Project(name=name, description=description, version=version, author=author, path=project.path)


def delete_project(path: Path):
    project = open_project(path)
    project.path.rmdir()
    return project


def build_project(path: Path):
    project = open_project(path)
    os.execv('pyinstaller', ['pyinstaller', 'src/main.py', '-n', project.name, '-p', 'src', '-d', 'dist'])
