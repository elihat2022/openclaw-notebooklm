#!/bin/bash
# Script de prueba local del instalador

set -e

echo "======================================"
echo "Testing openclaw-notebooklm installer"
echo "======================================"
echo ""

# Crear backup de configuraciones existentes
echo "[*] Creating backups..."
BACKUP_DIR="/tmp/openclaw-notebooklm-backup-$(date +%s)"
mkdir -p "$BACKUP_DIR"

if [ -d "$HOME/.openclaw/skills/notebooklm" ]; then
    cp -r "$HOME/.openclaw/skills/notebooklm" "$BACKUP_DIR/"
    echo "    Backed up skill to $BACKUP_DIR"
fi

if [ -f "$HOME/.openclaw/openclaw.json" ]; then
    cp "$HOME/.openclaw/openclaw.json" "$BACKUP_DIR/"
    echo "    Backed up openclaw.json to $BACKUP_DIR"
fi

if [ -f "$HOME/.openclaw/mcporter.json" ]; then
    cp "$HOME/.openclaw/mcporter.json" "$BACKUP_DIR/"
    echo "    Backed up mcporter.json to $BACKUP_DIR"
fi

echo ""
echo "[*] Installing package in development mode..."
pip install -e .

echo ""
echo "[*] Running installer..."
openclaw-notebooklm-install

echo ""
echo "======================================"
echo "Installation test complete!"
echo "======================================"
echo ""
echo "Backups saved to: $BACKUP_DIR"
echo ""
echo "To restore backups:"
echo "  cp -r $BACKUP_DIR/* $HOME/.openclaw/"
echo ""
