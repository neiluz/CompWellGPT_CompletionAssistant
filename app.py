# ✅ app.py - Versión Final con File Search, Code Interpreter y Functions

import streamlit as st
import pandas as pd
import openai
import os
from utils import openai_assistant  # Este archivo debe contener funciones para interactuar con la API
import pathlib
import base64


# Configurar API
openai.api_key = st.secrets["OPENAI_API_KEY"]
ASSISTANT_ID = st.secrets["ASSISTANT_ID"]

with open("banner_2.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <style>
        .banner img {{
            height: 200px;
            object-fit: contain;
        }}
    </style>
    <div class="banner">
        <img src="data:image/png;base64,{encoded}"/>
    </div>
""", unsafe_allow_html=True)



st.set_page_config(page_title="CompWellGPT - Completación de Pozos", layout="wide")
st.markdown("""
## 🧠 CompWellGPT - Asistente Experto en Completación de Pozos

CompWellGPT es tu asistente técnico inteligente. Está diseñado para apoyarte en tareas clave relacionadas con la completación de pozos, de forma interactiva y automatizada.

Con este chatbot puedes:
- 📄 Consultar documentación técnica (PDF, DOCX, TXT).
- 📊 Subir archivos CSV con datos de presión, producción, corte de agua, etc., y obtener análisis automáticos.
- 🤖 Recibir respuestas inteligentes con análisis contextual y funciones personalizadas para la toma de decisiones técnicas.
            
---

💬 **Bienvenido/a. Puedes iniciar haciendo tu primera consulta técnica o subir un archivo para comenzar el análisis.**
""")

# Inicializar hilo
if "thread_id" not in st.session_state:
    st.session_state.thread_id = openai_assistant.create_thread()

# Subida de documentos para File Search
st.sidebar.subheader("🔍 Documentos técnicos (PDF, DOCX, TXT)")
doc_file = st.sidebar.file_uploader("Sube documentos de referencia", type=["pdf", "txt", "docx"])
if doc_file:
    # Recuperar extensión original del archivo subido
    extension = pathlib.Path(doc_file.name).suffix
    file_path = f"temp_doc{extension}"

    with open(file_path, "wb") as f:
        f.write(doc_file.read())
    
    uploaded_doc = openai.files.create(file=open(file_path, "rb"), purpose="assistants")
    
    openai.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content="He subido un documento técnico. Por favor, analízalo.",
        attachments=[
            {
                "file_id": uploaded_doc.id,
                "tools": [{"type": "file_search"}]
            }
        ]
    )

    st.sidebar.success("📄 Documento cargado y enviado al asistente.")

# Subida de CSV para Code Interpreter
st.sidebar.subheader("📈 Datos dinámicos (CSV)")
uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV para análisis", type=["csv"])

if uploaded_file:
    with open("temp.csv", "wb") as f:
        f.write(uploaded_file.read())

    df = pd.read_csv("temp.csv")
    st.session_state["uploaded_df"] = df

    # Subir archivo CSV a OpenAI
    uploaded_openai_file = openai.files.create(file=open("temp.csv", "rb"), purpose="assistants")
    st.session_state["csv_file_id"] = uploaded_openai_file.id

    # Enviar mensaje con el archivo como attachment para code_interpreter
    openai.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content="Acabo de subir un archivo CSV llamado temp.csv. Por favor, analízalo.",
        attachments=[
            {
                "file_id": uploaded_openai_file.id,
                "tools": [{"type": "code_interpreter"}]
            }
        ]
    )
    st.sidebar.success("✅ Archivo CSV enviado correctamente al asistente.")

# Mostrar preview del CSV
if "uploaded_df" in st.session_state:
    st.markdown("### 📈 Vista previa del CSV cargado")
    st.dataframe(st.session_state.uploaded_df.head(), use_container_width=True)

# Chat general
st.markdown("### 💬 Chat Técnico con el Asistente")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    st.markdown(f"**{msg['role']}:** {msg['content']}")

user_input = st.chat_input("Haz tu consulta técnica...")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    openai_assistant.send_message(st.session_state.thread_id, user_input)
    with st.spinner("CompWellGPT está pensando..."):
        run_id = openai_assistant.run_assistant(st.session_state.thread_id)
        response = openai_assistant.get_response(st.session_state.thread_id, run_id)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.markdown(f"**🤖 CompWellGPT:** {response}")
