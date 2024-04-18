from __future__ import annotations

import os
import shutil
from pathlib import Path
from urllib.parse import urlparse

from git import Repo


def clone_repository(url: str, path: Path) -> None:
    """
    Clone git repository.

    Parameters
    ----------
    url : str
        URL of the repository.
    path : Path
        Path where to save the repository.

    Returns
    -------
    None
    """
    clean_path(path)
    checkout_object = get_checkout_object(url)
    url = add_credentials_git_remote_url(url)
    repo = clone_from_url(url, path)
    if checkout_object != "":
        repo.git.checkout(checkout_object)


def get_checkout_object(url: str) -> str:
    """
    Get checkout object.

    Parameters
    ----------
    url : str
        URL of the repository.

    Returns
    -------
    str
        Checkout object (branch, tag, commit).
    """
    return urlparse(url).fragment


def checkout(repo: Repo, checkout_object: str) -> None:
    """
    Checkout object.

    Parameters
    ----------
    repo : Repo
        Repository.
    checkout_object : str
        Object to checkout.

    Returns
    -------
    None
    """
    repo.git.checkout(checkout_object)


def clean_path(path: Path) -> None:
    """
    Clean path.

    Parameters
    ----------
    path : Path

    Returns
    -------
    None
    """

    shutil.rmtree(path, ignore_errors=True)


def get_git_username_password_from_token(token: str) -> tuple[str, str]:
    """
    Parse token to get username and password.

    Parameters
    ----------
    token : str
        Token to parse.

    Returns
    -------
    tuple[str, str]
        Username and password.
    """
    # Mutued from mlrun
    if token.startswith("github_pat_") or token.startswith("glpat"):
        username = "oauth2"
        password = token
    else:
        username = token
        password = "x-oauth-basic"
    return username, password


def add_credentials_git_remote_url(url: str) -> str:
    """
    Add credentials to git remote url.

    Parameters
    ----------
    url : str
        URL of the repository.

    Returns
    -------
    str
        URL with credentials.
    """
    url_obj = urlparse(url)

    # Get credentials from environment variables
    username = os.getenv("GIT_USERNAME")
    password = os.getenv("GIT_PASSWORD")
    token = os.getenv("GIT_TOKEN")

    # Get credentials from token
    if token is not None:
        username, password = get_git_username_password_from_token(token)

    if username is not None and password is not None:
        return f"https://{username}:{password}@{url_obj.hostname}{url_obj.path}"

    return url


def clone_from_url(url: str, path: Path) -> Repo:
    """
    Clone repository from url. Wraps git.Repo.clone_from.

    Parameters
    ----------
    url : str
        HTTP(S) URL of the repository.
    path : Path
        Path where to save the repository.

    Returns
    -------
    Repo
        Cloned repository.
    """
    return Repo.clone_from(url=url, to_path=path)
