from rich.console import Console

console = Console()
from rich.prompt import IntPrompt


def select_source(client):
    response = client.get_organization()
    if response.status_code != 200:
        console.print("Error")
    data = response.json()
    # console.print(data)

    orgs = data

    console.print("*" * 80)
    console.print("Select the destination for your uploaded files")
    console.print("*" * 80)

    sources = []
    for org in data:
        for project in org.get("projects", []):
            for source in project.get("file_sources", []):
                console.print(f"[{source['id']}]: {project['name']} / {source['name']}")
                sources.append(source["id"])

    # print(sources)
    source_id = IntPrompt.ask("Which project?", choices=[str(i) for i in sources])

    return source_id
