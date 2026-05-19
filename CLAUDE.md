# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Portuguese-language Flask web application showcasing Brazilian postgraduate programs in Demography. Displays four university programs (UFMG, Unicamp, ENCE, UFRN) with detail pages for each.

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server (debug mode enabled)
python app.py
```

The app runs at `http://localhost:5000` with Flask's built-in dev server.

## Architecture

The project follows a simple MVC-like pattern:

- **`app.py`** — Two routes: `GET /` lists all programs; `GET /programa/<id>` shows program detail. Returns 404 for unknown IDs.
- **`data/programas.py`** — Single source of truth for program data. Exports `PROGRAMAS` (list) and `PROGRAMAS_BY_ID` (dict keyed by ID string like `"ufmg"`, `"unicamp"`, `"ence"`, `"ufrn"`).
- **`templates/`** — Jinja2 templates extending `base.html`. All user-facing text is in Portuguese.
- **`static/css/style.css`** — Single stylesheet using CSS custom properties (`--azul`, `--dourado`, etc.) for theming; responsive at 600px breakpoint.

To add a new program: add an entry to `PROGRAMAS` in `data/programas.py` (fields: `id`, `nome`, `universidade`, `cidade`, `descricao`, `linhas`, `site`) — the templates and routing handle it automatically.
