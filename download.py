import requests
estados = ['AC', 'AL','AM', 'AP', 'BA', 'CE', 'DF', 'ES','GO', 'MA', 
           'MG', 'MS', 'MT', 'PA', 'PB', 'PE','PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']


def download_file(estado, mes, suffix):
    url = 'http://ftp.dadosabertos.ans.gov.br/FTP/PDA/TISS/HOSPITALAR/2019/'+estado+'/'
    if mes < 10: 
        mes = "0" + str(mes) 
    else: 
        mes = str(mes)
    filename = estado + '_2019'+ str(mes) +'_HOSP_'+ suffix +'.zip'
    final_url = url + filename
    print(final_url)
    # r = requests.get(final_url, allow_redirects=True)
    # open(filename, 'wb').write(r.content)


def download_files(estado):
    for i in range(1, 13):
        download_file(estado, i, 'DET')
        download_file(estado, i, 'CONS')
        # filename_det = estado +'_2019'+ str(mes) +'_HOSP_DET.zip'
        # final_url_det = url + filename_det
        # print(final_url_det)
        # r = requests.get(final_url_det, allow_redirects=True)
        # open(filename_det, 'wb').write(r.content)




download_files('AC')

