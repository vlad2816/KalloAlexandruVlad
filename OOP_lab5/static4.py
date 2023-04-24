class Car:

    sound = 'Ti ti ti '

    def __init__(self) -> None:
        self.__engine_started = False
        Car.horn()

    def start_engine(self):
        self.__engine_started = True

    def stop_engine(self):
        self.__engine_started = False

    @staticmethod
    def horn():
        print(Car.sound)


vw = Car()  # Always start with tit tit tit because the staticmethod is inside the constructor
