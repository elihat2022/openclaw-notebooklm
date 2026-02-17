#!/usr/bin/env python3
"""
OpenClaw NotebookLM Installer
Automates the installation and configuration of NotebookLM MCP skill for OpenClaw
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any


class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


class OpenClawNotebookLMInstaller:
    """Installer for NotebookLM MCP skill in OpenClaw"""

    def __init__(self):
        self.home = Path.home()
        self.openclaw_dir = self.home / ".openclaw"
        self.skill_dir = self.openclaw_dir / "skills" / "notebooklm"
        self.config_file = self.openclaw_dir / "openclaw.json"
        self.mcporter_config = self.openclaw_dir / "mcporter.json"
        self.auth_file = self.home / ".notebooklm-mcp" / "auth.json"

    def print_step(self, message: str):
        """Print a step message"""
        print(f"{Colors.OKBLUE}[*]{Colors.ENDC} {message}")

    def print_success(self, message: str):
        """Print a success message"""
        print(f"{Colors.OKGREEN}[✓]{Colors.ENDC} {message}")

    def print_error(self, message: str):
        """Print an error message"""
        print(f"{Colors.FAIL}[✗]{Colors.ENDC} {message}")

    def print_warning(self, message: str):
        """Print a warning message"""
        print(f"{Colors.WARNING}[!]{Colors.ENDC} {message}")

    def run_command(self, cmd: list, capture_output=False) -> Optional[str]:
        """Run a shell command"""
        try:
            if capture_output:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                return result.stdout.strip()
            else:
                subprocess.run(cmd, check=True)
                return None
        except subprocess.CalledProcessError as e:
            return None

    def check_command_exists(self, command: str) -> bool:
        """Check if a command exists in PATH"""
        return shutil.which(command) is not None

    def check_prerequisites(self) -> bool:
        """Check if all prerequisites are installed"""
        self.print_step("Checking prerequisites...")

        missing = []

        # Check OpenClaw
        if not self.check_command_exists("openclaw"):
            missing.append("openclaw")
            self.print_error("OpenClaw not found")
        else:
            self.print_success("OpenClaw found")

        # Check mcporter
        if not self.check_command_exists("mcporter"):
            missing.append("mcporter")
            self.print_warning("mcporter not found - will install")
        else:
            self.print_success("mcporter found")

        # Check notebooklm-mcp
        if not self.check_command_exists("notebooklm-mcp"):
            missing.append("notebooklm-mcp")
            self.print_warning("notebooklm-mcp not found - will install")
        else:
            self.print_success("notebooklm-mcp found")

        # Check uvx (for running notebooklm-mcp)
        if not self.check_command_exists("uvx"):
            self.print_warning("uvx not found - recommended for notebooklm-mcp")

        return "openclaw" not in missing

    def install_dependencies(self) -> bool:
        """Install missing dependencies"""
        self.print_step("Installing dependencies...")

        # Install mcporter
        if not self.check_command_exists("mcporter"):
            self.print_step("Installing mcporter...")
            if self.run_command(["npm", "install", "-g", "mcporter"]) is not None:
                self.print_error("Failed to install mcporter")
                return False
            self.print_success("mcporter installed")

        # Install notebooklm-mcp
        if not self.check_command_exists("notebooklm-mcp"):
            self.print_step("Installing notebooklm-mcp...")
            if self.run_command(["npm", "install", "-g", "notebooklm-mcp-cli"]) is not None:
                self.print_error("Failed to install notebooklm-mcp")
                return False
            self.print_success("notebooklm-mcp installed")

        return True

    def authenticate_notebooklm(self) -> bool:
        """Run NotebookLM authentication"""
        self.print_step("Checking NotebookLM authentication...")

        if self.auth_file.exists():
            self.print_success(f"Auth file already exists: {self.auth_file}")
            response = input(f"{Colors.WARNING}Re-authenticate? (y/N): {Colors.ENDC}")
            if response.lower() != 'y':
                return True

        self.print_step("Starting NotebookLM authentication...")
        self.print_warning("A Chrome window will open. Please log in to your Google account.")
        input(f"{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

        # Run authentication
        result = os.system("notebooklm-mcp-auth")
        if result != 0:
            self.print_error("Authentication failed")
            return False

        if not self.auth_file.exists():
            self.print_error(f"Auth file not created at {self.auth_file}")
            return False

        self.print_success("Authentication successful")
        return True

    def create_mcporter_config(self) -> bool:
        """Create mcporter config file"""
        self.print_step("Creating mcporter configuration...")

        config = {
            "mcpServers": {
                "notebooklm": {
                    "command": "uvx" if self.check_command_exists("uvx") else "npx",
                    "args": ["--from", "notebooklm-mcp-cli", "notebooklm-mcp"]
                }
            }
        }

        try:
            with open(self.mcporter_config, 'w') as f:
                json.dump(config, f, indent=2)
            self.print_success(f"mcporter config created at {self.mcporter_config}")
            return True
        except Exception as e:
            self.print_error(f"Failed to create mcporter config: {e}")
            return False

    def create_skill(self) -> bool:
        """Create the NotebookLM skill"""
        self.print_step("Creating NotebookLM skill...")

        # Create skill directory
        self.skill_dir.mkdir(parents=True, exist_ok=True)

        # Create SKILL.md
        skill_md = self.skill_dir / "SKILL.md"
        skill_content = get_skill_md_template()
        try:
            with open(skill_md, 'w') as f:
                f.write(skill_content)
            self.print_success(f"Created {skill_md}")
        except Exception as e:
            self.print_error(f"Failed to create SKILL.md: {e}")
            return False

        # Create wrapper script
        wrapper_script = self.skill_dir / "notebooklm.sh"
        wrapper_content = get_wrapper_script_template()
        try:
            with open(wrapper_script, 'w') as f:
                f.write(wrapper_content)
            # Make executable
            wrapper_script.chmod(0o755)
            self.print_success(f"Created {wrapper_script}")
        except Exception as e:
            self.print_error(f"Failed to create wrapper script: {e}")
            return False

        return True

    def update_openclaw_config(self) -> bool:
        """Update OpenClaw configuration"""
        self.print_step("Updating OpenClaw configuration...")

        if not self.config_file.exists():
            self.print_error(f"OpenClaw config not found at {self.config_file}")
            return False

        try:
            # Read current config
            with open(self.config_file, 'r') as f:
                config = json.load(f)

            # Ensure skills section exists
            if "skills" not in config:
                config["skills"] = {}
            if "entries" not in config["skills"]:
                config["skills"]["entries"] = {}

            # Add notebooklm skill entry
            config["skills"]["entries"]["notebooklm"] = {
                "enabled": True,
                "env": {
                    "MCPORTER_CONFIG": str(self.mcporter_config)
                }
            }

            # Write updated config
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)

            self.print_success("OpenClaw config updated")
            return True

        except Exception as e:
            self.print_error(f"Failed to update config: {e}")
            return False

    def restart_openclaw(self) -> bool:
        """Restart OpenClaw daemon"""
        self.print_step("Restarting OpenClaw daemon...")

        result = os.system("openclaw daemon restart")
        if result != 0:
            self.print_warning("Failed to restart daemon - you may need to restart manually")
            return False

        self.print_success("OpenClaw daemon restarted")
        return True

    def verify_installation(self) -> bool:
        """Verify the installation"""
        self.print_step("Verifying installation...")

        # Check skill is listed
        output = self.run_command(["openclaw", "skills", "list"], capture_output=True)
        if output and "notebooklm" in output:
            self.print_success("Skill registered in OpenClaw")
        else:
            self.print_warning("Skill not yet visible - may need a new session")

        # Test wrapper script
        test_cmd = str(self.skill_dir / "notebooklm.sh")
        result = subprocess.run([test_cmd, "list"], capture_output=True, text=True)
        if result.returncode == 0:
            self.print_success("Skill wrapper working correctly")
            return True
        else:
            self.print_error("Skill wrapper test failed")
            print(result.stderr)
            return False

    def print_next_steps(self):
        """Print next steps for the user"""
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}✨ Installation Complete!{Colors.ENDC}\n")
        print(f"{Colors.OKCYAN}Next steps:{Colors.ENDC}\n")
        print(f"1. {Colors.BOLD}Start a new OpenClaw session{Colors.ENDC} (or restart openclaw-tui)")
        print(f"2. Ask the agent: {Colors.OKGREEN}\"List my NotebookLM notebooks\"{Colors.ENDC}")
        print(f"3. Try: {Colors.OKGREEN}\"Ask my notebook about X\"{Colors.ENDC}")
        print(f"\n{Colors.OKCYAN}Skill location:{Colors.ENDC} {self.skill_dir}")
        print(f"{Colors.OKCYAN}Config location:{Colors.ENDC} {self.mcporter_config}")
        print(f"{Colors.OKCYAN}Auth location:{Colors.ENDC} {self.auth_file}")
        print(f"\n{Colors.WARNING}Note:{Colors.ENDC} If the agent doesn't see the skill, exit and restart your session.\n")

    def install(self) -> bool:
        """Run the full installation process"""
        print(f"\n{Colors.HEADER}{Colors.BOLD}OpenClaw NotebookLM Installer{Colors.ENDC}")
        print(f"{Colors.HEADER}================================{Colors.ENDC}\n")

        steps = [
            ("Prerequisites", self.check_prerequisites),
            ("Dependencies", self.install_dependencies),
            ("Authentication", self.authenticate_notebooklm),
            ("mcporter Config", self.create_mcporter_config),
            ("Skill Creation", self.create_skill),
            ("OpenClaw Config", self.update_openclaw_config),
            ("Restart Daemon", self.restart_openclaw),
            ("Verification", self.verify_installation),
        ]

        for step_name, step_func in steps:
            try:
                if not step_func():
                    self.print_error(f"Installation failed at: {step_name}")
                    return False
            except Exception as e:
                self.print_error(f"Error during {step_name}: {e}")
                return False
            print()  # Blank line between steps

        self.print_next_steps()
        return True


def get_skill_md_template() -> str:
    """Return the SKILL.md template"""
    return """---
