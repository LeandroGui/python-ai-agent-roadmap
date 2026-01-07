# 🧠 Python AI Agent Roadmap: From Script to Framework

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Google Colab](https://img.shields.io/badge/Colab-Notebooks-orange?style=for-the-badge&logo=googlecolab)
![AI Agents](https://img.shields.io/badge/AI-Agents-purple?style=for-the-badge)

## 📌 Visión General

Este repositorio no es solo una colección de tutoriales de Python. Es un **Roadmap de Ingeniería** diseñado con un objetivo claro: **Construir un Framework de Agentes de IA desde cero.**

A través de 5 niveles progresivos, evolucionaremos desde la sintaxis básica hasta la creación de un sistema capaz de razonar, planificar y ejecutar tareas complejas (Agentes). Todo el código está documentado y preparado para ejecutarse en **Google Colab**.

## 🧵 El Hilo Conductor: "Project Cortex"

Para evitar el aprendizaje fragmentado, todos los niveles contribuyen a un único mega-proyecto llamado **Cortex**.
* En el Nivel 1, Cortex será una simple línea de comandos.
* En el Nivel 2, tendrá estructura interna (Clases).
* En el Nivel 3, aprenderá a planificar (Grafos y Algoritmos).
* En el Nivel 4, se volverá asíncrono y robusto.
* En el Nivel 5, le daremos cerebro (LLMs) y ojos (Data Science).

---

## 🗺️ Mapa de Ruta (Roadmap)

### 🔹 Nivel 1: Básico (El Núcleo Lógico)
*Fundamentos de la manipulación de memoria y flujo.*
* **Temas:** Sintaxis, Variables, Control de Flujo, Funciones, Colecciones, Manejo de Errores.
* **🛠️ Proyecto Integrador:** `Cortex CLI` - Una consola interactiva para procesamiento de comandos básicos.

### 🔹 Nivel 2: OOP (Arquitectura Modular)
*Encapsulamiento y diseño de software escalable.*
* **Temas:** Clases, Objetos, Herencia, Polimorfismo, Métodos Mágicos.
* **🛠️ Proyecto Integrador:** `Cortex Entity System` - Refactorización del núcleo usando un sistema de Entidades y Tareas.

### 🔹 Nivel 3: DSA (Algoritmia para Agentes)
*Estructuras de datos para la toma de decisiones eficiente.*
* **Temas:** Pilas, Colas, Matrices, Árboles, Grafos (DAGs), Algoritmos de Búsqueda y Recursión.
* **🛠️ Proyecto Integrador:** `Cortex Orchestrator` - Implementación de un planificador de tareas basado en grafos y prioridades.

### 🔹 Nivel 4: Avanzado (Eficiencia y Metaprogramación)
*Optimización y herramientas de alto nivel.*
* **Temas:** List Comprehensions, Generadores, Decoradores, Regex, Lambdas, Asincronía.
* **🛠️ Proyecto Integrador:** `Cortex Async Pipeline` - Un sistema de procesamiento paralelo con validación de datos.

### 🔹 Nivel 5: Especializado (La Mente Agéntica)
*La convergencia de Datos e Inteligencia Artificial.*
* **Temas:** Análisis de Datos (Pandas/Numpy), Ciencia de Datos, IA Generativa (LLMs), RAG, Sistemas Agénticos.
* **🛠️ Proyecto Final:** `Cortex Agentic Framework` - Un marco de trabajo completo para crear agentes que analizan datos y toman decisiones autónomas.

---

## 📂 Estructura del Repositorio

El contenido está organizado por niveles de competencia. Cada carpeta de nivel contiene dos subdirectorios principales: `notebooks` (Teoría práctica en Colab) y `proyecto_integrador` (La evolución del framework Cortex).

```text
python-ai-agent-roadmap/
│
├── README.md               # Documentación general y Mapa de Ruta
├── requirements.txt        # Dependencias globales del proyecto
├── .gitignore              # Archivos ignorados por Git
│
├── 01_basico/              # [Nivel 1] Fundamentos Lógicos
│   ├── notebooks/          # 📓 S01_sintaxis.ipynb, S02_control.ipynb...
│   └── proyecto_cortex_v1/ # 🛠️ Cortex CLI (Script interactivo)
│
├── 02_oop/                 # [Nivel 2] Arquitectura & Objetos
│   ├── notebooks/          # 📓 S01_clases.ipynb, S02_herencia.ipynb...
│   └── proyecto_cortex_v2/ # 🛠️ Cortex Entity System (Estructura modular)
│
├── 03_dsa/                 # [Nivel 3] Algoritmos & Estructuras
│   ├── notebooks/          # 📓 S01_pilas_colas.ipynb, S03_grafos.ipynb...
│   └── proyecto_cortex_v3/ # 🛠️ Cortex Orchestrator (Planificador)
│
├── 04_avanzado/            # [Nivel 4] Eficiencia & Python Moderno
│   ├── notebooks/          # 📓 S01_asyncio.ipynb, S02_pydantic.ipynb...
│   └── proyecto_cortex_v4/ # 🛠️ Cortex Async Pipeline (Motor concurrente)
│
└── 05_especializado/       # [Nivel 5] Data Science & AI Agents
    ├── notebooks/          # 📓 S01_pandas_etl.ipynb, S02_llm_chain.ipynb...
    └── proyecto_final/     # 🧠 Cortex Framework v1.0 (Sistema Agéntico Completo)
```
## 🚀 Cómo usar este repositorio

Este repositorio está diseñado para seguirse secuencialmente.

1.  **Navega a la carpeta del nivel:** Cada nivel tiene su propia carpeta (ej. `01_basico`).
2.  **Abre los Notebooks:** Encontrarás enlaces directos para abrir los archivos `.ipynb` en **Google Colab**.
3.  **Completa el Proyecto Integrador:** Al final de cada nivel, usa lo aprendido para construir la siguiente versión de *Cortex*.

---

*Desarrollado por [Leandro] - Licenciatura en Análisis y Gestión de Datos. Con el objetivo de democratizar la ingeniería de Agentes de IA.*
