from netmiko import BaseConnection
import typer

from core.utils import is_valid_interface


def create_state_app(connection: BaseConnection):
    app = typer.Typer()

    @app.command("on")
    def turn_on(interface_name: str):
        """Changes state of interface to ON"""
        if not is_valid_interface(interface_name):
            print("Error! Name of interface should be ge-(0-9)/(0-9)/(0-9)")
            raise typer.Abort()

        connection.send_command("configure")
        connection.send_command(f"delete interfaces {interface_name} disable")
        print(f"Interface {interface_name} is ON")

    @app.command("off")
    def turn_off(interface_name: str):
        """Changes state of interface to OFF"""
        if not is_valid_interface(interface_name):
            print("Error! Name of interface should be ge-(0-9)/(0-9)/(0-9)")
            raise typer.Abort()

        connection.send_command("configure")
        connection.send_command(f"set interfaces {interface_name} disable")
        print(f"Interface {interface_name} is OFF")

    return app
