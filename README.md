# 📡 Monitor de Red y Test de Velocidad

Este script de Python realiza monitoreos diarios del uso de red en tu máquina y ejecuta un test de velocidad para registrar el rendimiento de tu conexión a internet. Los resultados se guardan en archivos `.txt` dentro de la carpeta `logs`.

---

## 🚀 Características

- Obtiene estadísticas de uso de red (datos enviados, recibidos, errores, etc.).
- Ejecuta un test de velocidad (descarga, subida y ping).
- Genera informes diarios automáticos a las 22:00 hs.
- Posibilidad de ejecución manual inmediata.
- Guarda los informes con timestamp en una carpeta `logs/`.

---

## 📦 Requisitos

Instalá las dependencias necesarias con:

```bash
pip install psutil schedule speedtest-cli

🛠️ Uso
▶️ Ejecución Manual

Al ejecutar el script, se genera un informe inmediato y se muestra en consola:

python script.py

El archivo generado se guarda en la carpeta logs con el formato:

reporte_YYYY-MM-DD_HH-MM-SS.txt

🔁 Ejecución Automática

El script queda corriendo en segundo plano y generará un informe automáticamente todos los días a las 22:00 hs.
📁 Estructura de Carpeta

/
├── logs/
│   └── reporte_2025-04-14_22-00-00.txt
├── script.py
├── README.md

📋 Ejemplo de Informe

📅 Informe AUTOMÁTICO de Internet - 2025-04-14 a las 22-00-00
============================================================
📶 USO DE RED
  - MB Enviados   : 12.34 MB
  - MB Recibidos  : 56.78 MB
  - Paquetes Enviados : 1234
  - Paquetes Recibidos: 5678
  - Errores Entrada: 0
  - Errores Salida : 0

🚀 TEST DE VELOCIDAD
  - Descarga (↓): 45.67 Mbps
  - Subida   (↑): 12.34 Mbps
  - Ping         : 23.45 ms
============================================================