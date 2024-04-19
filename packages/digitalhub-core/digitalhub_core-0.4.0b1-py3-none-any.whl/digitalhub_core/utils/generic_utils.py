"""
General utilities module.
"""
from __future__ import annotations

import base64
import os
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from uuid import uuid4
from zipfile import ZipFile

from boto3 import client as boto3_client
from digitalhub_core.utils.io_utils import read_text
from requests import get as requests_get


def build_uuid(uuid: str | None = None) -> str:
    """
    Create a uuid if not given

    Parameters
    ----------
    uuid : str
        ID of the object in form of UUID. Optional.

    Returns
    -------
    str
        The uuid.
    """
    if uuid is not None:
        return uuid
    return str(uuid4())


def get_timestamp() -> str:
    """
    Get the current timestamp timezoned.

    Returns
    -------
    str
        The current timestamp.
    """
    return datetime.now().astimezone().isoformat()


def decode_string(string: str) -> str:
    """
    Decode a string from base64.

    Parameters
    ----------
    string : str
        The string to decode.

    Returns
    -------
    str
        The string decoded from base64.
    """
    return base64.b64decode(string).decode()


def encode_string(string: str) -> str:
    """
    Encode a string in base64.

    Parameters
    ----------
    string : str
        The string to encode.

    Returns
    -------
    str
        The string encoded in base64.
    """
    return base64.b64encode(string.encode()).decode()


def encode_source(path: str) -> str:
    """
    Read a file and encode in base64 the content.

    Parameters
    ----------
    path : str
        The file path to read.

    Returns
    -------
    str
        The file content encoded in base64.
    """
    return encode_string(read_text(path))


def parse_entity_key(key: str) -> tuple[str]:
    """
    Parse the entity key.

    Parameters
    ----------
    key : str
        The entity key.

    Returns
    -------
    tuple[str]
        Project, entity type, kind, name and uuid.
    """
    try:
        # Remove "store://" from the key
        key = key.replace("store://", "")
        # Split the key into parts
        parts = key.split("/")
        # The project is the first part
        project = parts[0]
        # The entity type is the second part
        entity_type = parts[1]
        # The kind is the third part
        kind = parts[2]
        # The name and uuid are separated by a colon in the last part
        name, uuid = parts[3].split(":")
        return project, entity_type, kind, name, uuid
    except Exception as e:
        raise ValueError("Invalid key format.") from e


def requests_chunk_download(source: str, filename: Path) -> None:
    """
    Download a file in chunks.

    Parameters
    ----------
    source : str
        URL to download the file.
    filename : Path
        Path where to save the file.

    Returns
    -------
    None
    """
    with requests_get(source, stream=True) as r:
        r.raise_for_status()
        with filename.open("wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


def extract_archive(path: Path, filename: Path) -> None:
    """
    Extract a zip archive.

    Parameters
    ----------
    path : Path
        Path where to extract the archive.
    filename : Path
        Path to the archive.

    Returns
    -------
    None
    """
    with ZipFile(filename, "r") as zip_file:
        zip_file.extractall(path)


def get_s3_source(bucket: str, key: str, filename: Path) -> None:
    """
    Get S3 source.

    Parameters
    ----------
    bucket : str
        S3 bucket name.
    key : str
        S3 object key.
    filename : Path
        Path where to save the function source.

    Returns
    -------
    None
    """
    s3 = boto3_client("s3", endpoint_url=os.getenv("S3_ENDPOINT_URL"))
    s3.download_file(bucket, key, filename)


def get_bucket_and_key(path: str) -> tuple[str, str]:
    """
    Get bucket and key from path.

    Parameters
    ----------
    path : str
        The source path to get the key from.

    Returns
    -------
    tuple[str, str]
        The bucket and key.
    """
    parsed = urlparse(path)
    return parsed.netloc, parsed.path
