class Bond:
    def __init__(self, principal, coupon_rate, yield_to_maturity, periods):
        self.principal = principal
        self.coupon_rate = coupon_rate
        self.yield_to_maturity = yield_to_maturity
        self.periods = periods
        self.coupon = principal * coupon_rate

    @property
    def discount_factor(self):
        discount_factor = 1 / (1 + self.yield_to_maturity)**self.periods

        return discount_factor

    @property
    def pv_annuity(self):
        pv = self.coupon * ((1 - self.discount_factor) /
                            self.yield_to_maturity)

        return pv

    @property
    def pv_principal(self):
        pv = self.principal * self.discount_factor

        return pv

    @property
    def pv(self):
        pv = self.pv_annuity + self.pv_principal

        return pv

    def current_yield(self, price=None):
        if price:
            current_yield = self.coupon / price
        else:
            current_yield = self.coupon / self.pv

        return current_yield


def real_rate(nominal_rate, inflation_rate):
    rate = ((1 + nominal_rate) / (1 + inflation_rate)) - 1

    return rate


def nominal_rate(real_rate, inflation_rate):
    rate = (1 + real_rate) * (1 + inflation_rate) - 1

    return rate


def inflation_rate(nominal_rate, real_rate):
    rate = (1 + nominal_rate) / (1 + real_rate) - 1

    return rate
