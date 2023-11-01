import json
import os
import csv
inventar = ["пистолет 12/12"]
filename = 'D:\\С моего компа\\Project MPT\\Python\\gg\\save.json'

def save(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename,'w',encoding='utf-8') as file:
        json.dump(data,file,indent = 4, ensure_ascii=False)
      
def load(filename):
    with open(filename,'r',encoding='utf-8') as file:
        return json.load(file)
        

def vibor(newname):
    print("Кажется, комната напоминает спальню. У вас есть два выбора:\n1. Выйти из комнаты.\n2. Остаться в комнате и поспать.")
    vibr = input().capitalize()
    match(vibr):
        case "1":
            viboretaja(newname)
        case "2":
            print("Вы решили, что вас обязательно спасут и не стали даже пытаться что-то предпринять.\nВы легли в кроватку и уснули, больше не проснувшись.\nПлохая концовка #1")
            print()
            notclose = input()
            save(data, filename)
            exit()
        case "Чё":
            print("А ничё. Читай внимательнее. Умер нафиг.\nСекретная концовка #1")
            print()
            notclose = input()
            save(data, filename)
            exit()
        case "I":
            print(inventar)
            vibor(newname)
        case _:
            print("Вы не разобрались в выборе направления и свернулись калачиком и стали плакать.\nПлохая концовка #2")
            print()
            notclose = input()
            save(data, filename)
            exit()
def viboretaja(newname):
    print()
    print("Вы оказались на втором этаже.\nВы можете обследовать первый этаж, второй этаж, на котором вы сейчас находитесь или чердак.\n1. Исследовать первый этаж.\n2. Исследовать второй этаж.\n3. Исследовать чердак.")
    etaj = input().capitalize()
    match etaj:
        case "1":
            etaj1(newname)
        case "2":
            etaj2(newname)
        case "3":
            cherdak(newname)
        case "I":
            print(inventar)
            viboretaja(newname)
        case _:
            print("Пока вы стояли и долго думали куда идти, кто-то ударил вас по голове бейсбольной битой, от чего вы потеряли сознание и умерли.\nПлохая концовка # 3.")
            print()
            notclose = input()
            save(data, filename)
            exit()
def cherdak(newname):
    print()
    print("Вы на чердаке.\nВы можете осмотреть чердак. Выберете что осмтореть\n1. Осмотреть чердачное окно.\n2. Осмотреть шкаф.\n3. Осмотреть стол.\n4. Осмотреть сундук\n5. Вернуться на второй этаж.")
    osmotr = input().capitalize()
    match(osmotr):
        case "1":
            if "напильник" in inventar:
                print("Вы спилили решётку, открыли окно, прыгнули на улицу и бежали так, что пятки сверкали.\nВы выжили.\nХорошая концовка # 1.")
                print()
                notclose = input()
                save(data, filename)
                exit()
            else:
                print("Вы осмотрели чердачное окно.\nВы заметили на нём решётку.\nПоразмыслив немного, вы пришли к выводу, что решётку можно было бы спилить напильником.\nВы нашли один из возможных выходов, но его ещё нужно разблокировать.")
                cherdak(newname)
        case "2":
            print("Вы осмотрели шкаф, это было не лучшее ваше решение.\nИз шкафа на вас выпала куча булыжников, которые расплющили вас. Вы действительно идиот раз попались на такую тупую ловушку.\nПлохая концовка # 4.")
            print()
            notclose = input()
            save(data, filename)
            exit()
        case "3":
                if "ключ в виде скорпиона" in inventar and "напильник" in inventar:
                    print("Вы уже осмотрели это место. Здесь больше ничего нет.")
                    cherdak(newname)
                else:
                    print("На столе вы нашли ключ в виде скорпиона.\nПредмет был добавлен в ваш инвентарь.")
                    inventar.append("ключ в виде скорпиона")
                    data = load(filename)
                    data[newname]["inventar"] = inventar
                    save(data,filename)
                    print(inventar)
                    cherdak(newname)
        case "4":
            if "ключ от сундука" in inventar:
                print("Вы подходите к деревянному сундуку и пытаетесь открыть его. Он закрыт, вам нужен ключ.")
                print("Вы открыли сундук и внутри нашли фонарик. Должен пригодиться.\nПредмет добавлен в ваш инвентарь")
                inventar.remove("ключ от сундука")
                inventar.append("фонарик")
                data = load(filename)
                data[newname]["inventar"] = inventar
                save(data,filename)
                print(inventar)
                cherdak(newname)
            elif "фонарик" in inventar:
                print("Вы уже осмотрели это место. Здесь больше ничего нет.")
                cherdak(newname)
            else:
                print("Вы подходите к деревянному сундуку и пытаетесь открыть его. Он закрыт, вам нужен ключ.")
                print("У вас пока что нет ключа. Продолжайте поиски")
                cherdak(newname)
        case "5":
            if "напильник" not in inventar:
                print("Вы решили вернуться на второй этаж.")
                viboretaja(newname)
            else:
                print("Вы не собираетесь спускаться на второй этаж, когда вы так близки к побегу.")
                cherdak(newname)
        case "I":
            print(inventar)
            cherdak(newname)
        case _:
            print("Дружище, выбирай из пяти цифр, пожалуйста.")
            cherdak(newname)

