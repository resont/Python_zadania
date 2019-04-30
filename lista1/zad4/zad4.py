import Smartphones, pickle

smartphones = [
    Smartphones.Smartphone('Samsung', 'S10', 4500),
    Smartphones.Smartphone('Iphone', 'X', 9999999),
    Smartphones.Smartphone('OnePlus', '5T', 2000)]

for x in smartphones:
    print(x)

pickle.dump(smartphones, open('phones.dat','wb'))

smarthphones2 = pickle.load(open('phones.dat','rb'))

for x in smarthphones2:
    print(x)