class Person:
    def __init__(self, ism, yoshi, tyili, shahar):
        self.ism = ism
        self.yoshi = yoshi
        self.tyili = tyili
        self.shahar = shahar

    def get_info_person(self):
        return f"{self.ism}, {self.yoshi}, {self.tyili}, {self.shahar}"


class Talaba(Person):
    def __init__(self, ism, yoshi, tyili, shahar, universitet, guruhi):
        super().__init__(ism, yoshi, tyili, shahar)
        self.universitet = universitet
        self.guruhi = guruhi

    def get_info_person(self):
        super().get_info_person()
        return self.ism, self.tyili, self.guruhi, self.shahar, self.yoshi, self.universitet


    def get_info_talaba(self):
        return f"{self.ism}, {self.yoshi}, {self.universitet}, {self.guruhi}"



person = Person('Baxtiyor', 24, 'Surxondaryo', 2001)
talaba1 = Talaba('Baxtiyor', 24, 'Surxondaryo', 2001,'TIFT', 'ITK-22/01')

print(talaba1.ism)
print(talaba1.get_info_talaba())
print(talaba1.get_info_person())
print(person.get_info_person())



class Texnika:
    def __init__(self, nomi, kompaniyasi, yili, shahar):
        self.nomi = nomi
        self.kompaniyasi = kompaniyasi
        self.yili = yili
        self.shahar = shahar

class Kompyuter(Texnika):
    def __init__(self, nomi, kompaniyasi, yili, shahar, xotira, ekran, operativka):
        super().__init__(nomi, kompaniyasi, yili, shahar)
        self.xotira = xotira
        self.ekran = ekran
        self.operativka = operativka

class Noutbook(Kompyuter):
    def __init__(self, nomi, kompaniyasi, yili, shahar, xotira, ekran, operativka, batareya, kamera):
        super().__init__(nomi, kompaniyasi, yili, shahar, xotira, ekran, operativka)
        self.batareya = batareya
        self.kamera = kamera

class PC(Kompyuter):
    def __init__(self, nomi, kompaniyasi, yili, shahar, xotira, ekran, operativka, video_card, klaviatura):
        super().__init__(nomi, kompaniyasi, yili, shahar, xotira, ekran, operativka)
        self.video_card = video_card
        self.klaviatura = klaviatura


class Elektromobil(Texnika):
    def __init__(self, nomi, kompaniyasi, yili, shahar, ot_kuchi, yoqilgi, mexanika):
        Texnika.__init__(self, nomi, kompaniyasi, yili, shahar)
        self.yoqilgi = yoqilgi
        self.ot_kuchi = ot_kuchi
        self.mexanika = mexanika



class Chevrolet(Texnika):
    def __init__(self, nomi, kompaniyasi, yili, shahar, ot_kuchi, tablo):
        Texnika.__init__(self, nomi, kompaniyasi, yili, shahar)
        self.tablo = tablo
        self.ot_kuchi = ot_kuchi


class MashinaGibrid(Elektromobil, Chevrolet):
    def __init__(self, nomi, kompaniyasi, yili, shahar, ot_kuchi, yoqilgi, tablo, mexanika):
        Elektromobil.__init__(self, nomi, kompaniyasi, yili, shahar, ot_kuchi, yoqilgi, mexanika)
        Chevrolet.__init__(self, nomi, kompaniyasi, yili, shahar, ot_kuchi, tablo)


mashina1 = MashinaGibrid('Tesla_model', 'Tesla', 2025, 'Ohayo', 1000, 'Gibrid', 'Ekran', False)


print(mashina1.yoqilgi)

noutbook = Noutbook('Asus Vivokook', 'Asus', 2024, 'Dubai', 512, '16 dyum', 16, 5200, '4 mp')


print(mashina1.ot_kuchi)



