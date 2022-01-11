import numpy as np

km = np.loadtxt(fname = 'data\carros-km.txt', dtype = int)
anos = np.loadtxt(fname = 'data\carros-anos.txt', dtype = int)
valor = np.loadtxt(fname = 'data\carros-valor.txt')

km_media = km / (2019-anos)

#print(km)
#print(km_media)
#print(type(km_media))
#print(km.shape)

dataset = np.column_stack((anos, km, valor))
#print(dataset)
#print(dataset.shape)

np.mean(dataset)
#média de todos os valores misturados

np.mean(dataset, axis = 0)
#média dos valores de cada coluna separados

np.mean(dataset, axis = 1)
#média caso os dados estivessem por linhas

np.mean(dataset[:,0])
#calcula apenas a média dos anos
#colocando 1, calcula a média km e 2, média dos valores

np.std(dataset[:, 0])
#calcula o desvio padrão

dataset.sum(axis = 0)
np.sum(dataset, axis = 0)
#fazem a somatória de cada coluna separadamente

dataset[:, 1].sum()
np.sum(dataset[:,1])
#fazem a somatória apenas do item 1(km)

