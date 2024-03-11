class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price
  def get_name(self):
    return self.name
  def __str__(self):
    return self.name
  def __repr__(self):
    return self.name+" : "+str(self.price)+"원"
  

product = Product('피자',format(25000,','))
print(product.get_name())

print(product)