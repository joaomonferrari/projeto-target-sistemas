import json
import xml.etree.ElementTree as ET

def processar_dados(dados):
    # Ignorar valores zerados
    valores_validos = [dia["valor"] for dia in dados if dia["valor"] > 0]

    menor = min(valores_validos)
    maior = max(valores_validos)
    media = sum(valores_validos) / len(valores_validos)
    acima_media = sum(1 for valor in valores_validos if valor > media)

    return menor, maior, acima_media

def ler_json(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def ler_xml(caminho):
    tree = ET.parse(caminho)
    root = tree.getroot()

    dados = []
    for row in root.findall("row"):
        valor = float(row.find("valor").text)
        dia = int(row.find("dia").text)
        dados.append({"dia": dia, "valor": valor})
    
    return dados

def imprimir_resultados(nome_arquivo, menor, maior, acima_media):
    print(f"\nResultados para: {nome_arquivo}")
    print(f"Menor valor de faturamento (sem considerar zeros): R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {acima_media} dia(s)")

# Arquivos
arquivo_json = 'faturamento_json.json'
arquivo_xml = 'faturamento_xml.xml'

# Processar JSON
dados_json = ler_json(arquivo_json)
menor_json, maior_json, acima_media_json = processar_dados(dados_json)
imprimir_resultados(arquivo_json, menor_json, maior_json, acima_media_json)

# Processar XML
dados_xml = ler_xml(arquivo_xml)
menor_xml, maior_xml, acima_media_xml = processar_dados(dados_xml)
imprimir_resultados(arquivo_xml, menor_xml, maior_xml, acima_media_xml)
