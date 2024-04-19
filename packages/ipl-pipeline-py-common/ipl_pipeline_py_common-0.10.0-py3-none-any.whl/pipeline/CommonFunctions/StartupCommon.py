import os
import logging


class StartupVariablesCommon:
    """
    Grabs variables from environment variables
    """
    node_id: str
    debug: bool

    @staticmethod
    def _get_key_or_error(key_name: str) -> str:
        """
        Gets a value from env, errors out if value not found
        :param key_name: key name
        :return: key value
        """
        if not (return_value := os.getenv(key_name)):
            logging.error(f"static.env - '{key_name}' key not found. Cannot start API.")
            raise EnvironmentError
        return return_value

    @staticmethod
    def _get_key_or_default(key_name: str, default_value: str) -> str:
        """
        Gets a value from env, if env have no value, will return the default value given
        :param key_name: key name
        :param default_value: default value
        :return: key/default value
        """
        if not (return_value := os.getenv(key_name)):
            return_value = default_value
        return return_value

    def __init__(self):
        self.node_id = self._get_key_or_default("NODE_ID", "unknown")
        self.debug = bool(self._get_key_or_default("DEBUG", "False") == "True" or "1")

    @property
    def node_id_int(self) -> int:
        if self.node_id == "unknown":
            return -1
        return int(self.node_id)
