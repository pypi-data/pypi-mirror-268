# DemoRolloutHelper - Dero

![Static Badge](https://img.shields.io/badge/3.12-3572a5?logo=python&logoColor=3572a5&label=Python)

This repository contains the code for the DemoRolloutHelper project and its respective modules.
The project aims to enable the automation of the rollout processes for demo environments.

## Installation

```shell
pip install aruba-dero --user
dero
```

> [!TIP]
> It is likely that when installed with the `--user` flag, the `dero` command is not available in your PATH.
> In this case, add it to your PATH or use the full path to the executable.
> Àfter opening a **NEW** terminal windows, the helper can be accessed by typing `dero`

or with **Docker-Compose**:

```shell
docker compose run dero
```

> [!TIP]
> Please refer to the docker-compose guide in the example [docker-compose.yml](example/docker-compose.yml) file.

or with **Docker**:

```shell
docker run --rm -it likqez/aruba-dero <args>
```

> [!IMPORTANT]
> Always refer to the respective module documentation for additional installation instructions.

## Available Modules

- [ClearPass Certificate Rollout](src/dero-modules/clearpass/README.md)
