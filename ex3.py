class Calculadora:
    def adicionar(self, a, b):
        return a+b
    def subtrair(self, a, b):
        return a-b
    def mult(self, a, b):
        return a*b
    def divisao(self, a, b):
        if b == 0: 
            return ("Não dividimos por zero")
        else:
            return (a/b)   
calc = Calculadora()
print(calc.adicionar(10,5))
print(calc.subtrair(10,5))
print(calc.divisao(5,0))
print(calc.mult(5,0))
