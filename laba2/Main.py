from goods.Cavlar import *
from goods.Stuffing import *
from goods.Fish import *
from FishShop import *
from enums.FishType import *

if __name__ == '__main__':
    shop = FishShop()

    karas = Fish("KARASIK", 4, 120, FishType.LIVE)
    okyn = Fish("OKYN", 2, 100, FishType.FRAZE)
    karas_okyn = Stuffing("karas+okyn", 6, 47, FishType.MIXED)
    okyn_som = Stuffing("okyn+som", 5, 40, FishType.MIXED)
    zamorska = Cavlar("IKRA ZAMORSKA9", 2, 20, FishType.RED)
    chorna = Cavlar("IKRA CHORNA9", 3, 76, FishType.BLACK)

    shop.goods = [karas, okyn, karas_okyn, okyn_som, zamorska, chorna]
    print("Full list:")
    shop.print_goods()

    shop.sort_by_weight()
    print("Sorted list")
    shop.print_goods()

    print("Found list by price")
    for good in shop.find_by_price(1, 2100):
        print(good)

    print("\n")

    shop.goods = shop.find_by_type(FishType.MIXED, FishType.RED, FishType.LIVE)
    print("Found list by enums")
    shop.print_goods()

