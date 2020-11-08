import csv
import numpy as np
import matplotlib.pyplot as plt

def plot(route_filename, img_filename, background=False):
    '''
    Cria um plot da rota (minima) que passa por todas as coordenadas.
    As informacoes deste plot veem de um arquivo csv com as rotas e plota
    uma imagem (img_name)

    Parametros
    ----------
        route_filename : str
            arquivo csv com as rotas. O cabecalho do arquivo csv eh
            x_i, y_i, x_j e y_j sendo i a coordenada de saida e j a
            coordenada de entrada
        img_name : str
            nome do arquivo de plot
        background : bool
            flag que indica se o plot vai ter uma image de fundo
            (background=True) ou nao (background=False). Por padrao
            background=False
    '''

    with open(route_filename, 'r') as route_file:

        reader = list(csv.DictReader(route_file))

        line_color = 'black'

        if background:
            img = plt.imread('galaxy_image.jpg')
            plt.imshow(img, extent=[0, 1920, 0, 1080])
            line_color = 'white'

        for row in reader:
            plt.plot([float(row['x_i']), float(row['x_j'])], 
                     [float(row['y_i']), float(row['y_j'])], 
                      '--', lw = 3, color = line_color)

        for row in reader:
            plt.plot(float(row['x_i']), float(row['y_i']), marker = '*', ms = 30, color = 'red')
        
        plt.axis('off')

        plt.savefig(img_filename)