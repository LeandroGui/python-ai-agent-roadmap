"""
------------------------------------------------------------------------------
PROYECTO INTEGRADOR NIVEL 1: CORTEX CLI (v0.1)
------------------------------------------------------------------------------
Autor: Leandro Guiñazu
Nivel: Básico (Fundamentos de Python)
Descripción:
    Este script implementa un agente conversacional básico que opera en la consola.
    Simula el ciclo de vida de una IA (Input -> Process -> Output) y demuestra
    la persistencia de datos mediante archivos de texto.

Características Técnicas:
    - Bucle infinito (While True) para ejecución continua.
    - Persistencia de datos (Lectura/Escritura de logs).
    - Modularización mediante funciones (Skills).
    - Manejo de excepciones (Try/Except) para robustez.
    - Procesamiento básico de cadenas de texto.

Uso:
    Ejecutar este script en terminal: `python cortex_cli.py`
    Comandos disponibles: 'hola', 'memoria', 'analizar: [texto]', 'salir'.
------------------------------------------------------------------------------
"""

import os
import datetime

# --- CONFIGURACIÓN INICIAL ---
AGENT_NAME = "CORTEX v0.1"
MEMORY_FILE = "cortex_memory.txt"

def load_memory():
    """Carga el historial desde un archivo de texto si existe."""
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return f.readlines()

def save_memory(entry):
    """Guarda una nueva interacción en el archivo."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_entry = f"[{timestamp}] {entry}\n"

    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(formatted_entry)

def analyze_input(text):
    """
    Capacidad Analítica Básica:
    Cuenta palabras y detecta si es una pregunta.
    """
    # split() Convierte el texto en una lista de palabras individuales
    # para poder contarlas o procesarlas.
    words = text.split()
    stats = {
        "longitud": len(words),
        "es_pregunta": "?" in text,
        "contiene_numeros": any(char.isdigit() for char in text)
    }
    print(f"estoy visualizando stats: {stats}")
    return stats

def run_cortex():
    print(f"🔵 {AGENT_NAME} INICIADO. Escribe 'salir' para terminar.")
    print("---")

    while True:
        try:
            # 1. PERCEPCIÓN (Input)

            # strip() limpia el texto ingresado quitando espacios en blanco
            # o saltos de línea sobrantes.
            user_input = input("TU: ").strip()

            if not user_input:
                continue

            # Condición de salida
            if user_input.lower() in ["salir", "exit", "off"]:
                print(f"🔴 {AGENT_NAME} APAGANDO...")
                break

            # 2. RAZONAMIENTO (Processing)
            # Guardamos en memoria lo que dijo el usuario
            save_memory(f"User: {user_input}")

            response = ""

            # Comandos simples (Hardcoded skills)
            if user_input.lower() == "hola":
                response = "Hola, Leandro. Soy Cortex. ¿Qué datos analizamos hoy?"

            elif user_input.lower() == "memoria":
                # Leer archivo
                history = load_memory()
                response = f"He recordado {len(history)} eventos pasados.\nÚltimos 3:\n" + "".join(history[-3:])

            elif user_input.lower().startswith("analizar:"):
                # Simulación de Data Science Tool
                content_to_analyze = user_input.split(":", 1)[1]
                stats = analyze_input(content_to_analyze)
                response = f"📊 REPORTE DE ANÁLISIS:\n- Palabras: {stats['longitud']}\n- ¿Pregunta?: {stats['es_pregunta']}\n- Datos numéricos: {stats['contiene_numeros']}"

            else:
                response = "Comando no reconocido. Prueba: 'hola', 'memoria', o 'analizar: [texto]'."

            # 3. ACCIÓN (Output)
            print(f"🤖 CORTEX: {response}")

            # Guardamos en memoria lo que respondió Cortex
            save_memory(f"Cortex: {response.replace(chr(10), ' ')}") # chr(10) es salto de linea

        except KeyboardInterrupt:
            print("\n⚠️ Interrupción forzada detected.")
            break
        except Exception as e:
            print(f"❌ ERROR CRÍTICO DEL SISTEMA: {e}")

if __name__ == "__main__":
    run_cortex()


