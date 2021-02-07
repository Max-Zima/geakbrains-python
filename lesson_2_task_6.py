product_list = []
num = 0
while input("Хотите добаваить продук? введите да/нет: ") == 'да':
    num += 1
    features = {}
    while input("Хотите добавить пармаетр? Введите да/нет: ") == 'да':
        feature_key = input("Название парамера: ")
        feature_value = input("Значене параметра: ")
        features[feature_key] = feature_value
    product_list.append(tuple([num, features]))
print(product_list)

analitic = {}
for el in product_list:
    for feature_key, feature_value in el[1].items():
        if feature_key in analitic:
            analitic[feature_key].append(feature_value)
        else:
            analitic[feature_key] = [feature_value]
print(analitic)