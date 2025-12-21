# clazai

**claude code to z.ai toggle**

Una aplicación GUI para configurar e integrar Z.AI con Claude Code fácilmente.

![clazai](https://img.shields.io/badge/python-3.x-blue.svg)
![platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey.svg)

## 🚀 Características

- **Configuración de API Token**: Ingresa y guarda tu token API de Z.AI de forma segura
- **Seguridad**: El token se oculta por defecto con opción de mostrar
- **Integración con Claude Code**: Botón toggle para activar/desactivar Z.AI con un solo clic
- **Detección automática**: Detecta automáticamente el directorio del usuario
- **Configuración completa**: Establece todos los modelos por defecto de Z.AI
- **Estado en tiempo real**: Muestra si Z.AI está activado o desactivado
- **Ayuda integrada**: Instrucciones detalladas para obtener tu API key

## 📦 Requisitos

- Python 3.x (tkinter viene incluido por defecto)
- Claude Code instalado
- Una API Key de Z.AI

## 🛠️ Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/clazai.git
   cd clazai
   ```

2. Ejecuta la aplicación:
   ```bash
   python zai_config.py
   ```

## 📖 Cómo usar

### 1. Obtener tu API Key de Z.AI

1. Accede a [Z.AI Open Platform](https://z.ai)
2. Regístrate o inicia sesión
3. Crea una API Key en la página de administración
4. Copia tu API Key

### 2. Configurar el API Token

1. Abre la aplicación `clazai`
2. Pega tu token API en el campo correspondiente
3. Haz clic en "Save" para guardarlo localmente

### 3. Activar Z.AI en Claude Code

1. Asegúrate de haber guardado tu token API
2. Haz clic en el botón "Activar" en la sección "Claude Code Integration"
3. ¡Listo! Claude Code ahora usará los modelos de Z.AI

### 4. Desactivar Z.AI

Cuando quieras volver a usar los modelos originales de Anthropic:
1. Haz clic en el botón "Desactivar"
2. La configuración de Z.AI será eliminada

## ⚙️ Configuración

Al activar Z.AI, el programa configura automáticamente las siguientes variables de entorno en `~/.claude/settings.json`:

```json
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "tu_token_aqui",
        "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic",
        "API_TIMEOUT_MS": "3000000",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.5-air",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-4.6",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-4.6"
    }
}
```

## 📁 Archivos

- **`zai_config.py`**: Aplicación principal
- **`zai_config.json`**: Archivo local que almacena tu token API (creado automáticamente)
- **`~/.claude/settings.json`**: Configuración de Claude Code (modificado automáticamente)

## 🔒 Seguridad

- El token se almacena localmente en `zai_config.json`
- El token está oculto por defecto en la interfaz
- Puedes borrar el archivo `zai_config.json` en cualquier momento

## 🤝 Contribuir

Las contribuciones son bienvenidas! Por favor:

1. Fork este repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Made by @cisnerosnow**

## 🙏 Agradecimientos

- Gracias al equipo de Z.AI por su increíble plataforma
- Gracias a Anthropic por Claude Code

---

**Disclaimer**: Esta herramienta no es oficial de Z.AI ni de Anthropic. Es una aplicación de terceros para facilitar la configuración.