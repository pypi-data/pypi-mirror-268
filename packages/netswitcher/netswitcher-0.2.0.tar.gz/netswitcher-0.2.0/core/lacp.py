from netmiko import BaseConnection
import typer
from .utils import is_valid_interface


def create_lacp_app(connection: BaseConnection):
    app = typer.Typer()

    # TODO: check if both interfaces have same speed
    @app.command()
    def create(
        port: int, description: str, first_interface: str, second_interface: str
    ):
        """Creates LACP"""
        if port < 0:
            print("Port must be greater than zero")
            raise typer.Abort()
        if not (
            is_valid_interface(first_interface) and is_valid_interface(second_interface)
        ):
            print("Error! Name of interface should be ge-(0-9)/(0-9)/(0-9)")
            raise typer.Abort()

        connection.send_command("configure")
        connection.send_command(
            f"set interfaces ae{port} aggregated-ether-options lacp active"
        )
        connection.send_command(
            f"set interfaces ae{port} aggregated-ether-options lacp periodic fast"
        )
        connection.send_command(f'set interfaces ae{port} description "{description}"')
        connection.send_command(
            f"set interfaces ae{port} unit 0 family ethernet-switching"
        )

        for i in (first_interface, second_interface):
            connection.send_command(f"delete interfaces {i} unit 0")
            connection.send_command(
                f"set interfaces {i} ether-options 802.3ad ae{port}"
            )
            connection.send_command(f"delete protocols rstp interface {i}")

        connection.send_command("commit")
        print(f"LACP ae{port} created")

    @app.command()
    def delete(lacp_number: int):
        """Deletes LACP"""
        if lacp_number < 0:
            print("Port must be greater than zero")
            raise typer.Abort()
        connection.send_command("configure")
        connection.send_command(f"delete interfaces ae{lacp_number}")
        connection.send_command("commit")
        print(f"LACP ae{lacp_number} deleted")

    @app.command()
    def remove(interface_name: str):
        """Removes interface from LACP"""
        if not is_valid_interface(interface_name):
            print("Error! Name of interface should be ge-(0-9)/(0-9)/(0-9)")
            raise typer.Abort()

        connection.send_command("configure")
        connection.send_command(f"delete interfaces {interface_name}")
        connection.send_command(
            f"set interfaces {interface_name} unit 0 family ethernet-switching"
        )
        connection.send_command(
            f"set interfaces {interface_name} unit 0 family ethernet-switching storm-control default"
        )
        connection.send_command(f"set protocols rstp {interface_name}")
        connection.send_command("commit")
        print(f"Interface {interface_name} removed from LACP")

    return app
