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

def display_lang():
    """ Display the base code for GUI messages customizations """

    src   = Path(__file__).with_name('custom_lang_src.py')
    code  = src.read_text(encoding='utf-8')
    start = code.index('"""', 3)
    out   = f"\n{ code[start+3:].strip() }\n"
    print(out)
