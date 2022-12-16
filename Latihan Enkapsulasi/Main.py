class Hero:
    __jumlah = 0

    def __init__(self, nama, darah, dmg, pertahanan):
        self.__nama = nama
        self.__darahAwal = darah
        self.__dmgAwal = dmg
        self.__armorAwal = pertahanan
        self.__exp = 0
        self.__level = 1

        self.__darahMax = self.__darahAwal * self.__level
        self.__dmg = self.__dmgAwal * self.__level
        self.__pertahanan = self.__armorAwal * self.__level

        self.__darah = self.__darahMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {}:\n\tdarah = {}/{}\n\tkekuatan = {}\n\tpertahanan = {}".format(self.__nama, self.__level, self.__darah, self.__darahMax, self.__dmg, self.__pertahanan)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, tambahExp):
        self.__exp += tambahExp
        if (self.__exp >= 100):
            print('level Up')
            self.__level += 1
            self.__exp -= 100

            self.__darahMax = self.__darahAwal * self.__level
            self.__dmg = self.__dmgAwal * self.__level
            self.__pertahanan = self.__armorAwal * self.__level

    def serang(self, musuh):
        self.gainExp = 50


layla = Hero('layla', 100, 5, 10)
miya = Hero('miya', 100, 5, 5)
print(layla.info)
print(miya.info)

layla.serang(miya)
layla.serang(miya)
layla.serang(miya)
print(layla.info)
