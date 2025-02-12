# Norwegian Tide Lite

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs) ![Maintenance](https://img.shields.io/maintenance/yes/2025.svg)

This is a Home Assistant custom integration for Norwegian Tide which is interfacing an open API by the [Norwegian Mapping Authority (Kartverket)](https://kartverket.no/en/), more precisely [sehavniva.no](http://www.sehavniva.no/) which provides information about water levels and tidal predicitions and forecasts. **All data is ©[Norwegian Mapping Authority (Kartverket)](https://kartverket.no/en/)**.

This light version is a fork of the code authored by [tmjo] without the camera entity included. The camera entity required
matplotlib to be installed and this fails with Raspberry Pi installations of Home Assistant. The version here
is quite different from the original, though the original author [tmjo] has done much of the "heavy lifting" to make this
integration work. The Norwegian Tide integration is slimmed down to remove some of the sensors and functionality that can
be provided by Home Assistant through templating. The full forecast is also not provided as part of the sensor entity anymore
but is available through a weather forecast style of service. This contributes to a reduction in the amount of storage required
for the tide state.

Unfortunately the service only provides data for geographical positions in Norway - this is a limitation in the API and not in this integration.

## Installation
There are different methods of installing the custom component. HACS is by far the simplest way for unexperienced users and is recomended.

### HACS installation
The installation is currently not included in HACS as a default repo, but can be installed through HACS *by adding this repo as a custom repository*.

1. Make sure you have [HACS](https://hacs.xyz/) installed in your Home Assistant environment.
2. Go to **HACS**, select **Integrations**.
3. Click on the three dots in the upper right corner and select **Custom repositories**
4. Copy/paste the **URL for this repo** `https://github.com/jm-cook/ha-norwegiantide-lite` into the URL-field, select **Integration as category** and then click **Add**.
5. You should now find the **Norwegian Tide** integration by searching for it in HACS, proceed to install it.
6. Restart Home Assistant (a warning should be shown in log saying you're using a custom integration).
7. Continue to the Configuration-section.


### Manual
1. Navigate to you home assistant configuration folder.
2. Create a `custom_components` folder of it does not already exist, then navigate into it.
3. Download the folder `norwegiantide_lite` from this repo and add it into your custom_components folder.
4. Restart Home Assistant (a warning should be shown in log saying you're using a custom integration).
5. Continue to the Configuration-section.


### Git installation
1. Make sure you have git installed on your machine.
2. Navigate to you home assistant configuration folder.
3. Create a `custom_components` folder of it does not already exist, then navigate into it.
4. Execute the following command: `git clone https://github.com/tmjo/ha-norwegiantide-lite ha-norwegiantide-lite`
5. Run `bash links.sh`
6. Restart Home Assistant (a warning should be shown in log saying you're using a custom integration).
7. Continue to the Configuration-section.

## Configuration
Configuration is done through UI/Lovelace. In Home Assistant, click on Configuration > Integrations where you add it with the + icon.

You will be asked to give your location a name and to provide latitude and longitude as geographical position for the location you want to track. Finally select which sensors you would like the integration to add. More detailed description of this will be added, but in short there is one main sensor which contains all info and for most people probably this may be sufficient. You do not need to add other entities unless you want, but several detailed entities are available if you prefer to have them as separate entities instead of attributes on the main sensor. There is also a camera entity which creates a plot of the data by using Matplotlib.

Entities can be added and removed by clicking *Options* in HA integreation view at any time. It is also possible to enable more than one location by adding the integration several times.

## Usage
Use the integration as you please, but a recommended plot is the [Apexchart-card](https://github.com/RomRider/apexcharts-card) by Romrider - it is an excellent graph card for lovelace which also enables the possibility to show future values. This is necessary to display prediction- and forecast values which are stored as attributes in the main sensor. Example:

![apexchart-card](img/norwegiantide_apexchart_.png "apexchart-card")

The example above was created using [Apexchart-card](https://github.com/RomRider/apexcharts-card). 

[See here for example configurations.](lovelace/README.md)

More detailed description will follow, but worth mentioning:
 - Prediction: A calculated prediction for the location
 - Forecast: Includes the weather effect on top of the prediction
 - Observation: The observed value on the closest station to your location

If you are curious about specific details and definitions, please see [www.sehavniva.no](http://www.sehavniva.no/).

The main sensor will keep the current forecast value as state and will contain all or most data as attributes. The other entities will contain more specific data according to their name.


## Issues and development
Please report issues on github. If you would like to contribute to development, please do so through PRs.

## License
MIT © [Tor Magne Johannessen][tmjo]. **All data is ©[Norwegian Mapping Authority (Kartverket)](https://kartverket.no/en/)**.

<!-- Badges -->
[hacs-url]: https://github.com/custom-components/hacs
[hacs-image]: https://img.shields.io/badge/HACS-Custom-orange.svg
[buymeacoffee-url]: https://www.buymeacoffee.com/tmjo
[buymeacoffee-image]: https://img.shields.io/badge/support-buymeacoffee-222222.svg?style=flat-square
[tmjo]: https://github.com/tmjo
[jmc]: https://github.com/jm-cook
