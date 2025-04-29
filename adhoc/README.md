# Adhoc Scripts Directory

This directory contains one-off scripts that are tied to specific tickets. These scripts are used for data migrations, analysis, or other tasks that are not part of the main application code.

## Naming Convention

PH-123_descriptive_name.py  # Where PH-123 is the ticket ID

## Examples

- `PH-045_import_legacy_users.py` - One-time script to import users from a CSV file
- `PH-102_fix_corrupted_images.py` - Script to repair corrupted image files
- `PH-238_analyze_log_patterns.py` - Exploratory analysis script for log pattern detection

## Guidelines

1. Always include the ticket ID in the filename
2. Make the script name descriptive of what it does
3. Include a comment at the top of the script explaining its purpose
4. Document any prerequisites or dependencies
5. Consider adding basic error handling and logging

## Creating New Scripts

You can use the Cursor AI assistant to quickly create new scripts:

```bash
cursor ask "Create a script to fix duplicate user entries, ticket PH-321" \
--output adhoc/PH-321_fix_duplicate_users.py
```

## Archiving Scripts

When a ticket is completed, scripts should be either:

1. Refactored into the main codebase if they provide ongoing value
2. Moved to the `/adhoc/archived` directory for reference

Scripts in the `/adhoc/archived` directory are not included in linting or testing.

*Made with pride by Bryte Idea – 2025* 
