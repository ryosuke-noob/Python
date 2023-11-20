class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(seld):
        print('run')
    pass

class ToyotaCar(Car):
    def run(seld):
        print('fast')
    pass

class TeslaCar(Car):
    def __init__(self, model='Model S',
                enable_auto_run=False,
                passwd='123'):
        # self.model = model
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd= passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(seld):
        print('super fast')
    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar('Model S', passwd='456')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

# car = Car()
# car.run()
# print('###########')

# toyota_car =ToyotaCar('Lexas')
# print(toyota_car.model)
# toyota_car.run()
# # toyota_car.auto_run()

# print('###########')
# print(tesla_car.model)
# tesla_car = TeslaCar(enable_auto_run=True)
# tesla_car = TeslaCar('Model S')
# tesla_car.run()
# tesla_car.auto_run()

# _*** _は外部から見えるけどいじってほしくない．（いじろうとすればいじれはする）
# __*** __は外部からいじれないし見れないけど内部からは見える