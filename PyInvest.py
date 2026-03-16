import math
import random
import statistics
import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

capital = float(input('Capital inicial: '))
aporte = float(input('Aporte mensal: '))
meses = int(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual %: ')) / 100
perc_cdb = float(input('Percentual do CDI - CDB (%)')) / 100
perc_lci = float(input('Percentual do CDI - LCI (%)')) / 100
perc_fii = float(input('Rentabilidade do FII (%)')) / 100
meta = float(input('Meta financeira (R$): '))

# conversão CDI
cdi_mensal = math.pow((1 + cdi_anual), 1/12) - 1

# total investido
total_investido = capital + (aporte * meses)

# CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1 + taxa_cdb), meses)) + (aporte * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

# LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses)) + (aporte * meses)

# Poupança
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1 + taxa_poupanca), meses)) + (aporte * meses)

# FII
base_fii = (capital * math.pow((1 + perc_fii), meses)) + (aporte * meses)

fii1 = base_fii + random.uniform(-0.03, 0.03) * base_fii
fii2 = base_fii + random.uniform(-0.03, 0.03) * base_fii
fii3 = base_fii + random.uniform(-0.03, 0.03) * base_fii
fii4 = base_fii + random.uniform(-0.03, 0.03) * base_fii
fii5 = base_fii + random.uniform(-0.03, 0.03) * base_fii

lista_fii = [fii1, fii2, fii3, fii4, fii5]

media_fii = statistics.mean(lista_fii)
mediana_fii = statistics.median(lista_fii)
desvio_fii = statistics.stdev(lista_fii)

valor_fii = media_fii

# datas
data_simulacao = datetime.datetime.now()
dias = meses * 30
data_resgate = data_simulacao + datetime.timedelta(days=dias)

# meta financeira
meta_atingida = valor_fii >= meta

# formatação monetária
capital_formatado = locale.currency(capital, grouping=True)
aporte_formatado = locale.currency(aporte, grouping=True)
meta_formatado = locale.currency(meta, grouping=True)
total_formatado = locale.currency(total_investido, grouping=True)
cdb_formatado = locale.currency(montante_cdb_liquido, grouping=True)
lci_formatado = locale.currency(montante_lci, grouping=True)
poupanca_formatado = locale.currency(montante_poupanca, grouping=True)
fii_formatado = locale.currency(valor_fii, grouping=True)

mediana_formatada = locale.currency(mediana_fii, grouping=True)
desvio_formatado = locale.currency(desvio_fii, grouping=True)

# gráfico ASCII
blocos_cdb = int(montante_cdb_liquido / 1000)
blocos_lci = int(montante_lci / 1000)
blocos_poupanca = int(montante_poupanca / 1000)
blocos_fii = int(valor_fii / 1000)

grafico_cdb = "█" * blocos_cdb
grafico_lci = "█" * blocos_lci
grafico_poupanca = "█" * blocos_poupanca
grafico_fii = "█" * blocos_fii

# RELATÓRIO FINAL
print("\n====================================")
print("PyInvest - Simulador de Investimentos")
print("====================================")

print("\nData da simulação:", data_simulacao.strftime("%d/%m/%Y"))
print("Data estimada de resgate:", data_resgate.strftime("%d/%m/%Y"))

print(f"\nTotal investido: {total_formatado}")

print("\n--- RESULTADOS FINANCEIROS ---")
print(f"CDB: {cdb_formatado}")
print(grafico_cdb)

print(f"\nLCI/LCA: {lci_formatado}")
print(grafico_lci)

print(f"\nPoupança: {poupanca_formatado}")
print(grafico_poupanca)

print(f"\nFII (média): {fii_formatado}")
print(grafico_fii)

print("\n--- ESTATÍSTICAS FII ---")
print(f"Mediana: {mediana_formatada}")
print(f"Desvio padrão: {desvio_formatado}")

print(f"\nMeta atingida? {meta_atingida}")
print("====================================")