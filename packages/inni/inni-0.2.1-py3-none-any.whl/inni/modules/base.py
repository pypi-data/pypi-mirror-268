from rich.console import Console

from inni.template import template_to_vars


class BaseModule:
    login_template_keys = ()
    logout_template_keys = ()

    def __init__(self, config: dict, out: Console, err: Console):
        self.config = config
        self.out = out
        self.err = err
        self.setUp()

    def setUp(self):
        pass

    def template_variables(self) -> dict[str, tuple[str, ...]]:
        """
        Returns the list of variables that the module expects
        """

        def keys_to_vars(keys):
            return tuple(
                var
                for key in keys
                for var in template_to_vars(self.config.get(key, ""))
            )

        return {
            "login": keys_to_vars(self.login_template_keys),
            "logout": keys_to_vars(self.logout_template_keys),
        }

    def login(self, responses: dict):
        raise NotImplementedError()

    def logout(self, responses: dict):
        raise NotImplementedError()
