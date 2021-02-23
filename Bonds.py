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
