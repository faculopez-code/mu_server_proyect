import re
import subprocess
import shutil

# --- Paso 1: pedir IP al usuario ---
ip_nueva = input("🔧 Ingresá la nueva IP para configurar el servidor: ").strip()

# Verificación mínima de formato de IP
if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip_nueva):
    print("❌ IP inválida. Asegurate de usar el formato 123.123.123.123")
    exit()

print(f"✅ Usando IP: {ip_nueva}")

# --- Paso 2: modificar archivos de configuración ---
archivos_txt = [
    "MuServer/ConnectServer/ServerList.dat",
    "MuServer/Data/MapServerInfo.dat",
    "MuServer/Tools/MAIN_INFO/Maininfo.ini",
    "MuServer/Tools/AH_INFO/ClientInfo.ini"
]

for ruta in archivos_txt:
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()

        # Buscar y reemplazar cualquier IP en el texto
        contenido_modificado = re.sub(r"\d{1,3}(?:\.\d{1,3}){3}", ip_nueva, contenido)

        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido_modificado)

        print(f"📝 Archivo actualizado: {ruta}")
    except Exception as e:
        print(f"❌ Error al modificar {ruta}: {e}")

# --- Paso 3: ejecutar GetClientInfo.exe ---
try:
    print("⚙️ Ejecutando GetClientInfo.exe...")
    subprocess.run(["MuServer/Tools/AH_INFO/GetClientInfo.exe"], check=True) 
    print("✅ GetClientInfo ejecutado correctamente.")
except Exception as e:
    print(f"❌ Error ejecutando GetClientInfo.exe: {e}")

# --- Paso 4: mover archivos generados al Cliente/ ---
archivos_generados = [
    "MuServer/Tools/AH_INFO/ah.emu",
    "MuServer/Tools/AH_INFO/MHPClient.dll",
    "MuServer/Tools/AH_INFO/MHPVerify.dll"
]

for archivo in archivos_generados:
    try:
        destino = f"Cliente/{archivo.split('/')[-1]}"
        shutil.copy(archivo, destino)
        print(f"📁 Archivo copiado: {archivo} → {destino}")
    except Exception as e:
        print(f"❌ Error al copiar {archivo}: {e}")

print("\n🎉 Todo listo. Los archivos han sido actualizados y copiados.")
