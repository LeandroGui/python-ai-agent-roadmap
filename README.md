# 🧠 Python for AI & Agents: From Zero to Agentic Systems

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![AI Agents](https://img.shields.io/badge/AI-Agents-orange?style=for-the-badge)
![Data Science](https://img.shields.io/badge/Data-Science-green?style=for-the-badge)

## 📌 Sobre este Repositorio

Este repositorio documenta una ruta de aprendizaje técnica y aplicada para dominar Python, con un enfoque específico en **Ingeniería de Datos, Inteligencia Artificial y Sistemas Agénticos**.

A diferencia de los cursos genéricos de programación, este roadmap está estructurado para transformar conceptos de sintaxis en **herramientas para construir IAs**. Pasamos de variables simples a tensores, y de funciones básicas a agentes autónomos capaces de razonar y usar herramientas.

## 🗺️ Mapa de Ruta (Roadmap)

El repositorio está organizado en niveles progresivos. Cada nivel contiene scripts de **Teoría** (conceptos aislados) y un **Proyecto Integrador** (aplicación real).

### 🔹 Nivel 1: Los Fundamentos del Dato
**Enfoque:** Lógica algorítmica y manipulación de estructuras de datos en memoria.
* **Conceptos:** Tipos de datos, Control de flujo, Colecciones, Funciones.
* **🎯 Proyecto Integrador:** `Text Analyzer CLI` (Procesamiento de texto crudo y estadística básica).

### 🔹 Nivel 2: Ingeniería de Software & Estructura
**Enfoque:** Programación Orientada a Objetos (POO), persistencia y buenas prácticas.
* **Conceptos:** Clases, Herencia, Manejo de Archivos (JSON/CSV), Virtual Environments, Logs.
* **🎯 Proyecto Integrador:** `Academic Data Manager` (Sistema CRUD con persistencia de datos).

### 🔹 Nivel 3: Optimización y Validación (Pre-Agentic)
**Enfoque:** Preparando el terreno para la IA (Validación estricta y Concurrencia).
* **Conceptos:** Pydantic (Validación), Asyncio (Concurrencia), Decoradores, Testing.
* **🎯 Proyecto Integrador:** `Async Data Pipeline` (Simulador de ingesta de datos validada asíncrona).

### 🔹 Nivel 4: Data Science e Inteligencia Artificial
**Enfoque:** El ecosistema `.agnt` (NumPy, Pandas, LLMs).
* **4a. Ciencia de Datos:** Análisis exploratorio y visualización.
* **4b. Agentes (From Scratch):** Construcción de un bucle de razonamiento (ReAct) sin frameworks.
* **4c. Frameworks:** Implementación profesional con LangGraph / CrewAI.
* **🎯 Proyecto Integrador Final:** `University Tutor Agent` (Agente capaz de resolver dudas académicas usando herramientas).

---

## 🛠️ Estructura de Directorios

```text
python-ai-agent-roadmap/
│
├── 01_nivel_basico/        # Fundamentos
│   ├── teoria/
│   └── proyecto_integrador/
│
├── 02_nivel_intermedio/    # POO y Persistencia
│   ├── teoria/
│   └── proyecto_integrador/
│
├── 03_nivel_avanzado/      # Async & Pydantic
│   ├── teoria/
│   └── proyecto_integrador/
│
├── 04_nivel_agentes_ia/    # DS & AI Frameworks
    ├── 04a_ciencia_datos/
    ├── 04b_agente_scratch/
    └── 04c_frameworks/
