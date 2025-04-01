import random
import speech_recognition as sr
import pyttsx3
import datetime
import json
import os


class Asistente_IA:
    def __init__(self):
        # Configuración inicial
        self.nombre = "Jarvis"
        self.perfil_usuario = self.cargar_perfil()
        self.conocimiento = {
            "preferencias": {},
            "historial_interacciones": [],
            "tareas_aprendidas": []
        }

        # Configuración de reconocimiento de voz y síntesis
        self.reconocedor = sr.Recognizer()
        self.motor_voz = pyttsx3.init()

    def cargar_perfil(self):
        """Cargar perfil de usuario guardado"""
        try:
            with open('perfil_usuario.json', 'r') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {
                "nombre": "Usuario",
                "preferencias": {},
                "nivel_personalización": 0
            }

    def guardar_perfil(self):
        """Guardar perfil de usuario actualizado"""
        with open('perfil_usuario.json', 'w') as archivo:
            json.dump(self.perfil_usuario, archivo, indent=4)

    def escuchar(self):
        """Escuchar comandos de voz"""
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = self.reconocedor.listen(source)
            try:
                comando = self.reconocedor.recognize_google(audio, language='es-ES')
                return comando.lower()
            except sr.UnknownValueError:
                print("No entendí el comando")
                return ""

    def hablar(self, texto):
        """Convertir texto a voz"""
        self.motor_voz.say(texto)
        self.motor_voz.runAndWait()

    def analizar_comando(self, comando):
        """Analizar y procesar comandos con capacidad de aprendizaje"""
        comandos_conocidos = {
            "hora": self.dar_hora,
            "fecha": self.dar_fecha,
            "clima": self.simular_clima,
            "saludar": self.saludar
        }

        # Búsqueda de comando
        for key, funcion in comandos_conocidos.items():
            if key in comando:
                return funcion()

        # Modo de aprendizaje adaptativo
        self.aprender_nuevo_comando(comando)
        return "Comando no reconocido, pero he tomado nota para aprender."

    def aprender_nuevo_comando(self, comando):
        """Registrar comandos nuevos para futuro aprendizaje"""
        self.conocimiento["historial_interacciones"].append(comando)

        # Simulación de aprendizaje
        if len(self.conocimiento["historial_interacciones"]) > 5:
            nuevo_comando = random.choice(self.conocimiento["historial_interacciones"])
            print(f"Nuevo comando aprendido: {nuevo_comando}")
            self.conocimiento["tareas_aprendidas"].append(nuevo_comando)

    def dar_hora(self):
        """Mostrar hora actual"""
        hora = datetime.datetime.now().strftime("%H:%M")
        self.hablar(f"Son las {hora}")
        return f"Hora actual: {hora}"

    def dar_fecha(self):
        """Mostrar fecha actual"""
        fecha = datetime.datetime.now().strftime("%d de %B de %Y")
        self.hablar(f"Hoy es {fecha}")
        return f"Fecha actual: {fecha}"

    def simular_clima(self):
        """Simular información del clima"""
        clima_opciones = [
            "Soleado con 25 grados",
            "Nublado con probabilidad de lluvia",
            "Frío con 15 grados"
        ]
        clima = random.choice(clima_opciones)
        self.hablar(f"El clima de hoy está {clima}")
        return f"Clima: {clima}"

    def saludar(self):
        """Saludar de manera personalizada"""
        nombre = self.perfil_usuario.get("nombre", "Usuario")
        saludos = [
            f"Hola {nombre}, ¿en qué puedo ayudarte?",
            f"Buenas, {nombre}. Estoy listo para tus órdenes.",
            f"Un placer verte, {nombre}. ¿Qué necesitas?"
        ]
        saludo = random.choice(saludos)
        self.hablar(saludo)
        return saludo

    def iniciar(self):
        """Bucle principal del asistente"""
        self.hablar("Sistemas Jarvis activados. Estoy a su servicio.")

        while True:
            comando = self.escuchar()
            if comando:
                print(f"Comando recibido: {comando}")
                respuesta = self.analizar_comando(comando)
                print(respuesta)

                if "apagar" in comando or "desactivar" in comando:
                    self.hablar("Desactivando sistemas. Hasta pronto.")
                    break


# Inicializar y ejecutar Jarvis
if __name__ == "__main__":
    jarvis = Asistente_IA()
    jarvis.iniciar()