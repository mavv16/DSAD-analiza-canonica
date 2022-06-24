import numpy as np
import pandas as pd
from PySide2.QtWidgets import QFileDialog

from grafice import dendrograma

np.set_printoptions(precision=5, suppress=True)

def nan_replace(x):
    is_nan = np.isnan(x)
    k_nan = np.where(is_nan)
    x[k_nan] = np.round(np.nanmean(x[:, k_nan[1]], axis=0))


# h - functia noastra (modelul)
# p - pasii nostrii
# n - nr de elemente sunt pasii +1
# metoda Ward sau variantei minime
def partitie(h, nr_clusteri, p, instante, metoda):
    k_dif_max = p - nr_clusteri
    prag = (h[k_dif_max, 2] + h[k_dif_max + 1, 2]) / 2

    dendrograma(h, instante, "Partitia cu " + str(nr_clusteri) + " clusteri. Metoda: " + metoda, prag)

    n = p + 1

    # c[i] = clusterul din care face parte instanta i
    c = np.arange(n)
    for i in range(n - nr_clusteri):
        k1 = h[i, 0]
        k2 = h[i, 1]
        c[c == k1] = n + i
        c[c == k2] = n + i

    coduri = pd.Categorical(c).codes
    return np.array(["c" + str(cod + 1) for cod in coduri])


def citire_fisier_variabile():
    dialog = QFileDialog(directory=".")
    dialog.setNameFilter("Fisiere csv (*.csv)")
    dialog.exec_()

    fisiere = dialog.selectedFiles()

    if len(fisiere) > 0:
        tabel = pd.read_csv(fisiere[0])
        print(tabel)
        variabile = list(tabel)[2:]
        instante_idx = list(tabel["Code"])

        n = len(instante_idx)
        m = len(variabile)

        x = tabel[variabile].values
        nan_replace(x)

        df = pd.DataFrame(x)
        df.to_csv('out/x_complet.csv')

        return x, variabile, instante_idx, fisiere[0], n, m
