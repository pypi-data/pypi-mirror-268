# UTE API Wrapper 🇺🇾

# THIS API NO LONGER WORKS

UTE deprecated the API that this wrapper uses on April 15th 2024. More information [here](https://github.com/rogsme/ute_homeassistant_integration/issues/3#issuecomment-2054332575).

I'll archive this repository in a few days.

<p align="center">
    <img src="https://gitlab.com/uploads/-/system/project/avatar/48558040/icon.png" alt="ute-wrapper"/>
</p>

[![codecov](https://codecov.io/gl/rogs/ute/graph/badge.svg?token=D1B2J3EB6K)](https://codecov.io/gl/rogs/ute)
[![PyPI version](https://badge.fury.io/py/ute-wrapper.svg)](https://badge.fury.io/py/ute-wrapper)

This Python package provides a convenient wrapper for interacting with the [UTE (Administración Nacional de Usinas y Trasmisiones Eléctricas)](https://portal.ute.com.uy/) API in Uruguay 🇺🇾. It allows you to retrieve various information related to your UTE account, electricity consumption, network status, and more.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can install the UTE API Wrapper using pip:

```bash
pip install ute-wrapper
```

## Usage

Import the `UTEClient` class from the package and create an instance with your UTE account details:

```python
from ute_wrapper.ute import UTEClient

email = "your_email@example.com"
phone_number = "your_phone_number"
device_id = "your_device_id"  # Optional
average_cost_per_kwh = 4.0  # Optional, your average cost per kWh in UYU
power_factor = 0.9 # Optional, your power factor. It's almost always close to 1

ute_client = UTEClient(email, phone_number, device_id, average_cost_per_kwh, power_factor)
```

### Available Methods

- `get_devices_list()`: Get a list of UTE devices associated with the account.
- `get_account()`: Get UTE account information for the specified device ID.
- `get_peak()`: Get UTE peak information for the specified device ID.
- `get_network_status()`: Get UTE network status information.
- `get_renewable_sources()`: Get the percentage of UTE renewable sources.
- `get_historic_consumption(date_start=None, date_end=None)`: Get historic UTE consumption information within a specified date range.
- `get_current_usage_info()`: Get current usage information for the specified device ID.
- `get_average_price(plan)`: Get the average price for a specific UTE plan ("triple" or "doble").


## Examples

### Get Historic Consumption

```python
historic_consumption = ute_client.get_historic_consumption(date_start="2023-08-01", date_end="2023-08-15")
print(historic_consumption)
```

### Get Current Usage Info

```python
current_usage_info = ute_client.get_current_usage_info()
print(current_usage_info)
```

## Contributing

Contributions are welcome! If you find a bug or have a suggestion, please create an issue or submit a Merge Request on [Gitlab](https://gitlab.com/rogs/ute).

## License

This project is licensed under the GNU General Public License, version 3.0. For more details, see [LICENSE](LICENSE).

---

*This project is not affiliated with UTE (Administración Nacional de Usinas y Trasmisiones Eléctricas) or its affiliates.*
