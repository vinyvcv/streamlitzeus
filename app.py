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

    # Definir valores antes de usar
    valor_total = 70000
    desconto = valor_total * 0.105
    valor_final = valor_total - desconto

    st.markdown(f"### **💰 Valor Total do Projeto: R$ 70.000**")
    st.markdown(f"### **📉 Desconto (10,50% de nota): R$ {desconto:,.2f}**")
    st.markdown(f"### **✅ Valor Final após desconto: R$ {valor_final:,.2f}**")
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
        # Definir valores antes de usá-los
        valor_total = 70000
        desconto = valor_total * 0.105
        valor_final = valor_total - desconto
        tempo_estimado = "40 dias"

        equipe = [
            ("Desenvolvedor Frontend", 5000),
            ("Desenvolvedor Backend", 5000),
            ("Especialista em Banco de Dados", 5000),
            ("Especialista em UX/UI", 5000),
            ("Engenheiro de Qualidade (QA)", 5000),
        ]
        total_equipe = sum(c[1] for c in equipe)

        infraestrutura = [
            ("Servidores Cloud", "R$ 500 - R$ 1.500/mês"),
            ("Banco de Dados", "R$ 300 - R$ 1.000/mês"),
            ("Domínio + Certificado SSL", "R$ 150 - R$ 300 (anual)"),
            ("Ferramentas de IA", "R$ 1.000 - R$ 3.000/mês"),
        ]

        pdf = FPDF()
        pdf.add_page()
        
        # Usar fonte padrão do FPDF para evitar erro
        pdf.set_font("Arial", "B", 16)

        # Título Principal
        pdf.cell(200, 10, "Orçamento Empresarial", ln=True, align="C")
        pdf.ln(10)

        # 📌 Informações Gerais
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, "📌 Informações Gerais", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.cell(200, 10, f"Valor Total do Projeto: R$ {valor_total:,.2f}", ln=True)
        pdf.cell(200, 10, f"Desconto (10,50% de nota): R$ {desconto:,.2f}", ln=True)
        pdf.cell(200, 10, f"Valor Final após desconto: R$ {valor_final:,.2f}", ln=True)
        pdf.cell(200, 10, f"Tempo estimado de trabalho: {tempo_estimado}", ln=True)
        pdf.ln(10)

        # 💼 Custos com Equipe
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, "💼 Custos com Equipe", ln=True)
        pdf.set_font("Arial", "", 12)

        for prof, custo in equipe:
            pdf.cell(200, 10, f"{prof}: R$ {custo:,.2f}", ln=True)
        pdf.cell(200, 10, f"Total com equipe: R$ {total_equipe:,.2f}", ln=True)
        pdf.ln(10)

        # 🖥 Infraestrutura
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, "🖥 Custos com Infraestrutura", ln=True)
        pdf.set_font("Arial", "", 12)

        for servico, custo in infraestrutura:
            pdf.cell(200, 10, f"{servico}: {custo}", ln=True)
        pdf.ln(10)

        # 📄 Salvar e disponibilizar PDF
        pdf_file_path = "orcamento.pdf"
        pdf.output(pdf_file_path, "F")

        st.success("✅ PDF gerado com sucesso! Baixe abaixo:")
        with open(pdf_file_path, "rb") as file:
            st.download_button("📥 Baixar PDF", file, file_name="orcamento.pdf", mime="application/pdf")


