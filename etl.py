import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="C0mp4ny",
  database="neurotech",
  port=3308
)

cursor = connection.cursor()

def process_cons(filename):
  data = pd.read_csv('./files/'+filename, delimiter=';')
  df = pd.DataFrame(data)

  pd.to_numeric(df["ID_EVENTO_ATENCAO_SAUDE"])
  pd.to_numeric(df["ID_PLANO"])
  pd.to_numeric(df["CD_MUNICIPIO_BENEFICIARIO"])
  pd.to_numeric(df["TEMPO_DE_PERMANENCIA"])
  pd.to_numeric(df["CD_CARATER_ATENDIMENTO"])
  pd.to_numeric(df["CD_TIPO_INTERNACAO"])
  pd.to_numeric(df["CD_REGIME_INTERNACAO"])
  pd.to_numeric(df["CD_MOTIVO_SAIDA"])
  df = df.where(pd.notnull(df), None)

  for index, row in df.iterrows():
    query = 'INSERT INTO cons(id_evento, id_plano, faixa_etaria, sexo, cod_municipio, porte, nome_modalidade, UF, tempo_permanencia, ano_evento, mes_evento, cod_carater_atendimento, cod_tipo, regime_internacao, motivo_saida, cid, diarias_uti)'
    query +='VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    
    try:
      id_evento = row['ID_EVENTO_ATENCAO_SAUDE']
      id_plano = row['ID_PLANO']
      faixa_etaria = row['FAIXA_ETARIA']
      sexo = row['SEXO'][0]
      cod_municipio = int(row['CD_MUNICIPIO_BENEFICIARIO'])
      porte = row['PORTE']
      nome_modalidade = row['NM_MODALIDADE']
      UF = row['UF_PRESTADOR']
      tempo_permanencia = row['TEMPO_DE_PERMANENCIA']
      ano_evento = int(row['ANO_MES_EVENTO'].split('-')[0])
      mes_evento = int(row['ANO_MES_EVENTO'].split('-')[1])
      cod_carater_atendimento = row['CD_CARATER_ATENDIMENTO']
      cod_tipo = row['CD_TIPO_INTERNACAO']
      regime_internacao = row['CD_REGIME_INTERNACAO']
      motivo_saida = row['CD_MOTIVO_SAIDA']
      cid = row['CID_1']
      diarias_uti = row['QT_DIARIA_UTI']
      cursor.execute(query, (id_evento, id_plano, faixa_etaria, sexo, cod_municipio, porte, nome_modalidade, UF, tempo_permanencia, ano_evento, mes_evento, cod_carater_atendimento, cod_tipo, regime_internacao, motivo_saida, cid, diarias_uti))
    except Exception as e:
      print("Erro na linha " +str(index)+ " do arquivo " + filename)
      print(e)
      print()
  
  connection.commit()

def process_det(filename):
  data = pd.read_csv('./files/'+filename, delimiter=';')
  df = pd.DataFrame(data)
  
  for index, row in df.iterrows():
    query = 'INSERT INTO det(id_evento, cod_procedimento, qtd_item_informado, valor_item_informado, valor_item_pago_fornecedor)'
    query +='VALUES(%s, %s, %s, %s, %s)'
    
    try:
      id_evento = int(row['ID_EVENTO_ATENCAO_SAUDE'])
      cod_procedimento = int(row['CD_PROCEDIMENTO'])
      qtd_item_informado = int(row['QT_ITEM_EVENTO_INFORMADO'])
      valor_item_informado = float(str(row['VL_ITEM_EVENTO_INFORMADO']).replace(',', '.'))
      valor_item_pago_fornecedor = float(str(row['VL_ITEM_PAGO_FORNECEDOR']).replace(',', '.'))
      cursor.execute(query, (id_evento, cod_procedimento, qtd_item_informado, valor_item_informado, valor_item_pago_fornecedor))
    except Exception as e:
      print("Erro na linha " +str(index)+ " do arquivo " + filename)
      print(e)
      print()
  
  connection.commit()









