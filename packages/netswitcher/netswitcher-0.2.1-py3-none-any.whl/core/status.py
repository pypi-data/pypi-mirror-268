import re
from typing_extensions import Annotated
from netmiko import BaseConnection
import typer
from .utils import is_valid_interface, is_valid_mac


def create_status_app(connection: BaseConnection):
    app = typer.Typer()

    @app.command("show")
    def show_config(
        interface_name: str, mac: Annotated[bool, typer.Option("--mac")] = False
    ):
        """Shows current configuration of interface"""
        if mac:
            if is_valid_mac(interface_name):
                print(f"show ethernet-switching table | match {interface_name}")
            else:
                print("Error! Not a valid MAC")
        elif not is_valid_interface(interface_name):
            print("Error! Name of interface should be ge-(0-9)/(0-9)/(0-9)")
            raise typer.Abort()
        output = connection.send_command(
            f"show configuration interfaces {interface_name}"
        )
        print(f"Interface {interface_name} \n {output}")

    @app.command("lacp")
    def show_all_lacp(lacp_name: str):
        """Shows active LACP with given name and all created LACP"""
        if not re.match(r"ae\d+", lacp_name):
            print("Error! Name of LACP should be ae(0-9)")
            raise typer.Abort()
        print(f"All active LACP with name {lacp_name}")
        print(connection.send_command(f"show lacp interfaces | match {lacp_name}"))
        print("All created LACP")
        print(
            connection.send_command(
                "show configuration interfaces | display set relative | match aggregated-ether-options | no-more"
            )
        )

    @app.command("int")
    def show_status(interface_name: str):
        """Shows current state of interface"""
        if not is_valid_interface(interface_name):
            print("Error! Name of interface should be ge-(0-9)/(0-9)/(0-9)")
            raise typer.Abort()
        output = connection.send_command(
            f"show interfaces {interface_name} terse | no-more"
        )
        print(output)

    return app
