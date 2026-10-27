import streamlit as st

def init_session_state():
    """Inicializa as variáveis de controle de sessão do utilizador."""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "role" not in st.session_state:
        st.session_state.role = "Visitante"

def verificar_creditos(usuario, senha):
    """Validação simulada de utilizadores."""
    usuarios_db = {
        "admin": {"senha": "123", "nome": "Engenheiro Chefe", "role": "Administrador"},
        "operador": {"senha": "123", "nome": "Almoxarife João", "role": "Operador"},
    }
    if usuario in usuarios_db and usuarios_db[usuario]["senha"] == senha:
        return usuarios_db[usuario]
    return None

def render_login_component():
    """Renderiza uma interface de login profissional estilo Split Screen."""
    
    # Injeção de CSS para remodelar completamente a interface do Streamlit
    st.markdown("""
        <style>
            /* Ocultar elementos padrão do Streamlit */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Ajuste de margens do container principal */
            .block-container {
                padding-top: 2rem !important;
                padding-bottom: 2rem !important;
                max-width: 1200px !important;
            }

            /* Estilização dos campos de texto (Inputs) */
            .stTextInput > div > div > input {
                border-radius: 8px !important;
                background-color: #1E293B !important;
                color: #F8FAFC !important;
                border: 1px solid #334155 !important;
                padding: 12px !important;
            }
            .stTextInput > div > div > input:focus {
                border-color: #2563EB !important;
                box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2) !important;
            }

            /* Estilização do Botão Primário */
            .stButton > button {
                border-radius: 8px !important;
                font-weight: 600 !important;
                transition: all 0.3s ease !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Divisão da Tela em Duas Colunas (Split Screen)
    col_banner, col_login = st.columns([1.2, 1], gap="large")

    # --- LADO ESQUERDO: BANNER PAINEL INDUSTRIAL ---
    with col_banner:
        with st.container(border=True):
            st.markdown("""
                <div style="padding: 20px 10px;">
                    <h1 style="color: #2563EB; margin-bottom: 0px; font-size: 2.2rem;">🛠️ ToolManager Pro</h1>
                    <p style="color: #94A3B8; font-size: 1.1rem; margin-top: 5px;">Sistema Integrado de Gestão de Ferramental e Armazém</p>
                    <hr style="border-color: #334155; margin: 20px 0;">
                    <ul style="color: #CBD5E1; font-size: 0.95rem; line-height: 1.8; list-style-type: none; padding-left: 0;">
                        <li>⚡ <b>Rastreabilidade em Tempo Real:</b> Controle de ciclo de vida e aferições.</li>
                        <li>📊 <b>Métricas de Consumo & ROP:</b> Alertas inteligentes de stock mínimo.</li>
                        <li>🛡️ <b>Segurança e Permissões:</b> Perfil por nível de acesso hierárquico.</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

    # --- LADO DIREITO: FORMULÁRIO DE AUTENTICAÇÃO ---
    with col_login:
        with st.container(border=True):
            st.markdown("""
                <div style="text-align: center; margin-bottom: 15px;">
                    <h3 style="color: #F8FAFC; margin-bottom: 5px;">Acesso ao Portal</h3>
                    <p style="color: #64748B; font-size: 0.85rem;">Insira as suas credenciais corporativas</p>
                </div>
            """, unsafe_allow_html=True)

            with st.form("form_login_custom"):
                usuario_input = st.text_input("Utilizador", placeholder="ex: admin")
                senha_input = st.text_input("Palavra-passe", type="password", placeholder="••••••••")
                
                st.markdown("<br>", unsafe_allow_html=True)
                submitted = st.form_submit_button("Entrar na Plataforma", use_container_width=True, type="primary")

                if submitted:
                    user_data = verificar_creditos(usuario_input, senha_input)
                    if user_data:
                        st.session_state.logged_in = True
                        st.session_state.username = user_data["nome"]
                        st.session_state.role = user_data["role"]
                        st.success(f"Sessão iniciada: {user_data['nome']}")
                        st.rerun()
                    else:
                        st.error("Credenciais inválidas. Verifique o utilizador e a palavra-passe.")

            st.markdown("<hr style='border-color: #334155; margin: 15px 0;'>", unsafe_allow_html=True)
            
            if st.button("🌐 Acessar Catálogo Público (Visitante)", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.username = "Visitante Anônimo"
                st.session_state.role = "Visitante"
                st.rerun()
