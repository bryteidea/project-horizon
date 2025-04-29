#!/usr/bin/env python3
"""
# PH-035 - Changelog Automation Script

This script automates the process of updating the CHANGELOG.md file based on:
1. Git commit history
2. Ticket references in commit messages
3. Major feature implementation tracking

Usage:
    python scripts/update_changelog.py [--since-tag <tag>] [--until-tag <tag>]
"""

import argparse
import datetime
import os
import re
import subprocess
import sys
from typing import Dict, List, Optional, Tuple


class ChangelogUpdater:
    """Updates the CHANGELOG.md file based on git commit history and ticket references."""

    TICKET_PATTERN = r'(MP|SS|PX)-\d+'
    CHANGELOG_PATH = 'CHANGELOG.md'
    MAJOR_FEATURES_PATH = 'docs/boilerplate/MAJOR_FEATURES_TEMPLATE.md'
    VERSION_PATH = 'VERSION'
    
    SECTIONS = {
        'feature': '### ✨ New Features',
        'fix': '### 🐛 Bug Fixes',
        'docs': '### 📚 Documentation',
        'refactor': '### ♻️ Refactors',
        'test': '### 🧪 Tests',
        'chore': '### 🔧 Chores'
    }
    
    def __init__(self, since_tag: Optional[str] = None, until_tag: Optional[str] = None):
        """Initialize the changelog updater.
        
        Args:
            since_tag: The tag to start the changelog from (default: latest tag)
            until_tag: The tag to end the changelog at (default: HEAD)
        """
        self.since_tag = since_tag
        self.until_tag = until_tag
        self.version = self._get_current_version()
        
    def _get_current_version(self) -> str:
        """Read the current version from the VERSION file."""
        try:
            with open(self.VERSION_PATH, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return '0.1.0'  # Default version if file doesn't exist
    
    def _run_git_command(self, command: List[str]) -> str:
        """Run a git command and return its output."""
        try:
            result = subprocess.run(
                ['git'] + command,
                capture_output=True,
                check=True,
                text=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error running git command: {e}")
            return ""
    
    def _get_latest_tag(self) -> str:
        """Get the latest git tag."""
        return self._run_git_command(['describe', '--tags', '--abbrev=0'])
    
    def _get_commits(self) -> List[Dict[str, str]]:
        """Get commits between the specified tags."""
        if not self.since_tag:
            self.since_tag = self._get_latest_tag()
            if not self.since_tag:
                self.since_tag = "HEAD~50"  # Fallback if no tags exist
                
        until_ref = self.until_tag if self.until_tag else "HEAD"
        
        # Format: hash|author|date|subject
        format_str = "--pretty=format:%H|%an|%ad|%s"
        date_format = "--date=format:%Y-%m-%d"
        
        commits_str = self._run_git_command([
            'log', 
            f'{self.since_tag}..{until_ref}',
            format_str,
            date_format
        ])
        
        if not commits_str:
            return []
            
        commits = []
        for line in commits_str.split('\n'):
            if not line.strip():
                continue
                
            parts = line.split('|', 3)
            if len(parts) < 4:
                continue
                
            hash_val, author, date, subject = parts
            
            # Extract ticket references
            tickets = re.findall(self.TICKET_PATTERN, subject)
            
            # Determine change type from conventional commits
            change_type = 'chore'  # Default
            if ':' in subject:
                prefix = subject.split(':', 1)[0].lower()
                if any(t in prefix for t in ['feat', 'feature']):
                    change_type = 'feature'
                elif 'fix' in prefix:
                    change_type = 'fix'
                elif 'doc' in prefix:
                    change_type = 'docs'
                elif 'refactor' in prefix:
                    change_type = 'refactor'
                elif 'test' in prefix:
                    change_type = 'test'
            
            commits.append({
                'hash': hash_val,
                'author': author,
                'date': date,
                'subject': subject,
                'tickets': tickets,
                'type': change_type
            })
            
        return commits
    
    def _categorize_commits(self, commits: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
        """Categorize commits by type."""
        categorized = {section_type: [] for section_type in self.SECTIONS}
        
        for commit in commits:
            commit_type = commit['type']
            if commit_type in categorized:
                categorized[commit_type].append(commit)
        
        return categorized
    
    def _format_commit_line(self, commit: Dict[str, str]) -> str:
        """Format a commit for the changelog."""
        tickets_str = ' '.join([f'[{t}]' for t in commit['tickets']])
        if tickets_str:
            tickets_str = f' {tickets_str}'
            
        # Clean up commit subject
        subject = commit['subject']
        # Remove ticket references already included separately
        for ticket in commit['tickets']:
            subject = subject.replace(ticket, '').strip()
        # Remove conventional commit type prefix
        if ':' in subject:
            subject = subject.split(':', 1)[1].strip()
            
        return f"- {subject}{tickets_str} ({commit['date']})"
    
    def _update_major_features(self, commits: List[Dict[str, str]]) -> List[Tuple[str, str]]:
        """Update the major features tracking and return the updated features."""
        updated_features = []
        
        # Read major features file
        try:
            with open(self.MAJOR_FEATURES_PATH, 'r') as f:
                content = f.read()
                
            # Find all incomplete feature lines with ticket references
            incomplete_features = re.findall(r'- \[ \] (.+?) \((MP-\d+)(?:, \d+%)?\)', content)
            
            # Check if any commits reference these tickets
            commit_tickets = {ticket for commit in commits for ticket in commit['tickets']}
            
            for feature, ticket in incomplete_features:
                if ticket in commit_tickets:
                    # Mark as completed in the file
                    old_str = f'- [ ] {feature} ({ticket}'
                    new_str = f'- [x] {feature} ({ticket}'
                    content = content.replace(old_str, new_str)
                    updated_features.append((feature, ticket))
            
            # Write updated content back to file
            with open(self.MAJOR_FEATURES_PATH, 'w') as f:
                f.write(content)
                
        except FileNotFoundError:
            print(f"Warning: Major features file not found at {self.MAJOR_FEATURES_PATH}")
            
        return updated_features
    
    def update_changelog(self) -> bool:
        """Update the CHANGELOG.md file.
        
        Returns:
            bool: True if the changelog was updated, False otherwise
        """
        commits = self._get_commits()
        if not commits:
            print("No new commits found since the last tag.")
            return False
            
        # Update major features tracking
        updated_features = self._update_major_features(commits)
        
        # Categorize commits
        categorized = self._categorize_commits(commits)
        
        # Read existing changelog
        try:
            with open(self.CHANGELOG_PATH, 'r') as f:
                changelog_content = f.read()
        except FileNotFoundError:
            changelog_content = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n"
        
        # Create new entry
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        new_entry = f"## [{self.version}] - {today}\n\n"
        
        # Add completed major features section if any
        if updated_features:
            new_entry += "### 🚀 Completed Major Features\n\n"
            for feature, ticket in updated_features:
                new_entry += f"- {feature} [{ticket}]\n"
            new_entry += "\n"
        
        # Add sections with commits
        for section_type, section_header in self.SECTIONS.items():
            section_commits = categorized[section_type]
            if section_commits:
                new_entry += f"{section_header}\n\n"
                for commit in section_commits:
                    new_entry += f"{self._format_commit_line(commit)}\n"
                new_entry += "\n"
                
        # Add new entry to changelog
        parts = changelog_content.split('\n\n', 2)
        if len(parts) >= 3:
            header1, header2, rest = parts
            updated_content = f"{header1}\n\n{header2}\n\n{new_entry}{rest}"
        else:
            updated_content = f"{changelog_content}\n{new_entry}"
        
        # Write updated changelog
        with open(self.CHANGELOG_PATH, 'w') as f:
            f.write(updated_content)
            
        print(f"Updated {self.CHANGELOG_PATH} with new entry for version {self.version}")
        return True


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Update CHANGELOG.md based on git commits and tickets')
    parser.add_argument('--since-tag', help='Start changelog from this tag')
    parser.add_argument('--until-tag', help='End changelog at this tag')
    
    args = parser.parse_args()
    
    updater = ChangelogUpdater(args.since_tag, args.until_tag)
    updater.update_changelog()


if __name__ == '__main__':
    main() 
