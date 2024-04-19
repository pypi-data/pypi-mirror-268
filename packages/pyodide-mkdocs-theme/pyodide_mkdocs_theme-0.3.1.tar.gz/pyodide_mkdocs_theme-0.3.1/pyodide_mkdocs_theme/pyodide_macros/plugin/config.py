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


from mkdocs.config.base import Config
from mkdocs.config import config_options as C

from mkdocs_macros.plugin import MacrosPlugin
from .maestro_tools import typ_deprecated_with_custom_msg







# Verify if something changed on the MacrosPlugin side... (moved to on_startup)
# Current setup for MacrosPlugin v1.0.5

_EXPECTED_MACRO_CONF = set("""
module_name
modules
render_by_default
include_dir
include_yaml
j2_block_start_string
j2_block_end_string
j2_variable_start_string
j2_variable_end_string
on_undefined
on_error_fail
verbose
""".strip().splitlines())

_SRC_MACROS_CONF = dict(MacrosPlugin.config_scheme)

_MISSING_MACROS_PLUGIN_PROPS = _EXPECTED_MACRO_CONF - set(_SRC_MACROS_CONF)
MISSING_MACROS_PROPS = (
    "" if not _MISSING_MACROS_PLUGIN_PROPS else "\nDisappeared from MacrosPlugin:" + ''.join(
        f'\n\t{name}' for name in _MISSING_MACROS_PLUGIN_PROPS
    )
)

_NEW_MACROS_PLUGIN_PROPS = set(_SRC_MACROS_CONF) - _EXPECTED_MACRO_CONF
EXTRAS_MACROS_PROPS = (
    "" if not _NEW_MACROS_PLUGIN_PROPS else "\nNew config in MacrosPlugin:" + ''.join(
        f'\n\t{name}' for name in _NEW_MACROS_PLUGIN_PROPS
    )
)


J2_STRING                  = _SRC_MACROS_CONF['include_dir'].default
DEFAULT_MODULE_NAME        = _SRC_MACROS_CONF['module_name'].default
DEFAULT_UNDEFINED_BEHAVIOR = _SRC_MACROS_CONF['on_undefined'].default







class OtherConfig(Config):
    """ Options used in the macros that have not been updated yet """

    scripts_url = typ_deprecated_with_custom_msg('scripts_url', str)
    site_root   = typ_deprecated_with_custom_msg('site_root', str)




class IdeConfig(Config):
    """ All options related to validation tests (IDEs) """

    show_assertion_code_on_failed_test = C.Type(bool, default=True)
    """
    When an assertion fails in the secret tests and that assertion doesn't have any assertion
    message, the code of the assertion itself will be displayed in the terminal if this option
    is set to True (default).

    This behavior is global, but can be overridden on a "per IDE" base, using the `auto_log_assert`
    optional argument.
    """

    max_attempts_before_corr_available = C.Type(int, default=5)
    """
    Global setting for all IDE in the documentation: max number of tries a user can do before
    correction and remarks become available (reminder: they are in a collapsed details/admonition,
    requiring the user to click to reveal the content. This way, they can still try to get the code
    right without actually seeing the solution, before actually giving up).

    This behavior is global, but can be overridden on a "per IDE" base, using the `MAX` optional
    argument.
    """

    decrease_attempts_on_user_code_failure = C.Type(bool, default=True)
    """
    If true, any failure when running the user code during a validation will decrease the number
    of attempts left. Note this means even syntax errors will decrease the count.

    When this option is set to True, any error raised within the code of the editor will stop
    the validation process without modifying the number of attempts left.
    """







