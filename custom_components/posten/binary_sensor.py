"""Binary sensor platform for posten."""
import datetime
from homeassistant.components.binary_sensor import BinarySensorEntity

from .const import (
    BINARY_SENSOR,
    BINARY_SENSOR_DEVICE_CLASS,
    DEFAULT_NAME,
    DOMAIN,
    ICON,
    ICON_OPEN
)
from .entity import IntegrationPostenEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([IntegrationPostenBinarySensor(coordinator, entry)])


class IntegrationPostenBinarySensor(IntegrationPostenEntity, BinarySensorEntity):
    """posten binary_sensor class."""

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DEFAULT_NAME}_{BINARY_SENSOR}"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        nextdelivery = self.coordinator.data.get("delivery_dates")

        year, month, day = map(int, nextdelivery[0].split("-"))

        d1 = datetime.date(year, month, day)

        return datetime.date.today() == d1

    @property
    def icon(self):
        """Return the icon of the sensor."""
        nextdelivery = self.coordinator.data.get("delivery_dates")

        year, month, day = map(int, nextdelivery[0].split("-"))

        d1 = datetime.date(year, month, day)

        if datetime.date.today() == d1:
            return ICON_OPEN
        return ICON