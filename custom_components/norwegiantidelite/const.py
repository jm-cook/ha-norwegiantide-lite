"""Constants for NorwegianTide."""
from homeassistant.components.sensor.const import SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfTime, UnitOfLength, Platform

# from .api import CONST_DIR_DEFAULT

# Base component constants
NAME = "Norwegian Tide Lite"
DOMAIN = "norwegiantidelite"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.1.4"
ATTRIBUTION = "Data from ©Kartverket (www.kartverket.no)"
MANUFACTURER = f"{NAME}"
ISSUE_URL = "https://github.com/jm-cook/ha-norwegiantide-lite/issues"

# Platforms
PLATFORMS: list[Platform] = [Platform.SENSOR]

# Configuration and options
CONF_ENABLED = "enabled"
CONF_PLACE = "place"
CONF_LAT = "latitude"
CONF_LONG = "longitude"
CONF_STRINGTIME = "%d.%m %H:%M"

# Defaults
STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

TIDE_EBB = "ebb"
TIDE_FLOW = "flow"
TIDE_LOW = "low"
TIDE_HIGH = "high"
TIDE_STATUS = {
    1: TIDE_EBB,
    2: TIDE_FLOW,
}

ENTITIES = {
    "tide_main": {
        "type": "sensor",
        "key": "currentdata.forecast",
        "attrs": [
            CONF_LAT,
            CONF_LONG,
            "location_details",
            "ebb_flow",
            "ebbing",
            "flowing",
            "tide_state",
            # "next_tide",
            # "next_tide_high",
            "currentdata.prediction",
            "currentdata.forecast",
            "currentdata.observation",
            "currentobservation.weathereffect"
        ],
        "units": UnitOfLength.CENTIMETERS,
        "convert_units_func": None,
        "device_class": SensorStateClass.MEASUREMENT,
        "icon": "mdi:wave",
        "state_func": None,
    },
    "tide_next_low": {
        "type": "sensor",
        "key": "next_tide_low.time",
        "attrs": ["next_tide_low"],
        "units": None,
        "convert_units_func": "",
        "device_class": SensorDeviceClass.TIMESTAMP,
        "icon": "mdi:wave",
    },
    "tide_next_high": {
        "type": "sensor",
        "key": "next_tide_high.time",
        "attrs": ["next_tide_high"],
        "units": None,
        "convert_units_func": "",
        "device_class": SensorDeviceClass.TIMESTAMP,
        "icon": "mdi:waves",
    },
    # "tide_state": {
    #     "type": "sensor",
    #     "key": "tide_state",
    #     "attrs": ["next_tide_time"],
    #     "units": None,
    #     "convert_units_func": None,
    #     "device_class": None,
    #     "icon": "mdi:wave",
    # },
    # "tide_prediction": {
    #     "type": "sensor",
    #     "key": "currentdata.prediction",
    #     "attrs": [
    #         "ebb_flow",
    #         "next_tide_time"
    #     ],
    #     "units": UnitOfLength.CENTIMETERS,
    #     "convert_units_func": None,
    #     "device_class": None,
    #     "icon": "mdi:wave",
    # },
    # "tide_forecast": {
    #     "type": "sensor",
    #     "key": "currentdata.forecast",
    #     "attrs": [
    #         "ebb_flow",
    #         "next_tide_time"
    #     ],
    #     "units": UnitOfLength.CENTIMETERS,
    #     "convert_units_func": None,
    #     "device_class": None,
    #     "icon": "mdi:wave",
    # },
    # "tide_observation": {
    #     "type": "sensor",
    #     "key": "currentobservation.observation",
    #     "attrs": [
    #         "ebb_flow",
    #         "next_tide_time",
    #         "time_to_next_tide",
    #     ],
    #     "units": UnitOfLength.CENTIMETERS,
    #     "convert_units_func": None,
    #     "device_class": None,
    #     "icon": "mdi:wave",
    # },
    "tide_weathereffect": {
        "type": "sensor",
        "key": "currentobservation.weathereffect",
        "attrs": [],
        "units": UnitOfLength.CENTIMETERS,
        "convert_units_func": None,
        "device_class": None,
        "icon": "mdi:wave",
    }
}