name: notebooklm
description: Interact with Google NotebookLM - list notebooks, create sources, ask questions, and manage AI notes
user-invocable: true
metadata: { "openclaw": { "emoji": "📓", "requires": { "bins": ["mcporter"] }, "homepage": "https://notebooklm.google.com" } }
---

# NotebookLM Integration

This skill provides access to Google NotebookLM through the `notebooklm-mcp` MCP server via `mcporter`.

## How It Works

`notebooklm-mcp` is an MCP server (uses stdin/stdout), not a direct CLI. This skill uses `mcporter` to:
1. Manage the MCP server lifecycle
2. Route tool calls to the appropriate MCP methods
3. Format responses for the agent

## Available Operations

### List Notebooks
```bash
{Dir}/notebooklm.sh list
```
Natural language: "List my NotebookLM notebooks"

### Create a Notebook
```bash
{Dir}/notebooklm.sh create "My Notebook" source_url=https://example.com
```
Natural language: "Create a NotebookLM notebook called 'Research' with URL https://example.com"

### Add Sources
```bash
{Dir}/notebooklm.sh add_source <notebook_id> source_url=https://example.com
```
Natural language: "Add https://example.com to my notebook <id>"

### Ask Questions
```bash
{Dir}/notebooklm.sh ask <notebook_id> "What are the main topics?"
```
Natural language: "Ask my notebook: What are the main topics?"

