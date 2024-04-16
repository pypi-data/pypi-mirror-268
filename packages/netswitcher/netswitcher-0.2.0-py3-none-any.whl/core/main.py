from netmiko import ConnectHandler
from netmiko import BaseConnection
import typer

import core.status as status
import core.speed as speed
import core.lacp as lacp
import core.state as state
import core.acl as acl

def create_app() -> typer.Typer:
    device = {
    'device_type': 'juniper_junos',
    'ip': '127.0.0.1',
    'username': '',
    'password': '',
    }
    connection: BaseConnection = ConnectHandler(**device)
    app = typer.Typer()
    app.add_typer(status.create_status_app(connection), name="status")
    app.add_typer(speed.create_speed_app(connection), name="speed")
    app.add_typer(lacp.create_lacp_app(connection), name="lacp")
    app.add_typer(state.create_state_app(connection), name="state")
    app.add_typer(acl.create_acl_app(connection), name="acl")

    return app()

if __name__ == "__main__":
    app = create_app()
    app()