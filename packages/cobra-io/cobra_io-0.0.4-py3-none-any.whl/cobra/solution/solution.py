import argparse
import json
import re
from pathlib import Path
from typing import Optional, Tuple, Union, Dict, List, Any

import jsonschema

from cobra.user.user import login
from cobra.utils import utils
from cobra.utils.caches import SOLUTION_CACHE
from cobra.utils.configurations import COBRA_VERSION
import cobra.utils.logging as logging
from cobra.utils.requests import session
from cobra.task.task import find_tasks, get_task
from cobra.utils.urls import RANKING_URL, SOLUTION_URL
from cobra.utils.utils import map2path


def find_solutions(task_id: Optional[str] = None, task_uuid: Optional[str] = None, version: str = COBRA_VERSION,
                   cost_function: Optional[str] = None) -> Tuple[List[str], List[Dict[str, Any]]]:
    """
    Return a list of solutions for the given task.

    :param task_id: The id of the task the solutions belong to.
    :param task_uuid: The uuid of the task the solutions belong to.
    :param version: The version of the CoBRA benchmark to use.
    :param cost_function: The cost function to filter for.
    :return: A list of solution uuids + their details from the database.
    """
    if task_uuid is None and task_id is None:
        raise ValueError("Either task_uuid or task_id must be given.")
    if task_uuid is None:
        _, details = find_tasks(id=task_id, version=version)
        if len(details) != 1:
            raise KeyError(f"Task with id {task_id} not unique in version {version}.")
        task_uuid = details[0]['id']
    query = RANKING_URL + task_uuid + "/"
    if cost_function is not None:
        query += f"?costFunction__icontains={cost_function}"
    r = session.get(query)
    if r.status_code != 200:
        raise ValueError(f"Solutions for task with uuid {task_uuid} not found.")
    if r.json()['next'] is not None:
        logging.warning(f"Only the first {r.json()['count']} solutions are returned.")
    return [res["id"] for res in r.json()['results']], r.json()['results']


def get_solution_details(solution_uuid: str) -> Dict[str, Any]:
    """
    Return the details of a solution from the CoBRA API.

    :param solution_uuid: The uuid of the solution to return.
    :return: The details of the solution as given by https://cobra.cps.cit.tum.de/api/ -> solutioncrok_read
    """
    r = session.get(SOLUTION_URL + solution_uuid + '/')
    if r.status_code != 200:
        raise ValueError(f"Solution with uuid {solution_uuid} not available.")
    return r.json()


def get_solution(solution_uuid: str, force_download: bool = False) -> Tuple[Path, Path]:
    """
    Return a solution file with the given uuid.

    :param solution_uuid: The uuid of the solution to return.
    :param force_download: Whether to force download the solution file.
    :return: The solution file and associated task file.
    """
    solution_file = SOLUTION_CACHE.joinpath(solution_uuid + ".json")
    if solution_file.exists() and not force_download:
        logging.debug("Solution file already exists. Returning cached version.")
        solution_data = json.load(solution_file.open("r"))
        return solution_file, get_task(id=solution_data["taskID"], version=solution_data["version"])

    r = session.get(SOLUTION_URL + solution_uuid + "/")
    if r.status_code != 200:
        raise ValueError(f"Solution with uuid {solution_uuid} not available.")
    r_json = session.get(r.json()["json"])
    if r_json.status_code != 200:
        raise ValueError(f"Solution json for uuid {solution_uuid} not available.")

    with open(solution_file, "wb") as f:
        f.write(r_json.content)

    task_file = get_task(uuid=r.json()["scenario_id"], force_download=force_download)

    return solution_file, task_file


def submit_solution(solution_file: Union[Path, str], user_email: str,
                    password: Optional[str] = None) -> Tuple[bool, str]:
    """
    Submit a solution file to the CoBRA benchmark.

    :param solution_file: The solution file to submit.
    :param user_email: The email of the user submitting the solution.
    :param password: The password of the user submitting the solution. Alternative enter via CLI input.
    :return: True if successful + UUID of solution.
    """
    access_token = login(user_email, password)
    r = session.post(SOLUTION_URL + 'solutionsupload/upload/',
                     files={"json": map2path(solution_file).open("rb")},
                     headers={"Authorization": f"Bearer {access_token}"})
    if r.status_code != 201:
        if r.status_code == 400 and b'Set overwrite=True in order to overwrite' in r.content:
            logging.info("Solution already exists. Did not overwrite.")
            uuid = re.findall("((?<=uuid: )[0-9a-f-]+)", str(r.content))
            if len(uuid) == 1:
                return True, uuid[0]
        raise ValueError(f"Solution upload failed with status code {r.status_code}; details: {r.content}.")
    return True, r.json()['id']


