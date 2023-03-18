def box_price(height, length, width, t=1, price=25):
    raw_price = height * length * width * price
    if t == 2:
        return raw_price * 1.1
    if t == 3:
        return raw_price * 1.2
    return raw_price


print(box_price(1, 2, 3, t=3))
# print(box_price(t=2, width=3, height=1, length=2)) Mai buna este varianta declarata initial.
