"""
Information
---------------------------------------------------------------------
Name        : utils.py
Location    : ~/
Author      : Tom Eleff
Published   : 2024-03-19
Revised on  : 2024-03-24

Description
---------------------------------------------------------------------
Contains utility functions for managing directories and data-types.
"""

import os
import ast
import json
from typing import Union


# Directory management function(s)
def generate_output_directory(
    path: str,
    root: str,
    sub_folders: Union[list, None] = None
):
    """ Generates an output directory with subfolders.

    Parameters
    ----------
    path : `str`
        Directory path to the folder that will contain the output folder
            directories.
    root : `str`
        The name of the root folder of the directory to create within `path`.
    sub_folders: `list`
        A list of folders to create within ~/`path`/`root`
    """

    if root not in os.listdir(path):

        # Create root output directory
        os.mkdir(os.path.join(path, root))

        # Create output sub-directories
        if sub_folders:
            for folder in sub_folders:
                os.mkdir(os.path.join(path, root, folder))
    else:
        raise OSError(
            '{~/%s} already exists.' % (root)
        )


# Data-type parsing function(s)
def as_type(
    value: str,
    return_dtype: str = 'str'
) -> Union[str, int, float, bool, list, dict]:
    """ Returns `value` as `return_dtype`.

    Parameters
    ----------
    value : `str`
        String of the value to convert to `return_dtype`.
    return_dtype : `str`
        Name of the datatype (`str`, `int`, `float`, `bool`, `list`, `dict`) of
            the returned value. If the returned value cannot be converted
            to `return_dtype` then a `TypeError` is raised. If the name of the
            `return_dtype` is invalid, then a `NameError` is returned.
    """

    try:
        if return_dtype.strip().upper() == 'STR':
            return str(value)

        elif return_dtype.strip().upper() == 'INT':
            return int(value)

        elif return_dtype.strip().upper() == 'FLOAT':
            return float(value)

        elif return_dtype.strip().upper() == 'BOOL':

            try:
                return ast.literal_eval(value)
            except (SyntaxError, ValueError):
                raise TypeError(
                    ' '.join([
                        "{%s} value" % (
                            value
                        ),
                        "cannot be converted to {%s}." % (
                            return_dtype
                        )
                    ])
                )

        elif (
            (return_dtype.strip().upper() == 'LIST')
            or (return_dtype.strip().upper() == 'DICT')
        ):
            try:
                return json.loads(value)
            except json.decoder.JSONDecodeError:
                raise TypeError(
                    ' '.join([
                        "{%s} value" % (
                            value
                        ),
                        "cannot be converted to {%s}." % (
                            return_dtype
                        )
                    ])
                )
        else:
            raise NameError(
                'Invalid return datatype {%s}.' % (
                    return_dtype
                )
            )
    except ValueError:
        raise TypeError(
            ' '.join([
                "{%s} value" % (
                    value
                ),
                "cannot be converted to {%s}." % (
                    return_dtype
                )
            ])
        )
