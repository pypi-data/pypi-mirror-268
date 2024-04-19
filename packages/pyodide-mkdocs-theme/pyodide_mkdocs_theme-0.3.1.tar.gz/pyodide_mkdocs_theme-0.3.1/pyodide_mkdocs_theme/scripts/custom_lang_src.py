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

from pyodide_mkdocs_theme.pyodide_macros import (
    PyodideMacrosPlugin,
    Msg, MsgPlural, TestsToken, Tip,
)


def define_env(env:PyodideMacrosPlugin):
    """ The customization has to be done at macro definition time.
        You could paste the code inside this function into your own main.py (or the equivalent
        package if you use a package instead of a single file). If you don't use personal macros
        so far, copy the full code into a `main.py` file at the root of your project (note: NOT
        in the docs_dir!)

        * Change whatever string you want.
        * Remove the entries you don't want to modify
        * See the documentation for more details about which string is used for what purpose
          and any constraints on the arguments.
        * DO NOT change the keyboard shortcuts (the values or for informational purpose only)

        Reminder:       Msg(msg)
                        MsgPlural(msg, plural="")
                        Tip(width_in_em, msg, kbd=None)
                        TestsToken(token_str)
    """

    custom = {
    # Editors:
        "comments":   Tip(15, "(Dés-)Active le code après la ligne <code>{tests}</code> "
                             "(insensible à la casse)", "Ctrl+I"),
        "tests":      TestsToken("\n\n# Tests\n\n"),


    # Terminals
        "run_script":    Msg("Script lancé..."),
        "success_msg":   Msg("Terminé sans erreur !"),
        "install_start": Msg("Installation de paquets python. Ceci peut prendre un certain temps..."),
        "install_done":  Msg("Installations terminées!"),
        "feedback":      Tip(15, "Tronquer ou non le feedback dans les terminaux (sortie standard"
                                " & stacktrace / relancer le code pour appliquer)"),

    # Terminals: validation success/failure messages
        "success_head":  Msg("Bravo !"),
        "success_head_extra":  Msg("Vous avez réussi tous les tests !"),
        "fail_head":     Msg("Dommage !"),
        "success_tail":  Msg("Pensez à lire"),
        "reveal_corr":   Msg("le corrigé"),
        "reveal_join":   Msg("et"),
        "reveal_rem":    Msg("les commentaires"),
        "fail_tail":     MsgPlural("est maintenant disponible", "sont maintenant disponibles"),


    # Corr  rems admonition:
        "title_corr": Msg('Solution'),
        "title_rem":  Msg('Remarques'),
        "corr":       Msg('🐍 Proposition de correction'),
        "rem":        Msg('Remarques'),


    # IDEs buttons & counter:
        "play":       Tip(9,  "Exécuter le code", "Ctrl+S"),
        "check":      Tip(9,  "Valider", "Ctrl+Enter"),
        "download":   Tip(0,  "Télécharger"),
        "upload":     Tip(0,  "Téléverser"),
        "restart":    Tip(0,  "Réinitialiser l'éditeur"),
        "save":       Tip(0,  "Sauvegarder dans le navigateur"),
        "attempts_left": Msg("Évaluations restantes"),

    # QCMS
        "qcm_title":     MsgPlural("Question"),
        "qcm_mask_tip":  Tip(15, "Les réponses resteront cachées..."),
        "qcm_check_tip": Tip(11, "Vérifier les réponses"),
        "qcm_redo_tip":  Tip(9,  "Recommencer"),

    # Others
        "tip_trash": Tip(15, "Supprimer du navigateur les codes enregistrés pour {site_name}")
    }

    env.lang.overload(custom)
