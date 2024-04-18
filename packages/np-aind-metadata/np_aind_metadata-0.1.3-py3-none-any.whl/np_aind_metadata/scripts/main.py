import datetime
import json
import logging
import os
import pathlib
import typing

import click

from np_aind_metadata import common, utils
from np_aind_metadata.np import dynamic_routing_task as dynamic_routing_task_np
from np_aind_metadata.update import dynamic_routing_task as dynamic_routing_task_update

logger = logging.getLogger(__name__)


NPEXP_PATH_ROOT = os.getenv("NPEXP_PATH_ROOT")
now = datetime.datetime.now()


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.option("--log-file", default=False, is_flag=True)
def cli(debug: bool, log_file: bool) -> None:
    click.echo(f"Debug mode is {'on' if debug else 'off'}")
    if debug:
        dynamic_routing_task_np.logger.setLevel(logging.DEBUG)
        dynamic_routing_task_update.logger.setLevel(logging.DEBUG)
        utils.logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)

    if log_file:
        handler = logging.FileHandler(
            now.strftime("np-aind-metadata_%Y-%m-%d-%H-%M-%S") + ".log"
        )
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(handler)
        dynamic_routing_task_np.logger.addHandler(handler)
        dynamic_routing_task_update.logger.addHandler(handler)
        utils.logger.addHandler(handler)


@cli.command()
@click.argument(
    "rig-name",
    type=str,
)
@click.argument(
    "modification-date-str",
    type=str,
)
@click.option(
    "--output-directory",
    type=pathlib.Path,
    default=pathlib.Path("./"),
)
def init_rig(
    rig_name: str,
    modification_date_str: str,
    output_directory: pathlib.Path,
) -> None:
    if rig_name not in ["NP0", "NP1", "NP2", "NP3"]:
        raise ValueError(f"Invalid rig name: {rig_name}")

    modification_date = datetime.datetime.strptime(
        modification_date_str, "%Y-%m-%d"
    ).date()

    output_path = dynamic_routing_task_np.init_rig_from_np_config(
        rig_name,
        modification_date,
        output_directory,
    )
    click.echo(f"Rig json generated at: {output_path}")


@cli.command()
@click.argument(
    "rig-path",
    type=pathlib.Path,
)
@click.argument(
    "session-dir",
    type=pathlib.Path,
)
@click.option(
    "--output-dir",
    type=pathlib.Path,
    default=pathlib.Path("./"),
)
@click.option(
    "--include",
    multiple=True,
)
def update_dynamic_routing_rig(
    rig_path: pathlib.Path,
    session_dir: pathlib.Path,
    output_dir: pathlib.Path,
    include: typing.Optional[list[str]],
) -> None:
    rig_path = utils.fix_allen_path(rig_path)
    session_dir = utils.fix_allen_path(session_dir)
    logger.debug("Rig path: %s" % rig_path)
    logger.debug("Session dir: %s" % session_dir)
    logger.debug("Include: %s" % json.dumps(include))
    output_path = dynamic_routing_task_np.update_rig_from_session_dir(
        rig_path,
        session_dir,
        output_dir=output_dir,
        include=include,
    )
    click.echo(f"Updated rig json generated at: {output_path}")


@cli.command()
@click.argument("rig-path", type=pathlib.Path)
@click.argument("session-root-dirs", type=pathlib.Path, nargs=-1)
@click.option("--output-dir", type=pathlib.Path, default=pathlib.Path("./"))
@click.option(
    "--include",
    multiple=True,
)
def batch_generate_np(
    rig_path: pathlib.Path,
    session_root_dirs: list[pathlib.Path],
    output_dir: pathlib.Path,
    include: typing.Optional[list[str]],
) -> None:
    rig_path = utils.fix_allen_path(rig_path)
    session_root_dirs = [utils.fix_allen_path(p) for p in session_root_dirs]
    logger.debug(f"Rig path: {rig_path}")
    logger.debug(f"Session root dirs: {session_root_dirs}")
    for session_dir in dynamic_routing_task_np.get_sorted_session_dirs(
        *session_root_dirs
    ):
        output_path = dynamic_routing_task_np.update_rig_from_session_dir(
            rig_path,
            session_dir,
            output_dir=output_dir,
            include=include,
        )
        logger.debug(f"Updated rig json generated at: {output_path}")


@cli.command()
@click.argument("rig-path", type=pathlib.Path)
@click.argument("sorted-sessions-path", type=pathlib.Path)
@click.option("--output-dir", type=pathlib.Path, default=pathlib.Path("./"))
def backfill_generate(
    rig_path: pathlib.Path,
    sorted_sessions_path: pathlib.Path,
    output_dir: pathlib.Path,
) -> None:
    rig_path = utils.fix_allen_path(rig_path)
    session_dir_infos = [
        (pathlib.Path(path), subject_id, is_surface)
        for _, path, subject_id, is_surface in json.loads(
            sorted_sessions_path.read_text()
        )
    ]
    logger.debug(f"Rig path: {rig_path}")
    for session_dir, subject_id, is_surface in session_dir_infos:
        update_context = dynamic_routing_task_np.update_rig_from_session_dir(
            rig_path,
            session_dir,
            output_dir=output_dir,
            include=["open_ephys_context"],
            id_prefix=subject_id,
            id_suffix="surface_channels" if is_surface else None,
        )
        logger.debug(f"Updated rig json generated at: {update_context.updated}")
        if not update_context.updated:
            logger.error("Failed to update rig json.")
            continue
        rig_path = update_context.updated


@cli.command()
@click.argument("rig-path", type=pathlib.Path)
@click.option("--mvr-source", type=pathlib.Path)
@click.option("--sync-source", type=pathlib.Path)
@click.option("--output-path", type=pathlib.Path)
def manual_update(
    rig_path: pathlib.Path,
    mvr_source: pathlib.Path | None,
    sync_source: pathlib.Path | None,
    output_path: pathlib.Path | None,
) -> None:
    context = common.DynamicRoutingTaskUpdateContext(
        source=rig_path,
    )
    if mvr_source:
        context.mvr_context = common.MVRContext(
            source=mvr_source,
        )
    if sync_source:
        context.sync_context = common.SyncContext(
            source=sync_source,
        )
    if output_path is None:
        output_path = rig_path
    updated_context = dynamic_routing_task_update.update_rig(context, output_path)
    click.echo(f"Updated rig json generated at: {updated_context.updated}")


if __name__ == "__main__":
    cli()
