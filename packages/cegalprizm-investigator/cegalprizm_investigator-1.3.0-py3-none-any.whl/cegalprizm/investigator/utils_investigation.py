# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.

from typing import List

def find_children_tags_by_name(names: List[str], name: str) -> List[str]:
    """Finds all the names in the list that are children of the given name

    Args:
        names (List[str]): A list of names (for example, a entry from the discrete_dimension_tags dictionary) 
        name (str): The 

    Raises:
        ValueError: if names or name are not valid parameters

    Returns:
        List[str]: A list of names of entries that are children of the given name
    """
    if names is None or not isinstance(names, list):
        raise ValueError("names invalid: must be a list[str]")
    if name is None or not isinstance(name, str):
        raise ValueError("name invalid: must be a str")
    return [n for n in names if n.startswith(f'{name}/')]