### Generate Study Guide
```bash
{Dir}/notebooklm.sh study_guide <notebook_id>
```
Natural language: "Generate a study guide for my notebook"

## Tips for the Agent

- **Always list notebooks first** to get notebook IDs
- Notebook IDs are required for most operations
- Sources can be: URLs, text snippets, or uploaded files
- Authentication tokens expire - if you get auth errors, ask the user to re-run `notebooklm-mcp-auth`
- Use the wrapper script `{Dir}/notebooklm.sh` for consistent mcporter routing
"""


def get_wrapper_script_template() -> str:
    """Return the wrapper script template"""
    return """#!/bin/bash
# NotebookLM MCP wrapper for OpenClaw using mcporter

set -euo pipefail

# Set mcporter config path to OpenClaw directory (accessible from sandbox)
export MCPORTER_CONFIG="${MCPORTER_CONFIG:-$HOME/.openclaw/mcporter.json}"

# Check if mcporter is available
if ! command -v mcporter &> /dev/null; then
    echo "Error: mcporter not found. Install it first:"
    echo "  npm install -g mcporter"
    exit 1
fi

# Check auth
AUTH_FILE="$HOME/.notebooklm-mcp/auth.json"
if [ ! -f "$AUTH_FILE" ]; then
    echo "Error: Not authenticated to NotebookLM."
    echo "Run: notebooklm-mcp-auth"
    exit 1
fi

# Parse the user's request and route to appropriate mcporter call
ACTION="$1"
shift

case "$ACTION" in
    list|list_notebooks)
        mcporter call notebooklm.notebook_list max_results="${1:-10}"
        ;;

    create|create_notebook)
        TITLE="$1"
        shift
        mcporter call notebooklm.notebook_create title="$TITLE" "$@"
        ;;

    add_source)
        NOTEBOOK_ID="$1"
        shift
        mcporter call notebooklm.notebook_addSource notebook_id="$NOTEBOOK_ID" "$@"
        ;;

    ask|query)
        NOTEBOOK_ID="$1"
        QUESTION="$2"
        mcporter call notebooklm.notebook_query notebook_id="$NOTEBOOK_ID" question="$QUESTION"
        ;;

    study_guide)
        NOTEBOOK_ID="$1"
        mcporter call notebooklm.notebook_generateStudyGuide notebook_id="$NOTEBOOK_ID"
        ;;

    *)
        echo "Usage: $0 {list|create|add_source|ask|study_guide} [args...]"
        echo ""
        echo "Examples:"
        echo "  $0 list"
        echo "  $0 create \\"My Notebook\\" source_url=https://example.com"
        echo "  $0 ask <notebook_id> \\"What are the main topics?\\""
        exit 1
        ;;
esac
"""


def main():
    """Main entry point"""
    installer = OpenClawNotebookLMInstaller()
    success = installer.install()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
