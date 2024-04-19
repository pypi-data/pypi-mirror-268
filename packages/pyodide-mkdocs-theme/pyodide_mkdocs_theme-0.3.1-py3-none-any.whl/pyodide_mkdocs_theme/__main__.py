"""
pyodide-mkdocs-theme
Copyleft GNU GPLv3 🄯 2024 Frédéric Zinelli

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.
If not, see <https://www.gnu.org/licenses/>.
"""

from pathlib import Path
from argparse import ArgumentParser
from contextlib import redirect_stdout

from .__version__ import __version__
from .scripts.custom_lang import display_lang
from .scripts.mkdocs_yaml import display_yml



parser = ArgumentParser(
    'pyodide_mkdocs_theme',
    description="Scripts for pyodide-mkdocs-theme",
    epilog="""Copyleft GNU GPLv3 🄯 2024 Frédéric Zinelli

This program comes with ABSOLUTELY NO WARRANTY."""
)
parser.add_argument(
    '-V', '--version', action='version', version=f'pyodide-mkdocs-theme {__version__}'
)
parser.add_argument(
    '--lang', action='store_true', help='Print the base python code to customize some messages.'
)
parser.add_argument(
    '--yml', action='store_true', help='Print a base configuration for the mkdocs.yml file.'
)
parser.add_argument(
    '-F', '--file', default="",
    help='Use this argument to write the information into a file instead of the stdout '
         '(existing content will be overridden. Use an absolute path or relative to cwd).'
)



def main():
    # pylint: disable=multiple-statements

    args = parser.parse_args()

    def inner():
        if args.yml:     display_yml()
        elif args.lang:  display_lang()


    if not args.file:
        inner()

    else:
        path = Path(args.file)
        path.touch(exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f, redirect_stdout(f):
            inner()



if __name__ == '__main__':
    main()
