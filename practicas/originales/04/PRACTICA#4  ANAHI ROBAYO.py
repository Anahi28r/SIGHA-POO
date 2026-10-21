from abc import ABC, abstractmethod
class PasarelaDePago(ABC):
    @abstractmethod
    def cobrar(self, monto:float) -> bool:
        pass
class PasarelaPaypal(PasarelaDePago):
    def cobrar(self, monto:float) -> bool:
        if monto > 0:
            print(f"Pago con monto de ${monto:.2f} realizado desde Paypal")
            return True
        print(f"Error: El monto no se valido en Paypal")
        return False
class PasarelaStripe(PasarelaDePago):
    def cobrar(self, monto:float) -> bool:
        if monto > 0:
            print(f"Pago con monto de ${monto:.2f} realizado desde Stripe")
            return True
        print(f"Error: El monto no se valido en Stripe")
        return False

class ServicioDeCaja:
    def __init__(self,pasarela:PasarelaDePago):
        self.pasarela = pasarela
    def realiza_pago(self, monto:float):
            if self.pasarela.cobrar(monto):
             print(f"La Transacción es exitosa")
            else:
             print(f"La Transacción fue rechazada")


print(f"PAGOS DESDE LA PLATAFORMA PAYPAL")
caja = ServicioDeCaja(PasarelaPaypal())
caja.realiza_pago(150.00)

print(f"PAGOS DESDE LA PLATAFORMA STRIPE")
caja = ServicioDeCaja(PasarelaStripe())
caja.realiza_pago(250.00)
            