def delete_solution(solution_uuid: str, user_email: str, password: Optional[str] = None) -> bool:
    """
    Delete solution with given uuid.

    :param solution_uuid: The uuid of the solution to delete.
    :param user_email: The email of the user deleting the solution.
    :param password: The password of the user deleting the solution. Alternative enter via CLI input.
    :return: True if successful.
    :raises ValueError: If deletion fails.
    """
    access_token = login(user_email, password)
    r = session.delete(SOLUTION_URL + f"{solution_uuid}/",
                       headers={"Authorization": f"Bearer {access_token}"})
    if r.status_code != 204:
        raise ValueError(f"Solution deletion failed with status code {r.status_code}; details: {r.content}.")
    solution_file = SOLUTION_CACHE.joinpath(solution_uuid + ".json")
    solution_file.unlink(missing_ok=True)  # Also remove from cache
    return True


def get_schema(version: str = COBRA_VERSION, force_download: bool = False) -> Path:
    """
    Return the schema file for solutions in the given version of the CoBRA benchmark.

    :param version: The version of the CoBRA benchmark to use.
    :param force_download: Whether to force download the schema file.
    :return: The schema file.
    :raise ValueError: If schema does not found for specific CoBRA version or other backend error encountered.
    """
    return utils.get_schema('SolutionSchema', version, force_download)


def get_schema_validator(version: str = COBRA_VERSION,
                         force_download: bool = False) -> Tuple[Dict, jsonschema.Validator]:
    """
    Return the json schema for CoBRA solutions in the given version of the CoBRA benchmark + a validator to check with.

    :param version: The version of the CoBRA benchmark to use.
    :param force_download: Whether to force download the schema file.
    :return: The schema + jsonschema validator.
    :raise ValueError: If schema does not found for specific CoBRA version or other backend error encountered.
    """
    return utils.get_schema_validator('SolutionSchema', version, force_download)


def main():
    """Entry point to use solution as a command line tool for solution overview and file retrieval."""
    parser = argparse.ArgumentParser(description="Download solutions from the CoBRA benchmark.")
    parser.add_argument("--task_id", type=str, help="The id of the task to download solutions for.", default=None)
    parser.add_argument("--task_uuid", type=str, help="The uuid of the task to download solutions for.", default=None)
    parser.add_argument("--solution_uuid", type=str, help="The uuid of the solution to download.", default=None)
    parser.add_argument("--version", type=str, default=COBRA_VERSION, help="The version of the CoBRA benchmark to use.")
    parser.add_argument("--cost_function", type=str, default=None,
                        help="The cost function to use when querying solutions to a task.")
    args = parser.parse_args()

    if args.task_id is None and args.task_uuid is None and args.solution_uuid is None:
        raise ValueError("Either task_id, task_uuid, or solution_uuid must be given.")

    if args.solution_uuid is not None:
        if args.task_id is not None or args.task_uuid is not None:
            logging.warning("Ignoring task_id and task_uuid as solution_uuid is given.")
        solution, task = get_solution(args.solution_uuid)
        print(f"Solution file: {solution}, Task file: {task}")
    else:
        solution_uuids, solutions = find_solutions(task_id=args.task_id, task_uuid=args.task_uuid,
                                                   version=args.version, cost_function=args.cost_function)
        print(f"Found {len(solutions)} solutions for task {args.task_id} in version {args.version}.")
        print("Solution id                          | Cost     | Cost function")
        print("-------------------------------------+----------+--------------")
        for solution in solutions:
            print(f"{solution['id']} | {solution['cost']:8.2f} | {solution['costFunction']}")
    return 0


if __name__ == "__main__":
    main()
