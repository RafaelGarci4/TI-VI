import cv2
import os

def selecionar_area_interesse(imagem, nome_imagem):
    # Exibir a imagem para seleção
    cv2.imshow('Selecione a área de interesse', imagem)
    # Selecionar a área de interesse
    x, y, w, h = cv2.selectROI('Selecione a área de interesse', imagem, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()
    # Recortar a área de interesse
    area_interesse = imagem[y:y+h, x:x+w]
    # Salvar a área de interesse em uma pasta com um nome único
    caminho_saida = f'imgsADIprocessadas/{nome_imagem}_area_interesse.png'
    print(f'Salvando área de interesse em: {caminho_saida}')
    cv2.imwrite(caminho_saida, area_interesse)

# Pasta de entrada contendo as imagens de área de interesse
pasta_entrada = "imgsAreaDeInteresse"
# Pasta de saída onde as áreas de interesse recortadas serão exportadas
pasta_saida = "imgsADIprocessadas"

# Verificar e criar a pasta de saída se ela não existir
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Iterar sobre as imagens na pasta de entrada
for nome_imagem in os.listdir(pasta_entrada):
    # Carregar a imagem
    imagem = cv2.imread(os.path.join(pasta_entrada, nome_imagem))
    print(f'Selecionando área de interesse em: {nome_imagem}')
    # Chamar a função para selecionar a área de interesse e exportá-la
    selecionar_area_interesse(imagem, os.path.splitext(nome_imagem)[0])
