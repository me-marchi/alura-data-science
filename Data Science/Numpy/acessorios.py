import numpy as np

dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

Acessorios = np.array(dados)
#print(Acessorios)

#print(Acessorios.shape)

#print(Acessorios[:, 1:3])
##print(Acessorios[:, 1:3][0])
#print(Acessorios[:, 1:3][0][0])
#print(Acessorios[:, 1:3][0,0])

#print(np.resize(Acessorios,(2,3)))