shopping = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}
print('\nLista zakupów')
q = []
for shop, prod_list in shopping.items():
    shop = shop.capitalize()
    prod_list = [prod.capitalize() for prod in prod_list]