import streamlit as st
from auth import init_session_state, render_login_component

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Gestão Profissional de Ferramental",
    page_icon="🛠️",
    layout="wide"
)

# Inicializa o controle de sessão
init_session_state()

# -----------------------------------------------------------------------------
# ROTEAMENTO DE TELA (LOGADO VS NÃO LOGADO)
# -----------------------------------------------------------------------------
if not st.session_state.logged_in and st.session_state.role == "Visitante":
    # Se não estiver logado, exibe a tela de login estilizada
    render_login_component()
else:
    # Barra lateral para usuários autenticados
    st.sidebar.title(f"👤 {st.session_state.username}")
    st.sidebar.caption(f"Nível de Acesso: **{st.session_state.role}**")
    st.sidebar.markdown("---")

    if st.sidebar.button("🚪 Sair (Logout)", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = "Visitante"
        st.rerun()

    # Conteúdo da Página Principal com base no cargo
    st.title("🛠️ ToolManager Pro - Painel Principal")
    
    if st.session_state.role == "Administrador":
        st.success("🔓 Acesso Administrativo Total Liberado (Custos, Indicadores, ROP e Gestão).")
    elif st.session_state.role == "Operador":
        st.info("🔒 Acesso Operacional (Controle de Estoque e Lançamento de Movimentações).")
    else:
        st.warning("🌐 Modo Visitante (Apenas Catálogo Público de Confiabilidade).")
