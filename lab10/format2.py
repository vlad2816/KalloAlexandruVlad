auto = {
    'marca': 'Audi',
    'model': 'A4',
    'usi': 4
}

USER_TEMPLATE = 'Detin o masina marca {0}, model {1}, si are {2} usi '

print(USER_TEMPLATE.format(
    auto['marca'], auto['model'], auto['usi']))