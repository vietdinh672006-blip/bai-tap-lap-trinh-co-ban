class Hinhchunhat(object):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    def area(self):
        return self.dai * self.rong
hinh_chu_nhat_moi = Hinhchunhat(8,10)
print(hinh_chu_nhat_moi.area())
