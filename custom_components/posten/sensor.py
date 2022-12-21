"""Sensor platform for integration_posten."""
from homeassistant.components.sensor import SensorEntity

from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import IntegrationPostenEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([IntegrationPostenSensor(coordinator, entry)])


class IntegrationPostenSensor(IntegrationPostenEntity, SensorEntity):
    """integration_posten Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        return self.coordinator.data.get("isStreetAddressReq")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON