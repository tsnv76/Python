class Sklad:
    def __init__(self, lists):
        self.sk_dic = dict(lists)

    def my_dict(self):
        return self.sk_dic

    def put_in_sklad(self, name, num):
        self.sk_dic[name] += int(num)
        return self.sk_dic

    def take_from_sklad(self, name, num):
        if self.sk_dic[name] >= num:
            self.sk_dic[name] -= num
        else:
            print(f'На складе не хватает {num - self.sk_dic[name]} {name}ов. Выдано {self.sk_dic[name]}')
            self.sk_dic[name] = 0
        return self.sk_dic


class OrgTeh:
    def __init__(self, name, _list):
        self.name = name
        self.sector_dic = dict(_list)

    def __str__(self):
        return f'Оргтехника в продразделении  {self.name} - {self.sector_dic}'


class Printer(OrgTeh):
    def __init__(self, num):
        self.name = 'Принтер'
        self.num = num

    def my_dict(self):
        self.pr_dic = {}
        self.pr_dic[self.name] = self.num
        return self.pr_dic


class Scaner(OrgTeh):
    def __init__(self, num):
        self.name = 'Сканер'
        self.num = num

    def my_dict(self):
        self.sc_dic = {}
        self.sc_dic[self.name] = self.num
        return self.sc_dic


class Xerox(OrgTeh):
    def __init__(self, num):
        self.name = 'Ксерокс'
        self.num = num

    def my_dict(self):
        self.xr_dic = {}
        self.xr_dic[self.name] = self.num
        return self.xr_dic


pr = Printer(20)
sc = Scaner(30)
xr = Xerox(40)

sk_list = pr.my_dict() | sc.my_dict() | xr.my_dict()
sk = Sklad(sk_list)
my_dic = sk.my_dict()
print(f'Добавляем на склад {my_dic}')
or_teh = {}
sector_tech = {}
sector = input('Введите наименование подразделения ->')
while True:
    s_tech = input('Введите наименование техники ->')
    if s_tech.lower() in ['принтер', 'сканер', 'ксерокс']:
        sector_tech = s_tech.capitalize()
        break
while True:
    _num = input('Введите количество техники ->')
    if _num.isdigit():
        sector_num = int(_num)
        break

or_teh[sector_tech] = sector_num
print(or_teh)
o_t = OrgTeh(sector, or_teh)
t_i_sk = sk.take_from_sklad(sector_tech, sector_num)
my_dic = sk.my_dict()
print(f'Остаток на складе {my_dic}')
