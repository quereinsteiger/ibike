import time
import sqlite3 as sql


class fahrer():
    """ Abbildung der Fahrer und deren Eigenschaften
        -hinzufügen neuer Fahrer
        -auswählen eines Fahrers"""
    def __init__(self, Username, Vorname,Nachname,Geburtsdatum,Geschlecht, Groesse, Gewicht,id=0):

        self.__id = id
        self.Username = Username
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Geburtsdatum = Geburtsdatum
        self.Geschlecht = Geschlecht
        self.Groesse = Groesse
        self.Gewicht = Gewicht

    def alter(self):
        date_of_birth=time.strptime(self.Geburtsdatum, "%d.%m.%Y")
        num_from_birth=time.mktime(date_of_birth)
        age=time.time()-num_from_birth
        return time.localtime(age).tm_year-1970

    def anlegen(self):
        con = sql.connect("./data/ibike.sqlite")
        cursor=con.cursor()
        cursor.execute("INSERT INTO tblFahrer(Username,Vorname,Nachname,Geburtsdatum,Geschlecht,Groesse,Gewicht) Values(?,?,?,?,?,?,?);"
                        , (str(self.Username),str(self.Vorname),str(self.Nachname),str(self.Geburtsdatum),str(self.Geschlecht),str(self.Groesse),str(self.Gewicht)))
        con.commit()
        con.close()
        return
