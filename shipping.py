from customer import *

class Shipping(Costomer):
    def __init__(self, name, address, delivery_method):
        super().__init__(name)
        self.shipping_info ={
            "address": self.address,
            "Delivery_method": self.delivery_method
        }

shipping_info = Shipping("Marcelo Manzano", "sicsican", "Super-express")
shipping_info.set_shipping_info()