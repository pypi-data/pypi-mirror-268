import subprocess
from pathlib import Path


if not Path('/sbin/iw').is_file():
    raise FileNotFoundError('command `iw` not found, please run `sudo apt-get install iw`')


def mac(mac_address: str, interface: str = 'wlan0') -> dict:
    """
    Gather the information in relation to a single sensor by MAC address.
    """
    client_info_dict = dict()
    try:
        client_info_output = subprocess.check_output(
            ["/sbin/iw", "dev", interface, "station", "get", mac_address]
        ).decode(
            "utf-8")
        client_info_lines = client_info_output.split("\n")
        client_info_dict = {}
        for line in client_info_lines:
            if ":" in line:
                key, value = line.split(":", 1)
                client_info_dict[key.strip()] = value.strip()
    except subprocess.CalledProcessError:
        print(f'client {mac_address} not found on interface {interface}')
    return client_info_dict


def info(interface: str = 'wlan0') -> dict:
    """
    This will grab the connection stats of the clients connected to the specified interface.

    returns: {'<MAC ADDRESS>': {'inactive time': <value>, 'rx bytes': <value>, ...}}
    """
    mac_addresses_output = subprocess.check_output(["/sbin/iw", "dev", interface, "station", "dump"]).decode("utf-8")
    mac_addresses_list = [line.split()[1] for line in mac_addresses_output.split("\n") if "Station" in line]
    clients_info = {}
    for mac_address in mac_addresses_list:
        client_info_dict = mac(mac_address, interface)
        clients_info[mac_address] = client_info_dict
    return clients_info


def test():
    """
    Example usage:
    """
    interface = "wlan0"  # Replace with your wireless interface
    connected_clients_info = info(interface)
    print(connected_clients_info)
