from e2e_cli.core.py_manager import Py_version_manager
from e2e_cli.core import constants


# =========================================
# Custom help formatter for our argparser
# ==========================================
def cli_formatter():
    from argparse import HelpFormatter, _SubParsersAction

    class NoSubparsersMetavarFormatter(HelpFormatter):

        def _format_action(self, action):
            result = super(NoSubparsersMetavarFormatter,
                        self)._format_action(action)
            if isinstance(action, _SubParsersAction):
                return "%*s%s" % (self._current_indent, "", result.lstrip())
            return result

        def _format_action_invocation(self, action):
            if isinstance(action, _SubParsersAction):
                return ""
            return super(NoSubparsersMetavarFormatter,
                        self)._format_action_invocation(action)

        def _iter_indented_subactions(self, action):
            if isinstance(action, _SubParsersAction):
                try:
                    get_subactions = action._get_subactions
                except AttributeError:
                    pass
                else:
                    for subaction in get_subactions():
                        yield subaction
            else:
                for subaction in super(NoSubparsersMetavarFormatter,
                                    self)._iter_indented_subactions(action):
                    yield subaction
    
    return NoSubparsersMetavarFormatter



# =========================
# e2e pkg/ver-info functions
# =========================
def e2e_version_info():
        print(constants.PACKAGE_VERSION)

def e2e_pakage_info():
        print(constants.PACKAGE_INFO)


# =========================
# e2e Parsing errors
# =========================

def show_parsing_error(Parsing_Errors):
    if(Parsing_Errors):
        print("Parsing Errors :")
        print(*Parsing_Errors, sep="\n")
        print("")