shopping = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}
print('\nLista zakupów')
q = []
for shop, prod_list in shopping.items():
    shop = shop.capitalize()
    prod_list = [prod.capitalize() for prod in prod_list]
    print('Idę do', shop, end = ', ')
    print('kupuję tu następujące rzeczy:', prod_list, end = '.\n')
print('W sumie kupuję', sum(q), 'produktów.\n')