def etaj2(newname):
    print()
    print("Вы на втором этаже.\nУ вас есть выбор, что осмотреть.\n1. Ванная\n2. Игровая комната.\n3. Вернуться к выбору этажа.")
    viborkomn = input().capitalize()
    match(viborkomn):
        case "1":
            if "аптечка" not in inventar:
                print("Вы вошли в ванную.\nВы заметили аптечку, валяющуюся на полу и решили взять её с собой. Лишней не будет.\nАптечка добавлена в ваш инвентарь.")
                inventar.append("аптечка")
                data = load(filename)
                data[newname]["inventar"] = inventar
                save(data,filename)
                print(inventar)
                etaj2(newname)
            else:
                print("Вы уже здесь были. Здесь больше нечего искать.")
                etaj2(newname)
        case "2":
            print("Вы вошли в игровую комнату и заметили PlayStation 5 и топовый ПК.\nВы решили, что это единственная ваша возможность нормально поиграть в игры с вашим то слабеньким компудахтером дома.\nВы сели за плойку и настолько увлеклись игрой, что не заметили, как к вам подкрался маньяк и порубил вас на кусочки.\nПлохая концовка # 5.")
            print()
            notclose = input()
            save(data, filename)
            exit()
        case "3":
            viboretaja(newname)
        case "I":
            print(inventar)
            etaj2(newname)
        case _:
            print("Написано же только три цифры! Вчитайся, чёрт возьми!")
            etaj2(newname)
    
