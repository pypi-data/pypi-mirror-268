import typing as t
from warnings import warn
import tomli
import pathlib
import os


def get_dict():
    warn("get_dict is deprecated, use read_repo instead")

    prefix = os.getenv("TC_URL", "git@github.com:svtter")

    template_dict = {
        "django": "{prefix}/cookiecutter-django.git".format(prefix=prefix),
        "package": "{prefix}/cookiecutter-pypackage.git".format(prefix=prefix),
        "compose": "{prefix}/cookiecutter-compose.git".format(prefix=prefix),
    }
    return template_dict


def create(name):
    """
    create template via name
    """
    # repo: dict[name, url]
    template_dict = read_repo()

    template = template_dict[name]
    os.system(f"cookiecutter {template}")


def get_choice() -> t.List[str]:
    """get the choice from toml file"""
    repos = read_repo()
    return repos.keys()


def read_repo():
    """get the repos from toml file"""
    c_path = pathlib.Path.home() / ".config" / "tt.toml"
    with open(c_path, "rb") as fp:
        config = tomli.load(fp)

    return config["repos"]
