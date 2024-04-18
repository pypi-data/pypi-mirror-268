# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rh_aws_saml_login']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.34.37,<2.0.0',
 'humanize>=4.9.0,<5.0.0',
 'iterfzf>=1.1.0.44.0,<2.0.0.0.0',
 'pyquery>=2.0.0,<3.0.0',
 'requests-kerberos>=0.14.0,<0.15.0',
 'rich>=13.7.0,<14.0.0',
 'typer>=0.9.0,<0.10.0',
 'tzlocal>=5.2,<6.0']

entry_points = \
{'console_scripts': ['rh-aws-saml-login = rh_aws_saml_login.__main__:app']}

setup_kwargs = {
    'name': 'rh-aws-saml-login',
    'version': '0.3.1',
    'description': 'A CLI tool that allows you to log in and retrieve AWS temporary credentials using Red Hat SAML IDP',
    'long_description': '# rh-aws-saml-login\n\n[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)\n[![PyPI](https://img.shields.io/pypi/v/rh-aws-saml-login)][pypi-link]\n[![PyPI platforms][pypi-platforms]][pypi-link]\n![PyPI - License](https://img.shields.io/pypi/l/rh-aws-saml-login)\n\nA CLI tool that allows you to log in and retrieve AWS temporary credentials using Red Hat SAML IDP.\n\n![demo](/demo/quickstart.gif)\n\n## Pre-requisites\n\n- Python 3.11 or later\n- Connected to Red Hat VPN\n- A Red Hat managed computer (Kerberos must be installed and configured) and you are logged in with your Red Hat account\n\n## How it works\n\nThe `rh-aws-saml-login` CLI is a tool that simplifies the process of logging into an AWS account via Red Hat SSO. It retrieves a SAML token from the Red Hat SSO server, then fetches and parses the AWS SSO login page to present you with a list of all available accounts and their respective roles. You can then choose your desired account and role, and `rh-aws-saml-login` uses the SAML token to generate temporary AWS role credentials. Finally, it spawns a new shell with the necessary `AWS_` environment variables already set up, so you can immediately use the `aws` CLI without any further configuration.\n\n## Installation\n\nOn CSB Fedora, you need to install the Kerberos development package:\n\n```shell\nsudo dnf install krb5-devel\n```\n\nYou can install this library from [PyPI][pypi-link] with `pip`:\n\n```shell\npython3 -m pip install rh-aws-saml-login\n```\n\nor install it with `pipx`:\n\n```shell\npipx install rh-aws-saml-login\n```\n\nYou can also use `pipx` to run the library without installing it:\n\n```shell\npipx run rh-aws-saml-login\n```\n\n## Usage\n\n```shell\nrh-aws-saml-login\n```\n\nThis spawns a new shell with the following environment variables are set:\n\n- `AWS_ACCOUNT_NAME`: The name/alias of the AWS account\n- `AWS_ROLE_NAME`:  The name of the role\n- `AWS_ROLE_ARN`: The ARN of the role\n- `AWS_ACCESS_KEY_ID`: The access key used by the AWS CLI\n- `AWS_SECRET_ACCESS_KEY`: The secret access key used by the AWS CLI\n- `AWS_SESSION_TOKEN`: The session token used by the AWS CLI\n- `AWS_REGION`: The default region used by the AWS CLI\n\n## Features\n\nrh-aws-saml-login currently provides the following features (get help with `-h` or `--help`):\n\n- No configuration needed\n- Uses Kerberos authentication\n- Open the AWS web console for an account with the `--console` option\n- Shell auto-completion (bash, zsh, and fish) including AWS account names\n- Integrates nicely with the [starship](https://starship.rs)\n\n  ```toml\n   [env_var.AWS_ACCOUNT_NAME]\n   format = "$symbol$style [$env_value]($style) "\n   style = "cyan"\n   symbol = "🚀"\n  ```\n\n## Development\n\n[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)\n[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)\n\n- Update CHANGELOG.md with the new version number and date\n- Bump the version number in [pyproject.toml](/pyproject.toml)\n\n[pypi-link]:                https://pypi.org/project/rh-aws-saml-login/\n[pypi-platforms]:           https://img.shields.io/pypi/pyversions/rh-aws-saml-login\n',
    'author': 'Christian Assing',
    'author_email': 'cassing@redhat.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/app-sre/rh-aws-saml-login',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11',
}


setup(**setup_kwargs)
