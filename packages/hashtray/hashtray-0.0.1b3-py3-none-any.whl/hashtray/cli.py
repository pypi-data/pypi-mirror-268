import argparse
import sys

from rich.console import Console

from hashtray.email_enum import EmailEnum
from hashtray.gravatar import Gravatar

c = Console(highlight=False)


def parse_app_args(arguments=None):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="cmd")

    subp_email = subparsers.add_parser(
        "email", help="Find a Gravatar account from an email address"
    )
    subp_email.add_argument(
        "email", type=str, help="Email address to search in Gravatar.com"
    )

    subp_account = subparsers.add_parser(
        "account", help="Find an email address from a Gravatar username or hash"
    )
    subp_account.add_argument(
        "account",
        type=str,
        help="Gravatar username or hash to search for email in Gravatar.com",
    )
    subp_account.add_argument(
        "--domain_list",
        "-d",
        choices=["common", "long", "full"],
        help="Domain list to use for email enumeration. Default: common",
        default="common",
    )
    subp_account.add_argument(
        "--strings",
        "-s",
        type=str,
        help="Custom strings to search for email",
        nargs="*",
    )
    subp_account.add_argument(
        "--custom_domains",
        "-c",
        type=str,
        help="Custom domains to search for email",
        nargs="*",
    )

    return parser.parse_args(args=None if sys.argv[1:] else ["--help"])


def main() -> None:
    c.print(
        r"""
██╗░░██╗░█████╗░░██████╗██╗░░██╗████████╗██████╗░░█████╗░██╗░░░██╗
██║░░██║██╔══██╗██╔════╝██║░░██║╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
███████║███████║╚█████╗░███████║░░░██║░░░██████╔╝███████║░╚████╔╝░
██╔══██║██╔══██║░╚═══██╗██╔══██║░░░██║░░░██╔══██╗██╔══██║░░╚██╔╝░░
██║░░██║██║░░██║██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
                                             [white]j m . b a l e s t e k[/white]
 """, style="#1e8cbe")

    args = parse_app_args()
    if args.cmd == "email" and args.email:
        Gravatar(args.email).print_info()
    elif args.cmd == "account" and args.account:
        EmailEnum(
            args.account,
            domain_list=args.domain_list,
            strings=args.strings,
            custom_domains=args.custom_domains,
        ).find()
    else:
        exit("[red]Invalid command.[/red]")


if __name__ == "__main__":
    main()
