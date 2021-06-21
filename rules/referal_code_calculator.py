class ReferralCodeCalculator:
    referral_code: str

    def __init__(self, referal_code: str):
        self.referral_code = referal_code

    def calculator_referral_code(self):
        if self.referral_code == 'token1234':
            return 1
        return 0
