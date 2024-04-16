# TT (Template Creator)

This commandline application is built for create new project with specify code template.

## Installation

```bash
# from pypi
pip install svtter_template_creator

# or
pipx install svtter_template_creator
```

## Usage

`ttc create --name django`

edit your config file: `$HOME/.config/tt.toml`

example:

```toml
[repos]
compose='git@github.com:svtter/cookiecutter-compose.git'
django='git@github.com:svtter/cookiecutter-django.git'
package='git@github.com:svtter/cookiecutter-pypackage.git'
```

## TODO

1. [ ] add `bumpversion`
2. [ ] more options.
