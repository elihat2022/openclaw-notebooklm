# Quick Start - Publicar openclaw-notebooklm

## 🎯 Objetivo

Publicar el paquete `openclaw-notebooklm` en PyPI para que otros usuarios puedan instalar la integración de NotebookLM con OpenClaw con un solo comando.

---

## ⚡ TL;DR - Pasos Rápidos

```bash
cd ~/.openclaw/openclaw-notebooklm-installer

# 1. Probar localmente
pip install -e .
openclaw-notebooklm-install

# 2. Build
python -m build

# 3. Verificar
twine check dist/*

# 4. Publicar
twine upload dist/*
```

---

## 📝 Checklist Completo

### Pre-requisitos

- [ ] Cuenta en PyPI: https://pypi.org/account/register/
- [ ] API Token de PyPI: https://pypi.org/manage/account/token/
- [ ] GitHub account (para repo público)

### 1. Testing Local

```bash
cd ~/.openclaw/openclaw-notebooklm-installer

# Crear venv
python3 -m venv venv
source venv/bin/activate

# Instalar build tools
pip install build twine

# Instalar en modo desarrollo
pip install -e .

# Probar
openclaw-notebooklm-install

# ¿Funcionó? ✅ Continuar
# ¿No funcionó? ❌ Debuggear primero
```

### 2. Crear Repositorio en GitHub

```bash
# Inicializar git
git init
git add .
git commit -m "Initial commit: openclaw-notebooklm v0.1.0"

# Crear repo en GitHub primero (web UI):
# https://github.com/new
# Nombre: openclaw-notebooklm
# Público

# Conectar y push
git remote add origin https://github.com/TU-USERNAME/openclaw-notebooklm.git
git branch -M main
git push -u origin main

# Crear tag y release
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
```

### 3. Build del Paquete

```bash
# Limpiar builds anteriores
rm -rf dist/ build/ src/*.egg-info

# Build
python -m build

# Verificar archivos creados
ls -lh dist/
# Deberías ver:
# openclaw_notebooklm-0.1.0-py3-none-any.whl
# openclaw_notebooklm-0.1.0.tar.gz

# Verificar integridad
twine check dist/*
# Expected: PASSED para ambos archivos
```

### 4. Publicar en PyPI

```bash
# Upload
twine upload dist/*

# Cuando pida credenciales:
# Username: __token__
# Password: <pega-tu-token-de-pypi>

# Verificar publicación
open https://pypi.org/project/openclaw-notebooklm/
```

### 5. Verificar Instalación Final

```bash
# En un nuevo terminal (sin venv)
pip install openclaw-notebooklm

# Probar
openclaw-notebooklm-install

# Si funciona: 🎉 ¡Éxito!
```

---

## 🔧 Comandos de Referencia Rápida

### Desarrollo

```bash
# Instalar en modo editable
pip install -e .

# Ejecutar tests
./test_install.sh

# Desinstalar
pip uninstall openclaw-notebooklm
```

### Build & Publish

```bash
# Limpiar
rm -rf dist/ build/ src/*.egg-info

# Build
python -m build

# Check
twine check dist/*

# Test upload (TestPyPI)
twine upload --repository testpypi dist/*

# Producción upload (PyPI)
twine upload dist/*
```

### Git

```bash
# Commit cambios
git add .
git commit -m "Description"
git push

# Nueva versión
# 1. Actualizar version en pyproject.toml
# 2. Actualizar version en __init__.py
git add .
git commit -m "Bump version to 0.2.0"
git tag -a v0.2.0 -m "Release v0.2.0"
git push origin main v0.2.0
```

---

## 📦 Estructura del Paquete

```
openclaw-notebooklm/
├── src/openclaw_notebooklm/
│   ├── __init__.py              # Version info
│   └── installer.py             # Main installer logic
├── pyproject.toml               # Package config
├── README.md                    # User docs
├── LICENSE                      # MIT
├── PUBLISHING.md                # This guide (detailed)
├── GITHUB_SETUP.md              # GitHub setup guide
├── PACKAGE_OVERVIEW.md          # Technical overview
└── test_install.sh              # Local test script
```

---

## 🐛 Troubleshooting

### Error: "File already exists"

**Causa**: Ya publicaste esa versión.

**Solución**: Incrementa la versión en `pyproject.toml` y `__init__.py`.

### Error: "Invalid authentication"

**Causa**: Token incorrecto o username incorrecto.

**Solución**:
- Username debe ser exactamente: `__token__`
- Password debe ser tu token completo (con el prefijo `pypi-`)

### Error: "Package name taken"

**Causa**: Otro paquete ya usa ese nombre.

**Solución**: Cambiar `name` en `pyproject.toml` a algo único.

---

## 📚 Documentos Importantes

| Archivo | Propósito |
|---------|-----------|
| `README.md` | Documentación para usuarios finales |
| `PUBLISHING.md` | Guía detallada de publicación en PyPI |
| `GITHUB_SETUP.md` | Configurar GitHub repo y releases |
| `PACKAGE_OVERVIEW.md` | Vista técnica completa del paquete |
| `QUICK_START.md` | Este archivo - referencia rápida |

---

## 🎯 Próximos Pasos Después de Publicar

1. **Anunciar en la comunidad**:
   - OpenClaw Discord
   - Reddit r/Python y r/AI
   - Twitter/X
   - LinkedIn

2. **Monitorear**:
   - GitHub issues
   - PyPI download stats
   - User feedback

3. **Mejorar**:
   - Agregar tests
   - Mejorar docs
   - Nuevas features (ver PACKAGE_OVERVIEW.md)

---

## 💬 Plantilla de Anuncio

Para cuando publiques:

```
🚀 Nuevo paquete: openclaw-notebooklm

Integra Google NotebookLM con OpenClaw en un solo comando.

pip install openclaw-notebooklm
openclaw-notebooklm-install

✅ Auto-instala dependencias
✅ Configura todo automáticamente
✅ Maneja autenticación
✅ Setup completo en 2 minutos

GitHub: https://github.com/TU-USERNAME/openclaw-notebooklm
PyPI: https://pypi.org/project/openclaw-notebooklm/

#OpenClaw #NotebookLM #AI #Python #Automation
```

---

## ✅ Checklist Final Pre-Publicación

Testing:
- [ ] Funciona localmente con `pip install -e .`
- [ ] `./test_install.sh` pasa sin errores
- [ ] El skill aparece en `openclaw skills list`
- [ ] Puede listar notebooks correctamente

Documentación:
- [ ] README completo y claro
- [ ] Ejemplos de uso funcionan
- [ ] URLs actualizadas (no dice "TU-USERNAME")
- [ ] LICENSE incluido

Código:
- [ ] Versión correcta en `pyproject.toml`
- [ ] Versión correcta en `__init__.py`
- [ ] Code funciona sin errores
- [ ] Mensajes de error claros

Git/GitHub:
- [ ] Repositorio público creado
- [ ] Código pusheado
- [ ] Tag v0.1.0 creado
- [ ] Release creado con descripción

PyPI:
- [ ] `twine check dist/*` pasa
- [ ] Cuenta y token listos

Promoción:
- [ ] Anuncio preparado
- [ ] Screenshots/demos listos (opcional)

---

**¡Estás listo para publicar! 🎉**

Cualquier pregunta, revisa los otros documentos o abre un issue.
