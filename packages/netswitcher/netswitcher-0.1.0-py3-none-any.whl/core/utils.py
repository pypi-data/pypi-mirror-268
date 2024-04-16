import re
from ipaddress import IPv4Address, AddressValueError


def is_valid_interface(name: str) -> bool:
    """Checks if name follows the pattern of <ge-(0-9)/(0-9)/(0-9)>"""
    return re.match(r"^ge-\d+/\d+/\d+$", name)


def is_valid_mac(mac: str) -> bool:
    return re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower())


def is_valid_ipv4(ip: str) -> bool:
    try:
        IPv4Address(ip)
        return True
    except AddressValueError:
        return False
