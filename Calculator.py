import numpy_financial as npf


class Calculator:
    def __init__(self, koefficient, invest_volume, cash_threads_count, cash_threads_values):
        self.koefficient = koefficient
        self.invest_volume = invest_volume
        self.t = cash_threads_count
        self.ci = cash_threads_values
        self.ci2 = []
        self.tempmass = []
        self.irrmass = []
        self.pv = 0.0
        self.roisr = 0.0
        self.roi = 0.0
        self.npv = 0.0
        self.irr = 0.0
        self.pi = 0.0
        self.pdp = 0.0

    # Возвращаем массив с результатами вычислений и исходными данными для сравнения
    def get_results(self):
        return [self.invest_volume, self.t, self.koefficient, self.pv, self.npv, self.pdp, self.pi, self.irr,
                self.roi]

    def calc_mass2(self):
        i = 0
        while i < self.t:
            self.ci2.append(0)
            i = i + 1

    def calc_pvrass(self):
        i = 0
        while i < self.t:
            self.pv += round((self.ci[i]) / pow(1 + self.koefficient, i + 1), 2)
            self.ci2[i] = (self.ci[i]) / pow(1 + self.koefficient, i + 1)
            i = i + 1

    def calc_roistr(self):
        i = 0
        while i < self.t:
            self.roisr += self.ci[i]
            i = i + 1

    def calc_roirass(self):
        self.roi = round((self.roisr / self.t) / ((self.invest_volume - 0) / 2), 2)

    def calc_npvrass(self):
        self.npv = round(self.pv - self.invest_volume, 2)

    def calc_irrmassiv(self):
        self.irrmass = self.ci.copy()
        self.irrmass.insert(0, -self.invest_volume)

    def calc_irrrass(self):
        self.irr = round(npf.irr(self.irrmass), 2)

    def calc_pirass(self):
        pipol = 0
        piotr = 0
        i = 0
        while i < self.t:
            if self.ci2[i] < 0:
                piotr += self.ci2[i]
                i = i + 1
            else:
                pipol += self.ci2[i]
                i = i + 1

        self.pi = round(pipol / (self.invest_volume + (-piotr)), 3)

    def calc_pdprass(self):
        i = 0
        while i < self.t:
            self.tempmass.append(0)
            i = i + 1
        self.tempmass[0] = -self.invest_volume + self.ci2[0]

        i = 1
        while i < self.t:
            self.tempmass[i] = self.tempmass[i - 1] + self.ci2[i]
            i = i + 1

        i = 0
        k = 0
        while i < self.t:
            if self.tempmass[i] > 0:
                k = i
                break
            i = i + 1

        self.pdp = round(-self.tempmass[k - 1] / self.ci2[k] + k, 2)

    def calc_all(self):
        self.calc_mass2()
        self.calc_pvrass()
        self.calc_roistr()
        self.calc_roirass()
        self.calc_npvrass()
        self.calc_irrmassiv()
        self.calc_irrrass()
        self.calc_pirass()
        self.calc_pdprass()
