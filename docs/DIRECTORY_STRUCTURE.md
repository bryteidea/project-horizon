# Manhattan Project – Directory Structure Guide

Purpose: Explain where every file lives in a Manhattan‑Project–based repo and how temporary adhoc scripts flow into long‑term code or archival.

## Root Overview

manhattan-project/
├─ src/                  # Main application code (framework-specific)
├─ adhoc/                # **Ticket‑scoped scratch scripts** (see below)
│   └─ archived/         # Completed adhoc scripts moved here via PR
├─ scripts/              # Core CLI helpers (init_project.py, seed_db.py)
├─ templates/            # Project flavor templates (flask, fastapi, etc.)
├─ tests/                # Pytest suites mirroring src/
├─ config/               # YAML & .env.example
├─ docs/                 # Documentation (this file, API guides, etc.)
│   └─ boilerplate/
├─ assets/               # Static assets (optional)
├─ .github/              # Workflows, issue templates
├─ LICENSE
├─ README.md
├─ VERSION
├─ CHANGELOG.md
└─ requirements.txt

## Framework Flavors

Manhattan Project supports multiple frameworks through "flavors":

| Flavor | Main Structure | Notes |
|--------|----------------|-------|
| **flask** | src/blueprints/, models/, etc. | Flask-based web apps |
| **fastapi** | src/routers/, schemas/, etc. | API-focused applications |
| **django** | src/apps/, templates/, etc. | Full-featured web applications |
| **cli** | src/commands/, utils/, etc. | Command-line applications |

Choose your flavor during project initialization:
```
python scripts/init_project.py --name "My Project" --author "Your Name" --ticket MP-001 --flavor flask
```

## Folder Purpose & Best Practices

| Folder | Keep | Notes |
|--------|------|-------|
| src/ | Production application code only | Structure depends on flavor (flask, fastapi, django, cli) |
| config/ | Environment & deploy configs | .env.example, docker-compose.yml, supabase.yaml, etc. |
| docs/ | Markdown docs | Include architecture diagrams (docs/architecture.drawio). |
| scripts/ | Reusable, ticket‑independent helpers | e.g., seed_db.py, export_csv.py. Always referenced from README. |
| templates/ | Project flavor templates | Used by init_project.py to scaffold new projects. |
| adhoc/ | One‑off or WIP scripts bound to a ticket | File naming: MP-123_fix_ocr_exif.py. Cursor auto‑generates here. |
| adhoc/archived/ | Frozen, reference‑only scripts | Move scripts here in the PR that closes the ticket. No CI runs on this path. |
| assets/ | Images, JS, CSS | Optional; varies by flavor. |
| tests/ | Unit + integration tests | Mirror src/ structure; use fixtures in tests/conftest.py. |
| .github/ | CI, templates | Inherited org‑wide docs live in pixelmynixel/.github. |

## Adhoc Workflow (Scratch → Archive)

1. Generate script via Cursor
   ```
   cursor ask "Create a Python script that bulk‑renames images based on EXIF, ticket MP-456" --output adhoc/MP-456_bulk_exif_renamer.py
   ```

2. Iterate & test inside adhoc/ until it's production‑ready or obsolete.

3. When the ticket is resolved:
   - If the logic becomes permanent → refactor into src/ or scripts/ and add tests.
   - Otherwise → git mv adhoc/MP-456_bulk_exif_renamer.py adhoc/archived/.

4. Close ticket, reference commit hash in the ticket comments.

5. CI skips adhoc/** and adhoc/archived/** to keep pipelines fast.

## Naming Conventions

- Files & dirs: snake_case.
- Tickets: MP-123, SS-045, etc.
- Adhoc scripts: <TICKET>_<concise_description>.py.
- Backups/dumps: YYYYMMDD_what_it_is.ext (20250428_db_dump.sql).

## Adding New Directories

1. Confirm there isn't an existing dir that fits.
2. Discuss in the PR or ticket.
3. Add a README.md in the new dir explaining its purpose.
4. Update this document.

*Made with pride by PixelMyNixel – 2025* 