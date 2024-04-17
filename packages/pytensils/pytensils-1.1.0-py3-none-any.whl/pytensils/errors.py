"""
Information
---------------------------------------------------------------------
Name        : errors.py
Location    : ~/
Author      : Tom Eleff
Published   : 2024-04-15
Revised on  : .

Description
---------------------------------------------------------------------
Contains the `class` exceptions for all native `pytensils` errors and
all error accessor functions.
"""


class config:

    # Exceptions
    class OSError(OSError):
        pass

    class FileNotFoundError(FileNotFoundError):
        pass

    class TypeError(TypeError):
        pass

    class ValidationError(Exception):
        pass

    # Define static function(s)
    def all() -> tuple:
        """ Returns a list of all config-related exceptions.
        """
        return (
            config.OSError,
            config.FileNotFoundError,
            config.TypeError,
            config.ValidationError
        )

    def raise_exception(
        msg: str,
        exception: Exception
    ):
        """ Raises the corresponding exception with `err` as the
        exception string.

        Parameters
        ----------
        msg : `str`
            The exception error message.
        exception : `Exception`
            An instance of one of the config-related exceptions.
        """
        if isinstance(exception, config.OSError):
            raise config.OSError(msg)
        elif isinstance(exception, config.FileNotFoundError):
            raise config.FileNotFoundError(msg)
        elif isinstance(exception, config.TypeError):
            raise config.TypeError(msg)
        elif isinstance(exception, config.ValidationError):
            raise config.ValidationError(msg)
        else:
            raise NotImplementedError(
                'The exception {%s} is not implemented for `pytensils.config`.'
                % (
                    type(exception).__name__
                )
            )
