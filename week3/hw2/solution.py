import csv

class CarBase:
    def __init__(self, brand, photo, carry):
        self.car_type = None
        self.brand = brand
        self.photo_file_name = photo
        self.carrying = float(carry)
        
    def get_photo_file_ext(self):
        return '.' + self.photo_file_name.rpartition('.')[-1]


class Car(CarBase):
    def __init__(self, brand, photo, carry, passengers):
        super().__init__(brand, photo, carry)
        self.car_type = 'car'
        self.passenger_seats_count = int(passengers) if passengers else 0


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


class SpecMachine(CarBase):
    def __init__(self, brand, photo, carry, extra):
        super().__init__(brand, photo, carry)
        self.car_type = 'spec_machine'
        self.extra = extra


def analyzer(car):
    if car[0] and car[1] and car[3] and car[5]:
        if ('.' + car[3].rpartition('.')[-1]) in {'.jpg', '.jpeg', '.png', '.gif'}:
            if car[0] == 'car' and car[2]:
                res = Car(car[1], car[3], car[5], car[2])
            elif car[0] == 'truck':
                res = Truck(car[1], car[3], car[5], car[4])
            elif car[0] == 'spec_machine' and car[6]:
                res = SpecMachine(car[1], car[3], car[5], car[6])
            else:
                raise Exception
        else:
            raise Exception
    else:
        raise Exception
    return res



def get_car_list(csv_filename):  
    l = []
    with open(csv_filename, "r") as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                l.append(analyzer(row))#[0].split(',')))
            except:
                pass
    return l
