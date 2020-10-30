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





class Sedan(Transport):
    def __init__(self, transmission, *args):
        super().__init__(*args)
        self.transmission = transmission

    def inform (self):
        print('Cедан:',
              self.model,
              '\nМасса -', self.weight, 'кг.',
              '\nРазгон от 0 до 100 -', self.accelerationFrom0To100,'секунд.',
              '\nМощность двигателя -', self.enginePower,'л.с.',
              '\nЦвет кузова -', self.color,
              '\nТип топлива -', self.fuelType,
              '\nКоробка передач -', self.transmission,'\n')


class ExampleGenerator(Sedan):
    modelList = ['Mercedes', 'Audi    ', 'BMW     ', 'Opel    ']
    transmissionList = ['АКПП', 'МКПП']
    colorList = ['Крассный', 'Белый', 'Синий']
    fuelTypeList = ['Бензин', 'ДТ']
    autoSedanList = []
    autoCoupeList = []
    autoSuvList = []

    count = 0
    for i in range(80):
        acceleration = round(random.uniform(5, 9), 2)
        if acceleration > 7:
            engPower = random.randint(125, 200)
        else:
            engPower = random.randint(200, 270)

        autoSedanList.append(Sedan(random.choice(transmissionList),
                                             count,
                                             random.choice(modelList),
                                             random.randint(1700, 2600),
                                             acceleration,engPower,
                                             random.choice(colorList),
                                             random.choice(fuelTypeList)))
        count = count + 1

    lis = []
    for j in autoSedanList:
        if j.weight < 2000:
            lis.append(j)


    for k in lis:
        print(k.__dict__)

    print(autoSedanList[1].inform())

