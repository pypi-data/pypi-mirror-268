from audiospotter_cli.client import OrganizationClient
from audiospotter_cli.utils import (
    get_config,
    put_config,
)
from rich.prompt import Prompt, Confirm
from rich.console import Console

console = Console()
import requests


def return_client_or_configure():
    config = get_config()
    if not config:
        console.print(
            "[bold red]Could not find a config.yml file in this directory.[/bold red]"
        )
        if not Confirm.ask("Would you like to create a config file?", default=True):
            exit()

        server = Prompt.ask("Enter your API url")
        key = Prompt.ask("Enter your API key")

        put_config(server, key)

        # Test the config.
        client = return_client_or_configure()
        return client

    base_url = config["server"]
    key = config["key"]
    session = requests.Session()
    session.headers.update({"audiospotter-apikey": key})
    client = OrganizationClient(base_url, client=session)
    return client
