# 2) Replace with "x" last char in each product_code_list element.

product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf",
    "weee"
]

for i, v in enumerate(product_code_list):  # Mai verifica aici!!
    product_code_list[i] = f"{v[:-1]}x"

print(product_code_list)
