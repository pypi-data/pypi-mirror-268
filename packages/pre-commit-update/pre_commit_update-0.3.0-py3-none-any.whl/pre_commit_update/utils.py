import os
from typing import Dict

import click
from pyproject_parser import PyProject


class RepoType(click.types.StringParamType):
    name = "repo_url_trim"


def get_color(text: str, color: str) -> str:
    return click.style(str(text), fg=color)


def get_passed_params(ctx: click.Context) -> Dict:
    return {
        k: v
        for k, v in ctx.params.items()
        if ctx.get_parameter_source(k) == click.core.ParameterSource.COMMANDLINE
    }


def get_toml_config(defaults: Dict) -> Dict:
    try:
        toml_file: PyProject = PyProject.load(
            os.path.join(os.getcwd(), "pyproject.toml")
        )
        return {**defaults, **toml_file.tool["pre-commit-update"]}
    except (FileNotFoundError, KeyError):
        return defaults
