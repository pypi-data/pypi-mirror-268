from argparse import ArgumentParser
import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import jsonschema

from cobra.asset.asset import get_asset
from cobra.utils import utils
from cobra.utils.caches import TASK_CACHE
from cobra.utils.configurations import COBRA_VERSION
from cobra.utils.requests import session
from cobra.utils.urls import TASK_URL
from cobra.utils.utils import find_key


def find_tasks(version: str = COBRA_VERSION,
               id: str = None,
               id_contains: str = None,
               ) -> Tuple[List[str], List[Dict[str, Any]]]:
    """
    Return a set of tasks UUIDs matching the given query parameters and a result dictionary that gives more details for

    each returned UUID.

    :param id: Task ID to query for
    :param id_contains: also match partial id such as 'simple/'
    :param version: Version of CoBRA to query in.
    :return: * List of UUIDs uniquely identifying Tasks in CoBRA
             * List of results giving more details incl. task_id, json, version, html visualization, solution count, and
               additional meta data.
    """
    query = [TASK_URL + "?"]
    if id is not None:
        query.append(f"scenario_id={id}")
    if id_contains is not None:
        query.append(f"scenario_id__icontains={id_contains}")
    if version is not None:
        query.append(f"version={version}")
    # tags: Set[str] = None,
    # if tags is not None:
    #     query.append(f"metadata__tags={tags}")
    # goal_types: Set[str] = None,
    query = query[0] + "&".join(query[1:])
    r = session.get(query)
    if r.status_code == 200:
        return [res["id"] for res in r.json()['results']], r.json()["results"]


def get_task_details(task_uuid: str) -> Dict[str, Any]:
    """
    Return the details of a task from the CoBRA API.

    :param task_uuid: The uuid of the task to return.
    :return: The details of the task as given by https://cobra.cps.cit.tum.de/api/ -> scenariocrok_read
    """
    r = session.get(TASK_URL + task_uuid + '/')
    if r.status_code != 200:
        raise ValueError(f"Task with uuid {task_uuid} not available.")
    return r.json()


def get_task(uuid: Optional[str] = None,
             id: Optional[str] = None,
             version: str = COBRA_VERSION,
             fetch_assets: bool = True,
             force_download: bool = False) -> Path:
    """Return a task with the given id and version."""
    if uuid is None and id is None:
        raise ValueError("Either uuid or id must be given.")

    if uuid is not None:
        if id is not None:
            logging.info("Both uuid and id were given. Ignoring id.")
        r_task_overview = session.get(TASK_URL + uuid + "/")
        if r_task_overview.status_code != 200:
            raise KeyError(f"Task with UUID = {uuid} not found.")
        id = r_task_overview.json()['scenario_id']
        task_overview = r_task_overview.json()
    base_path = TASK_CACHE.joinpath(version)
    task_file = base_path.joinpath(id + ".json")

    if not force_download and task_file.exists():
        if fetch_assets:
            for asset in find_key('file', json.load(task_file.open("r")))[0]:
                asset_location = base_path.joinpath(asset)
                if not asset_location.exists():
                    file = get_asset(asset, version=version)
                    asset_location.parent.mkdir(parents=True, exist_ok=True)
                    os.symlink(file, asset_location)
        return task_file

    if uuid is None:
        tasks_uuids, task_results = find_tasks(id=id, version=version)
        if len(tasks_uuids) == 0:
            raise KeyError(f"Task with id = {id} not found in version {version}.")
        elif len(tasks_uuids) > 1:
            raise KeyError(f"Multiple tasks with id = {id} found in version {version}.")
        uuid = tasks_uuids[0]
        task_overview = task_results[0]

    # Get json
    r_task_json = session.get(task_overview['json'])
    if r_task_json.status_code != 200:
        raise ValueError(f"Task json not available: {task_overview['json']}; Error code: {r_task_json.status_code}")
    task_file.parent.mkdir(parents=True, exist_ok=True)
    with open(task_file, 'wb') as f:
        f.write(r_task_json.content)

    # Get assets and symlink relative to task
    if fetch_assets:
        for asset in task_overview['assets']:
            asset_file_desired = base_path.joinpath(asset['name'])
            if asset_file_desired.exists():
                os.remove(asset_file_desired)
            asset_file_desired.parent.mkdir(parents=True, exist_ok=True)
            asset_file_desired.symlink_to(get_asset(asset['name'], version=asset['version'], force_download=False))
    return task_file


def upload_task(task: Path, user: str):
    """Upload a task to the CoBRA server."""
    raise NotImplementedError


def get_schema(version: str = COBRA_VERSION, force_download: bool = False) -> Path:
    """
    Return the schema file for tasks in the given version of the CoBRA benchmark.

    :param version: The version of the CoBRA benchmark to use.
    :param force_download: Whether to force download the schema file.
    :return: The schema file.
    :raise ValueError: If schema does not found for specific CoBRA version or other backend error encountered.
    """
    return utils.get_schema('TaskSchema', version, force_download)


def get_schema_validator(version: str = COBRA_VERSION,
                         force_download: bool = False) -> Tuple[Dict, jsonschema.Validator]:
    """
    Return the json schema for tasks in the given version of the CoBRA benchmark + a validator to check tasks with.

    :param version: The version of the CoBRA benchmark to use.
    :param force_download: Whether to force download the schema file.
    :return: The schema + jsonschema validator.
    :raise ValueError: If schema does not found for specific CoBRA version or other backend error encountered.
    """
    return utils.get_schema_validator('TaskSchema', version, force_download)


def main():
    """Main function to use task as commandline tool showing local copy of desired task ID."""
    parser = ArgumentParser(description='Download a cobra task via task ID and optional version.')
    parser.add_argument('taskID', help='ID of task', nargs=1, type=str)
    parser.add_argument('-v', '--version', help='CoBRA version to look for task in.', required=False,
                        default=COBRA_VERSION, type=str)
    parser.add_argument('-f', '--force_download', help='Force download of task and asset files.', action='store_true')
    args = parser.parse_args()
    print(get_task(id=args.taskID[0], version=args.version, force_download=args.force_download))


if __name__ == '__main__':
    main()
