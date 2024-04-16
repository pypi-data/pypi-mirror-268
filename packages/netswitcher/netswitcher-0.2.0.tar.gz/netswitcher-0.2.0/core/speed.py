import re
from netmiko import BaseConnection
from .utils import is_valid_interface
import typer


def create_speed_app(connection: BaseConnection):
    app = typer.Typer()

    @app.command("set")
    def set_speed(interface_name: str, speed: str):
        """Set speed for interface"""
        if not is_valid_interface(interface_name):
            print("Error! Name of interface should be ge-(0-9)/(0-9)/(0-9)")
            raise typer.Abort()

        if not re.match(r"10m|100m|1g", speed):
            print("Error! Format of speed should be 10m|100m|1g")
            raise typer.Abort()
        connection.send_command("configure")
        connection.send_command(f"set interfaces {interface_name} speed {speed}")
        print(f"Speed of {interface_name} changed to {speed}")

    @app.command("desc")
    def set_description(interface_name: str, description: str):
        """Set description for interface"""
        if not is_valid_interface(interface_name):
            print("Error! Name of interface should be ge-(0-9)/(0-9)/(0-9)")
            raise typer.Abort()

        connection.send_command("configure")
        connection.send_command(
            f'set interfaces {interface_name} description "{description}"'
        )
        print(f"Description of {interface_name} changed to {description}")

    return app
