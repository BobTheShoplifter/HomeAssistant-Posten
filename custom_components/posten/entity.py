"""PostenEntity class"""
import datetime
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME, VERSION, ATTRIBUTION


class IntegrationPostenEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry):
        super().__init__(coordinator)
        self.config_entry = config_entry

    @property
    def _delivery_dates(self) -> list[datetime.date]:
        """Return valid delivery dates from the coordinator data."""
        raw_dates = (self.coordinator.data or {}).get("delivery_dates", [])
        if not isinstance(raw_dates, list):
            return []

        dates = []
        for raw_date in raw_dates:
            if not isinstance(raw_date, str):
                continue
            try:
                dates.append(datetime.date.fromisoformat(raw_date[:10]))
            except ValueError:
                continue

        return sorted(set(dates))

    @property
    def _next_delivery(self) -> datetime.date | None:
        """Return the next delivery as datetime.date."""
        return next(iter(self._delivery_dates), None)

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return self.config_entry.entry_id

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.config_entry.entry_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": NAME,
        }

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            "id": self.unique_id,
            "integration": DOMAIN,
            "delivery_dates": [date.isoformat() for date in self._delivery_dates],
        }
