# Core CLI v0.12.18

## Setup

### Install CLI

Install the CLI using [pip](https://pypi.org/project/neosctl/):

```bash
pip install neosctl
```

See [Local Development](#local-development) for details on installing from source.

### Setup environment
To setup an environment, run the following command:

```bash
neosctl env init -h <hub-host> -u <username> -a <account>
```
More information about this command you can find in the [DOCS.md](DOCS.md) file.

### Login to the system

To login to the system, run the following command:

```bash
neosctl env login
```

You will need username and password for that.

### Activate a core
To activate a core (for use in subsequent requests):

```bash
neoctl env list-cores
neosctl env activate-core <core-name>
```

### Setup service user (optional)

For some operations, you will need to provide a service user `access_key_id`
and `secret_access_key`, adding them into the file `~/.neosctl/credential`. To
create service user and get it's access and secret key, use:
```bash
neosctl iam user create-access-key
```

To configure the environment to use the key pair:

```bash
neosctl env credential <env-name> <access-key> <secret-key>
```

### Review settings

All setting are stored by default in the folder `~/.neosctl/`.

You can also review all settings by running the following commands:

```bash
neosctl env list
neosctl env view <env-name>
neosctl env active
```

## Usage

To see all available commands, run the following command:

```bash
neosctl --help
```

or go to the [DOCS.md](DOCS.md) file.

## Prerequisites

The following packages are used across python repositories. A global install of them all is _highly_ recommended.

- [Poetry](https://python-poetry.org/docs/#installation)
- [Invoke](https://www.pyinvoke.org/installing.html)

## Local Development

To install the CLI from source, clone the repository and run the following

```bash
$ invoke install-dev
```

Check the [Prerequisites](#prerequisites) for global installs required for local development.

When running locally, if you do not manage your own virtual environments, you
can use poetry to put you in a shell with access to the installed code.

```bash
$ poetry shell
```

## Code Quality

### Tests

```bash
invoke tests
invoke tests-coverage
```

## Linting

```bash
invoke check-style
invoke isort
```

## Generate docs

To generate docs in a markdown format, run the following command:

```bash
invoke generate-docs-md
```

The output [DOCS.md](./DOCS.md) file could be used to update the NEOS documentation site
([docs.neosmesh.com](https://docs.neosmesh.com)).

## Releases

Release management is handled using `changelog-gen`. The below commands will
tag a new release, and generate the matching changelog entries. Jenkins will
then publish the release to the artifact repository.

```bash
$ invoke release
$ invoke bump-patch
$ invoke bump-minor
$ invoke bump-major
> vX.Y.Z
```
