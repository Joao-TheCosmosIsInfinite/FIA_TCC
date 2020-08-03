# Importações
import requests
import os
import pathlib

class URLConnection:
    """
        Classe de conexão 

        Essa classe tem todas as informações e bibliotecas necessárias para baixar dados oriundos de sites. Esses dados são
        nada mais nada menos do que arquivos .xlsx, .csv, .json, .parquet, etc..
    """

    def __init__(self, p_url, p_file_name):
        """
        Constructor
        Args:
            p_url: O endereço URL
            p_name: LNome do arquivo
        """
        self.p_url = p_url
        self.p_path = str(os.path.abspath(p_file_name)).replace('src', 'data') 

    def md_download_file(self):

        response = requests.get(self.p_url, stream = True)

        if response.status_code == requests.codes.OK:
            with open(self.p_path, 'wb') as new_file:
                for piece in response.iter_content(chunk_size = 256):
                    new_file.write(piece)
            
            print("Download Finalizado.\nArquivo salvo em: {}".format(self.p_path))

        else:
            response.raise_for_status()


if __name__ == "__main__":

    url = 'https://dados.educacao.sp.gov.br/sites/default/files/IDESP_ESCOLA_2019.csv'
    name_file = 'IDESP_ESCOLA_2019.csv'

    cnn = URLConnection(url, name_file)
    cnn.md_download_file()