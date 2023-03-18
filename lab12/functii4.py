def box_price(height, length, width, type=1, p=25, **kwargs):
    """Calculate the box price.
    kwargs:
        -cq2: coefficient for type 2
        -cq3: coefficient for type 3
    """
    print(kwargs)
    raw_price = height * length * width * p
    if type == 2:
        return raw_price * kwargs.get('cq2', 1.1)
    if type == 3:
        return raw_price * kwargs.get('cq3', 1.1)
    return raw_price


def demo(**kwargs):
    print(kwargs)


boxes = [
    {
        "height": 2,
        "length": 3,
        "width": 4
    },
    {
        "height": 2,
        "length": 3,
        "width": 4,
        "type": 2
    },
    {
        "height": 2,
        "length": 3,
        "width": 4,
        "type": 3,
        "p": 23
    }
]


for box in boxes:
    demo(**box)

for box in boxes:
    print(f'Pret cutie: {box_price(**box)}')
