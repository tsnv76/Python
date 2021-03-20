import time


class TrafficLight:
    __color = [['красный', 7], ['желтый', 3], ['зеленый', 10]]

    def running(self):
        for item in self.__color:
            print(item[0])
            time.sleep(item[1])
        print('Конец цикла переключения')


t = TrafficLight()
print(t.running())
