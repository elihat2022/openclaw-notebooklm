# Guía de Publicación - openclaw-notebooklm

Pasos para publicar el paquete en PyPI y hacerlo disponible para que otros lo instalen.

## Pre-requisitos

1. **Cuenta en PyPI**: https://pypi.org/account/register/
2. **Cuenta en TestPyPI** (para testing): https://test.pypi.org/account/register/
3. **API Token de PyPI**:
   - Ve a https://pypi.org/manage/account/token/
   - Crea un nuevo token
   - Guárdalo en un lugar seguro

## 1. Preparar el Entorno

```bash
cd ~/.openclaw/openclaw-notebooklm-installer

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar herramientas de build
pip install --upgrade pip
pip install build twine
```

## 2. Probar la Instalación Localmente

```bash
# Instalar en modo desarrollo
pip install -e .

# Probar el comando
openclaw-notebooklm-install --help

# Si todo funciona, desinstalar
pip uninstall openclaw-notebooklm
```

## 3. Build del Paquete

```bash
# Limpiar builds anteriores
rm -rf dist/ build/ src/*.egg-info

# Build
python -m build

# Verificar que se crearon los archivos
ls -lh dist/
# Deberías ver:
# - openclaw_notebooklm-0.1.0-py3-none-any.whl
# - openclaw_notebooklm-0.1.0.tar.gz
```

## 4. Verificar el Paquete

```bash
# Verificar integridad
twine check dist/*

# Debería mostrar:
# Checking dist/openclaw_notebooklm-0.1.0-py3-none-any.whl: PASSED
# Checking dist/openclaw_notebooklm-0.1.0.tar.gz: PASSED
```

## 5. Publicar en TestPyPI (Opcional pero Recomendado)

```bash
# Subir a TestPyPI
twine upload --repository testpypi dist/*

# Te pedirá username y password
# Username: __token__
# Password: tu-token-de-testpypi
```

### Probar desde TestPyPI

```bash
# En un nuevo entorno
pip install --index-url https://test.pypi.org/simple/ openclaw-notebooklm

# Probar
openclaw-notebooklm-install
```

## 6. Publicar en PyPI (Producción)

```bash
# Subir a PyPI
twine upload dist/*

# Te pedirá username y password
# Username: __token__
# Password: tu-token-de-pypi
```

## 7. Verificar Publicación

```bash
# Visitar la página del paquete
open https://pypi.org/project/openclaw-notebooklm/

# Instalar desde PyPI
pip install openclaw-notebooklm

# Probar
openclaw-notebooklm-install
```

## 8. Crear un Release en GitHub

```bash
# Tag de la versión
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0

# Ir a GitHub y crear un Release desde el tag
# URL: https://github.com/tu-usuario/openclaw-notebooklm/releases/new
```

## Actualizar Versión (Para Futuras Releases)

1. **Actualizar versión en `pyproject.toml`**:
   ```toml
   version = "0.2.0"  # Incrementar versión
   ```

2. **Actualizar versión en `src/openclaw_notebooklm/__init__.py`**:
   ```python
   __version__ = "0.2.0"
   ```

3. **Crear el build**:
   ```bash
   rm -rf dist/
   python -m build
   ```

4. **Publicar**:
   ```bash
   twine upload dist/*
   ```

## Configurar GitHub Actions (Opcional)

Crea `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

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

    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

Luego agrega el token como secret en GitHub:
- Ve a Settings → Secrets → Actions
- Crea un nuevo secret llamado `PYPI_API_TOKEN`
- Pega tu token de PyPI

## Checklist Pre-Publicación

- [ ] Probado localmente con `pip install -e .`
- [ ] README.md completo y claro
- [ ] LICENSE incluido
- [ ] Versión actualizada en `pyproject.toml` y `__init__.py`
- [ ] `twine check dist/*` pasa sin errores
- [ ] Probado en TestPyPI
- [ ] Repositorio Git actualizado
- [ ] Tag de versión creado

## URLs Útiles

- **PyPI Package**: https://pypi.org/project/openclaw-notebooklm/
- **TestPyPI Package**: https://test.pypi.org/project/openclaw-notebooklm/
- **PyPI Account**: https://pypi.org/manage/account/
- **API Tokens**: https://pypi.org/manage/account/token/

## Troubleshooting

### Error: "File already exists"

Si ya publicaste esa versión, no puedes volver a subirla. Necesitas incrementar la versión.

### Error: "Invalid or non-existent authentication"

Verifica que estás usando:
- Username: `__token__`
- Password: tu token completo (incluyendo el prefijo `pypi-`)

### Error: "Package name already taken"

El nombre `openclaw-notebooklm` debe estar disponible. Si no, cambia el nombre en `pyproject.toml`.

## Promoción

Una vez publicado:

1. **Anunciar en la comunidad de OpenClaw**
2. **Crear un post en Reddit** (r/Python, r/AI)
3. **Tweet** sobre el lanzamiento
4. **Actualizar documentación** de OpenClaw si es relevante
5. **Agregar a awesome-lists** relacionadas con MCP o OpenClaw

---

¡Listo para publicar! 🚀
