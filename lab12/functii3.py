def box_price(height, length, width, t=1, price=25, **kwargs):
    """Calculate the box price.
    kwargs:
        -cq2: coefficient for type 2
        -cq3: coefficient for type 3
    """
    print(kwargs)
    raw_price = height * length * width * price
    if t == 2:
        return raw_price * kwargs.get('cq2', 1.1)
    if t == 3:
        return raw_price * kwargs.get('cq3', 1.1)
    return raw_price


def demo(**kwargs):
    print(kwargs)


# demo(vlad=24, new='test', x=3)

print(box_price(1, 2, 3, t=3, cq2=2, cq3=3))
