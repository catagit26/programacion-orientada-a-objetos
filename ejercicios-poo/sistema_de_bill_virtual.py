class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo
    @property
    def saldo(self):
        return self._saldo

    def depositar (self, monto):
        self._saldo += monto
        return f"deposito exitoso: {self._saldo}"

    def retirar(self, monto):
        if monto <= self.saldo:
            self._saldo -= monto
            print(f'Retiro exitoso en cuenta de {self.titular}: - ${monto}')
        else:
            print("Saldo insuficiente")

    def tipo_cuenta(self):
       return "Cuenta"

    def __str__(self):
        return f"{self.titular} | Saldo: {self.saldo}"

class CuentaBasica (Cuenta):
    def __init__(self, titular, saldo, limitite_retiro_diario):
        super().__init__(titular, saldo)
        self. limitite_retiro_diario = limitite_retiro_diario
    def tipo_cuenta(self):
        return "Básica"
    def __str__(self):
        return f"{self.titular} | Cuenta Básica | Saldo: ${self.saldo} | Limite diario: {self.limitite_retiro_diario}"

class CuentaPremium(Cuenta):
    def __init__(self, titular, saldo, cashback_porcentaje):
        super().__init__(titular, saldo)
        self. cashback_porcentaje = cashback_porcentaje
    def tipo_cuenta(self):
        return "Premium"
    def __str__(self):
        return f"{self.titular} | Cuenta Premium | Saldo: ${self.saldo} | Cashback: {self.cashback_porcentaje}%"


c_b1 = CuentaBasica ("Cata", 2000, 10000)
c_b2 = CuentaBasica ("Santino", 5600, 7000)
cp1 = CuentaPremium ("Luciano", 15000, 5)
cp2 = CuentaPremium ("Mariana", 20000, 2)
print("\n-----Cuentas:-----")
print(c_b1)
print(c_b2)
print(cp1)
print(cp2)
print("\n---Deposito---")
c_b1.depositar(100)
cp1.depositar(100)
print("\n---Retiro---")
c_b2.retirar(600)
print("\nIntento de retiro excesivo en cuenta de Santino:")
c_b2.retirar(10000)
print ("\n--- Cuentas Actualizadas---")
print(c_b1)
print(cp1)
print(c_b2)
print(cp2)

print(f"\n---Tipo de cuentas:---")
print(f"cuenta 1: {c_b1.tipo_cuenta()}")
print (f"cuenta 2: {c_b2.tipo_cuenta()}")
print(f"cuenta 3: {cp1.tipo_cuenta()}")
print(f"cuenta 4: {cp2.tipo_cuenta()}")

print("\n--Utilizamos Property saldo:--")
print(f"Saldo de {cp2.titular}: ${cp2.saldo}")



