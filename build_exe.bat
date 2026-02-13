@echo off
echo ========================================
echo Compilando clazai.py a .exe
echo ========================================
echo.

:: Verificar si PyInstaller está instalado
echo Verificando PyInstaller...
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller no encontrado. Instalando...
    pip install pyinstaller
    if errorlevel 1 (
        echo ERROR: No se pudo instalar PyInstaller
        pause
        exit /b 1
    )
)
echo PyInstaller listo.
echo.

:: Limpiar builds anteriores
echo Limpiando builds anteriores...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
echo Limpieza completa.
echo.

:: Compilar el script
echo Iniciando compilacion...
pyinstaller --onefile --windowed --name="clazai" --icon=logo_clazai.png --add-data="logo_clazai.png;." clazai.py

if errorlevel 1 (
    echo.
    echo ERROR: La compilacion fallo
    pause
    exit /b 1
)

echo.
echo ========================================
echo Compilacion exitosa!
echo El archivo .exe se encuentra en: dist\clazai.exe
echo ========================================
echo.

:: Preguntar si quiere abrir la carpeta dist
set /p open="Quieres abrir la carpeta dist? (S/N): "
if /i "%open%"=="S" (
    explorer dist
)

pause
