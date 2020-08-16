# Importações
import requests
import os
import pathlib

from tqdm import tqdm_notebook as tqdm

class URLConnection:
    """
        Classe de conexão 

        Essa classe tem todas as informações e bibliotecas necessárias para baixar dados oriundos de sites. Esses dados são
        nada mais nada menos do que arquivos .xlsx, .csv, .json, .parquet, etc..
    """

    def __init__(self, p_url, p_path, p_file_name):
        """
        Constructor
        Args:
            p_url: O endereço URL
            p_path: Caminho, a partir da raiz do projeto, onde o arquivo sera baixado
            p_file_name: Nome que o arquivo tera ao ser baixado
        """
        self.p_url = p_url
        self.p_path = p_path
        self.p_file_name = p_file_name

    def download_file(self):
        """
        Description:
            Método que faz o download do arquivo, seguindo o critério de baixar partes do arquivo

        Keyword arguments:
            None

        Return:
            None

        Exception:
            None
        """
        # Verificar se o diretorio existe, e caso não exista cria esse diretorio
        if not os.path.exists(self.p_path):
            os.makedirs(self.p_path)

        # Realizar um join entre o diretorio e o nome do arquivo
        str_path = os.path.join(self.p_path, self.p_file_name)

        # Realizar a requisição da URL
        response = requests.get(self.p_url, stream = True)

        if response.ok:
            pbar = tqdm(total = int(response.headers['Content-Length']),
                        unit_scale = True,
                        position = 0)

            with open(str_path, 'wb') as new_file:               

                for chunk in response.iter_content(chunk_size = 256):
                    if chunk:
                        new_file.write(chunk)
                        new_file.flush()
                        os.fsync(new_file.fileno())
                        pbar.update(len(chunk))
            pbar.close()
                    
            print("Download Finalizado !\nArquivo {}. salvo em: {}".format(self.p_file_name, self.p_path))

        else:
            print("Download Cancelado !\nCódigo do Erro: {}\nErro: {}".format(response.status_code, response.text))
            response.raise_for_status()

    def file_exists(self):
        """
        Description:
            Método que verifica se o arquivo existe no diretorio 

        Keyword arguments:
            None

        Return:
            1: Arquivo Existe
            0: Arquivo não Existe

        Exception:
            None
        """
        # Realizar um join entre o diretorio e o nome do arquivo
        str_path = os.path.join(self.p_path, self.p_file_name)

        return 1 if os.path.exists(str_path) else 0