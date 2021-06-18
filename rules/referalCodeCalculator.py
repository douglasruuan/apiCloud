class referalCode:
    referal_code: str

    def __init__(self, referal_code: str):
        self.referal_code = referal_code

    def calcultaorreferalcode(self):
        if self.referal_code == 'token1234':
            return 1
        return 0
