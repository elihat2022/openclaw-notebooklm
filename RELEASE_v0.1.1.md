# Release v0.1.1 - Instructions

## Cambios en esta versión

- ✅ Agregados enlaces de Buy Me a Coffee
- ✅ Botón de GitHub Sponsors
- ✅ Sección de soporte en README

## Pasos para publicar

### 1. Limpiar builds anteriores

```bash
cd ~/.openclaw/openclaw-notebooklm-installer
rm -rf dist/ build/ src/*.egg-info
```

### 2. Commit y Tag en Git

```bash
# Agregar cambios
git add .

# Commit
git commit -m "Bump version to 0.1.1 - Add Buy Me a Coffee support"

# Crear tag
git tag -a v0.1.1 -m "Release v0.1.1 - Add sponsorship links"

# Push
git push origin main
git push origin v0.1.1
```

### 3. Build del paquete

```bash
# Activar venv si es necesario
# source venv/bin/activate

# Instalar tools si aún no lo hiciste
pip install build twine

# Build
python -m build

# Verificar
ls -lh dist/
# Deberías ver:
# openclaw_notebooklm-0.1.1-py3-none-any.whl
# openclaw_notebooklm-0.1.1.tar.gz
```

### 4. Verificar integridad

```bash
twine check dist/*
# Expected: PASSED for both files
```

### 5. Publicar en PyPI

```bash
# Upload
twine upload dist/*

# Credenciales:
# Username: __token__
# Password: <tu-pypi-token>
```

### 6. Verificar publicación

```bash
# Abrir PyPI
open https://pypi.org/project/openclaw-notebooklm/

# Verificar que sea version 0.1.1
# Verificar que el README muestre los badges de Buy Me a Coffee
```

### 7. Crear Release en GitHub

1. Ve a: https://github.com/TU-USERNAME/openclaw-notebooklm/releases/new
2. Selecciona tag: `v0.1.1`
3. Release title: `v0.1.1 - Sponsorship Support`
4. Description:

```markdown
## 🎉 Version 0.1.1

### What's New

Added support links to help maintain and improve this project:

- ☕ Buy Me a Coffee badge in README
- ❤️ GitHub Sponsors button
- 📋 Funding metadata in package
- 📝 Support section in documentation

### How to Update

If you already have v0.1.0 installed:

```bash
pip install --upgrade openclaw-notebooklm
```

### Full Changelog

See [CHANGELOG.md](https://github.com/TU-USERNAME/openclaw-notebooklm/blob/main/CHANGELOG.md)

### Installation

```bash
pip install openclaw-notebooklm
openclaw-notebooklm-install
```

### Support This Project

If you find this project useful, consider [buying me a coffee](https://buymeacoffee.com/elihatdeveloper)! ☕

Your support helps maintain and improve this project.
```

5. Click "Publish release"

### 8. Anunciar (Opcional)

Tweet/Post ejemplo:

```
🚀 openclaw-notebooklm v0.1.1 released!

New: Support links added - buy me a coffee if you find it useful! ☕

Install: pip install openclaw-notebooklm

#OpenClaw #NotebookLM #Python #OpenSource

https://github.com/TU-USERNAME/openclaw-notebooklm
https://buymeacoffee.com/elihatdeveloper
```

## Verificación Final

- [ ] Versión actualizada en `pyproject.toml` (0.1.1)
- [ ] Versión actualizada en `__init__.py` (0.1.1)
- [ ] CHANGELOG.md creado y actualizado
- [ ] Commit realizado
- [ ] Tag v0.1.1 creado y pusheado
- [ ] Build exitoso
- [ ] `twine check` pasa
- [ ] Publicado en PyPI
- [ ] Release creado en GitHub
- [ ] Botón "Sponsor" visible en GitHub
- [ ] README en PyPI muestra badges correctamente

## Rollback (Si algo sale mal)

```bash
# Borrar tag local
git tag -d v0.1.1

# Borrar tag remoto
git push origin :refs/tags/v0.1.1

# Revertir commit (si aún no pusheaste)
git reset --soft HEAD~1
```

**Nota**: No puedes borrar una versión de PyPI una vez publicada. Solo puedes "yank" (ocultar):

```bash
# Yank version from PyPI (no la borra, la oculta)
# pip install --force-reinstall aún podrá instalarla
```

---

**Ready to release! 🚀**
