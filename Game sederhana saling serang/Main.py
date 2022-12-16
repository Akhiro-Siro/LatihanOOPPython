class Hero:

    def __init__(self, nama, darah, kekuatan, pertahanan):
        self.nama = nama
        self.darah = darah
        self.kekuatan = kekuatan
        self.pertahanan = pertahanan

    def serang(self, Musuh):
        print(self.nama + "menyerang " + Musuh.nama)
        Musuh.diserang(self, self.kekuatan)

    def diserang(self, Musuh, dmg):
        print(self.nama + " kena serang " + Musuh.nama)
        dmg_diterima = dmg/self.pertahanan
        print("dmg yang di terima " + str(dmg_diterima))
        self.darah -= dmg_diterima
        print("sisa darah dari " + self.nama + "tersisa " + str(self.darah))


hayabusa = Hero("hayabusa ", 100, 20, 5)
tigral = Hero("tigral ", 100, 3, 50)

tigral.serang(hayabusa)
print("\n")
hayabusa.serang(tigral)
print("\n")
tigral.serang(hayabusa)
print("\n")
hayabusa.serang(tigral)
