import sqlite3
import hashlib
db = sqlite3.connect('../../Users_information.data')
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Users_data (
                name TEXT PRIMARY KEY,
                last_name TEXT,
                otchestvo TEXT,
                password TEXT,
                mail TEXT,
                age INTEGER,
                pol TEXT,
                city TEXT
                playlists_dict)""")
cur.close()
db.close()


def registration(e,name_field_reg, last_name_field_reg, otchestvo_field_reg, pas_field_reg,
                 age_field_reg,mail_field,pol_vebor,city_field_reg):
    if any(field.value == "" for field in
           [name_field_reg, last_name_field_reg, otchestvo_field_reg, pas_field_reg, age_field_reg,
            city_field_reg]):
        return "snack_bar_open"
    else:
        try:
            db = sqlite3.connect('../../Users_information.data')
            cur = db.cursor()
            values = (
                str(name_field_reg.value),
                str(last_name_field_reg.value),
                str(otchestvo_field_reg.value),
                hashlib.blake2b(str(pas_field_reg.value).encode('utf-8')).hexdigest(),
                str(mail_field.value),
                int(age_field_reg.value),
                str(pol_vebor.value),
                str(city_field_reg.value),
                '-'
            )
            cur.execute(
                "INSERT INTO Users_data (name, last_name, otchestvo, password, mail, age, pol, city, playlist_dict) VALUES(?,?,?,?,?,?,?,?,?)",
                values)
            db.commit()
            return "open_dialg"
        except sqlite3.Error as e:
            print(e)
            return "snack_bar_open_reg"
        finally:
            cur.close()
            db.close()


def login(e,name_field_login,pas_field_login):
    admin = "Ilay"
    admin_pas = "b923a2f0d6052eb1c0b219b2ebbeadc9726793936ddb8d19d9665cb9acc664b646d759cb5a4d209aeb662350381b6927b8b41027e0d452989330073d22d8f3a3"
    db = sqlite3.connect('../../Users_information.data')
    cur = db.cursor()
    cur.execute("SELECT * FROM Users_data WHERE name=?", (name_field_login.value,))
    user = cur.fetchall()
    if user == []:
        return "snack_bar_open_whod"
    for row in user:
        if row[0] == admin:
            if row[3] == admin_pas:
                return "open_admin_panel"
            else:
                pass
        else:
            if row[3] == hashlib.blake2b(str(pas_field_login.value).encode('utf-8')).hexdigest():
                return "open_user_panel"
            else:
                pass
    cur.close()
    db.close()
