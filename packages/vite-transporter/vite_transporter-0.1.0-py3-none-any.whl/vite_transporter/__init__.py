import sys

from .helpers import Colr as _Colr
from .helpers import PyProjectConfig as _PyProjectConfig
from .helpers import _compile
from .parser import ArgumentParser as _ArgumentParser

__version__ = "0.1.0"


def _cli():
    pars = _ArgumentParser(prog="vtf", add_help=False)
    pars.add_argument(
        "--version", "-v", action="version", version=f"vite-to-flask {__version__}"
    )
    pars.add_argument("--help", "-h", action="help")

    subparsers = pars.add_subparsers()

    compile_parser = subparsers.add_parser("compile")
    compile_parser.set_defaults(compile=False)
    compile_parser.add_argument("-y", action="store_true")

    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(list=False)

    ls_parser = subparsers.add_parser("ls")
    ls_parser.set_defaults(list=False)

    with _PyProjectConfig() as pyproject:
        pypro: _PyProjectConfig = pyproject

        for vite_app in pypro.vite_apps:
            pars.vite_apps.append(
                {
                    "vite_app": vite_app,
                    "serve_app": pypro.vt_config.get("serve_app"),
                }
            )

        args = pars.parse_args()

        if hasattr(args, "compile"):
            _compile(
                pyproject,
                pars.vite_apps,
                replace=True if hasattr(args, "y") and args.y else False,
            )

            # exit after compiling
            sys.exit(0)

        if hasattr(args, "list") or hasattr(args, "ls"):
            print("")
            if not pars.vite_apps:
                print(
                    f" {_Colr.WARNING}No vite apps found in pyproject.toml{_Colr.END}"
                )
            else:
                for app in pars.vite_apps:
                    print(
                        f"{_Colr.OKGREEN}{app.get('vite_app')}/dist/assets{_Colr.END} "
                        f"{_Colr.BOLD}=>{_Colr.END} "
                        f"{_Colr.OKGREEN}{app.get('serve_app')}/vt/{app.get('vite_app')}/{_Colr.END}"
                    )
            print("")

            # exit after listing
            sys.exit(0)

    # print help if no command is given
    pars.print_help()
