# Manhattan Project  
*A Bryte Idea Open‑Source Template – v0.1.0*

> **Tagline:** *Clone → configure → ship.*  An AI‑accelerated full‑stack starter that sets sane defaults for Python back‑end, optional React/Expo front‑end, CI, docs, security, and an adhoc workflow for ticket‑scoped scripts.

---
## 🔗 Quick Links
| Resource | Description |
|----------|-------------|
| **🗂 Directory Structure** | [`docs/DIRECTORY_STRUCTURE.md`](docs/DIRECTORY_STRUCTURE.md) |
| **🤝 Contributing** | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| **🎫 Issue Templates** | `.github/ISSUE_TEMPLATE/` |
| **📜 Changelog** | [`CHANGELOG.md`](CHANGELOG.md) |
| **🌐 Org Home** | <https://github.com/bryte-idea> – other projects & roadmap |
| **Landing Site** (WIP) | <https://byteidea.com> |

---
## 💡 Why Manhattan Project?
Bryte Idea builds nostalgic media tools (e.g. **ShelfSnap** – physical‑media collector app). We needed a **repeatable, AI‑friendly scaffold**.  Now you can:

* Clone / use template in seconds.
* Let Cursor, Copilot, or ChatGPT refactor with consistent style.
* Ship back‑end + optional mobile front‑end with the same CI.

---
## 📂 Project Layout (after `init_project.py`)
```
manhattan-project/
├─ app/                  # Flask blueprints, services, models
├─ adhoc/                # Ticket-scoped scratch scripts (CI‑ignored)
│   └─ archived/         # Frozen scripts for reference
├─ scripts/              # Core CLI helpers (init_project.py, seed_db.py)
├─ tests/                # Pytest suites mirroring app/
├─ config/               # .env.example, YAML configs, docker-compose.yml
├─ static/               # Images, CSS, JS (optional)
├─ docs/
│   └─ boilerplate/      # Template markdown (README, CHANGELOG, etc.)
├─ docker/               # Dockerfile & compose (optional)
├─ .github/
│   └─ workflows/ci.yml  # Ruff, MyPy, pytest, Expo build
├─ requirements.txt      # Locked back‑end deps
├─ package.json          # (Optional) front‑end deps if you add React Native
├─ VERSION               # Semantic version file
└─ CHANGELOG.md
```
Need a React‑Native front‑end? Run `scripts/add_frontend.sh` after init.

---
## 🏁 Getting Started
### 1. Use as template (GitHub UI)
1. **Use this template ▸ Create a new repository** under your account or org.
2. Clone locally **or** open in Cursor Codespace.
3. Follow *Project Bootstrap* below.

### 2. Project Bootstrap (local)
```bash
# clone
git clone https://github.com/<you>/my-new-app.git && cd my-new-app

# Python env
python -m venv venv && source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Initialise placeholders & docs
python scripts/init_project.py \
       --name   "My New App" \
       --author "<Your Name>" \
       --ticket MP-001

pytest -q        # ✓ all green
```
*(Cursor users: open the folder; it auto‑detects the `venv` and test runner.)*

---
## 🔧 Prerequisites
| Tool | Minimum | Notes |
|------|---------|-------|
| **Python** | 3.9 | Back‑end & CLI scripts |
| **Node/npm** *(optional)* | 20 LTS | For React/Expo mobile front‑end |
| **Git** | 2.30 | |
| **Docker** *(optional)* | latest | Dev/prod parity via `docker-compose.yml` |

---
## 🔢 Versioning Policy (SemVer)
| Segment | Meaning |
|---------|---------|
| **MAJOR** x.0.0 | Breaking API changes |
| **MINOR** 0.x.0 | Backward‑compatible features |
| **PATCH** 0.0.x | Bug fixes |

Update **VERSION**, badge in README, and **CHANGELOG.md**. Tag release:
```bash
git tag -a vX.Y.Z -m "vX.Y.Z" && git push origin vX.Y.Z
```

---
## 🧪 Testing & CI
* **Pytest** for back‑end.
* **Ruff + Black** for lint/format.
* **MyPy** for type safety.
* **GitHub Actions** CI runs on push & PR; status checks required before merge.

---
## 🎫 Issue / Ticket Conventions
* Ticket ID format: `MP-123` (Manhattan Project) or project‑specific key (`SS-456`).
* PR titles: `feat: MP-123 short description` (Conventional Commits).
* Cursor‑generated adhoc scripts: `adhoc/MP-123_description.py`.

---
## 🔒 Security
* No secrets in VCS – use `.env` + GitHub Secrets.
* SQLAlchemy parameterised queries by default.
* Dependabot alerts enabled.

For vulnerabilities, see [`SECURITY.md`](SECURITY.md).

---
## 📜 License
MIT © Bryte Idea 2025.  See [`LICENSE`](LICENSE).

*Happy coding & may your pixels be ever nixel‑perfect!*