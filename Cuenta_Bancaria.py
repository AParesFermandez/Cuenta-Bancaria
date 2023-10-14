class CuentaBancaria:
    # Atributos de instancia: tasa de interés y balance
    def __init__(self, tasa_interes=0.01, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance

    # Método para realizar un depósito
    def deposito(self, amount):
        self.balance += amount
        return self

    # Método para realizar un retiro
    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self

    # Método para mostrar la información de la cuenta
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self

    # Método para generar interés
    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        return self

# Crear dos cuentas
cuenta1 = CuentaBancaria(0.02, 1000)
cuenta2 = CuentaBancaria()

# Realizar operaciones en la primera cuenta y mostrar la información en una línea
cuenta1.deposito(500).deposito(200).deposito(300).retiro(100).generar_interes().mostrar_info_cuenta()

# Realizar operaciones en la segunda cuenta y mostrar la información en una línea
cuenta2.deposito(300).deposito(400).retiro(50).retiro(200).retiro(100).retiro(150).generar_interes().mostrar_info_cuenta()
