import os
import csv


class CarBase:
    """Базовый класс всех машин"""
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    """Класс легковых автомобилей"""
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    """Класс грузовиков"""
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = 'truck'
        try:
            self.body_length, self.body_width, self.body_height = [float(_) for _ in self.body_whl.split('x')]
        except Exception:
            self.body_length, self.body_width, self.body_height = [0.0, 0.0, 0.0]

    def get_body_volume(self):
        """Возвращает объем грузовика"""
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    """Класс для спецмашин"""
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    """Функция, возвращающая список структур автомобилей из csv-файла"""
    car_list = []
    with open(csv_filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = [_ for _ in row]
                valid_row = car_type and photo_file_name and brand and carrying and car_type
                valid_type = car_type in ['car', 'truck', 'spec_machine']
                valid_extension = CarBase(brand, photo_file_name, carrying).get_photo_file_ext() in ['.jpg', '.jpeg',
                                                                                                     '.png',
                                                                                                     '.gif']
                if valid_row and valid_type and valid_extension:
                    if car_type == 'car' and passenger_seats_count:
                        car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
                    elif car_type == 'truck':
                        car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
                    elif car_type == 'spec_machine' and extra != '':
                        car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
            except ValueError:
                pass

    return car_list


if __name__ == '__main__':
    csv_filename = 'coursera_week3_cars.csv'
    cars = get_car_list(csv_filename)