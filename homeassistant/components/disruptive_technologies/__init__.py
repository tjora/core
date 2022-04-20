"""The Disruptive Technologies integration."""
from __future__ import annotations

import disruptive as dt

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_CLIENT_ID, CONF_CLIENT_SECRET, CONF_EMAIL, Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Disruptive Technologies from a config entry."""
    # TODO Store an API object for your platforms to access
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = DtApi(
        email=entry.data["email"],
        secret=entry.data["secret"],
        key_id=entry.data["key_id"],
    )

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class DtApi:
    """DtApi for interacting"""

    def __init__(self, email, secret, key_id):
        self.auth = dt.Auth.service_account(
            key_id=key_id,
            secret=secret,
            email=email,
        )
