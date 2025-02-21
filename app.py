import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from fpdf import FPDF

# Configuração da página
st.set_page_config(page_title="Orçamento - Sistema de Vistoria", layout="wide")

# Criar Menu Lateral
with st.sidebar:
    menu_selecionado = option_menu(
        "📌 Navegação",
        ["📊 Orçamento", "💼 Custos com Equipe", "🖥 Infraestrutura", "📄 Gerar PDF"],
        icons=["bar-chart", "people", "cloud", "file-earmark-pdf"],
        menu_icon="cast",
        default_index=0,
    )

# 📊 Página de Orçamento Geral
if menu_selecionado == "📊 Orçamento":
    st.title("📊 Orçamento - Projeto Zeus ")
    
    st.markdown("### **💰 Valor Total do Projeto: R$ 70.000**")
    st.markdown("✅ **Custo com equipe:** R$ 25.000")
    st.markdown("✅ **Infraestrutura variável:** R$ 2.000 - R$ 6.000/mês")
    st.markdown("✅ **Receita recorrente (suporte e manutenção):** R$ 3.000 - R$ 5.000/mês")

    st.success("Este orçamento garante um sistema robusto, escalável e sustentável para o cliente.")

# 💼 Custos com Equipe
elif menu_selecionado == "💼 Custos com Equipe":
    st.title("💼 Custos com Equipe de Desenvolvimento")
    
    equipe = {
        "Profissional": [
            "Desenvolvedor Frontend",
            "Desenvolvedor Backend",
            "Especialista em Banco de Dados",
            "Especialista em UX/UI",
            "Engenheiro de Qualidade (QA)",
        ],
        "Custo (R$)": [5.000, 5.000, 5.000, 5.000, 5.000],
    }
    
    df_equipe = pd.DataFrame(equipe)
    st.table(df_equipe)

    st.markdown("🔹 **Total com equipe:** **R$ 25.000**")

# 🖥 Infraestrutura e Custos Operacionais
elif menu_selecionado == "🖥 Infraestrutura":
    st.title("🖥 Custos com Infraestrutura")

    infraestrutura = {
        "Serviço": [
            "Servidores Cloud (AWS/DigitalOcean)",
            "Banco de Dados (RDS, Firebase, MongoDB Atlas)",
            "Domínio + Certificado SSL",
            "Ferramentas de IA (Reconhecimento Facial)",
        ],
        "Custo Mensal (R$)": ["500 - 1.500", "300 - 1.000", "150 - 300 (anual)", "1.000 - 3.000"],
    }

    df_infra = pd.DataFrame(infraestrutura)
    st.table(df_infra)

    st.markdown("💡 **Total estimado de infraestrutura:** **R$ 2.000 - R$ 6.000/mês**")

# 📄 Gerar PDF do Orçamento
elif menu_selecionado == "📄 Gerar PDF":
    st.title("📄 Gerar PDF do Orçamento")

    if st.button("📥 Gerar PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, "Orçamento Empresarial", ln=True, align="C")
        pdf.cell(200, 10, "", ln=True)  # Espaço
        
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, "Valor Total do Projeto: R$ 70.000", ln=True)
        pdf.cell(200, 10, "Custo com Equipe: R$ 25.000", ln=True)
        pdf.cell(200, 10, "Infraestrutura Mensal: R$ 2.000 - R$ 6.000/mês", ln=True)
        pdf.cell(200, 10, "Receita Recorrente: R$ 3.000 - R$ 5.000/mês", ln=True)
        
        pdf_file_path = "orcamento.pdf"
        pdf.output(pdf_file_path)

        st.success("PDF gerado com sucesso! Baixe abaixo:")
        with open(pdf_file_path, "rb") as file:
            st.download_button("📥 Baixar PDF", file, file_name="orcamento.pdf", mime="application/pdf")
