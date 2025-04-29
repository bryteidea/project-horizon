# tickets Directory

This directory contains detailed documentation for project tickets/issues. Each ticket file provides comprehensive information about features, bugs, or enhancements.

## Naming Convention
```
<TICKET-ID>_short_descriptive_name.md
```

Examples:
- `MP-001_initial_project_setup.md`
- `SS-042_user_authentication.md`
- `MP-123_fix_image_upload_bug.md`

## Contents Structure

Each ticket file should follow the template structure (see `TEMPLATE.md`):
- Title and ID
- Type and priority
- Description
- Tasks/steps
- Implementation details
- Expected results
- Resources and references
- Validation criteria
- Related tickets

## Example Tickets

### Feature Ticket
`MP-025_user_profile_page.md` - Documents requirements, design considerations, and implementation details for a new user profile page feature.

### Bug Fix Ticket
`MP-108_fix_password_reset.md` - Details a bug in the password reset flow, including steps to reproduce, root cause, and verification steps.

### Enhancement Ticket
`MP-203_optimize_image_loading.md` - Describes performance improvements to image loading, with before/after metrics.

## Using Ticket Files

These files serve as:
1. Living documentation during development
2. Historical record after completion
3. Reference for related future work
4. Communication tool between team members

## Creating a New Ticket

```bash
# Copy the template and rename
cp TEMPLATE.md MP-456_add_export_feature.md

# Edit with your preferred editor
code MP-456_add_export_feature.md
```

Made with love by Bryte Idea