def etaj1(newname):
    print()
    print("Вы на первом этаже.\nНа первом этаже вы видите проход на кухню, дверь наружу, дверь в подвал\nЧто ж, выбирайте.\n1. Кухня\n2. Дверь наружу\n3. Дверь в подвал\n4. Вернуться на второй этаж")
    viborputi = input().capitalize()
    match(viborputi):
        case "1":
            if "ключ от сундука" in inventar or "фонарик" in inventar:
                print("Вы уже осмотрели кухню. Вам больше нечего там искать.")
                etaj1(newname)
            else:
                kuhnya(newname)
        case "2":
            if "ключ от выхода" not in inventar:
                print("Вы решили осмотреть дверь наружу. Она заперта. Неудивительно.\nПродолжайте поиск предметов, ключ должен быть где-то в доме.")
                etaj1(newname)
            else:
                print("Вы открыли дверь на улицу и сбежали.\nВы выжили.\nХорошая концовка # 2.")
                print()
                notclose = input()
                save(data, filename)
                exit()
        case "3":
            if "ключ от выхода" not in inventar:
                print("Вы видите дверь в подвал и открываете её. Она открыта. Удивительно.\nНо в подвале слишком темно, вам нужен фонарик.")
                if "фонарик" in inventar:
                    podval(newname)
                else:
                    print("Ищите фонарик, вы же не хотите упасть и свернуть шею, да?(\"да\" или \"нет, хочу\")")
                    sheya = input().capitalize()
                    match(sheya):
                        case "Да":
                            print("Вот и славно. Ищи фонарик, братишка.")
                            etaj1(newname)
                        case "Нет, хочу":
                            print("Желание игрока закон. Вы ступаете в тёмный подвал, спотыкаетесь и падаете кувырком по лестнице и в итоге ломаете шею.\nСекретная концовка # 2.")
                            print()
                            notclose = input()
                            save(data, filename)
                            exit()
                        case _:
                            print("Я приму это как желание похрустеть шеей. Вы ступаете в тёмный подвал, спотыкаетесь и падаете кувырком по лестнице и в итоге ломаете шею. Не ошибайтесь в следующий раз.\nСекретная концовка # 3.")
                            print()
                            notclose = input()
                            save(data, filename)
                            exit()
            else:
                print("Вы уже нашли то, что искали. Вам туда больше не нужно.")
                etaj1(newname)
        case "4":
            if "ключ от выхода" not in inventar:
                viboretaja(newname)
            else:
                print("Вы не собираетесь идти на другие этажи, когда у вас есть всё для выхода.\nПросто откройте дверь.")
                etaj1(newname)
        case "I":
            print(inventar)
            etaj1(newname)
        case _:
            print("Я даже уже объяснять не буду что ты делаешь не так. Ты и сам знаешь, чел.")
            etaj1(newname)

def kuhnya(newname):
    print()
    print("Вы на кухне.\nВы видите стол и ящик внутри стола.\nЧто выберите?\n1. Осмотреть стол.\n2. Осмотреть ящичек\n3. Вернуться в коридор первого этажа. ")
    vibordeistv = input().capitalize()
    match(vibordeistv):
        case "1":
            if "кухонный нож" not in inventar:
                print("Вы увидели на столе кухонный нож и взяли его. Предмет добавлен в ваш инвентарь.")
                inventar.append("кухонный нож")
                data = load(filename)
                data[newname]["inventar"] = inventar
                save(data,filename)
                print(inventar)
                kuhnya(newname)
            else:
                print("Вы уже осмотрели это место. Здесь больше ничего нет.")
                kuhnya(newname)
        case "2":
            print("Вы решаете осмотреть ящичек, который находится внутри стола. Он выглядит довольно хлипеньким. Вы дёргаете его, но он не поддаётся.\nЗдесь мог бы пригодится кухонный нож для вскрытия.")
            if "кухонный нож" in inventar:
                print("Вы использовали кухонный нож на ящичке и приложили усилия. Ящичек открылся, но вы порезались.\nВам нужно что-то, что остановило бы кровотечение и срочно. Аптечка бы помогла.")
                if "аптечка" in inventar:
                    print("Вы открыли аптечку, достали бинты и дезинфицирующее средство и обработали рану. Теперь у вас есть доступ к открытому ящичку.")
                    print("Вы осмотрели ящичек и нашли ключ от сундука. Предмет добавлен в ваш инвентарь.")
                    inventar.remove("кухонный нож")
                    inventar.remove("аптечка")
                    inventar.append("ключ от сундука")
                    data = load(filename)
                    data[newname]["inventar"] = inventar
                    save(data,filename)
                    print(inventar)
                    print("Вы решаете вернуться в коридор первого этажа.")
                    etaj1(newname)
                else:
                    print("Вы не смогли остановить кровотечение и истекли кровью насмерть. В следующий раз ищите аптечку.\nПлохая концовка # 6.")
                    print()
                    notclose = input()
                    save(data, filename)
                    exit()
            else:
                print("Вы ещё не нашли кухонный нож.")
                kuhnya(newname)
        case "3":
            etaj1(newname)
        case "I":
            print(inventar)
            etaj1(newname)
        case _:
            print("(-_-)")
            etaj1(newname)

