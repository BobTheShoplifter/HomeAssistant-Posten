"""Constants for posten."""
# Base component constants
NAME = "Når kommer Posten"
DOMAIN = "posten"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.1.8"
ATTRIBUTION = "Data provided by https://www.posten.no/levering-av-post/_/component/main/1/leftRegion/9?postCode=xxxx"
ISSUE_URL = "https://github.com/BobTheShoplifter/HomeAssistant-Posten/issues"

# Icons
ICON = "mdi:mailbox"
ICON_OPEN = "mdi:mailbox-open"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "None"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
PLATFORMS = [BINARY_SENSOR, SENSOR]


# Configuration and options
CONF_ENABLED = "enabled"
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

DAYS = {
    "0": "Søndag",
    "1": "Mandag",
    "2": "Tirsdag",
    "3": "Onsdag",
    "4": "Torsdag",
    "5": "Fredag",
    "6": "Lørdag",
}
