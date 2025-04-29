#!/usr/bin/env python3
"""
# PH-045 - Ticket Relationship Visualization Tool

This script analyzes ticket files in the tickets/ directory and generates
a visualization of relationships between tickets (parent-child, dependencies).

The output is a GraphViz DOT file or an HTML file with an interactive graph.

Usage:
    python scripts/visualize_tickets.py [--format dot|html] [--output filename]
"""

import argparse
import glob
import os
import re
from typing import Dict, List, Optional, Set, Tuple


class TicketNode:
    """Represents a ticket in the relationship graph."""
    
    def __init__(self, ticket_id: str, title: str = "", ticket_type: str = ""):
        self.ticket_id = ticket_id
        self.title = title
        self.ticket_type = ticket_type.lower() if ticket_type else "task"
        self.parent: Optional[str] = None
        self.children: Set[str] = set()
        self.depends_on: Set[str] = set()
        self.blocked_by: Set[str] = set()
        
    def __str__(self) -> str:
        return f"{self.ticket_id}: {self.title}"


class TicketGraph:
    """Manages the graph of ticket relationships."""
    
    def __init__(self):
        self.nodes: Dict[str, TicketNode] = {}
        
    def add_node(self, ticket_id: str, title: str = "", ticket_type: str = "") -> TicketNode:
        """Add a new ticket node to the graph if it doesn't exist."""
        if ticket_id not in self.nodes:
            self.nodes[ticket_id] = TicketNode(ticket_id, title, ticket_type)
        return self.nodes[ticket_id]
    
    def add_relationship(self, source_id: str, target_id: str, relation_type: str):
        """Add a relationship between two tickets."""
        # Ensure both nodes exist
        if source_id not in self.nodes:
            self.add_node(source_id)
        if target_id not in self.nodes:
            self.add_node(target_id)
            
        source = self.nodes[source_id]
        
        if relation_type == "parent":
            source.parent = target_id
            self.nodes[target_id].children.add(source_id)
        elif relation_type == "depends_on":
            source.depends_on.add(target_id)
            self.nodes[target_id].blocked_by.add(source_id)
            
    def get_dot_representation(self) -> str:
        """Generate a GraphViz DOT representation of the ticket graph."""
        dot = [
            'digraph ticket_relationships {',
            '  rankdir=TB;',
            '  node [shape=box, style=filled, fontname="Arial"];',
            '  edge [fontname="Arial"];',
            ''
        ]
        
        # Define node styles based on ticket type
        type_colors = {
            "feature": "lightblue",
            "bug": "lightcoral",
            "enhancement": "lightgreen",
            "maintenance": "lightgrey",
            "documentation": "lightyellow",
            "security": "lightpink",
            "chore": "whitesmoke"
        }
        
        # Add nodes
        for ticket_id, node in self.nodes.items():
            color = type_colors.get(node.ticket_type, "white")
            label = f"{ticket_id}\\n{node.title}" if node.title else ticket_id
            dot.append(f'  "{ticket_id}" [label="{label}", fillcolor="{color}"];')
        
        # Add parent-child relationships
        for ticket_id, node in self.nodes.items():
            if node.parent:
                dot.append(f'  "{node.parent}" -> "{ticket_id}" [label="parent-child", style=solid, color="blue"];')
        
        # Add dependency relationships
        for ticket_id, node in self.nodes.items():
            for dep in node.depends_on:
                dot.append(f'  "{dep}" -> "{ticket_id}" [label="depends on", style=dashed, color="red"];')
        
        dot.append('}')
        return '\n'.join(dot)
    
    def get_html_representation(self) -> str:
        """Generate an interactive HTML visualization using vis.js."""
        nodes_json = []
        edges_json = []
        
        # Define node styles based on ticket type
        type_colors = {
            "feature": "#add8e6",  # lightblue
            "bug": "#f08080",      # lightcoral
            "enhancement": "#90ee90",  # lightgreen
            "maintenance": "#d3d3d3",  # lightgrey
            "documentation": "#ffffe0",  # lightyellow
            "security": "#ffb6c1",  # lightpink
            "chore": "#f5f5f5"     # whitesmoke
        }
        
        # Add nodes
        for ticket_id, node in self.nodes.items():
            color = type_colors.get(node.ticket_type, "#ffffff")
            label = f"{ticket_id}\n{node.title}" if node.title else ticket_id
            nodes_json.append(f'{{"id": "{ticket_id}", "label": "{label}", "color": "{color}"}}')
        
        # Add parent-child relationships
        for ticket_id, node in self.nodes.items():
            if node.parent:
                edges_json.append(
                    f'{{"from": "{node.parent}", "to": "{ticket_id}", '
                    f'"label": "parent-child", "arrows": "to", "color": "blue"}}'
                )
        
        # Add dependency relationships
        for ticket_id, node in self.nodes.items():
            for dep in node.depends_on:
                edges_json.append(
                    f'{{"from": "{dep}", "to": "{ticket_id}", '
                    f'"label": "depends on", "arrows": "to", "dashes": true, "color": "red"}}'
                )
        
        # Create the HTML content
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Ticket Visualization</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #333;
            border-bottom: 2px solid #ddd;
            padding-bottom: 10px;
        }}
        /* More styles... */
    </style>
