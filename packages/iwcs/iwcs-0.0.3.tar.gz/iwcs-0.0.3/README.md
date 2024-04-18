# IWCS - WiFi Client Stats Utility

This utility collects statistics of WiFi clients connected to a specified interface on your system.

## Prerequisites

Ensure that the `iw` command-line tool is installed on your system. If not, you can install it using the following command:

```bash
sudo apt-get install iw
```

## Usage

### Python Function

You can use the provided Python function `info(interface)` to collect WiFi client statistics.

```python
from iwcs import info

# Replace 'wlan0' with your wireless interface if necessary
stats = info(interface='wlan0')
print(stats)
```

The function returns a dictionary containing connection stats for each connected client identified by their MAC address.

### Example

```python
from iwcs import info

interface = "wlan0"  # Replace with your wireless interface
connected_clients_info = info(interface)
print(connected_clients_info)
```

## Output

The output is a dictionary where each key represents a MAC address of a connected client. The corresponding value is another dictionary containing various statistics such as inactive time, received bytes, transmitted bytes, signal level, etc.

---

## License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.


