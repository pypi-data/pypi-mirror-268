from importlib.util import module_from_spec, spec_from_file_location
from inspect import getmembers
from os import listdir, path
from typing import List

from flet_easy.pagesy import AddPagesy


def automatic_routing(dir: str) -> List[AddPagesy]:
    """
    A function that automatically routes through a directory to find Python files, extract AddPagesy objects, and return a list of them.

    Parameters:
    - dir (str): The directory path to search for Python files.

    Returns:
    - List[AddPagesy]: A list of AddPagesy objects found in the specified directory.
    """

    pages = []
    x = 0
    for file in listdir(dir):
        if (file.endswith(".py") or file.endswith(".pyc")) and file != "__init__.py":
            x = 1
            module_name = file.rstrip(".pyc")
            module_route = path.join(dir, file)
            spec = spec_from_file_location(module_name, module_route)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            for _, object_page in getmembers(module):
                x = 2
                if isinstance(object_page, AddPagesy):
                    x = 3
                    pages.append(object_page)
    if len(pages) == 0:
        raise ValueError(
           f"No instances of AddPagesy found. Check the assigned path of the 'path_views' parameter of the class (FletEasy). | {dir} | {listdir(dir)} | {x}"
        )

    return pages
