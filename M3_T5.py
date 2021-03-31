models = ['Volkswagen - Golf', 'Renault - Clio', 'Volkswagen - Polo',
          'Ford - Fiesta', 'Nissan - Qashqai', 'Peugeot - 208', 'VW - Tiguan', 'Skoda - Octavia',
          'Toyota - Yaris', 'Opel - Corsa', 'Dacia - Sandero', 'Renault - Captur', 'Citroen - C3',
          'Peugeot - 3008', 'Ford - Focus', 'Fiat - 500', 'Dacia - Duster', 'Peugeot - 2008',
          'Skoda - Fabia', 'Fiat - Panda', 'Opel - Astra', 'VW - Passat', 'Mercedes-Benz - A-Class',
          'Peugeot - 308', 'Ford - Kuga']

sales2018 = ['445,754', '336,268', '299,920', '270,738', '233,026', '230,049', '224,788',
             '223,352', '217,642', '217,036', '216,306', '214,720', '210,082', '204,197', '196,583',
             '191,205', '182,100', '180,204', '172,511', '168,697', '160,275', '157,986', '156,020',
             '155,925', '154,125']

sales2017 = ['483,105', '327,395', '272,061', '254,539', '247,939', '244,615', '234,916',
             '230,116', '199,182', '232,738', '196,067', '212,768', '207,299', '166,784', '214,661',
             '189,928', 'NA', '180,868', '180,136', '187,322', '217,813', '184,123', 'NA', 'NA', 'NA']

sales2016 = ['492,952', '315,115', '308,561', '300,528', '234,340', '249,047', '180,198',
             '230,255', '193,969', '264,844', '170,300', '217,105', '134,560', 'NA', '214,435',
             '183,730', 'NA', 'NA', '177,301', '191,617', '253,483', '208,575', 'NA', '195,653', 'NA']

model = [i.split(' - ') for i in models]
brands = [i[0] for i in model]
models = [i[1] for i in model]

sales2018 = [int(s18.replace(",", "").replace("NA", "0")) for s18 in sales2018]
sales2017 = [int(s17.replace(",", "").replace("NA", "0")) for s17 in sales2017]
sales2016 = [int(s16.replace(",", "").replace("NA", "0")) for s16 in sales2016]

cars = {}
for brand, model, s16, s17, s18 in zip(brands, models, sales2016, sales2017, sales2018):
    if not brand in cars:
        cars[brand] = {
            model: {'sales': {'2016': s16, '2017': s17, '2018': s18}}}
    else:
        cars[brand].update(
            {model: {'sales': {'2016': s16, '2017': s17, '2018': s18}}})

answer1 = max([[k1, v2['2017']] for v in cars.values() for k1, v1 in v.items()
               for v2 in v1.values()], key=lambda by_sales: by_sales[1])[0]
# wcześniejszy pomysł
#mod17 = [k1 for v in cars.values() for k1 in v.keys()]
#sel17 = [v2['2017'] for v in cars.values() for v1 in v.values() for v2 in v1.values()]
#answer1 = mod17[sel17.index(max(sel17))]

brands2018 = [[k, v2['2018']] for k, v in cars.items() for v1 in v.values()
              for v2 in v1.values()]
brands18 = {}
for p, s in brands2018:
    if not p in brands18:
        brands18[p] = [s]
    else:
        brands18[p].append(s)  # lub extend([s])
brand18 = [p for p in brands18.keys()]
sel18 = [sum(s) for s in brands18.values()]
answer2 = brand18[sel18.index(max(sel18))]

analize = [[k1, v2['2016'], v2['2017'], v2['2018']]
           for v in cars.values() for k1, v1 in v.items() for v2 in v1.values()]
answer3 = [a for a, b, c, d in analize if b == 0 and c != 0]

least = [b+c+d for a, b, c, d in analize]
answer4 = analize[least.index(min(least))][0]

ford17 = [v2['2017'] for v1 in cars['Ford'].values() for v2 in v1.values()]
ford18 = [v2['2018'] for v1 in cars['Ford'].values() for v2 in v1.values()]
answer5 = str(int((sum(ford18)/sum(ford17)-1)*100))+'%'
