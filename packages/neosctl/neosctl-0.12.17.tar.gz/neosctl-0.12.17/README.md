# Core CLI v0.12.17

## Prerequisites

The following packages are used across python repositories. A global install of them all is _highly_ recommended.

- [Poetry](https://python-poetry.org/docs/#installation)
- [Invoke](https://www.pyinvoke.org/installing.html)
- [Kubefwd](https://kubefwd.com)

### WSL (optional)

If running on Windows, you may need to install `distutils` to install the service.

```bash
$ sudo apt-get install python3.10-distutils
```

### Port forwarding (optional)

To access the APIs locally, you will need to connect to the pod inside
the cluster using `kubefwd`.

```bash
$ sudo kubefwd svc -n core-gateway -c ~/.kube/config
```

## Setup

### Install CLI

Install the CLI using [pip](https://pypi.org/project/neosctl/):

```bash
pip install neosctl
```

To install the CLI from source, clone the repository and run the following

```bash
$ invoke install-dev
```

When running locally, if you do not manage your own virtual environments, you
can use poetry to put you in a shell with access to the installed code.

```bash
$ poetry shell
```

### Setup profile
To setup a profile, run the following command:

```bash
neosctl profile init
```
and set all required parameters. More information about this command you can find in the [DOCS.md](DOCS.md) file.

### Login to the system

To login to the system, run the following command:

```bash
neosctl auth login
```

You will need username and password for that.

### Setup service user (optional)

For some operations, you will need to provide a service user `access_key_id` and `secret_access_key`, adding them into the file `~/.neosctl/credential`. To create service user and get it's access and secret key, use IAM API.

### Review settings

All setting are stored by default in the folder `~/.neosctl/`.

You can also review all settings by running the following commands:

```bash
neosctl profile list
neosctl profile view
```

### Reuse profile

To work with the same profile across multiple commands you can export the
profile name as an `NEOSCTL_PROFILE` environment variable.

```bash
$ neosctl -p my-profile --help
...
$ export NEOSCTL_PROFILE=my-profile
$ neosctl --help
```

## Usage

To see all available commands, run the following command:

```bash
neosctl --help
```

or go to the [DOCS.md](DOCS.md) file.


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
