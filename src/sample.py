import principal as pr

if __name__ == "__main__":

    url = 'https://dados.educacao.sp.gov.br/sites/default/files/IDESP_ESCOLA_2019.csv'
    name_file = 'IDESP_ESCOLA_2019.csv'
    output_file = 'output/data'

    cnn = pr.URLConnection(url, output_file, name_file)
    print("Arquivo existe: {}".format(cnn.file_exists()))
    cnn.download_file()