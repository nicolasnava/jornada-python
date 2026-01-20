import streamlit as st
import google.generativeai as genai

try:
    chave = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=chave)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro ao configurar chave/modelo: {e}")

st.write("### ChatBot com IA (Google Gemini)")

# Memória do Streamlit (Histórico)
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Exibe o histórico de mensagens na tela
for mensagem in st.session_state["lista_mensagens"]:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

# Campo de entrada do usuário
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # 1. Mostra e salva a mensagem do usuário
    st.chat_message("user").write(mensagem_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})

    try:
        # 2. Resposta real da IA
        with st.spinner("Pensando..."):
            # O Gemini 1.5 aceita o histórico completo como entrada
            resposta = model.generate_content(mensagem_usuario)
            texto_resposta = resposta.text

        # 3. Exibe e salva a resposta da IA
        st.chat_message("assistant").write(texto_resposta)
        st.session_state["lista_mensagens"].append({"role": "assistant", "content": texto_resposta})
    
    except Exception as e:
        st.error(f"Erro na API do Google: {e}")