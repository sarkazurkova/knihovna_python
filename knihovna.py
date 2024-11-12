import csv
import json
class KnihovniSystem:
    def __init__(self, nazev_souboru):
        self.soubor = nazev_souboru
        self.knihy = self.nacti_knihy()

    def nacti_knihy(self):
        try:
            with open(self.soubor, 'r', encoding='utf-8') as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            print('Soubor nebyl nalezen')
        except:
            print('Stalo se cosi divného')
            return []


    def uloz_knihy(self, json_soubor):
        with open(json_soubor, 'x', encoding='utf-8') as f:
            f.write(json.dumps(self.knihy, indent=4))

system = KnihovniSystem("knihy.csv")
print(system.knihy[0]['nazev_knihy'])
system.uloz_knihy('knihy.json')