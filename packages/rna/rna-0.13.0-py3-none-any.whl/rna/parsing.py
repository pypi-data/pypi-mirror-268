"""
Collection of standard parent parsers.
"""
import argparse
import logging
import rna.log


# pylint:disable=protected-access
class LoggingAction(argparse._StoreAction):
    """
    Call basic config with namespace.level
    """

    def __call__(self, parser, namespace, values, option_string=None):
        super().__call__(parser, namespace, values, option_string=option_string)
        # logging.basicConfig(level=namespace.level)
        root = logging.getLogger()
        root.setLevel(namespace.log_level)

        formatter = rna.log.ColorFormatter(namespace.log_format)

        terminal_handler = logging.StreamHandler()
        terminal_handler.setFormatter(formatter)
        root.addHandler(terminal_handler)

        if namespace.log_file:
            file_handler = logging.FileHandler(filename=namespace.log_file, mode="w")
            file_handler.setFormatter(formatter)
            root.addHandler(file_handler)


class LogParser(argparse.ArgumentParser):
    """
    ArgumentParser concerning logging setup.
    Actions are already setting handlers and formatters.

    Examples:
        >>> import argparse
        >>> import rna.parsing
        >>> parser = argparse.ArgumentParser(parents=[rna.parsing.LogParser()])

        >>> args, _ = parser.parse_known_args("--log_level 42".split())
        >>> args.log_level
        42
    """

    def __init__(
        self,
        add_help=False,
        level=logging.INFO,
        file=None,
        format=rna.log.FORMAT,
        **kwargs
    ):
        super().__init__(add_help=add_help, **kwargs)
        group = self.add_argument_group("logging")
        group.add_argument(
            "--log_level",
            type=int,
            default=level,
            help="Level of root logger.",
        )
        file_kwargs = dict(default=file if file else None)
        group.add_argument(
            "--log_file",
            type=str,
            help="FileHandler to be added to root logger",
            **file_kwargs
        )
        file_kwargs = dict(default=file if file else None)
        group.add_argument(
            "--log_format",
            type=str,
            help="Logging format. Default: rna.log.FORMAT",
            default=format,
        )
        # group._add_action(LoggingAction)
        group.add_argument(
            "__logging_action", action=LoggingAction, nargs="?", help=argparse.SUPPRESS
        )