def podval(newname):
    print()
    print("Вы в подвале и фонарик освещает вам местность.\nВы видите перед собой всякое барахло, но также можете заметить потайной ход за грудой хлама.\n1. Отодвинуть хлам и посмотреть на потайную дверь.\n2. Порыться в хламе.\n3. Ну его нафиг.\n4. Выйти из подвала.")
    vibrat = input().capitalize()
    match(vibrat):
        case "1":
            print()
            print("Вы видите перед вами дверь\nОсмотрев замок и знак на двери, вы понимаете что для неё нужен ключ со скорпионом.")
            if "ключ в виде скорпиона" in inventar and "напильник" not in inventar:
                secretroom(newname)
            elif "напильник" in inventar:
                print("Вы не считаете нужным открывать дверь, так как у вас доступен один из выходов побега.")
                cherdak(newname)
            else:
                print("Вы ещё не нашли этот ключ. Осмотрите дом внимательнее.")
                podval(newname)
        case "2":
            if "напильник" not in inventar:
                print("Вы порылись в хламе и нашли напильник.\nПредмет добавлен в ваш инвентарь.")
                inventar.append("напильник")
                data = load(filename)
                data[newname]["inventar"] = inventar
                save(data,filename)
                print(inventar)
                podval(newname)
            else:
                print("Вы уже нашли, что искали. Здесь больше нечего искать.")
                podval(newname)
        case "3":
            print("Вы решили, что вам это нафиг не надо, поэтому развернулись и собирались уходить, но наступили на ловушку и на вас упала наковальня(не спрашивай откуда она там, маньяк дофига крутой).\Плохая концовка # 7.")
            print()
            notclose = input()
            save(data, filename)
            exit()
        case "4":
            etaj1(newname)
        case "I":
            print(inventar)
            podval(newname)
        case _:
            print("Я отказываюсь что-либо писать")
            podval(newname)

def secretroom(newname):
    print("Вы открыли дверь и вошли в комнату.\nПеред вами тир и три мишени. Здесь вам и пригодится пистолет.\n1. Стрелять в мишени.\n2. Выйти из комнаты ")
    strel = input().capitalize()
    match(strel):
        case "1":
            print("Вы стреляете по мишеням и после попадания по всем трём вам открывается секретный комод с ключом от входа.\nПредмет добавлен в ваш инвентарь.")
            inventar.remove("пистолет 12/12")
            inventar.insert(0, "пистолет 9/12")
            inventar.append("ключ от выхода")
            data = load(filename)
            data["inventar"] = inventar
            save(data,filename)
            print(inventar)
            etaj1(newname)
        case "2":
            podval(newname)
        case "I":
            print(inventar)
            secretroom(newname)
        case _:
            print("Ну ты и сам понял, братиш.")
            secretroom(newname)

print("Вы проснулись в одной из комнат заброшенного особняка.\nВы не помните как оказались здесь, но ваша главная задача - сбежать отсюда и не умереть.\nВ вашем инвентаре есть полностью заряженный на 12 патронов пистолет.")
print("Чтобы посмотреть ваш инвентарь, нажмите i в любой момент.")
if not os.path.exists(filename):
  namepers = input("Введите имя вашего героя: ")
  print(f"Твоя история начинается сейчас, {namepers}")
  newname= namepers.capitalize()
  data = {
    newname : {
      "name" : newname,
      "inventar" : inventar
    }
  }
  save(data, filename)
  vibor(newname)
else:
  data = load(filename)
  igrok = list(data.keys())[-1]
  while(True):
    print("Все игроки:")
    for clikuha in data:
      print(clikuha)
    
    print("Загрузить данные", igrok,"? \nДа или Нет")
    namevibor = input().capitalize()
    match (namevibor):
      case "Да":
        newname = igrok
        print("Данные загруженны")
        inventar = data[newname]["inventar"]
        viboretaja(newname)
      case "Нет":
          print("Предыдущее сохранение стёрто. Началась новая игра")
          namepers = input("Введите имя вашего героя: ")
          print(f"Твоя история начинается сейчас, {namepers}")
          newname = namepers.capitalize()     
          newdata = {
          newname:  {
                "name": newname,
                "inventar" : inventar
            }
          }    
          data.update(newdata)
          save(data, filename)
          vibor(newname)      