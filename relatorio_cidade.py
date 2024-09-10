from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from apliCidade import Cidades  # Certifique-se de que o nome está correto e corresponde à sua classe

def gerar_relatorio(caminho_arquivo):
    # Cria um objeto Canvas
    c = canvas.Canvas(caminho_arquivo, pagesize=letter)
    width, height = letter

    # Adiciona um título ao relatório
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, height - 1 * inch, "Relatório de Cidades")

    # Adiciona uma linha de separação
    c.setLineWidth(1)
    c.line(0.5 * inch, height - 1.2 * inch, width - 0.5 * inch, height - 1.2 * inch)

    # Adiciona cabeçalhos das colunas
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.5 * inch, height - 1.5 * inch, "ID")
    c.drawString(1.5 * inch, height - 1.5 * inch, "Cidade")
    c.drawString(3.5 * inch, height - 1.5 * inch, "UF")

    # Adiciona uma linha de separação entre cabeçalhos e dados
    c.setLineWidth(0.5)
    c.line(0.5 * inch, height - 1.7 * inch, width - 0.5 * inch, height - 1.7 * inch)

    # Adiciona os dados das cidades
    y = height - 2 * inch
    c.setFont("Helvetica", 10)

    cid = Cidades()
    cidades = cid.selectAllCidades()  # Certifique-se de que este método está correto
    for cidade in cidades:
        # Ajuste o número de colunas conforme o número de dados disponíveis
        c.drawString(0.5 * inch, y, str(cidade[0]))  # ID
        c.drawString(1.5 * inch, y, cidade[1])       # Nome da cidade
        c.drawString(3.5 * inch, y, cidade[2])       # UF
        y -= 0.3 * inch  # Espaçamento entre as linhas

        # Adiciona nova página se necessário
        if y < 1 * inch:
            c.showPage()  # Finaliza a página atual
            c.setFont("Helvetica-Bold", 16)
            c.drawString(1 * inch, height - 1 * inch, "Relatório de Cidades")
            c.setFont("Helvetica-Bold", 12)
            c.drawString(0.5 * inch, height - 1.5 * inch, "ID")
            c.drawString(1.5 * inch, height - 1.5 * inch, "Cidade")
            c.drawString(3.5 * inch, height - 1.5 * inch, "UF")
            c.setLineWidth(0.5)
            c.line(0.5 * inch, height - 1.7 * inch, width - 0.5 * inch, height - 1.7 * inch)
            y = height - 2 * inch  # Reseta a posição vertical

    # Finaliza o documento
    c.save()

if __name__ == "__main__":
    gerar_relatorio("relatorio_cidade.pdf")
