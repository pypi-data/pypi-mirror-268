import os
import sys
from typing import Any, Dict, Tuple

import click

from .managers import EnvManager, MessageManager, RepoManager, YAMLManager
from .utils import RepoType, get_color, get_passed_params, get_toml_config


def _run(
    dry_run: bool, all_versions: bool, verbose: bool, exclude: Tuple, keep: Tuple
) -> None:
    # Backup and set needed env variables
    env_manager: EnvManager = EnvManager()
    env_manager.setup()
    # Do the magic
    try:
        yaml_manager: YAMLManager = YAMLManager(
            os.path.join(os.getcwd(), ".pre-commit-config.yaml")
        )
        repo_manager: RepoManager = RepoManager(
            yaml_manager.data["repos"], all_versions, exclude, keep
        )
        message_manager: MessageManager = MessageManager()
        repo_manager.get_updates(message_manager)

        if verbose:
            for output in (
                message_manager.excluded,
                message_manager.kept,
                message_manager.no_update,
            ):
                if not output:
                    continue
                message_manager.output_messages(output)

        if message_manager.to_update:
            message_manager.output_messages(message_manager.to_update)

            if dry_run:
                raise click.ClickException(get_color("Changes detected", "red"))

            yaml_manager.data["repos"] = repo_manager.repos_data
            yaml_manager.dump()
            click.echo(get_color("Changes detected and applied", "green"))
            return

        click.echo(get_color("No changes detected", "green"))

    except Exception as ex:
        sys.exit(str(ex))

    finally:
        # Restore env variables
        env_manager.restore()


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "-d/-nd",
    "--dry-run/--no-dry-run",
    is_flag=True,
    show_default=True,
    default=False,
    help="Dry run only checks for the new versions without updating",
)
@click.option(
    "-a/-na",
    "--all-versions/--no-all-versions",
    is_flag=True,
    show_default=True,
    default=False,
    help="Include the alpha/beta versions when updating",
)
@click.option(
    "-v/-nv",
    "--verbose/--no-verbose",
    is_flag=True,
    show_default=True,
    default=False,
    help="Display the complete output",
)
@click.option(
    "-e",
    "--exclude",
    multiple=True,
    type=RepoType(),
    default=(),
    help="Exclude specific repo(s) by the `repo` url trim",
)
@click.option(
    "-k",
    "--keep",
    multiple=True,
    type=RepoType(),
    default=(),
    help="Keep the version of specific repo(s) by the `repo` url trim (still checks for the new versions)",
)
@click.pass_context
def cli(ctx: click.Context, **_: Any):
    defaults: Dict = {p.name: p.default for p in ctx.command.params}
    cmd_params: Dict = get_passed_params(ctx)
    toml_params: Dict = get_toml_config(defaults)
    is_default: bool = defaults == ctx.params and len(cmd_params) == 0

    if is_default:
        _run(**{**defaults, **toml_params})
        return

    _run(**{**toml_params, **cmd_params})


if __name__ == "__main__":
    cli()
