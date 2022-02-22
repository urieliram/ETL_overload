
import numpy as np
import pandas as pd
import os 
import time

raiz = 'C:/Users/uriel/OneDrive - uanl.edu.mx/Escenarios y resultados de pruebas paper MDA/'

#areas = ['CEN','GUA','NES','NOR','NTE','OCC','ORI','PEE','PEN','CEN_min','GUA_min','NES_min','NOR_min','NTE_min','OCC_min','ORI_min','PEE_min','PEN_min']
dfdir = pd.read_csv('directorios.csv', header = None)
dfram = pd.read_csv('GRUPOSRAMAS.csv', header = None)
dfare = pd.read_csv('AREAMEM.csv',     header = None)
n = len(dfdir.index)

#Agregar columnas que representan líneas
column_lines = []
for i in dfram.index:
    column_lines.append(i+1)
    
#Agregar columnas que representan líneas
column_areas = []
for i in dfare.index:
    column_areas.append(str(dfare[0][i]))

column_areas_min = []
for i in dfare.index:
    cad = str(dfare[0][i]) + '_min'
    column_areas.append(cad)

columns = ['Num'] + column_lines + column_areas + column_areas_min
dfout = pd.DataFrame(columns = columns)

#Iniciamos lista de ceros
ncols = dfout.columns
listofzeros = []
for i in range(len(ncols) ):
    listofzeros.append(0)
    
#Aplicamos lista de ceros por defecto al dataframe dfout de resultados
for i in range(n):
    dfout.loc[i] = listofzeros
    
file = 'CONJACTIV.csv'
for i in dfdir.index:
    dir = str(dfdir[1][i])
    dir = dir + '/'
    df  = pd.read_csv(raiz + dir + file, header = None)
    dfout.loc[i,'Num'] = int(dfdir[0][i])
    
    for j in df.index:
        #nlinea = int(df[0][j])
        #print(df[1][j])
        #print(dfram.index[dfram[1] == str(df[1][j].strip())].tolist())
        aux = dfram.index[dfram[1] == str(df[1][j].strip())]
        dfout.loc[i,aux+1] = 1
        #time.sleep(3)        
    
dfout.to_csv('dfout.csv')