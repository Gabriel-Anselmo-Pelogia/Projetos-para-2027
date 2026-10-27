import streamlit as st

def init_session_state():
    """Inicializa as variáveis de controle de sessão do usuário."""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "role" not in st.session_state:
        st.session_state.role = "Visitante"  # Nível padrão

def verificar_creditos(usuario, senha):
    """Simula a validação de usuários (futuramente integrado ao Banco SQL)."""
    usuarios_db = {
        "admin": {"senha": "123", "nome": "Engenheiro Chefe", "role": "Administrador"},
        "operador": {"senha": "123", "nome": "Almoxarife João", "role": "Operador"},
    }
    
    if usuario in usuarios_db and usuarios_db[usuario]["senha"] == senha:
        return usuarios_db[usuario]
    return None

def render_login_component():
    """Renderiza o componente de login com layout em cartão centralizado."""
    # Espaçamento vertical para empurrar o card para o meio da tela
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Criando colunas para centralizar o layout horizontalmente
    _, col_centro, _ = st.columns([1, 1.2, 1])
    
    with col_centro:
        # Card nativo com borda
        with st.container(border=True):
            st.markdown("### 🛠️ ToolManager Pro")
            st.caption("Controle Avançado de Ferramental e Ciclo de Vida")
            st.markdown("---")
            
            with st.form("form_login"):
                usuario_input = st.text_input("Usuário", placeholder="Digite seu usuário...")
                senha_input = st.text_input("Senha", type="password", placeholder="••••••••")
                
                st.markdown("") # Espaçamento estético
                submitted = st.form_submit_button("Entrar no Sistema", use_container_width=True)
                
                if submitted:
                    user_data = verificar_creditos(usuario_input, senha_input)
                    if user_data:
                        st.session_state.logged_in = True
                        st.session_state.username = user_data["nome"]
                        st.session_state.role = user_data["role"]
                        st.success(f"Bem-vindo, {user_data['nome']}!")
                        st.rerun()
                    else:
                        st.error("Usuário ou senha incorretos.")

            st.markdown("---")
            
            # Opção de acesso público limpa
            if st.button("🌐 Acessar Portal Público (Visitante)", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.username = "Visitante Anônimo"
                st.session_state.role = "Visitante"
                st.rerun()
