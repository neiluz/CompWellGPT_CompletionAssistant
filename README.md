# 🛢️ CompWellGPT - Asistente en Completación de Pozos Petroleros
![CompWellGPT Banner](https://github.com/neiluz/CompWellGPT_CompletionAssistant/blob/main/banner_2.png)


**CompWellGPT** es un asistente inteligente diseñado para apoyar a ingenieros y especialistas en el análisis técnico-operativo de pozos petroleros. Utiliza inteligencia artificial para interpretar documentos, detectar patrones operativos, generar recomendaciones y responder preguntas sobre datos reales de completación y producción.

---

## 📌 Funcionalidades principales

- ✅ Consulta de problemas operacionales históricos
- 📈 Análisis de producción: corte de agua, % de arena, eficiencia
- 🛠 Diagnóstico de pozos con obstrucciones, daños, fallas de tubing, etc.
- 🤖 Respuestas contextualizadas gracias a la integración con OpenAI Assistants API
- 💡 Soporte para toma de decisiones en intervenciones, mantenimientos y estrategias de completación

---

## 🗂 Estructura del proyecto

```
CompWellGPT/
│
├── app/
│   └── main.py                  # App principal en Streamlit
│
├── data/
│
├── utils/
│   └── openai_assistant.py      # Funciones para conectar con la API de OpenAI
│
├── README.md                    # Este archivo
└── requirements.txt             # Dependencias del proyecto
```

---

## ⚙️ Requisitos

- Python 3.10+
- Cuenta de OpenAI con acceso a GPT-4 Assistants API
- API Key de OpenAI
- Archivos de datos `.csv` estructurados

---

## 🚀 Cómo ejecutar el proyecto

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/CompWellGPT.git
cd CompWellGPT
```

2. Crea entorno virtual e instala dependencias:

```bash
python -m venv venv
source venv/bin/activate      # o venv\Scripts\activate en Windows
pip install -r requirements.txt
```

3. Ejecuta la app:

```bash
streamlit run app/main.py
```

---

## 🧠 ¿Qué hace el asistente?

- Usa una base con documentos técnicos relevantes para ofrecer respuestas basadas en contexto real
- Lee archivos de producción y clasificación de pozos
- Procesa datos operacionales e identifica problemas
- Responde en lenguaje natural sobre pozos, fallas, inactividad o estrategias técnicas
- Detecta anomalías como:
  - Arenamiento
  - Pérdidas de presión
  - Fracturas mal ejecutadas
  - Daños en tubing o válvulas
  - Pozos inyectores ineficientes

---

## 👩‍🔬 Autora

Este trabajo fue desarrollado como parte de la evaluación del Máster en Inteligencia Artificial Aplicada a los Negocios. Se combina experiencia práctica en completación de pozos con un enfoque actual en ciencia de datos, creando soluciones que integran IA con operaciones reales de campo.

---

## 🛣️ Futuras mejoras

- ⏳ Integración con bases de datos reales de producción
- 📊 Dashboard de monitoreo por pozo
- 🔍 Búsqueda semántica en documentos de completación
- 💬 Chat multi-pozo con contexto dinámico

---

## 📬 Contacto

¿Ideas, sugerencias o colaboración?  
Escríbeme o contribuye directamente al repositorio.

---

**¡Bienvenido a CompWellGPT! Donde los datos de campo cobran vida.**
