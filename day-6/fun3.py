def dis_price(price,rate):
    discount=price*(rate/100)
    final_price=price-discount
    return final_price
price_a=dis_price(10000,10) #a상품: 10000원 할인율: 10%
print(f"a상품은 {price_a} 입니다")
price_b=dis_price(50000,20) #b상품: 50000원 할인율: 20%
print(f"b상품은 {price_b} 입니다")