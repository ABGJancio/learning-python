models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

model = [i.split(' - ') for i in models]

brands = []
for i in model:
    brands.append(i[0])

models = []
for i in model:
    models.append(i[1])

sales2018 = [s18.replace(",","") for s18 in sales2018]
sales2018 = [s18.replace("NA","0") for s18 in sales2018]
sales2018 = [int(s18) for s18 in sales2018]

sales2017 = [s17.replace(",","") for s17 in sales2017]
sales2017 = [s17.replace("NA","0") for s17 in sales2017]
sales2017 = [int(s17) for s17 in sales2017]

sales2016 = [s16.replace(",","") for s16 in sales2016]
sales2016 = [s16.replace("NA","0") for s16 in sales2016]
sales2016 = [int(s16) for s16 in sales2016]

d = list(zip(brands, models, sales2016, sales2017, sales2018))

cars = {}
for i in d:
    if not i[0] in cars:
        cars[i[0]] = {i[1]: {'sales': {'2016': i[2], '2017': i[3], '2018': i[4]}}}
    else:
        cars[i[0]].update({i[1]: {'sales': {'2016': i[2], '2017': i[3], '2018': i[4]}}})

best2017 = []
for k in cars.keys():
    for k1 in cars[k].keys():
        for k2 in cars[k][k1].keys():
            best2017.append([k1, cars[k][k1][k2]['2017']])
b17 = [b for a, b in best2017]
i17 = b17.index(max(b17))
bm17 = best2017[i17][0]

best2018 = []
for k in cars.keys():
    for k1 in cars[k].keys():
        for k2 in cars[k][k1].keys():
            best2018.append([k, cars[k][k1][k2]['2018']])
b18 = [b for a, b in best2018]
i18 = b18.index(max(b18))
bp18 = best2018[i18][0]

analize = []
for k in cars.keys():
    for k1 in cars[k].keys():
        for k2 in cars[k][k1].keys():
            analize.append([k1, cars[k][k1][k2]['2016'], cars[k][k1][k2]['2017']])
dif = [a for a, b, c in analize if b == 0 and c != 0]

least_one = []
for k in cars.keys():
    for k1 in cars[k].keys():
        for k2 in cars[k][k1].keys():
            least_one.append([k1, cars[k][k1][k2]['2016'], cars[k][k1][k2]['2017'], cars[k][k1][k2]['2018']])
least = [a+b+c for i, a, b, c in least_one]
l = least.index(min(least))
lm = least_one[l][0]

Ford17 = []
Ford18 = []
k = 'Ford'
for k1 in cars[k].keys():
    for k2 in cars[k][k1].keys():
        Ford17.append(cars[k][k1][k2]['2017'])
        Ford18.append(cars[k][k1][k2]['2018'])
up = str(int((sum(Ford18)/sum(Ford17)-1)*100))+'%'

answer1 = bm17 # wskaż nazwę modelu jako string
answer2 = bp18 # wskaż producenta jako string
answer3 = dif # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = lm # wskaż nazwę modelu jako string
answer5 = up # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

