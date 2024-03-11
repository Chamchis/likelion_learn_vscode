# Class 정리
# 클래스 : 메뉴(메뉴보여주기,메뉴추가,삭제), 상점(메뉴보여주기,주문받기,결제하기)
class Menu:
    def __init__(self):
        self.menus = dict()
    def add_menu(self,name,price):
        self.menus[name] = price
    def delete_menu(self,name):
        pass
    def show_menus(self):
        print('메뉴입니다.')
        for name, price in self.menus.items():
            print(f'{name} : {price}')

menu = Menu()
menu.add_menu('coffee',format(5000,','))
menu.add_menu('latte',format(6000,','))
menu.add_menu('espresso',format(7000,','))

class Shop:
    def __init__(self,menus,shop_name,address):
        self.shop_name = shop_name
        self.address = address
        self.menus = menus
    def show_shop_menus(self):
        print('언제나 최고를 추구합니다')
        self.menus.show_menus()
shop = Shop(menu,'Rising Sun','경기도 경성부')
print(shop.show_shop_menus())

class Cafe(Shop):
    def __init__(self, menu,shop_name,address,point_discount):
        super().__init__(menu,shop_name,address)
        self.point_discount = point_discount
        self.orders_count = 0
    def show_shop_menus(self):
        print('우리는 회원분들께 10% 할인해드립니다.')
        self.menus.show_menus()
    @property
    def count_menu(self):
        return len(self.menus.menus)
    def order(self):
        print('주문이 완료되었습니다.')
        self.orders_count += 1
    def get_order_count(self):
        return self.orders_count

cafe = Cafe(menu,'Rising Sun','경기도 경성부',point_discount=0.1)
print(cafe.order())
print(cafe.get_order_count())