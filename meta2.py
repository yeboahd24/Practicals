import inspect


class BranchMetaclass(type):
    def __new__(classitself, classname, baseclasses, attributes):
        newattributes = {}

        for attribute, value in attributes.items():
            if attribute.startswith("__"):
                newattributes[attribute] = value
            elif inspect.isfunction(value):
                newattributes["branch" + attribute.title()] = value
                for attribute, value in attributes.items():
                    if attribute.startswith("__"):
                        newattributes[attribute] = value
                    elif inspect.isfunction(value):
                        newattributes["branch" + attribute.title()] = value
                    else:
                        newattributes[attribute] = value
        return type.__new__(classitself, classname, baseclasses, newattributes)

    def buy_product(product, unit_price, quantity, statetax_rate, promotiontype):
        statetax_rate = statetax_rate
        initialprice = unit_price * quantity
        sales_price = initialprice + initialprice * statetax_rate
        return sales_price, product, promotiontype


class Brooklyn(metaclass=BranchMetaclass):
    product_id = 100902
    product_name = "Iphone X"
    product_category = "Electronics"
    unit_price = 700

    def maintenance_cost(self, product_type, quantity):
        self.product_type = product_type
        self.quantity = quantity
        cold_storage_cost = 100
        if product_type == "Electronics":
            maintenance_cost = self.quantity * 0.25 + cold_storage_cost
            return maintenance_cost
        else:
            return "We don't stock this product"


brooklyn = Brooklyn()
print(brooklyn.branchMaintenance_Cost("Electronics", 10))