class Choose(ExampleGenerator):

    bodyChoice = input('Здравствуйте! Вы решили выбрать автомобиль. Отлично, какой кузов вы рассмотриваете? '
          'Если это седан нажмите 1, если это купе нажмите 2, если вы хотите выбрать внедорожник нажмете 3: ')
    if bodyChoice == '1':
        sedanList = []
        selectionParameter = input('По какому параметру вы хотите выбрать седан? Выберите из списка: '
                                   'Марка авто - 1, Цвет - 2, Тип топлива - 3, Коробка передач - 4, Мощность двигателя - 5,'
                                   'Разгон от 0 до 100 км/ч - 6: ')

        if selectionParameter == '1':
            modelStr = input('Какую марку авто вы рассматриваете? Выберите из списка. Mercedes - 1, Audi - 2, BMW - 3, Opel - 4: ')

            if modelStr == '1':
                for i in ExampleGenerator.autoSedanList:
                    if i.model == 'Mercedes':
                        sedanList.append(i)
                for k in sedanList:
                    print(k.__dict__)
                transmissionStr = input('Mercedes - это отличный выбор! Давайте определися с какой коробкой передач вы хотите машину. АКПП - 1, МКПП - 2: ')
                transmissionList = []
                if transmissionStr == '1':
                    for i in sedanList:
                        if i.transmission == 'АКПП':
                            transmissionList.append(i)
                    for k in transmissionList:
                        print(k.__dict__)
                    fuelTypeStr = input('Автоматическая коробка передач для тех кто не хочет сильно заморачиватся, осталось определится с типом топлива.'
                                   '\nБензин - 1, Дизельное топливо - 2: ')
                    fuelTypeList = []
                    if fuelTypeStr == '1':
                        for i in transmissionList:
                            if i.fuelType == 'Бензин':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                    elif fuelTypeStr == '2':
                        for i in transmissionList:
                            if i.fuelType == 'ДТ':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                elif transmissionStr == '2':
                    for i in sedanList:
                        if i.transmission == 'МКПП':
                            transmissionList.append(i)

                    for k in transmissionList:
                        print(k.__dict__)
                    fuelTypeStr = input(
                        'Автоматическая коробка передач для тех кто не хочет сильно заморачиватся, осталось определится с типом топлива.'
                        '\nБензин - 1, Дизельное топливо - 2: ')
                    fuelTypeList = []
                    if fuelTypeStr == '1':
                        for i in transmissionList:
                            if i.fuelType == 'Бензин':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                    elif fuelTypeStr == '2':
                        for i in transmissionList:
                            if i.fuelType == 'ДТ':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()

            elif modelStr == '2':
                for i in ExampleGenerator.autoSedanList:
                    if i.model == 'Audi    ':
                        sedanList.append(i)
                for k in sedanList:
                    print(k.__dict__)

                transmissionStr = input('Audi - это надежная машина! Давайте определися с какой коробкой передач вы хотите машину. АКПП - 1, МКПП - 2: ')
                transmissionList = []
                if transmissionStr == '1':
                    for i in sedanList:
                        if i.transmission == 'АКПП':
                            transmissionList.append(i)
                    for k in transmissionList:
                        print(k.__dict__)
                    fuelTypeStr = input(
                        'Автоматическая коробка передач для тех кто не хочет сильно заморачиватся, осталось определится с типом топлива.'
                        '\nБензин - 1, Дизельное топливо - 2: ')
                    fuelTypeList = []
                    if fuelTypeStr == '1':
                        for i in transmissionList:
                            if i.fuelType == 'Бензин':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                    elif fuelTypeStr == '2':
                        for i in transmissionList:
                            if i.fuelType == 'ДТ':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                elif transmissionStr == '2':
                    for i in sedanList:
                        if i.transmission == 'МКПП':
                            transmissionList.append(i)

                    for k in transmissionList:
                        print(k.__dict__)
                    fuelTypeStr = input(
                        'Автоматическая коробка передач для тех кто не хочет сильно заморачиватся, осталось определится с типом топлива.'
                        '\nБензин - 1, Дизельное топливо - 2: ')
                    fuelTypeList = []
                    if fuelTypeStr == '1':
                        for i in transmissionList:
                            if i.fuelType == 'Бензин':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                    elif fuelTypeStr == '2':
                        for i in transmissionList:
                            if i.fuelType == 'ДТ':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()

            elif modelStr == '3':
                for i in ExampleGenerator.autoSedanList:
                    if i.model == 'BMW     ':
                        sedanList.append(i)
                for k in sedanList:
                    print(k.__dict__)
                transmissionStr = input('BMW - выбор для тех кто всегда упевает! Давайте определися с какой коробкой передач вы хотите машину. АКПП - 1, МКПП - 2: ')
                transmissionList = []
                if transmissionStr == '1':
                    for i in sedanList:
                        if i.transmission == 'АКПП':
                            transmissionList.append(i)
                    for k in transmissionList:
                        print(k.__dict__)
                    fuelTypeStr = input(
                        'Автоматическая коробка передач для тех кто не хочет сильно заморачиватся, осталось определится с типом топлива.'
                        '\nБензин - 1, Дизельное топливо - 2: ')
                    fuelTypeList = []
                    if fuelTypeStr == '1':
                        for i in transmissionList:
                            if i.fuelType == 'Бензин':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                    elif fuelTypeStr == '2':
                        for i in transmissionList:
                            if i.fuelType == 'ДТ':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                elif transmissionStr == '2':
                    for i in sedanList:
                        if i.transmission == 'МКПП':
                            transmissionList.append(i)

                    for k in transmissionList:
                        print(k.__dict__)
                    fuelTypeStr = input(
                        'Автоматическая коробка передач для тех кто не хочет сильно заморачиватся, осталось определится с типом топлива.'
                        '\nБензин - 1, Дизельное топливо - 2: ')
                    fuelTypeList = []
                    if fuelTypeStr == '1':
                        for i in transmissionList:
                            if i.fuelType == 'Бензин':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                    elif fuelTypeStr == '2':
                        for i in transmissionList:
                            if i.fuelType == 'ДТ':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()

            elif modelStr == '4':
                for i in ExampleGenerator.autoSedanList:
                    if i.model == 'Opel    ':
                        sedanList.append(i)
                for k in sedanList:
                    print(k.__dict__)
                transmissionStr = input('Opel - это просто машина! Давайте определися с какой коробкой передач вы хотите машину. АКПП - 1, МКПП - 2: ')
                transmissionList = []
                if transmissionStr == '1':
                    for i in sedanList:
                        if i.transmission == 'АКПП':
                            transmissionList.append(i)
                    for k in transmissionList:
                        print(k.__dict__)
                    fuelTypeStr = input(
                        'Автоматическая коробка передач для тех кто не хочет сильно заморачиватся, осталось определится с типом топлива.'
                        '\nБензин - 1, Дизельное топливо - 2: ')
                    fuelTypeList = []
                    if fuelTypeStr == '1':
                        for i in transmissionList:
                            if i.fuelType == 'Бензин':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                    elif fuelTypeStr == '2':
                        for i in transmissionList:
                            if i.fuelType == 'ДТ':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                elif transmissionStr == '2':
                    for i in sedanList:
                        if i.transmission == 'МКПП':
                            transmissionList.append(i)

                    for k in transmissionList:
                        print(k.__dict__)
                    fuelTypeStr = input(
                        'Автоматическая коробка передач для тех кто не хочет сильно заморачиватся, осталось определится с типом топлива.'
                        '\nБензин - 1, Дизельное топливо - 2: ')
                    fuelTypeList = []
                    if fuelTypeStr == '1':
                        for i in transmissionList:
                            if i.fuelType == 'Бензин':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()
                    elif fuelTypeStr == '2':
                        for i in transmissionList:
                            if i.fuelType == 'ДТ':
                                fuelTypeList.append(i)
                        print('Теперь вы можете ознакомиться со списком машин, которые могут вам подойти: \n')
                        for k in fuelTypeList:
                            k.inform()



        elif selectionParameter == '2':
            modelColor = input('Какой цвет авто вы рассматриваете? Выберите из списка. Красный - 1, Белый - 2, Синий - 3: ')
        elif selectionParameter == '3':
            modelColor = input('Какой тип топлива в авто вы рассматриваете? Выберите из списка. Бензин - 1, Дизельное топливо - 2: ')
        elif selectionParameter == '4':
            modelColor = input('Авто с какой коробкой передач вы рассматриваете? Выберите из списка. АКПП - 1, МКПП - 2: ')

        print()