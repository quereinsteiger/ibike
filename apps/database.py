import sqlite3 as sql
from apps import objects

class datenbank():
    """docstring for ."""
    def __init__(self, datenbank="./data/ibike.sqlite"):
        self.datenbank = datenbank

    def fahrer_lesen(self, id=1):
        con=sql.connect(self.datenbank)
        con.row_factory=zeilen_dict
        cursor=con.cursor()
        cursor.execute("SELECT * FROM tblFahrer WHERE tblFahrer.ID=" + str(id) + ";")
        driver=cursor.fetchall()

        id=int(driver[0]["ID"])
        Username=driver[0]["Username"]
        Vorname=driver[0]["Vorname"]
        Nachname=driver[0]["Nachname"]
        Geburtsdatum=driver[0]["Geburtsdatum"]
        Geschlecht=driver[0]["Geschlecht"]
        Groesse=driver[0]["Groesse"]
        Gewicht=driver[0]["Gewicht"]

        return objects.fahrer(  Username=Username,
                                Vorname=Vorname,
                                Nachname=Nachname,
                                Geburtsdatum=Geburtsdatum,
                                Geschlecht=Geschlecht,
                                Groesse=Groesse,
                                Gewicht=Gewicht,
                                id= id)





# Hilfsfunktionen

# Ausgabe der Abfragen als Dictionary
def zeilen_dict(cursor, zeile):
    ergebnis = {}
    for spaltennr, spalte in enumerate(cursor.description):
        ergebnis[spalte[0]] = zeile[spaltennr]
    return ergebnis

# >>> connection.row_factory = zeilen_dict
# >>> cursor = connection.cursor()
# >>> cursor.execute("SELECT * FROM kunden")
# >>> cursor.fetchall()
