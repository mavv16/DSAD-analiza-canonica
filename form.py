from controller import *
from grafice import *
from mainWindow import *


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_cititre.clicked.connect(self.citire)
        self.sp_nr_clusteri.valueChanged.connect(self.setSpinner)
        self.btn_dendrograma.clicked.connect(self.afiseazaDendrograma)
        self.btn_histograme.clicked.connect(self.afiseazaHistograma)

    def citire(self):
        self.tabel, self.vb_col, self.vb_idx, fis, self.n, self.m = citire_fisier_variabile()
        if self.tabel is not None:
            print(self.tabel)

            self.tb_citire.setText(fis)
            self.tb_n.setText("n=" + str(self.n))
            self.tb_m.setText("m=" + str(self.m))

            self.linkage_matrix()
        else:
            print("err1")

    def linkage_matrix(self):
        self.h = hclust.linkage(self.tabel, method="ward")
        self.input_matrix.append(str(self.h))

        self.p = self.n - 1  # procesarea
        self.k_dif_max = np.argmax(self.h[1:, 2] - self.h[:(self.p - 1), 2])

        self.lb_index_max.setText(str(self.k_dif_max))

        self.nr_clusteri = self.p - self.k_dif_max
        self.sp_nr_clusteri.setValue(self.nr_clusteri)

    def setSpinner(self):
        self.nr_clusteri = self.sp_nr_clusteri.value()

    def afiseazaDendrograma(self):
        self.partitie_opt = partitie(self.h, self.nr_clusteri, self.p, self.vb_idx, "ward")
        partitie_opt_df = pd.DataFrame(
            data={"Cluster": self.partitie_opt},
            index=self.vb_idx
        )
        partitie_opt_df.to_csv("out/partitie_opt_" + str(self.nr_clusteri) + ".csv")
        show()

    def afiseazaHistograma(self):
        for i in range(self.m):
            histograma(self.tabel[:, i], self.vb_col[i], self.partitie_opt)
        show()
