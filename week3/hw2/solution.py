import os
import csv


def get_photo_file_ext(photo):
    return os.path.splitext(photo)[-1]


class CarBase:

    def __init__(self, brand: str, photo: str, carry):
        self.car_type: str = ''
        self.brand: str = brand
        self.photo_file_name: str = photo
        self.carrying: float = float(carry)

    def get_photo_file_ext(self):
        return get_photo_file_ext(self.photo_file_name)


class Truck(CarBase):

    def __init__(self, brand, photo, carry, body_whl=''):
        super().__init__(brand, photo, carry)
        self.car_type = 'truck'
        try:
            self.body_length, self.body_width, self.body_height = \
                (float(i) if i else 0.0 for i in body_whl.split('x'))
        except:
            self.body_length = self.body_width = self.body_height = 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class Car(CarBase):

    def __init__(self, brand, photo, carry, passengers):
        super().__init__(brand, photo, carry)
        self.car_type = 'car'
        self.passenger_seats_count = int(passengers) if passengers else 0


class SpecMachine(CarBase):

    def __init__(self, brand, photo, carry, extra):
        super().__init__(brand, photo, carry)
        self.car_type = 'spec_machine'
        self.extra = extra


def analyzer(car):
    try:
        car_type, brand, passengers, photo, body, carrying, extra = car
    except ValueError:
        assert False
    assert car_type and brand and photo and carrying
    assert car_type in {'car', 'truck', 'spec_machine'}
    assert get_photo_file_ext(photo) in {'.jpg', '.jpeg', '.png', '.gif'}
    if car_type == 'car':
        assert passengers
        res = Car(brand, photo, carrying, passengers)
    elif car_type == 'truck':
        res = Truck(brand, photo, carrying, body)
    else:
        assert extra
        res = SpecMachine(brand, photo, carrying, extra)
    return res


def get_car_list(csv_filename):
    l = []
    with open(csv_filename, "r") as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                l.append(analyzer(row))
            except AssertionError:
                pass
    return l


if __name__ == '__main__':
    print(get_car_list('cars.csv'))
