from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as hclust

def dendrograma(h, instante, titlu, prag=None):
    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(titlu, fontsize=18, color='r')
    hclust.dendrogram(h, labels=instante, ax=ax, color_threshold=prag)


def histograma(x, variabila, partitia):
    fig = plt.figure(figsize=(14, 8))

    fig.suptitle("Histograme pt variabila " + variabila, fontsize=18, color='r')

    clusteri = list(set(partitia))
    size = len(clusteri)

    axs = fig.subplots(1, size, sharey=True)

    for i in range(size):
        ax = axs[i]
        ax.set_xlabel(clusteri[i])
        ax.hist(x[partitia == clusteri[i]], bins=10, rwidth=0.9, range=(min(x), max(x)))


def show():
    plt.show()
