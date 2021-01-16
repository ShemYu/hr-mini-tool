import pandas as pd


class Mail():
    pass
    def __init__(self):
        pass

    def send(self):
        pass

class BaseData():
    def __init__(self, default_path = ""):
        self.default_path = default_path
        self.from_excel()
    def from_excel(self):
        pass
    def to_excel(self):
        pass

class HrData(BaseData):
    pass
    def cal_seniority():
        pass


class VacRule():
    def __init__(self, default_path = "docs/員工特修表 - 空白.xlsx"):
        self.default_path = default_path
        self.from_excel(self)