class BuildConfig(Config):
    """ Build configuration options """


    ignore_macros_plugin_diffs = C.Type(bool, default=False)
    """
    Set to True to bypass the compatibility check of the `PyodideMacrosPlugin` config against
    the original `MacrosPlugin` one.

    ??? note "Reasons behind this verification"

        `MacrosPlugin` is configured the "old fashion" way while `PyodideMacrosPlugin` is using
        mkdocs 1.5+ Config classes. This means that the `MacrosPlugin` configuration had to be
        hardcoded in the `PyodideMacrosPlugin` config.

        Because of this, any config change on the `MacrosPlugin` side could break
        `PyodideMacrosPlugin` without warning, so this verification enforce the expected
        implementation of the parent class.

        If ever something unexpected is found, the build will be aborted, because no guarantee
        can be given about the correctness of the build in such a situation.

        In case of minor changes, this option will allow the build, but use it "at your own risks".
    """



    skip_py_md_paths_names_validation = C.Type(bool, default=False)
    """
    By default, the path names of all the `.py` and `.md` files present in the docs_dir are
    checked so that they do not contain any character other than letters, digits, dot or dash.
    This ensures that the macros related to IDEs will work properly.

    If unwanted characters are found, a BuildError is raised, but this verification can be turned
    off by setting this flag to True. Use it at your own risks.
    """



    check_python_files = C.Type(bool, default=False)
    """
    If True, the different sections of the python files will be tested against each others during
    the build and provide feedback in the console.

    Unless the `soft_check` option is used, a BuildError will be raised if something considered
    wrong happens. See the documentation for more details.

    Warning:
        - This is totally independent from the pyodide environment. For example, it won't
          give any warning if a forbidden function is used in the tests (which will fail
          on the website).
        - These verifications __considerably increase the build time__ (expect something
          around x10).
    """

    soft_check = C.Type(bool, default=True)
    """
    If True and `check_python_files` is also True, the python sections are verified, but the
    build won't be interrupted if something wrong or suspicious is discovered: a message will
    instead be displayed in the console.
    """



    load_yaml_encoding = C.Type(str, default='utf-8')
    """
    Encoding to use when loading yaml data with the original MacrosPlugin functionalities :

    The original method doesn't use any encoding argument, which can lead to different behaviors
    between Windows and Linux (typically: during a pipeline!).

    ??? note "Should be removed in the future"
        PR has been posted with the change on their repo. If ever it gets merged, this will
        have to be updated.
    """


    macros_with_indents = C.ListOfItems(C.Type(str), default=[])
    """
    Allow to register external macros, as a list of strings, that will need to insert properly
    indented multiline contents in the page.

    This is relying on `PyodideMacrosPlugin.get_indent` logistic.
    """


    bypass_indent_errors = C.Type(bool, default=False)
    """
    If True, all errors raised when trying to find what is the indentation level of a macro call
    are bypassed and a message is instead printed to the console.

    The purpose of this option is _not_ to deactivate the securities, but to allow gathering info
    about all the indentation problems at once: the resulting markdown content will most likely be
    incorrect and be rendered with unexpected results.
    """


    encrypt_corrections_and_rems = C.Type(bool, default=True)
    """
    If True, the html div under IDEs containing correction and remarks will be encrypted at build
    time.

    Passing this to False can be useful during development, but value should _ALWAYS_ be set
    to true on the deployed website: keep in mind the search engine can otherwise make surface
    contents from corrections and remarks as suggestions when the user is using the search bar.
    """



class QcmsConfig(Config):
    """ Options specific to the QCMs or QCSs"""

    multi = C.Optional(C.Choice((True, False, None), default=None))
    """
    Global choice for the `multi` argument.

    If this option is set to `True` or `False`, it will act as a documentation-wide setting to
    disambiguate questions having 0 or 1 correct answers only.
    """



# This only defines the values exposed to the user in mkdocs.yml.
# When a property is declared here, don't forgot to add the related extractor on the
# BaseMaestro class.
class PyodideMacrosConfig(Config):
    """ Configuration for the main pyodide-mkdocs-theme plugin. """


    build = C.SubConfig(BuildConfig)
    """ Build related options """


    ides = C.SubConfig(IdeConfig)
    """ Configuration related to the validation tests in IDEs """


    qcms = C.SubConfig(QcmsConfig)
    """ QCMs related options """


    _dev_mode = C.Type(bool, default=False)
    """ Run the plugin in development mode (...don't use that). """


    _others = C.SubConfig(OtherConfig)
    """ Old configuration options (unmaintained, so far) """


    # ---------------------------------------------------------------------------------------
    # Replication of MacrosPlugin options (merging the config_scheme properties programmatically
    # is not enough, unfortunately...)


    render_by_default        = C.Type(bool, default=True)
    """
    Render macros on all pages by default. If set to false, sets an opt-in mode where only pages
    marked with render_macros: true in header will be displayed.
    """
    module_name              = C.Type(str,  default=DEFAULT_MODULE_NAME)
    """
    Name of the Python module containing macros, filters and variables. Indicate the file or
    directory, without extension; you may specify a path (e.g. include/module). If no main
    module is available, it is ignored.
    """
    modules                  = C.Type(list, default=[])
    """
    List of pluglets to be added to mkdocs-macros (preinstalled Python modules that can be listed
    by pip list).
    """
    include_dir              = C.Type(str,  default=J2_STRING)
    """ Directory for including external files """
    include_yaml             = C.Type(list, default=[])
    """ Non-standard Jinja2 marker for start of block """
    j2_block_start_string    = C.Type(str,  default=J2_STRING)
    """ Non-standard Jinja2 marker for start of variable """
    j2_block_end_string      = C.Type(str,  default=J2_STRING)
    """ Non-standard Jinja2 marker for end of block """
    j2_variable_start_string = C.Type(str,  default=J2_STRING)
    """ Non-standard Jinja2 marker for end of variable """
    j2_variable_end_string   = C.Type(str,  default=J2_STRING)
    """ Non-standard Jinja2 marker for end of variable """
    on_error_fail            = C.Type(bool, default=False)
    """
    Make the building process fail in case of an error in macro rendering (this is useful when
    the website is rebuilt automatically and errors must be detected.)
    """
    on_undefined             = C.Type(str,  default=DEFAULT_UNDEFINED_BEHAVIOR)
    """
    Behavior of the macros renderer in case of an undefined variable in a page. By default, it
    leaves the Jinja2 statement untouched (e.g. {{ foo }} will appear as such in the page.) Use
    the value 'strict' to make it fail.
    """
    verbose                  = C.Type(bool, default=False)
    """ Print debug (more detailed) statements in the console. """
