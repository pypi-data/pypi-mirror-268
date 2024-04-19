import click
from audiospotter_cli.client import OrganizationClient
from audiospotter_cli.utils import (
    upload_file,
    get_files_by_extensions,
    get_config,
    put_config,
)
from audiospotter_cli.sources import select_source
from audiospotter_cli.config import return_client_or_configure
from rich.console import Console
from rich.prompt import Confirm
from rich.progress import track
import hashlib
from os import path

import os
import sys
from datetime import datetime, date, time
from wavinfo import WavInfoReader


console = Console()


@click.group()
def run():
    pass


@run.command()
@click.argument("dir_path", default=".")
@click.option("--extensions", default="flac,mp3,wav,WAV,MP3,FLAC")
@click.option("--omit-duplicates", default=True)
def upload(dir_path, extensions, omit_duplicates):
    """Upload a directory to your project's source bucket."""

    console.print("Finding file source ...")
    client = return_client_or_configure()

    file_source_id = select_source(client)
    # console.print(file_source_id)

    console.print("Parsing the file path ...")
    console.print(f"{dir_path}")
    extensions = extensions.split(",")
    dir_list = get_files_by_extensions(dir_path, extensions)

    # prints all files
    console.print(dir_list)

    if not Confirm.ask("Are you sure you want to upload these files?"):
        console.print("Upload cancelled.")
        exit()

    duplicates_skipped = 0
    files_uploaded = 0

    for file_name in track(dir_list, description="Uploading..."):
        file_path = path.join(dir_path, file_name)
        if dir_path == ".":
            file_path = file_name
        checksum = hashlib.md5(open(file_path, "rb").read()).hexdigest()
        response = client.get_signed_path(
            file_source_id, path=file_path, checksum=checksum
        )
        data = response.json()
        # console.print(data)
        if data["checksum_exists_in_project"]:
            # console.print("Checksum already exists!")
            if omit_duplicates:
                duplicates_skipped = duplicates_skipped + 1
                continue

        presigned_url = data["url"]
        presigned_fields = data["fields"]
        response = upload_file(presigned_url, presigned_fields, file_path)

        response = client.ingest_file_source(
            file_source_id, path=file_path, checksum=checksum
        )

        files_uploaded = files_uploaded + 1

    console.print(f"Files uploaded: {files_uploaded}")
    if duplicates_skipped > 0:
        console.print(f"Duplicates skipped: {duplicates_skipped}")


@run.command()
def connect():
    """Verify the connection to the AudioSpotter API."""
    client = return_client_or_configure()
    response = client.get_organization()
    console.print(response.json())


@run.command()
def configure():
    """Configure your credentials to the AudioSpotter API."""
    client = return_client_or_configure()
    response = client.get_organization()
    console.print(response.json())


@run.command()
@click.argument("dir_path", default=".")
@click.option("--extensions", default="wav,WAV")
def timestamp(dir_path, extensions):
    """Parse BEXT timestamp from WAV and rename files."""

    console.print("Looking for files to rename ...")
    console.print("Attempting to parse WAV files for BEXT metadata ...")
    extensions = extensions.split(",")
    dir_list = get_files_by_extensions(dir_path, extensions)

    dir_list.sort()
    standard_format = "%Y%m%d_%H%M%S"

    # prints all files
    console.print(dir_list)

    rename_list = []
    for file_name in dir_list:
        # Path to the file
        file_path = path.join(dir_path, file_name)
        _, extension = os.path.splitext(file_path)
        info = WavInfoReader(file_path)
        d = datetime.strptime(
            f"{info.bext.originator_date} {info.bext.originator_time}",
            "%Y-%m-%d %H:%M:%S",
        )
        datestr = d.strftime(standard_format)
        new_name = f"{datestr}{extension}"
        console.print(f"{file_name} -> {new_name}")

        rename_list.append((file_name, new_name))

    if not Confirm.ask("Are you sure you want to rename these files?"):
        console.print("timestamp command cancelled.")
        exit()

    console.print("Renaming ...")
    console.print(rename_list)

    for file_name, new_name in rename_list:
        file_path = path.join(dir_path, file_name)
        new_file_path = path.join(dir_path, new_name)
        os.rename(file_path, new_file_path)


if __name__ == "__main__":
    run()
