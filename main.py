from kivy.app import App
import sqlite3 as sq


class TestApp(App):
    def on_start(self):
        with sq.connect('price.db') as con:
            cur = con.cursor()
            cur.execute("""
                    SELECT * FROM price 
                """)
            arr = cur.fetchall()

        self.stand_width_db = arr[0][1]
        self.root.ids['stand_width'].text = self.stand_width_db
        self.stand_height_db = arr[0][2]
        self.root.ids['stand_height'].text = self.stand_height_db
        self.pvh_width_db = arr[0][3]
        self.root.ids['pvh_width'].text = self.pvh_width_db
        self.pvh_height_db = arr[0][4]
        self.root.ids['pvh_height'].text = self.pvh_height_db
        self.pvh_price_db = arr[0][5]
        self.root.ids['pvh_price'].text = self.pvh_price_db
        self.folia_price_db = arr[0][6]
        self.root.ids['folia_price'].text = self.folia_price_db
        self.pet_with_db = arr[0][7]
        self.root.ids['pet_width'].text = self.pet_with_db
        self.pet_height_db = arr[0][8]
        self.root.ids['pet_height'].text = self.pet_height_db
        self.pet_price_db = arr[0][9]
        self.root.ids['pet_price'].text = self.pet_price_db
        self.a3_db = arr[0][10]
        self.root.ids['a3'].text = self.a3_db
        self.a4_db = arr[0][11]
        self.root.ids['a4'].text = self.a4_db
        self.a5_db = arr[0][12]
        self.root.ids['a5'].text = self.a5_db
        self.scotch_width_db = arr[0][13]
        self.root.ids['scotch_width'].text = self.scotch_width_db
        self.scotch_lenght_db = arr[0][14]
        self.root.ids['scotch_length'].text = self.scotch_lenght_db
        self.scotch_price_db = arr[0][15]
        self.root.ids['scotch_price'].text = self.scotch_price_db

    def press(self):
        stand_width = int(self.root.ids['stand_width'].text) / 1000
        stand_height = int(self.root.ids['stand_height'].text) / 1000
        stand_area = stand_height * stand_width
        pvh_width = int(self.root.ids['pvh_width'].text) / 1000
        pvh_height = int(self.root.ids['pvh_height'].text) / 1000
        pvh_area = pvh_height * pvh_width
        pvh_price = stand_area / pvh_area * int(self.root.ids['pvh_price'].text)
        folia_price = stand_area * (int(self.root.ids['folia_price'].text))
        a4_area = 0.21 * 0.297 * (int(self.root.ids['a4'].text))
        a3_area = 0.42 * 0.297 * (int(self.root.ids['a3'].text))
        a5_area = 0.21 * 0.148 * (int(self.root.ids['a5'].text))
        pet_width = int(self.root.ids['pet_width'].text) / 1000
        pet_height = int(self.root.ids['pet_height'].text) / 1000
        pet_area = pet_height * pet_width
        pet_price = (a4_area + a3_area + a5_area) / pet_area * (int(self.root.ids['pet_price'].text))
        per_a5 = 0.21 * 2 + 0.148 * 2
        per_a4 = 0.21 * 2 + 0.297 * 2
        per_a3 = 0.42 * 2 + 0.297 * 2
        per_pet = per_a5 * int(self.root.ids['a5'].text) + per_a4 * int(self.root.ids['a4'].text) + per_a3 * int(self.root.ids['a3'].text)
        scotch_per = int(self.root.ids['scotch_length'].text)
        scotch_price = per_pet / scotch_per * int(self.root.ids['scotch_price'].text)
        temp_price = int(pvh_price + folia_price + pet_price + scotch_price)
        total_price = temp_price * 3
        self.root.ids['sbs'].text = str(temp_price)
        self.root.ids['full_price'].text = str(total_price)

    def stand_btn(self):
        with sq.connect('price.db') as con:
            cur = con.cursor()
            cur.execute(f'UPDATE price SET stand_width = {self.root.ids["stand_width"].text}, stand_height = {self.root.ids["stand_height"].text};')

    def pvh_btn(self):
        with sq.connect('price.db') as con:
            cur = con.cursor()
            cur.execute(f'UPDATE price SET pvh_width = {self.root.ids["pvh_width"].text}, pvh_height = {self.root.ids["pvh_height"].text}, pvh_price = {self.root.ids["pvh_price"].text};')

    def folia_btn(self):
        with sq.connect('price.db') as con:
            cur = con.cursor()
            cur.execute(f'UPDATE price SET folia_price = {self.root.ids["folia_price"].text};')

    def pet_btn(self):
        with sq.connect('price.db') as con:
            cur = con.cursor()
            cur.execute(f'UPDATE price SET pet_width = {self.root.ids["pet_width"].text}, pet_height = {self.root.ids["pet_height"].text}, pet_price = {self.root.ids["pet_price"].text};')

    def papper_btn(self):
        with sq.connect('price.db') as con:
            cur = con.cursor()
            cur.execute(f'UPDATE price SET a3 = {self.root.ids["a3"].text}, a4 = {self.root.ids["a4"].text}, a5 = {self.root.ids["a5"].text};')

    def scotch_btn(self):
        with sq.connect('price.db') as con:
            cur = con.cursor()
            cur.execute(f'UPDATE price SET scotch_width = {self.root.ids["scotch_width"].text}, scotch_lenght = {self.root.ids["scotch_length"].text}, scotch_price = {self.root.ids["scotch_price"].text};')


TestApp().run()