</head>
<body>
    <h1>Project Horizon - Ticket Relationship Visualization</h1>
    <div id="visualization"></div>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <script>
        // Create nodes array
        var nodes = new vis.DataSet([
            {nodes_json}
        ]);
        
        // Create edges array
        var edges = new vis.DataSet([
            {edges_json}
        ]);

        // More JavaScript...
    </script>
</body>
</html>"""
        return html_content


class TicketParser:
    """Parses ticket files to extract relationships."""
    
    TICKET_DIR = "tickets"
    TICKET_ID_PATTERN = r'(PH|MP|SS|PX)-\d+'
    
    def __init__(self):
        self.graph = TicketGraph()
    
    def parse_ticket_file(self, file_path: str):
        """Parse a single ticket file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract ticket ID from filename or first line
        filename = os.path.basename(file_path)
        ticket_id_match = re.search(self.TICKET_ID_PATTERN, filename)
        
        if not ticket_id_match:
            # Try to find in first line
            first_line = content.split('\n', 1)[0]
            ticket_id_match = re.search(self.TICKET_ID_PATTERN, first_line)
            
        if not ticket_id_match:
            # Skip file if no ticket ID found
            return
            
        ticket_id = ticket_id_match.group(0)
        
        # Extract title
        title_match = re.search(r'#\s*' + re.escape(ticket_id) + r'\s*[–-]\s*(.+?)(?:\n|\s*🎫)', content)
        title = title_match.group(1).strip() if title_match else ""
        
        # Extract ticket type
        type_match = re.search(r'## Type.*\n\s*([A-Za-z\s]+)', content)
        ticket_type = type_match.group(1).strip() if type_match else ""
        
        # Create node
        node = self.graph.add_node(ticket_id, title, ticket_type)
        
        # Extract related tickets
        related_section_match = re.search(r'## Related Tickets.*\n(.*?)(?:\n\n|\n\*|$)', content, re.DOTALL)
        if related_section_match:
            related_section = related_section_match.group(1)
            
            # Look for parent ticket
            parent_match = re.search(r'(' + self.TICKET_ID_PATTERN + r')\s*[–-]\s*Parent epic', related_section)
            if parent_match:
                parent_id = parent_match.group(1)
                self.graph.add_relationship(ticket_id, parent_id, "parent")
                
            # Look for dependencies
            dependency_matches = re.finditer(r'(' + self.TICKET_ID_PATTERN + r')\s*[–-]\s*(?:Dependency|Cross-repo dependency)', related_section)
            for match in dependency_matches:
                dep_id = match.group(1)
                self.graph.add_relationship(ticket_id, dep_id, "depends_on")
    
    def parse_all_tickets(self):
        """Parse all ticket files in the tickets directory."""
        ticket_files = glob.glob(os.path.join(self.TICKET_DIR, "**/*.md"), recursive=True)
        for file_path in ticket_files:
            self.parse_ticket_file(file_path)
        return self.graph


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Visualize ticket relationships')
    parser.add_argument('--format', choices=['dot', 'html'], default='html',
                        help='Output format (dot for GraphViz, html for interactive)')
    parser.add_argument('--output', type=str, help='Output file path')
    
    args = parser.parse_args()
    
    # Parse tickets and build graph
    ticket_parser = TicketParser()
    graph = ticket_parser.parse_all_tickets()
    
    # Generate visualization
    if args.format == 'dot':
        output = graph.get_dot_representation()
        extension = '.dot'
    else:  # html
        output = graph.get_html_representation()
        extension = '.html'
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        output_dir = 'docs'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f'ticket_relationships{extension}')
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"Visualization generated at: {output_path}")


if __name__ == '__main__':
    main() 
