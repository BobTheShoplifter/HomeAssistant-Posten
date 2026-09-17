"""Calendar platform for Posten delivery dates."""
from __future__ import annotations

import datetime

from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util.dt import as_utc, now

from .const import DOMAIN


class PostenCalendarEntity(CoordinatorEntity, CalendarEntity):
    """Representation of a Posten calendar entity."""

    def __init__(self, coordinator, config_entry) -> None:
        """Initialize the calendar entity."""
        super().__init__(coordinator)
        self._attr_name = "Posten Calendar"
        self._events: list[CalendarEvent] = []
        self.config_entry = config_entry
        self._update_events()

    @property
    def event(self) -> CalendarEvent | None:
        """Return the current or next upcoming event."""
        today = now().date()
        return next(
            (event for event in self._events if event.end > today),
            None,
        )

    @property
    def unique_id(self) -> str:
        """Return a unique ID to use for this entity."""
        return self.config_entry.entry_id

    async def async_get_events(
        self,
        hass: HomeAssistant,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
    ) -> list[CalendarEvent]:
        """Return calendar events within a datetime range."""
        start = as_utc(start_date).date()
        end = as_utc(end_date).date()
        return [
            event
            for event in self._events
            if event.start < end and event.end > start
        ]

    @callback
    def _handle_coordinator_update(self) -> None:
        """Update cached events when the coordinator receives new data."""
        self._update_events()
        super()._handle_coordinator_update()

    def _update_events(self) -> None:
        """Build calendar events from the coordinator data."""
        raw_deliveries = (self.coordinator.data or {}).get("delivery_dates", [])
        if not isinstance(raw_deliveries, list):
            raw_deliveries = []

        events = []
        for delivery in raw_deliveries:
            if not isinstance(delivery, str):
                continue
            try:
                delivery_date = datetime.date.fromisoformat(delivery[:10])
            except ValueError:
                continue
            events.append(
                CalendarEvent(
                    summary="Levering",
                    start=delivery_date,
                    end=delivery_date + datetime.timedelta(days=1),
                )
            )

        self._events = sorted(events, key=lambda event: event.start)


async def async_setup_entry(hass, config_entry, async_add_entities) -> None:
    """Set up the Posten calendar platform."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([PostenCalendarEntity(coordinator, config_entry)])
