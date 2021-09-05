class complejo:
  def __init__(self,real=0,imaginario=0):
    self.real=real
    self.imaginario=imaginario
  def set_real(self,value):
    self.real=value
  def set_imaginario(self,value):
    self.imaginario=value
  def mult(self,complejo2):
    aux_real=self.real*complejo2.real-self.imaginario*complejo2.imaginario
    aux_imaginario=self.real*complejo2.imaginario+self.imaginario*complejo2.real
    self.real=aux_real
    self.imaginario=aux_imaginario

a=complejo(3,4)

b=complejo(2,3)

a.mult(b)

print(a.real)
print("Hello Manu")