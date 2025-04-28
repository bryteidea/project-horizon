# Manhattan Project – Cursor IDE Quick‑Spin Playbook  
*Aligned with **[`ronavis/bitgeek-project-template`](https://github.com/ronavis/bitgeek-project-template)** (last synced: 2025‑04‑28).*  Follow this to go **from clone → code → deploy in ≈15 min** using Cursor IDE.

---
## 0 · Prerequisites
| Tool | Min Version | Install |
|------|-------------|---------|
| **Git** | 2.30 | <https://git-scm.com/downloads> |
| **Python** | 3.9 | <https://python.org/downloads> |
| **Cursor IDE** | 0.41 | <https://cursor.sh> |
| **Node / npm** | 20 LTS | <https://nodejs.org> |
| **Docker Desktop** (optional) | latest | <https://docker.com> |

Configure Git once (update email if necessary):
```bash
git config --global user.name  "Ron Avis"       # GitHub: ronavis
git config --global user.email "ronavis@gmail.com"
```
Paste your GitHub PAT into **Cursor ▷ Settings ▷ Integrations** so pushes are seamless.

---
## 1 · One‑Minute Bootstrap
```bash
# 1 · Clone template
git clone https://github.com/ronavis/bitgeek-project-template manhattan-project
cd manhattan-project

# 2 · Create & activate venv
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate

# 3 · Install Python deps
pip install -r requirements.txt

# 4 · Project initialiser
python scripts/init_project.py \ 
       --name   "Manhattan Project" \ 
       --author "Ron Avis"          \ 
       --ticket AV‑001

# 5 · Run tests
pytest -q   # expect ✅
```
**Repo sanity‑check**
```
.vscode/   app/   config/   scripts/   tests/   static/   ci/   .docs/
```

---
## 2 · Recommended Cursor‑Centric Flow
| Task | Command | Shortcut |
|------|---------|----------|
| Ask the model | **Ask** | ⌥ Space |
| Generate file | **Generate Code** | ⌘ K g |
| Refactor sel. | **Refactor Selection** | ⌘ K r |
| Run tests | **Run Tests** | ⌘ ⇧ T |
| Toggle term. | **Terminal** | ` (back‑tick) |
| Markdown prev. | **Open Preview** | ⌘ P → `preview` |

> Keep `.specstory` updated—Cursor injects it into every prompt.

---
## 3 · Handy AI Prompts
```text
"Generate a SQLAlchemy Movie model (id, title, year, rating) with inline step hints." 
"Scaffold CRUD Flask blueprint for /api/v1/movies using the service layer pattern." 
"Write pytest for MovieService.get_movie including 200 and 404 cases." 
"Append new route docs to docs/API_ENDPOINTS.md following existing table format." 
```

---
## 4 · Git & Release Routine
```bash
# new feature branch
git checkout -b feature/AV‑002‑add‑movie‑endpoint

# code → commit → push
git commit -am "AV‑002: Add /movies/<id> endpoint & tests"
git push -u origin feature/AV‑002‑add‑movie‑endpoint
```
Open PR in Cursor (⇧⌘P → **Create Pull Request…**). Update **VERSION** & **CHANGELOG.md** before merge (SemVer).

---
## 5 · Smoke Test
```bash
flask --app app run
# visit → http://127.0.0.1:5000/health  ➜  {"status": "ok"}
```

---
## 6 · Next‑Step Checklist
- [ ] **pre‑commit hooks**: `pip install pre‑commit && pre‑commit install`
- [ ] **.env**: copy `config/.env.example` → `.env`, fill secrets (TMDB_KEY, …)
- [ ] **Sample data**: `scripts/seed_db.py --sample`
- [ ] **CI**: enable `.github/workflows/ci.yml` (pytest + flake8) and add repo secrets.
- [ ] **Docker up**: `docker compose up --build` (Flask + Postgres)
- [ ] **Deploy**: script in `ci/deploy.sh` deploys to Render or Fly.io.

---
## 7 · **Recommended Improvements for the Template Repo**
*Quick wins that will pay dividends as the project scales.*

| # | Recommendation | Why it helps | Example/Tool |
|---|----------------|-------------|--------------|
| 1 | **Switch to Poetry** or **PDM** | Lockfile + env‑agnostic dependency management; generates `pyproject.toml` which many modern tools parse. | `poetry init` then migrate `requirements.txt` into it. |
| 2 | **Add type hints & enforce with MyPy** | Catches bugs early; improves AI auto‑completion in Cursor. | `pip install mypy` + `scripts/type_check.sh`. |
| 3 | **Black + isort + Ruff** in pre‑commit | Zero‑click consistent formatting & linting. | Extend `.pre‑commit‑config.yaml`. |
| 4 | **EditorConfig** root file | Unifies tabs/spaces/line‑endings across IDEs. | `.editorconfig` at repo root. |
| 5 | **Code owners & PR template** | Streamlines reviews; auto‑requests reviewers. | `.github/CODEOWNERS`, `PULL_REQUEST_TEMPLATE.md`. |
| 6 | **Coverage gating in CI** | Fail PR if coverage drops below threshold. | `pytest --cov` + Coveralls badge. |
| 7 | **Docker‑compose for dev & prod** | Parity between local and cloud; easy onboarding. | `docker-compose.dev.yml` & `docker-compose.prod.yml`. |
| 8 | **Makefile** wrapper | One‑liners for common tasks (`make up`, `make test`, `make fmt`). | `Makefile` at root. |
| 9 | **Automated schema migrations** | Avoid manual SQL changes. | Alembic or Flask‑Migrate. |
|10 | **GraphQL layer (optional)** | Cleaner API evolution vs REST sprawl. | Strawberry or Ariadne integration. |
|11 | **Architecture diagram in docs** | Communicates high‑level design to new contributors & AI tools. | Use `docs/architecture.drawio`. |
|12 | **Issue / discussion templates** | Captures bug reports & ideas in uniform format; speeds triage. | `.github/ISSUE_TEMPLATE/bug.yml`, `feature.yml`. |

> **Future‑proofing now = fewer headaches later.** Cursor thrives on well‑structured, type‑annotated, consistently formatted repos.

---
### Footnote
*Built by BitGeek Software · v2025‑04‑28*  
*Questions or tweaks? Ping the AI and iterate!*

