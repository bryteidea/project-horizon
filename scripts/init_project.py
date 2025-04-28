#!/usr/bin/env python
"""
Manhattan Project Initializer

This script sets up a new project based on the Manhattan Project template.
It allows selection of different project "flavors" (Flask, FastAPI, Django, CLI).

Usage:
    python scripts/init_project.py --name "My Project Name" --author "Your Name" --ticket MP-001 [--flavor flask]

Arguments:
    --name      Project name
    --author    Project author/org name
    --ticket    Initial ticket ID (e.g. MP-001)
    --flavor    Project flavor (flask|fastapi|django|cli) [default: flask]
"""

import argparse
import os
import shutil
import sys
from datetime import datetime

# Constants
FLAVORS = ["flask", "fastapi", "django", "cli"]
YEAR = datetime.now().year

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Initialize Manhattan Project")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--author", required=True, help="Project author/org name")
    parser.add_argument("--ticket", required=True, help="Initial ticket ID (e.g. MP-001)")
    parser.add_argument("--flavor", default="flask", choices=FLAVORS, 
                        help=f"Project flavor: {', '.join(FLAVORS)}")
    
    return parser.parse_args()

def create_base_structure():
    """Create the base project structure (flavor-agnostic)."""
    # Base directories shared by all flavors
    base_dirs = [
        "src",
        "adhoc",
        "adhoc/archived",
        "scripts",
        "tests",
        "config",
        "docs",
        "docs/api",
        "assets",
        "tickets",
        ".github",
        ".github/workflows",
        ".github/ISSUE_TEMPLATE",
    ]
    
    for directory in base_dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Created directory: {directory}")
    
    # Create base README.md in each directory
    for directory in base_dirs:
        if not os.path.exists(f"{directory}/README.md"):
            with open(f"{directory}/README.md", "w") as f:
                f.write(f"# {os.path.basename(directory)}\n\nPurpose: [Directory purpose]\n")

def apply_flavor(flavor):
    """Apply the selected flavor-specific structure."""
    print(f"\n▶ Applying {flavor.upper()} flavor...")
    
    if flavor == "flask":
        # Flask-specific directories
        flask_dirs = ["src/blueprints", "src/models", "src/services", "src/utils", "src/templates", "src/static"]
        for directory in flask_dirs:
            os.makedirs(directory, exist_ok=True)
            print(f"✓ Created Flask directory: {directory}")
        
        # Create Flask app.py
        with open("src/app.py", "w") as f:
            f.write("""from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
""")
        print("✓ Created Flask app.py")
        
        # Create requirements.txt for Flask
        with open("requirements.txt", "w") as f:
            f.write("flask==2.3.3\n")
        print("✓ Created Flask requirements.txt")
        
    elif flavor == "fastapi":
        # FastAPI-specific directories
        fastapi_dirs = ["src/routers", "src/models", "src/services", "src/schemas", "src/dependencies"]
        for directory in fastapi_dirs:
            os.makedirs(directory, exist_ok=True)
            print(f"✓ Created FastAPI directory: {directory}")
        
        # Create FastAPI main.py
        with open("src/main.py", "w") as f:
            f.write("""from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
""")
        print("✓ Created FastAPI main.py")
        
        # Create requirements.txt for FastAPI
        with open("requirements.txt", "w") as f:
            f.write("fastapi==0.103.1\nuvicorn==0.23.2\n")
        print("✓ Created FastAPI requirements.txt")
        
    elif flavor == "django":
        # Django-specific directories
        django_dirs = ["src/apps", "src/templates", "src/static", "src/media"]
        for directory in django_dirs:
            os.makedirs(directory, exist_ok=True)
            print(f"✓ Created Django directory: {directory}")
        
        # Create Django manage.py
        with open("src/manage.py", "w") as f:
            f.write("""#!/usr/bin/env python
\"\"\"
Django's command-line utility for administrative tasks.
\"\"\"
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
""")
        print("✓ Created Django manage.py")
        
        # Create requirements.txt for Django
        with open("requirements.txt", "w") as f:
            f.write("django==4.2.5\n")
        print("✓ Created Django requirements.txt")
        
    elif flavor == "cli":
        # CLI-specific directories
        cli_dirs = ["src/commands", "src/utils", "src/config"]
        for directory in cli_dirs:
            os.makedirs(directory, exist_ok=True)
            print(f"✓ Created CLI directory: {directory}")
        
        # Create CLI main.py
        with open("src/main.py", "w") as f:
            f.write("""#!/usr/bin/env python
\"\"\"
Command-line interface main entry point
\"\"\"
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI Tool")
    parser.add_argument("--version", action="store_true", help="Show version")
    
    args = parser.parse_args()
    
    if args.version:
        print("v0.1.0")
    else:
        print("Hello, World!")

if __name__ == "__main__":
    main()
""")
        print("✓ Created CLI main.py")
        
        # Create requirements.txt for CLI
        with open("requirements.txt", "w") as f:
            f.write("click==8.1.7\n")
        print("✓ Created CLI requirements.txt")

