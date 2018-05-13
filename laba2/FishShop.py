class FishShop:
    goods = []

    def __init__(self):
        pass

    def find_by_price(self, low, high):
        found_goods_by_price = []

        for good in self.goods:
            if (good.price > low) & (good.price < high):
                found_goods_by_price.append(good)

        return found_goods_by_price

    def find_by_type(self, fish_type, cavlar_type, stuffing_type):
        found_goods = []

        for good in self.goods:
            if (good.fishType == fish_type) | (good.fishType == cavlar_type) | (good.fishType == stuffing_type):
                found_goods.append(good)

        return found_goods

    def sort_by_weight(self):
        self.goods.sort(key=lambda Good: Good.weight)

    def add_good(self, good):
        self.goods += good

    def print_goods(self):
        for good in self.goods:
            print(good)
        print("\n")
