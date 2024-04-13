class trougao:
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def IZbir(self):
        return (self.a+self.b+self.c)
Tr1 = trougao(1,2,3)
tr1 = Tr1.IZbir()
Tr2 = trougao(12,2,31)
tr2 = Tr2.IZbir()
Tr3 = trougao(3,5,10)
tr3 = Tr3.IZbir()
print(max(tr1, tr2, tr3))
print(min(tr1, tr2, tr3))
