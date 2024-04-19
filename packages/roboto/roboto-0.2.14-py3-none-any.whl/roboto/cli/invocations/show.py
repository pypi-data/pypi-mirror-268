#  Copyright (c) 2023 Roboto Technologies, Inc.
import argparse

from ...domain.actions import Invocation
from ..command import RobotoCommand
from ..context import CLIContext


def show(
    args: argparse.Namespace, context: CLIContext, parser: argparse.ArgumentParser
) -> None:
    invocation = Invocation.from_id(
        args.invocation_id,
        invocation_delegate=context.invocations,
    )
    print(str(invocation))
    return


def show_parser(parser: argparse.ArgumentParser):
    parser.add_argument("invocation_id")


show_command = RobotoCommand(
    name="show",
    logic=show,
    setup_parser=show_parser,
    command_kwargs={"help": "Show invocation details."},
)
