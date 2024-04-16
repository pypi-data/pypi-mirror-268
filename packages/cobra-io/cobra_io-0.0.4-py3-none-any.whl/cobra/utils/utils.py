import json
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import jsonschema.validators

from cobra.utils.caches import SCHEMA_CACHE
from cobra.utils.configurations import COBRA_VERSION
from cobra.utils.urls import SCHEMA_URL
from cobra.utils.requests import session


def find_key(key: str, data: Union[Dict, Sequence], modifier: Optional[Callable[[Any], Any]] = None,
             search_depth: int = 20) -> Tuple[List[Any], List[Any]]:
    """
    Find all appearances of key in a nested dict / sequence combination and return references to each.

    :param key: The key to search for.
    :param data: The data to search in.
    :param modifier: An optional modifier function to apply to each found data.
    :param search_depth: The maximum depth to search in.
    :return: A tuple of lists of all found values with matching key before and after the applied modifier.
    :note: Based on
      https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-dictionaries-and-lists
    """
    if search_depth < 0:
        raise RecursionError("Maximum search depth exceeded.")
    matched_values = []
    post_modification_values = []
    for k, v in (
            data.items() if isinstance(data, Dict) else enumerate(data) if isinstance(data, Sequence) else []):
        if k == key:
            matched_values.append(data[k])
            if modifier is not None:
                data[k] = modifier(v)
            post_modification_values.append(data[k])
        elif isinstance(v, (Dict, Sequence)) and not isinstance(v, (str, bytes)):
            res = find_key(key, v, modifier, search_depth - 1)
            matched_values += res[0]
            post_modification_values += res[1]
    return matched_values, post_modification_values


def map2path(p: Union[str, Path]) -> Path:
    """Maps strings to paths, but does nothing else s.t., e.g., Django paths are not cast."""
    if isinstance(p, str):
        return Path(p)
    return p


def get_schema(schema: str, version: str = COBRA_VERSION, force_download: bool = False) -> Path:
    """
    Download a schema from the CoBRA API

    :param schema: The schema to download.
    :param version: The version of CoBRA to download from.
    :param force_download: Whether to force a download even if the schema is already cached.
    :return: The path to the downloaded schema.
    """
    if version != COBRA_VERSION:
        raise NotImplementedError
    schema_file = SCHEMA_CACHE.joinpath(f"{schema}.json")
    if not force_download and schema_file.exists():
        return schema_file
    r = session.get(SCHEMA_URL + f"{schema}.json")
    if r.status_code != 200:
        raise ValueError(f"Could not get schema {schema} from CoBRA (error {r.status_code}).")
    schema_file.write_text(r.text)
    return schema_file


def get_schema_validator(schema: str, version: str = COBRA_VERSION,
                         force_download: bool = False) -> Tuple[Dict, jsonschema.Validator]:
    """Return a loaded schema and a validator for it. Retrieval is done via get_schema."""
    schema_file = get_schema(schema, version, force_download)
    with open(schema_file) as f:
        main_schema = json.load(f)
    resolver = jsonschema.RefResolver.from_schema(main_schema)  # Use URL for sub-schemas

    # Allow also tuple as json array
    new_type_checker = jsonschema.Draft202012Validator.TYPE_CHECKER.redefine(
        "array", lambda _, instance:
        jsonschema.Draft202012Validator.TYPE_CHECKER.is_type(instance, "array") or isinstance(instance, tuple))
    validator_with_tuple = jsonschema.validators.extend(jsonschema.Draft202012Validator, type_checker=new_type_checker)
    validator = validator_with_tuple(main_schema, resolver=resolver)

    return main_schema, validator
