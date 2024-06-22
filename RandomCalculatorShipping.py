class EcommShopping:
    entry = 0


    def __init__(self, price = 0.0, region = ""):
        self.price = float(input("Enter the total cart price: "))
        self.region = input("Enter the delivery destination: ").title()
        global entry
        EcommShopping.entry += 1


    def calculate_shipping_fees(self):
        global region_fees, show_fees, price_plus_sfee
        region_fees = {
            "West": 15.00, "East": 5.00, "South": 10.00,
            "North": 9.00, "Oversea": 50.00
        }
        if (self.region == "West"):
            price_plus_sfee = self.price + 15.00
            show_fees = region_fees.get("West")
        elif (self.region == "North"):
            price_plus_sfee = self.price + 9.00
            show_fees = region_fees.get("North")
        elif (self.region == "South"):
            price_plus_sfee = self.price + 10.00
            show_fees = region_fees.get("South")
        elif (self.region == "East"):
            price_plus_sfee = self.price + 5.00
            show_fees = region_fees.get("East")
        elif (self.region == "Oversea"):
            price_plus_sfee = self.price + 50.00
            show_fees = region_fees.get("Oversea")
        else:
            raise Exception(f"Please enter East, North, West, South or Oversea.")


    def discount_above_200(self):
        global discount, discounted_price
        if (price_plus_sfee >= 200): #if statement attribute may be change to self.price to exclude shipping.
            discount = price_plus_sfee * 0.05
            discounted_price = price_plus_sfee - discount
        else:
            discount = 0.0
            discounted_price = price_plus_sfee


    def output_response(self):
        if (self.price <= 49):
            print("Note that there's a minimum order price of '$50' excluding shipping/delivery.")
        else:
            print(f"""Actual cost: ${price_plus_sfee:.2f}
Shipping Fee: ${show_fees}
Discount: ${discount:.2f} 
Payable: [${discounted_price:.2f}].""")


x = EcommShopping()
x.calculate_shipping_fees()
x.discount_above_200()
x.output_response()
print(f"Please bill {discounted_price:.2f}, max discount {discount:.2f}.")
