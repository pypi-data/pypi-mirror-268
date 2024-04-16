from netmiko import BaseConnection
import typer
from .utils import is_valid_interface, is_valid_ipv4


def create_acl_app(connection: BaseConnection):
    app = typer.Typer()

    @app.command()
    def create(name: str, ip: str):
        """Creates ACL rule with given name"""
        if not is_valid_ipv4(ip):
            print(f"{ip} is not valid IPv4 address")
            raise typer.Abort()
        connection.send_command("configure")
        connection.send_command(
            f"set firewall family ethernet-switching filter {name} term allow from ip-source-address {ip}/32"
        )
        connection.send_command(
            f"set firewall family ethernet-switching filter {name} term allow then accept"
        )
        connection.send_command(
            f"set firewall family ethernet-switching filter {name} term deny then discard"
        )
        connection.send_command("commit")
        print(f"IP {ip} added to ACL {name}")

    @app.command()
    def prune(name: str):
        """Deletes ACL rule with given name"""
        connection.send_command("configure")
        connection.send_command(
            f"delete firewall family ethernet-switching filter {name}"
        )
        connection.send_command("commit")
        print(f"ACL rule {name} deleted")

    @app.command()
    def delete(name: str, ip: str):
        """Deletes IP from ACL with given name"""
        if not is_valid_ipv4(ip):
            print(f"{ip} is not valid IPv4 address")
            raise typer.Abort()
        connection.send_command("configure")
        connection.send_command(
            f"delete firewall family ethernet-switching filter {name} term allow from ip-source-address {ip}/32"
        )
        connection.send_command("commit")
        print(f"IP {ip} deleted from ACL {name}")

    @app.command()
    def find(name: str):
        """Shows ACL with given name"""
        output = connection.send_command(
            "show configuration firewall family ethernet-switching | display set | match {name} | no-more"
        )
        print(output)
        print(f"ACL {name}")

    @app.command()
    def add(acl_name: str, interface_name: str):
        """Adds ACL rule with given name to interface"""
        if not is_valid_interface(interface_name):
            print("Error! Name of interface should be ge-(0-9)/(0-9)/(0-9)")
            raise typer.Abort()
        connection.send_command("configure")
        connection.send_command(
            f"set interfaces {interface_name} unit 0 family ethernet-switching filter input {acl_name}"
        )
        connection.send_command("commit")
        print(f"ACL added to {interface_name}")

    @app.command()
    def remove(acl_name: str, interface_name: str):
        """Removes ACL rule with given name from interface"""
        if not is_valid_interface(interface_name):
            print("Error! Name of interface should be ge-(0-9)/(0-9)/(0-9)")
            raise typer.Abort()
        connection.send_command("configure")
        connection.send_command(
            f"delete interfaces {interface_name} unit 0 family ethernet-switching filter input {acl_name}"
        )
        connection.send_command("commit")
        print(f"ACL {acl_name} removed from {interface_name}")

    return app
