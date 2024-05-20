
def discounted(price, discount, max_discount = 20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs (max_discount)
    if max_discount >= 100:
        raise ValueError ("Максимальная скидка не должна быть более 100")
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price*discount/100)
    return price_with_discount

print (discounted (100,5, max_discount=133))

#product = {
 #   "name" : "Iphone",
 #   "size" : "big",
 #   "amount" : 2,
 #   "price" : 252318.97,
#    "discount" : 33
#} 

#print (discounted(product["price"], product["discount"])) 
#product ["with_discount"] = discounted(product["price"], product["discount"])
#print (product)