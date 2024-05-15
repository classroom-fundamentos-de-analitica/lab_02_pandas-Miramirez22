"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    return tbl0.shape[0]


def pregunta_02():
    return tbl0.columns.size


def pregunta_03():
    return tbl0['_c1'].value_counts()


def pregunta_04():
    return tbl0.groupby('_c1')['_c2'].mean()


def pregunta_05():
    return tbl0.groupby('_c1')['_c2'].max()


def pregunta_06():
    unique_values = tbl1['_c4'].unique()
    upper_values = [value.upper() for value in unique_values]
    sorted_values = sorted(upper_values)
    return sorted_values


def pregunta_07():
    return tbl0.groupby('_c1')['_c2'].sum()


def pregunta_08():
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']
    return tbl0


def pregunta_09():
    tbl0['year'] = tbl0['_c3'].str.slice(0, 4)
    return tbl0


def pregunta_10():
    tbl0['_c2'] = tbl0['_c2'].astype(str)
    result = tbl0.sort_values(['_c1', '_c2']).groupby('_c1')['_c2'].apply(':'.join).reset_index()
    return result


def pregunta_11():
    tbl1['_c4'] = tbl1['_c4'].astype(str)
    result = tbl1.sort_values(['_c0', '_c4']).groupby('_c0')['_c4'].apply(','.join).reset_index()
    print(result)
    return result


def pregunta_12():
    tbl2['_c5'] = tbl2['_c5a'] + ':' + tbl2['_c5b'].astype(str) 
    result = tbl2.sort_values(['_c0', '_c5']).groupby('_c0')['_c5'].apply(','.join).reset_index()
    print(result)
    return result


def pregunta_13():
    merged = pd.merge(tbl0, tbl2, on='_c0')
    result = merged.groupby('_c1')['_c5b'].sum()
    return result
