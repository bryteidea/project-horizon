# Manhattan Project – Directory Structure Guide

Purpose: Explain where every file lives in a Manhattan‑Project–based repo and how temporary adhoc scripts flow into long‑term code or archival.

## Root Overview

manhattan-project/
├─ app/                  # Flask blueprints, services, models
├─ config/               # YAML & .env.example
├─ docs/                 # Documentation (this file, API guides, etc.)
│   └─ boilerplate/
├─ scripts/              # Core CLI helpers (init_project.py, seed_db.py)
├─ adhoc/                # **Ticket‑scoped scratch scripts** (see below)
│   └─ archived/         # Completed adhoc scripts moved here via PR
├─ static/               # Front‑end assets (optional)
├─ tests/                # Pytest suites mirroring app/
├─ .github/              # Workflows, issue templates
├─ docker/               # Dockerfile & compose (optional)
├─ LICENSE
├─ README.md
├─ VERSION
├─ CHANGELOG.md
└─ requirements.txt

## Folder Purpose & Best Practices

| Folder | Keep | Notes |
|--------|------|-------|
| app/ | Production application code only | Sub‑package by feature: blueprints/, services/, models/, utils/. |
| config/ | Environment & deploy configs | .env.example, docker-compose.yml, supabase.yaml, etc. |
| docs/ | Markdown docs | Include architecture diagrams (docs/architecture.drawio). |
| scripts/ | Reusable, ticket‑independent helpers | e.g., seed_db.py, export_csv.py. Always referenced from README. |
| adhoc/ | One‑off or WIP scripts bound to a ticket | File naming: MP-123_fix_ocr_exif.py.  Cursor auto‑generates here. |
| adhoc/archived/ | Frozen, reference‑only scripts | Move scripts here in the PR that closes the ticket. No CI runs on this path. |
| static/ | Images, JS, CSS for Flask views | Optional; omit if you're API‑only. |
| tests/ | Unit + integration tests | Mirror app/ structure; use fixtures in tests/conftest.py. |
| docker/ | Containerization resources | Keep minimal for dev/prod parity. |
| .github/ | CI, templates | Inherited org‑wide docs live in pixelmynixel/.github. |

## Adhoc Workflow (Scratch → Archive)

1. Generate script via Cursor
   ```
   cursor ask "Create a Python script that bulk‑renames images based on EXIF, ticket MP-456" --output adhoc/MP-456_bulk_exif_renamer.py
   ```

2. Iterate & test inside adhoc/ until it's production‑ready or obsolete.

3. When the ticket is resolved:
   - If the logic becomes permanent → refactor into scripts/ or app/utils/ and add tests.
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

*Made with love by PixelMyNixel – 2025* 