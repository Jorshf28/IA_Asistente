from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

# Texto a convertir en voz
texto = "Alerta, Humedad baja, Por favor, riega la planta"

# Crear archivo de audio usando gTTS
tts = gTTS(text=texto, lang='es')  # Puedes cambiar 'es' por otros códigos de idioma (por ejemplo, 'en' para inglés)

# Guardar como archivo temporal en MP3
archivo_temp = "temp.mp3"
tts.save(archivo_temp)

# Reproducir el audio (opcional)
audio = AudioSegment.from_file(archivo_temp)
play(audio)

# Guardar como archivo MP3 definitivo
archivo_final = "voz_ejemplo.mp3"
audio.export(archivo_final, format="mp3")

# Eliminar el archivo temporal
os.remove(archivo_temp)

print(f"Archivo de voz guardado como {archivo_final}")