# Boilerplate Templates – Bryte Idea

Goal: Provide drop‑in markdown (and text) templates so every repo across the Bryte Idea org shares the same look‑and‑feel.

## 📦 Template Index

| File | Purpose |
|------|---------|
| DIRECTORY_STRUCTURE_TEMPLATE.md | Starter for documenting a repo's folder layout. |
| TICKET_TEMPLATE.md | Issue ticket skeleton (MP-XXX, SS-YYY, etc.). |
| README_TEMPLATE.md | Module or feature README boilerplate. |
| DIRECTORY_README_TEMPLATE.md | README for individual directories. |
| VERSION_TEMPLATE | Initial VERSION file (SemVer). |
| CHANGELOG_TEMPLATE.md | First CHANGELOG entry (Unreleased heading + table). |
| CONTRIBUTING_TEMPLATE.md | Baseline Contributing guide with versioning policy. |

## 🛠 How to Use

### 1. Create a ticket

```
cp docs/boilerplate/TICKET_TEMPLATE.md tickets/MP-123_add_ocr_module.md
```

Replace MP-123 with your project's ticket ID.

### 2. Start a new directory

```
mkdir app/services/image_ocr
cp docs/boilerplate/DIRECTORY_README_TEMPLATE.md app/services/image_ocr/README.md
```

Edit placeholders (<DIRECTORY_NAME>, <PURPOSE>).

### 3. Initialise docs for a fresh repo

```
cp docs/boilerplate/README_TEMPLATE.md README.md
cp docs/boilerplate/DIRECTORY_STRUCTURE_TEMPLATE.md docs/DIRECTORY_STRUCTURE.md
cp docs/boilerplate/CONTRIBUTING_TEMPLATE.md CONTRIBUTING.md
```

Update project name, badges, and links.

### 4. Tagging a release

```
cp docs/boilerplate/CHANGELOG_TEMPLATE.md CHANGELOG.md   # Only on first init
cp docs/boilerplate/VERSION_TEMPLATE VERSION             # Contains 0.1.0
```

Edit the "Unreleased" section; bump version per SemVer.

## ✍️ Editing Guidelines

- Replace MP-XXX with your ticket code (or SS-XXX, PX-XXX).
- Keep heading levels unchanged unless documented.
- Wrap lines at 120 chars for diff‑friendly commits.
- End every file (except VERSION_TEMPLATE) with a newline.

## 🤝 Contributing to the templates

- Open an issue titled "Template change: " explaining the rationale.
- Submit a PR to docs/boilerplate/ with clear before/after diff.
- One maintainer approval + CI pass required to merge.

Made with pride by Bryte Idea – 2025 