def create_project_docs(args):
    """Create and update project documentation files."""
    # Create README.md
    with open("README.md", "w") as f:
        f.write(f"""# {args.name}
*A PixelMyNixel Project – v0.1.0*

> **Flavor:** {args.flavor.upper()}

## 🔗 Quick Links
| Resource | Description |
|----------|-------------|
| **🗂 Directory Structure** | [`docs/DIRECTORY_STRUCTURE.md`](docs/DIRECTORY_STRUCTURE.md) |
| **🤝 Contributing** | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| **🎫 Issue Templates** | `.github/ISSUE_TEMPLATE/` |
| **📜 Changelog** | [`CHANGELOG.md`](CHANGELOG.md) |

## 🏁 Getting Started
```bash
# Clone repository
git clone <repository-url>
cd {args.name.lower().replace(' ', '-')}

# Setup environment
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt

# Run application
{"python src/app.py" if args.flavor == "flask" else
 "uvicorn src.main:app --reload" if args.flavor == "fastapi" else
 "python src/manage.py runserver" if args.flavor == "django" else
 "python src/main.py"}
```

## 📜 License
MIT © {args.author} {YEAR}

*Made with pride by {args.author} – {YEAR}*
""")
    print("✓ Created README.md")
    
    # Create VERSION file
    with open("VERSION", "w") as f:
        f.write("0.1.0")
    print("✓ Created VERSION file")
    
    # Create CHANGELOG.md
    with open("CHANGELOG.md", "w") as f:
        f.write(f"""# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Initial project structure ({args.flavor} flavor)
- Basic documentation
- {args.ticket}: Project initialization

### Changed
- N/A

### Fixed
- N/A
""")
    print("✓ Created CHANGELOG.md")
    
    # Create directory structure documentation
    with open("docs/DIRECTORY_STRUCTURE.md", "w") as f:
        f.write(f"""# {args.name} – Directory Structure Guide

Purpose: Explain where every file lives in the project repository.

## Root Overview

{args.name.lower().replace(' ', '-')}/
├─ src/                  # Main application code
├─ adhoc/                # Ticket-scoped scratch scripts (CI‑ignored)
│   └─ archived/         # Frozen scripts for reference
├─ scripts/              # Core CLI helpers
├─ tests/                # Test suites
├─ config/               # Configuration files
├─ docs/                 # Documentation
├─ assets/               # Static assets (optional)
└─ .github/              # Workflows, issue templates

## Flavor-Specific Structure ({args.flavor.upper()})

{"src/\n├─ blueprints/            # Route handlers/views\n├─ models/               # Data models\n├─ services/             # Business logic\n├─ utils/                # Helper functions\n├─ templates/            # Jinja2 templates\n└─ static/               # CSS, JS, images" if args.flavor == "flask" else
 "src/\n├─ routers/              # API routes\n├─ models/               # Data models\n├─ schemas/              # Pydantic schemas\n├─ services/             # Business logic\n└─ dependencies/         # FastAPI dependencies" if args.flavor == "fastapi" else
 "src/\n├─ apps/                 # Django applications\n├─ templates/            # HTML templates\n├─ static/               # CSS, JS, images\n└─ media/                # User-uploaded content" if args.flavor == "django" else
 "src/\n├─ commands/             # CLI commands\n├─ utils/                # Helper functions\n└─ config/               # Configuration classes"}

## Adhoc Workflow (Scratch → Archive)

1. Generate script via Cursor
   ```
   cursor ask "Create a Python script that processes data, ticket {args.ticket}" --output adhoc/{args.ticket.replace('-', '_').lower()}_data_processor.py
   ```

2. Iterate & test inside adhoc/ until it's production‑ready or obsolete.

3. When the ticket is resolved:
   - If the logic becomes permanent → refactor into src/ and add tests.
   - Otherwise → git mv adhoc/MP-456_bulk_exif_renamer.py adhoc/archived/.

4. CI skips adhoc/** and adhoc/archived/** to keep pipelines fast.

## Adding New Directories

1. Confirm there isn't an existing dir that fits.
2. Discuss in a PR or ticket.
3. Add a README.md in the new dir explaining its purpose.
4. Update this document.

*Made with pride by {args.author} – {YEAR}*
""")
    print("✓ Created docs/DIRECTORY_STRUCTURE.md")

    # Create major features tracking document
    with open("docs/MAJOR_FEATURES.md", "w") as f:
        f.write(f"""# Major Features Tracking – {args.name}

This document tracks the implementation progress of major features for the MVP (Minimum Viable Product) and beyond.

## 🚀 MVP Features

### Core Application Setup
- [ ] Initial project structure ({args.flavor} flavor)
- [ ] Configuration management
- [ ] Deployment pipeline

### Application Features
- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3

## 🛠 Development Guidelines

1. **Ticket Integration**:
   - Every feature must have a corresponding ticket (e.g., {args.ticket.split('-')[0]}-XXX).
   - Link the ticket number in parentheses next to each feature.
   - Update this document when major tickets are created.

2. **Progress Tracking**:
   - Mark completed features with [x] instead of [ ].
   - For partial progress, note percentage: [ ] Feature (75%).

*Made with pride by {args.author} – {YEAR}*
""")
    print("✓ Created docs/MAJOR_FEATURES.md")

    # Create first ticket from template
    if os.path.exists("tickets/TEMPLATE.md"):
        with open("tickets/TEMPLATE.md", "r") as template_file:
            template_content = template_file.read()
            
        # Customize the template for this project
        ticket_content = (template_content
            .replace("MP-XXX", args.ticket)
            .replace("Ticket Title Here", "Project Initialization")
            .replace("Concise ticket title here", "Project Initialization")
            .replace("Feature | Bug Fix | Enhancement | Maintenance | Documentation | Security | Chore", "Maintenance")
            .replace("High | Medium | Low", "High")
            .replace("Clear, concise explanation", f"Initialize the project structure using Manhattan Project template with {args.flavor} flavor")
            .replace("1. Top-level task\n2. Another task\n   - Subtask A\n   - Subtask B\n3. …", 
                     "1. Set up base directory structure\n2. Apply {args.flavor} flavor configuration\n3. Create initial documentation\n4. Set up CI/CD configuration")
            .replace("- Technical approach\n- Design or architectural notes\n- Libraries / APIs\n- Performance or security considerations",
                     f"- Using init_project.py script\n- Framework: {args.flavor.upper()}\n- Following Manhattan Project best practices")
            .replace("- What success looks like\n- Acceptance criteria / KPI / metric",
                     "- Working project structure\n- Documentation in place\n- Initial dependencies configured")
            .replace("- Docs / RFCs / screenshots\n- Sample data / test cases\n- Related code links",
                     f"- Manhattan Project template\n- {args.flavor.capitalize()} documentation")
            .replace("- How to QA or test\n- Edge cases\n- Definition of Done",
                     "- Project structure matches template\n- Basic application runs without errors\n- Documentation is accurate and complete")
            .replace("- MP-YYY – Parent epic\n- SS-ZZZ – Cross-repo dependency", "- None")
            .replace("PixelMyNixel", args.author)
        )
        
        with open(f"tickets/{args.ticket}_project_initialization.md", "w") as f:
            f.write(ticket_content)
        print(f"✓ Created first ticket: {args.ticket}_project_initialization.md")
    else:
        # If template doesn't exist, create a simpler ticket file
        with open(f"tickets/{args.ticket}_project_initialization.md", "w") as f:
            f.write(f"""# {args.ticket} – Project Initialization

## Description
Initialize the project structure using Manhattan Project template with {args.flavor} flavor.

## Tasks
1. Set up base directory structure
2. Apply {args.flavor} flavor configuration
3. Create initial documentation
4. Set up CI/CD configuration

*Made with pride by {args.author} – {YEAR}*
""")
        print(f"✓ Created first ticket: {args.ticket}_project_initialization.md")

def main():
    """Main function to orchestrate the initialization process."""
    args = parse_args()
    
    print(f"\n🚀 Initializing {args.name} with {args.flavor} flavor...")
    
    # Check if we're running in the correct directory
    if not os.path.exists("scripts") or not os.path.exists("docs"):
        print("❌ Error: Please run this script from the root of the Manhattan Project template.")
        sys.exit(1)
    
    # Create the base structure (shared across all flavors)
    create_base_structure()
    
    # Apply the selected flavor
    apply_flavor(args.flavor)
    
    # Create and update documentation
    create_project_docs(args)
    
    print(f"\n✅ Project {args.name} successfully initialized with {args.flavor} flavor!")
    print("\nNext steps:")
    print("1. Review the generated structure")
    print("2. Customize documentation as needed")
    print("3. Start building your application")
    print(f"4. Track progress in ticket {args.ticket}")
    
    # Clean up templates directory if not needed
    if input("\nWould you like to remove the templates directory? (y/n): ").lower() == 'y':
        if os.path.exists("templates"):
            shutil.rmtree("templates")
            print("✓ Removed templates directory")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 