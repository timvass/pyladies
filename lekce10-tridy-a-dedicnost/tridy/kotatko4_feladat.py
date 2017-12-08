# Abychom snadno rozeznali nekolik mnoukajicich kotatek, kazde kotatko nyni mnouka svym jmenem.
# V metode zamnoukej() nyni muzeme pristupovat k atributum instance pres self.
# self.jmeno pristupuje k atributu jmeno aktualni instance.


class Pes:
    def pozdrav(self, zprava):
        print('{} {}'.format(self.jmeno, zprava))

pes1 = Pes()
pes1.jmeno = "Bruno"
pes1.pozdrav("Haf")

class Hadatko:
    def plaz_se(self, cil):
        print('Plazim ssse, plazim do {}'.format(cil))

    def svlekni_kuzi(self):
        print('SSSvlekam svou kuzi barvy {}'.format(self.barva))

icke_hadatko = Hadatko()
icke_hadatko.barva = "hneda"
icke_hadatko.svlekni_kuzi()
icke_hadatko.plaz_se("Prahy")
