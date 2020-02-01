"""HACS Configuration Schemas."""
# pylint: disable=dangerous-default-value
import voluptuous as vol
from .const import LOCALE

# Configuration:
TOKEN = "token"
SIDEPANEL_TITLE = "sidepanel_title"
SIDEPANEL_ICON = "sidepanel_icon"
APPDAEMON = "appdaemon"
PYTHON_SCRIPT = "python_script"
THEME = "theme"

# Options:
COUNTRY = "country"
DEBUG = "debug"
RELEASE_LIMIT = "release_limit"
EXPERIMENTAL = "experimental"


def hacs_base_config_schema(config: dict = {}) -> dict:
    """Return a shcema configuration dict for HACS."""
    if not config:
        config = {TOKEN: "xxxxxxxxxxxxxxxxxxxxxxxxxxx"}
    return {vol.Required(TOKEN, default=config.get(TOKEN)): str}


def hacs_config_option_schema(options: dict = {}) -> dict:
    """Return a shcema for HACS configuration options."""
    if not options:
        options = {
            APPDAEMON: False,
            COUNTRY: "ALL",
            DEBUG: False,
            EXPERIMENTAL: False,
            RELEASE_LIMIT: 5,
            SIDEPANEL_ICON: "mdi:store",
            SIDEPANEL_TITLE: "HACS",
        }
    return {
        vol.Optional(SIDEPANEL_TITLE, default=options.get(SIDEPANEL_TITLE)): str,
        vol.Optional(SIDEPANEL_ICON, default=options.get(SIDEPANEL_ICON)): str,
        vol.Optional(COUNTRY, default=options.get(COUNTRY)): vol.In(LOCALE),
        vol.Optional(RELEASE_LIMIT, default=options.get(RELEASE_LIMIT)): int,
        vol.Optional(APPDAEMON, default=options.get(APPDAEMON)): bool,
        vol.Optional(EXPERIMENTAL, default=options.get(EXPERIMENTAL)): bool,
        vol.Optional(DEBUG, default=options.get(DEBUG)): bool,
    }
