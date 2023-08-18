# discord-py-template
This repository is meant to serve as a template for making new or improving existing Discord bots. This template is build to enhance the building of a Discord bot using the discord.py library.

# Project setup
To setup the projects and to get started with your environment you need to setup the following:<br>
`Python 3.11.*`<br>
`Poetry 1.5.*`<br>
`pre-commit 3.3.*` *Optional <br>
`docker -latest` *Optional

<hr>

Navigate to the root folder of your project.<br>
Setting up the environment:
```bash
poetry self add poetry-plugin-up \
poetry install
```

Optional if installed:
```bash
pre-commit install
```

<hr>

For the config-default file and .env you need to rename them.<br>
.env.exmaple -> .env <br>
config-default.yaml -> config.yaml

Fill in the config with your desired settings and populate the .env with the necessary content.
