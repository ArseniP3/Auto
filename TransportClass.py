import random
class Transport:
    def __init__(self, id, model, weight, accelerationFrom0To100, enginePower, color, fuelType):
        self.id = id
        self.model = model
        self.weight = weight
        self.accelerationFrom0To100 =accelerationFrom0To100
        self.enginePower = enginePower
        self.color = color
        self.fuelType = fuelType

    modelList = ['Mercedes', 'Audi    ', 'BMW     ','Opel    ']
    transmissionList = ['АКПП','МКПП']
    colorList = ['Крассный','Белый','Синий']
    fuelTypeList = ['Бензин', 'ДТ']
    enginePowerList = [3.5, 3.2, 3.0, 2.8, 2.5, 2.1, 2.0, 1.8]
    autoSedanList = []
    autoCoupeList = []
    autoSuvList = []



class Sedan(Transport):
    def __init__(self, transmission, *args):
        super().__init__(*args)
        self.transmission = transmission

    def inform (self):
        print('Вы выбрали отличный седан:',
              self.model,
              '\nМасса -', self.weight, 'кг.',
              '\nРазгон от 0 до 100 -', self.accelerationFrom0To100,'секунд.',
              '\nМощность двигателя -', self.enginePower,'л.с.',
              '\nЦвет кузова -', self.color,
              '\nТип топлива -', self.fuelType,
              '\nКоробка передач -', self.transmission)


count = 0
for i in range (100):

    x = round(random.uniform(5,9),2)
    if x > 7:
        y = random.randint(125, 200)
    else:
        y = random.randint(200, 270)

    Transport.autoSedanList.append(Sedan(random.choice(Transport.transmissionList),
                                    count,
                                    random.choice(Transport.modelList),
                                    random.randint(1700,2600),
                                    x,
                                    y,
                                    random.choice(Transport.colorList),
                                    random.choice(Transport.fuelTypeList)))
    count = count+1

for j in Transport.autoSedanList:
    print(j.__dict__)

