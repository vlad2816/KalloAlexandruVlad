# Group product codes from product_code_list in a dictionary by last char
product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf",
    "weee"
]

x = {}

for i in product_code_list:
    if i[-1:] not in x:
        x[i[-1:]] = [i]
    else:
        x[i[-1:]].append(i)
print(x)
