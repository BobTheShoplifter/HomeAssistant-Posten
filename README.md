# HomeAssistant-Posten
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/BobTheShoplifter/HomeAssistant-Posten)

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

[![Project Maintenance][maintenance-shield]][user_profile]

[![Discord][discord-shield]][discord]

_Component to integrate with [posten][posten]._

Posten integrasjon som trigger dagen når posten kommer: https://www.posten.no/levering-av-post

![screenshot](https://i.imgur.com/ZOISPzB.png)

![screenshot2](https://i.imgur.com/A09Ldga.png)

**This component will set up the following platforms.**

| Platform | Description         |
| -------- | ------------------- |
| `sensor` | Show info from API. |
| `binary_sensor` | Show info from API as True or False based on mail times. |

## Installation

### Method 1 (Installation using HACS)
1. Go to http://yourhomeassistant:8123/hacs/integrations
2. Press the 3 dots, click Custom repositories
3. Add https://github.com/BobTheShoplifter/HomeAssistant-Posten as an integration
4. Download the integration by searching posten

### Method 2 (Manual)
Copy contents of custom_components/posten/ to custom_components/posten/ in your Home Assistant config folder.


## Configuration is done in the UI

<!---->

---

[posten]: https://posten.no
[commits-shield]: https://img.shields.io/github/commit-activity/y/BobTheShoplifter/HomeAssistant-Posten.svg?style=for-the-badge
[commits]: https://github.com/BobTheShoplifter/HomeAssistant-Posten/commits/master
[discord]: https://2o.no/discord
[discord-shield]: https://img.shields.io/discord/856974237956177920.svg?style=for-the-badge
[license]: https://github.com/BobTheShoplifter/HomeAssistant-Posten/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/BobTheShoplifter/HomeAssistant-Posten.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Daniel%20Christensen-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/BobTheShoplifter/HomeAssistant-Posten.svg?style=for-the-badge
[releases]: https://github.com/BobTheShoplifter/HomeAssistant-Posten/releases
[user_profile]: https://github.com/BobTheShoplifter
