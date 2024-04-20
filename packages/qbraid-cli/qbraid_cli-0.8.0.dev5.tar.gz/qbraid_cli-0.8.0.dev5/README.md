<img width="full" alt="qbraid_cli" src="https://qbraid-static.s3.amazonaws.com/logos/qbraid-cli-banner.png">

[![Documentation](https://img.shields.io/badge/Documentation-DF0982)](https://docs.qbraid.com/projects/cli/en/stable/guide/overview.html)
[![PyPI version](https://img.shields.io/pypi/v/qbraid-cli.svg?color=blue)](https://pypi.org/project/qbraid-cli/)
[![Python verions](https://img.shields.io/pypi/pyversions/qbraid-cli.svg?color=blue)](https://pypi.org/project/qbraid-cli/)
[![Downloads](https://static.pepy.tech/badge/qbraid-cli)](https://pepy.tech/project/qbraid-cli)
[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/qBraid/qBraid-Lab/issues)
[![Discord](https://img.shields.io/discord/771898982564626445.svg?color=pink)](https://discord.gg/KugF6Cnncm)

Command Line Interface for interacting with all parts of the qBraid platform.

The **qBraid CLI** is a specialized command-line interface tool designed *exclusively* for use within the [qBraid Lab](https://docs.qbraid.com/projects/lab/en/latest/lab/overview.html) platform. It is not intended for local installations or use outside the qBraid Lab environment. This tool ensures seamless integration and optimized performance specifically tailored for qBraid Lab's unique cloud-based quantum computing ecosystem.

## Getting Started

To use the qBraid CLI, login to qBraid (or create an account), launch Lab, and then open Terminal. You can also access the CLI directly from within [Notebooks](https://docs.qbraid.com/projects/lab/en/latest/lab/notebooks.html) using the ``!`` operator. See [quantum jobs example](https://github.com/qBraid/qbraid-lab-demo/blob/045c7a8fbdcae66a7e64533dd9fe0e981dc02cf4/qbraid_lab/quantum_jobs/aws_quantum_jobs.ipynb).

- [Launch qBraid Lab &rarr;](https://lab.qbraid.com/)
- [Make an account &rarr;](https://account.qbraid.com/)

For help, see qBraid Lab User Guide: [Getting Started](https://docs.qbraid.com/projects/lab/en/latest/lab/getting_started.html).

## Basic Commands

```shell
$ qbraid
----------------------------------
  * Welcome to the qBraid CLI! * 
----------------------------------

        ____            _     _  
   __ _| __ ) _ __ __ _(_) __| | 
  / _` |  _ \| '__/ _` | |/ _` | 
 | (_| | |_) | | | (_| | | (_| | 
  \__,_|____/|_|  \__,_|_|\__,_| 
     |_|                         


- Use 'qbraid --help' to see available commands.

- Use 'qbraid --version' to see the current version.

Reference Docs: https://docs.qbraid.com/projects/cli/en/stable/guide/overview.html
```

A qBraid CLI command has the following structure:

```shell
$ qbraid <command> <subcommand> [options and parameters]
```

For example, to list installed environments, the command would be:

```shell
$ qbraid envs list
```

To view help documentation, use one of the following:

```shell
$ qbraid --help
$ qbraid <command> --help
$ qbraid <command> <subcommand> --help
```

For example:

```shell
$ qbraid --help

Usage: qbraid [OPTIONS] COMMAND [ARGS]...

The qBraid CLI.

Options
  --version                     Show the version and exit.
  --install-completion          Install completion for the current shell.
  --show-completion             Show completion for the current shell, to copy it or customize the installation.
  --help                        Show this message and exit.

Commands
  configure                     Configure qBraid CLI options.
  credits                       Manage qBraid credits.
  devices                       Manage qBraid quantum devices.
  envs                          Manage qBraid environments.
  jobs                          Manage qBraid quantum jobs.
  kernels                       Manage qBraid kernels.
```

To get the version of the qBraid CLI:

```shell
$ qbraid --version
```
