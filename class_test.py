class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"name:{self.name},age:{self.age}"


"""定义一个商品类，包含 商品名称 和 商品价格 两个属性，
实现商品类的对象描述方法和添加到购物车方法
定义一个购物车类，包含一个商品列表 属性，和 添加商品 及 显示所有商品 两个方法"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"name:{self.name},price:{self.price}"
    def cart_add(self,cart):
        cart.add_shop()
class shopping_cart:
    def __init__(self, product):
        self.product = product
        self.shopping_cart_items = []
    def __str__(self):
        return f"product:{self}"
    def add_shop(self):
        self.shopping_cart_items.append(self.product)
    def show_cart(self):
        #为什么不能直接打印
        # print(self.shopping_cart_items)
        for item in self.shopping_cart_items:
            print(item)

""" - 1.房子有户型，总面积和家具名称列表，新房子没有任何的家具。
    - 2.家具有名字和占地面积，其中 - 床：占4平米 - 衣柜：占2平米 - 餐桌：占1.5平米 - 
    - 3.将以上三件家具添加到房子中 - 
    - 4.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表"""
"""打印出的剩余面积是添加完最后一个家具剩余的，不是添加完所有家具剩余的"""
class House:
    def __init__(self, house_type, arer):
        self.house_type = house_type
        self.arer = arer
        self.house_furniture = []
    def __str__(self):
        return (f"house_type:{self.house_type}", f"area:{self.area}",
                f"house_furniture:{self.house_furniture}")
    def add_furniture(self,furniture):
        if self.arer > furniture.arer:
            self.house_furniture.append(furniture)
            #更新剩余面积
            self.residual_arer = self.arer - furniture.arer

            print(f"家具 {furniture.name}已经添加")
        else:
            print("房子空间不足，建议更换大房子")
    def house(self):
        print(f"您的房子{self.house_type}")
        for furn in self.house_furniture:
            print(f"您房子的家具{furn.name}")
        print(f"您房子的总面积{self.arer}，剩余面积{self.residual_arer}")


class Furniture:
    def __init__(self, name, arer):
        self.name = name
        self.arer = arer
    def __str__(self):
        return f"name:{self.name}", f"area:{self.arer}"

if __name__ == "__main__":
    # s1 = student('John', 20)
    # print(s1)
    # print((s1.name))
    # closes = Product("短袖",99)
    # cart = shopping_cart(closes)
    # closes.cart_add(cart)
    # cart.show_cart()
    villa = House("Villa", 400)
    bed = Furniture("Bed", 4)
    closet = Furniture("closet", 2)
    table = Furniture("table", 1.5)
    villa.add_furniture(bed)
    villa.add_furniture(closet)
    villa.add_furniture(table)
    villa.house()

