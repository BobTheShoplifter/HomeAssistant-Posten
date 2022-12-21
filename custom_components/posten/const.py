"""Constants for posten."""
# Base component constants
NAME = "Når kommer Posten"
DOMAIN = "posten"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "1.0.0"
ATTRIBUTION = "Data provided by https://www.posten.no/levering-av-post/_/component/main/1/leftRegion/1?postCode=xxxx"
ISSUE_URL = "https://github.com/BobTheShoplifter/HomeAssistant-Posten/issues"

# Icons
ICON = "mdi:format-quote-close"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_POSTALCODE = "postalcode"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""