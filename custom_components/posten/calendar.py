from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.core import callback
from homeassistant.util.dt import parse_datetime, as_utc, now
import datetime
from .const import DOMAIN

class PostenCalendarEntity(CalendarEntity):
    """Representation of a Posten Calendar Entity."""

    def __init__(self, coordinator, name, config_entry):
        """Initialize the calendar entity."""
        self.coordinator = coordinator
        self._name = name
        self._events = []
        self.config_entry = config_entry
        self._fetch_events()

    @property
    def name(self):
        """Return the name of the calendar entity."""
        return self._name

    @property
    def event(self):
        """Return the next upcoming event."""
        return self._get_next_event()
    
    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}"

    async def async_get_events(
        self,
        hass,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
    ) -> list[CalendarEvent]:
        """Return calendar events within a datetime range."""
        start_date = as_utc(start_date)
        end_date = as_utc(end_date)
        return self._events
    
    async def async_update(self):
        """Update the calendar with new events from the API."""
        self._events = self._fetch_events()

    def _fetch_events(self):
        """Call Posten API to fetch delivery dates."""
        deliveries = self.coordinator.data.get("delivery_dates")
        events = []
        for delivery in deliveries:
            delivery_date = parse_datetime(delivery).date()
            if delivery_date:
                events.append(CalendarEvent(
                    summary="Levering",
                    start=delivery_date,
                    end=delivery_date + datetime.timedelta(days=1)
                ))
        self._events = events
        return events

    def _get_next_event(self):
        """Return the next upcoming event."""
        if not self._events:
            return None
        return self._events[0]

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([PostenCalendarEntity(coordinator, "Posten Calendar", config_entry)])