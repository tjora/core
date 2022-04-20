from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Acmeda Rollers from a config entry."""
    hub = hass.data[DOMAIN][config_entry.entry_id]


class TemperatureSensor(SensorEntity):
    @property
    def name(self):
        return "Temperature"

    @property
    def native_value(self):
        return 24

    @property
    def native_unit_of_measurement(self) -> str:
        return TEMP_CELSIUS
