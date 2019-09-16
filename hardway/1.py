class People(object):
    def __init__(self):
        self.leg = 4

class Man(People):
    pass

Tom = Man()
print(Tom.leg)