`Diagrams as code`: declarative configurations using `YAML` for drawing cloud system architectures.

[![](https://github.com/dmytrostriletskyi/diagrams-yaml/actions/workflows/main.yaml/badge.svg?branch=main)](https://github.com/dmytrostriletskyi/diagrams-yaml/actions/workflows/main.yaml)
[![](https://img.shields.io/github/release/dmytrostriletskyi/diagrams-yaml.svg)](https://github.com/dmytrostriletskyi/diagrams-yaml/releases)
[![](https://img.shields.io/pypi/v/diagrams-yaml.svg)](https://pypi.python.org/pypi/diagrams-yaml)
[![](https://img.shields.io/pypi/l/diagrams-yaml.svg)](https://pypi.python.org/pypi/diagrams-yaml/)
[![](https://img.shields.io/pypi/pyversions/diagrams-yaml.svg)](https://pypi.python.org/pypi/diagrams-yaml/)

![](./assets/configurations-architecture-aligned.png)

Table of content:

* [Introduction](#introduction)
* [Roadmap](#roadmap)
* [Getting Started](#getting-started)
  * [How to Install](#how-to-install)
  * [Examples](#examples)
* [Usage](#usage)
  * [Command Line Interface](#command-line-interface)
* [Disclaimer](#disclaimer)

## Introduction

`Diagrams as code` is essentially the process of managing diagrams through code rather than interactively drawing them
on specific web services such as [draw.io](https://app.diagrams.net). It lets you generate the cloud system architecture
in a **declarative** way with widely used `YAML` syntax (which is de facto a standard for infrastructure and 
configurations).

Declarative method of describing things means that a user simply describes the solution they need, how it should look, 
and everything that would be in the state of the final solution, leaving the process for the software to decide.

`Diagrams as code` brings you the following benefits comparing to drawing architecture on your own, it:

* Does not require any knowledge about how to properly draw an architecture diagram. Basically, you just define a set of 
  resources, compose them into groups and set relationships, the rest is done for you.
* Allows you to track an architecture diagram changes with a version control systems such as `Git`.
* Moves collaboration to the next level: updating an architecture diagram through a pull request with a code review 
  instead of a video session and/or screen sharing.
* Reduces costs on further updating of an initial architecture diagram. Basically, when you create an image on a web 
  service you have to eventually store two files: `PNG`-like to put into your documentation and `XML` to be able to 
  adjust your image in the future. So, there is no need to care about `XML` anymore.
* Backups you in case of losing `XML` files as `YAML` files are always stored in a repository.
* Improves consistency as now a diagram is stored along the code in a repository, the place you visit and work on
  frequently, and it is easier to keep it up-to-date.

Currently, the following components are provided:

* Major cloud providers: AWS, Azure, GCP, IBM, Alibaba, Oracle, OpenStack, DigitalOcean and so on.
* On-Premise, Kubernetes, Firebase, Elastic, SaaS.
* Programming languages and frameworks.

## Roadmap

* Add support of [C4](https://diagrams.mingrammer.com/docs/nodes/c4).
* Add support of [Custom](https://diagrams.mingrammer.com/docs/nodes/custom).
* Add IDEs plugins and/or web user interface for live editing.
* Research Confluence integration to update images from the CI-builds directly.
* Research ChatGRT integration.

## Getting Started

### How to install

As the project uses [Graphviz](https://www.graphviz.org) to render the diagram, you need to install it:

* For `Linux` — https://graphviz.gitlab.io/download/#linux
* For `Windows` — https://graphviz.gitlab.io/download/#windows
* For `macOS` — https://graphviz.gitlab.io/download/#mac

After, you can install the project itself with the following command using `pip3`:

```bash
$ pip3 install diagrams-yaml
```

### Examples

You can find examples of `YAML` configurations in the [examples](https://github.com/dmytrostriletskyi/diagrams-yaml/tree/main/examples) 
folder. Below are placed are few of them (click on the name to redirect to the configurations file).

| [Web Services on AWS](https://github.com/dmytrostriletskyi/diagrams-yaml/blob/main/examples/web-services-aws.yaml)                | [Web Services On-Premise](https://github.com/dmytrostriletskyi/diagrams-yaml/blob/main/examples/web-services-on-premise.yaml)                | [Exposed Pods on Kubernetes](https://github.com/dmytrostriletskyi/diagrams-yaml/blob/main/examples/exposed-pods-kubernetes.yaml)                |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](./assets/web-services-architecture-on-aws.png)                                                                                | ![](./assets/web-services-architecture-on-premise.png)                                                                                       | ![](./assets/exposed-pods-architecture-on-kubernetes.png)                                                                                       |

| [Message Collecting on GCP](https://github.com/dmytrostriletskyi/diagrams-yaml/blob/main/examples/message-collecting-gcp.yaml)    | [Events Processing on AWS](https://github.com/dmytrostriletskyi/diagrams-yaml/blob/main/examples/events-processing-aws.yaml)                 | [Workers on AWS](https://github.com/dmytrostriletskyi/diagrams-yaml/blob/main/examples/workers-aws.yaml)                                        |
| --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](./assets/message-collecting-architecture-on-gcp.png)                                                                          | ![](./assets/events-processing-on-aws.png)                                                                                                   | ![](./assets/workers-architecture-on-aws.png)                                                                                                   |

## Usage

### Command Line Interface

To draw an architecture, call `diagrams-yaml` command line interface, providing a path to a `YAML` file with 
configurations. The drawing will be saved in the folder the command line interface was executed from.

```bash
$ diagrams-yaml examples/web-services-aws.yaml
```

## Disclaimer

`diagrams-yaml` is a wrapper around original [diagrams](https://github.com/mingrammer/diagrams). The original `diagrams` 
lets you draw the cloud system architecture in `Python` code. It was born for prototyping a new system architecture 
design without any design tools. Under the hood, `diagrams-yaml` parse a `YAML` file and map to specific set of 
`diagrams`'s functions and classes, and executes them in proper order.

But you don't have to worry about `diagrams` because `diagrams-yaml` is self-contained and encapsulates it well. 
