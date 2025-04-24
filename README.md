# Fapid Rest 🚀

A minimal, flexible and pragmatic **FastAPI** template to kickstart REST API development. Designed for **prototyping, PoCs**, internal tools, and dev utilities — with a strong foundation but without unnecessary complexity.

> [!Note]
> ⚠️ If you need something more robust for large-scale, production-ready services with full DDD, CQRS, or event-driven architectures — consider other templates.  
> `fapid-rest` is made for speed, clarity, and developer happiness 🚀

## Overview

> Service : A concrete service class defines the API of an external Service.
> Model : Defines the applications data model.
> Controllers : Where all the routes lives in API REST.

MCS stands for Model-Controller-Service. I don't want to bloater all with a lot of *Clases*, *Wrappers* or huge complexity, just `simple and minimaslitic`. Think of it like MVC — but:

- 🧠 Easier to reason about.
- 📁 Organized folder structure
- 🧪 Ideal for rapid PoC creation.
- ⚒️ Minimal setup. Easy to scale or swap in prod later.

Perfect when you want to start lean but keep your codebase clean.

## 🧰 Tech Stack

- **FastAPI** – Python’s async web framework for high-performance APIs.
- **Pydantic** - Data validation using Python type hints.
- **SQLModel** – Type-safe SQL layer, blending SQLAlchemy and Pydantic.

## ✨ Features

- 🧱 **Clean and simple MCS architecture**
- 🗂️ Predefined folder structure by **Domain**: `fapid_rest/user`, `fapid_rest/item`
- 🐳 Dockerized for local dev and deploy
- 🧪 Basic test setup with `pytest`
- 🧹 Linting and formatting via [ruff](https://docs.astral.sh/ruff/)
- 📦 Dependency management with [pip-tools](https://pip-tools.readthedocs.io/en/stable/)
- ⚡️ Powered by [uv](https://docs.astral.sh/uv/) for fast Python execution
- 🐣 Project management with [hatch](https://hatch.pypa.io/1.12/)
  
## 📦 Installation (Recommended with `pipx`)

[pipx](https://pipx.pypa.io/latest/installation/) is a tool to install and run Python CLI apps in isolated environments — safely and globally.

Instead of polluting your global Python environment with packages like hatch, uv, or black, pipx creates a virtual environment per tool, then exposes the CLI to your $PATH.

### Why Use pipx?

pipx is like nvm or rustup, but for Python CLI tools.

- 🔒 Isolated
- 🧼 Clean
- 🔁 Reproducible
- 💨 Fast when paired with uv

1. Zero conflicts across projects
   
    Installing CLI tools globally with pip can **easily cause version conflict**s. pipx keeps each tool isolated — no conflicts, no surprises.

2. Python **version friendly**

    Want to use Python 3.11 for uv, 3.10 for hatch? pipx supports that with:

3. Reproducibility + portability
   
    You can pin and install the **same versions of tools across machines or CI pipelines**, ensuring your dev environment is predictable.

4. Uninstalls cleanly
    pipx uninstall hatch deletes the tool and its virtualenv cleanly — **no residuals in your system**.

Here's a one-liner to install modern Python tooling that works across all your projects:

```bash
pipx install hatch uv pip-tools --python python3.11
```

### Create virtual environment

```bash
# with hatch
hatch env create
# with uv
uv venv --python 3.11
```

### Compile requirements

```bash
uv pip compile requirements/requirements.in -o requirements/requirements.txt
uv pip install -r requirements/requirements.txt
```

### Setup database

```bash
docker compose up -d
```

### Run the app

```bash
hatch run dev
```