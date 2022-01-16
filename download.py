import requests
import zipfile
import os
from utils import estados, get_filename

def download_file(estado, mes, suffix):
    url = 'http://ftp.dadosabertos.ans.gov.br/FTP/PDA/TISS/HOSPITALAR/2019/'+estado+'/'
    filename = get_filename(estado, mes, suffix)
    final_url = url + filename
    print(final_url)
    r = requests.get(final_url, allow_redirects=True)
    open(filename, 'wb').write(r.content)

def unzip_and_delete(estado, mes, suffix):
    filename = get_filename(estado, mes, suffix)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall('./files')
    os.remove(filename)


def download_files(estado):
    for i in range(1, 13):
        download_file(estado, i, 'DET')
        unzip_and_delete(estado, i, 'DET')
        download_file(estado, i, 'CONS')
        unzip_and_delete(estado, i, 'CONS')
