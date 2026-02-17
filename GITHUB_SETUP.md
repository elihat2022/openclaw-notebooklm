# Configuración de GitHub para openclaw-notebooklm

## 1. Crear el Repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre del repositorio: `openclaw-notebooklm`
3. Descripción: "One-command installer for integrating Google NotebookLM with OpenClaw via MCP"
4. Público/Privado: **Público** (para publicar en PyPI)
5. No inicializar con README (ya lo tenemos)
6. Click "Create repository"

## 2. Inicializar Git Local

```bash
cd ~/.openclaw/openclaw-notebooklm-installer

# Inicializar git
git init

# Agregar archivos
git add .

# Primer commit
git commit -m "Initial commit: OpenClaw NotebookLM installer v0.1.0"

# Agregar remote (reemplaza TU-USERNAME)
git remote add origin https://github.com/TU-USERNAME/openclaw-notebooklm.git

# Push
git branch -M main
git push -u origin main
```

## 3. Configurar Botón de Sponsor (Buy Me a Coffee)

El archivo `.github/FUNDING.yml` ya está creado, así que cuando subas el código:

1. Ve a tu repositorio en GitHub
2. Verás un botón "❤️ Sponsor" automáticamente
3. Al hacer click, te llevará a https://buymeacoffee.com/elihatdeveloper

## 4. Agregar Topics en GitHub

En la página del repo, click en el ícono de engranaje junto a "About" y agrega estos topics:

- `openclaw`
- `notebooklm`
- `mcp`
- `model-context-protocol`
- `ai`
- `python`
- `automation`
- `installer`

## 4. Crear el Primer Release

```bash
# Crear tag
git tag -a v0.1.0 -m "Release v0.1.0 - Initial release"
git push origin v0.1.0
```

Luego en GitHub:

1. Ve a la pestaña "Releases"
2. Click "Create a new release"
3. Selecciona el tag `v0.1.0`
4. Título: "v0.1.0 - Initial Release"
5. Descripción:

```markdown
## 🎉 First Release

One-command installer for integrating Google NotebookLM with OpenClaw.

### Features

- ✅ Automated installation and configuration
- 📦 Installs all dependencies (mcporter, notebooklm-mcp)
- 🔐 Handles NotebookLM authentication
- 📂 Creates OpenClaw skill structure
- ⚙️ Configures OpenClaw automatically

### Installation

```bash
pip install openclaw-notebooklm
openclaw-notebooklm-install
```

### What's Included

- NotebookLM skill for OpenClaw
- Wrapper script for mcporter integration
- Automatic configuration management
- Complete documentation

### Requirements

- OpenClaw installed
- Node.js (for npm packages)
- Google account (for NotebookLM)

### Documentation

See [README.md](https://github.com/TU-USERNAME/openclaw-notebooklm#readme) for full documentation.
```

6. Click "Publish release"

## 5. Agregar GitHub Actions (Opcional)

Crea `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [created]

permissions:
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine

    - name: Build package
      run: python -m build

    - name: Check package
      run: twine check dist/*

    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

Configurar el secret:

1. Ve a Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Nombre: `PYPI_API_TOKEN`
4. Valor: Tu token de PyPI
5. Click "Add secret"

## 6. Agregar Badge al README

Edita `README.md` y actualiza los badges:

```markdown
[![PyPI version](https://badge.fury.io/py/openclaw-notebooklm.svg)](https://badge.fury.io/py/openclaw-notebooklm)
[![Python Support](https://img.shields.io/pypi/pyversions/openclaw-notebooklm.svg)](https://pypi.org/project/openclaw-notebooklm/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/openclaw-notebooklm)](https://pepy.tech/project/openclaw-notebooklm)
```

## 7. Configurar GitHub Pages (Opcional)

Para documentación adicional:

1. Ve a Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main` / `docs` (si creas una carpeta docs/)
4. Click "Save"

## 8. Agregar Plantillas de Issues

Crea `.github/ISSUE_TEMPLATE/bug_report.md`:

```markdown
---
name: Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. See error

**Expected behavior**
What you expected to happen.

**Environment:**
 - OS: [e.g. macOS 13.0]
 - Python version: [e.g. 3.11]
 - openclaw-notebooklm version: [e.g. 0.1.0]
 - OpenClaw version: [e.g. 2026.2.9]

**Additional context**
Add any other context about the problem here.
```

Crea `.github/ISSUE_TEMPLATE/feature_request.md`:

```markdown
---
name: Feature request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

**Is your feature request related to a problem?**
A clear description of what the problem is.

**Describe the solution you'd like**
What you want to happen.

**Describe alternatives you've considered**
Other solutions you've thought about.

**Additional context**
Any other context or screenshots.
```

## 9. Agregar Archivo de Contribución

Crea `CONTRIBUTING.md`:

```markdown
# Contributing to openclaw-notebooklm

Thank you for your interest in contributing! 🎉

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test locally (`./test_install.sh`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

```bash
git clone https://github.com/TU-USERNAME/openclaw-notebooklm.git
cd openclaw-notebooklm
pip install -e .
```

## Testing

```bash
./test_install.sh
```

## Code Style

- Follow PEP 8
- Use type hints where possible
- Add docstrings to functions
- Keep functions focused and small

## Reporting Bugs

Use the GitHub issue tracker with the bug report template.

## Questions?

Open a discussion on GitHub Discussions.
```

## 10. Actualizar URLs en pyproject.toml

Edita `pyproject.toml` y reemplaza las URLs:

```toml
[project.urls]
Homepage = "https://github.com/TU-USERNAME/openclaw-notebooklm"
Documentation = "https://github.com/TU-USERNAME/openclaw-notebooklm#readme"
Repository = "https://github.com/TU-USERNAME/openclaw-notebooklm.git"
Issues = "https://github.com/TU-USERNAME/openclaw-notebooklm/issues"
```

## 11. Checklist Final

- [ ] Repositorio creado en GitHub
- [ ] Código subido con `git push`
- [ ] Topics agregados
- [ ] README actualizado con URLs correctas
- [ ] License incluido (MIT)
- [ ] Issue templates creados
- [ ] CONTRIBUTING.md creado
- [ ] GitHub Actions configurado (opcional)
- [ ] Primer release creado
- [ ] PyPI secret configurado (si usas Actions)

---

¡Listo para compartir con la comunidad! 🚀
