estados = ['AC', 'AL','AM', 'AP', 'BA', 'CE', 'DF', 'ES','GO', 'MA', 
           'MG', 'MS', 'MT', 'PA', 'PB', 'PE','PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

def get_filename(estado, mes, suffix):
    if mes < 10: 
        mes = "0" + str(mes) 
    else: 
        mes = str(mes)
    return estado + '_2019'+ str(mes) +'_HOSP_'+ suffix +'.zip'