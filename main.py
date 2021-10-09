from operator import itemgetter

all_coordinates = []
list_coordinates = []
count = []
dict_mini ={}
class Point:
    def __init__(self, x, y, point):
        self.x = x
        self.y = y
        self.point = point

    def begin(self, *args):
        dict_mini[self.point] = [self.x, self.y]
        for arg in args:
            dict_mini[arg.point] = [arg.x, arg.y]

        self.coord_list(*args)


    def point_coordinates(self):
        for key, value in dict_mini.items():
            if key != self.point:
                all_coordinates.append(value)

    def coord_list(self, *args):
        self.point_coordinates()
        for arg in args:
            arg.point_coordinates()



point_1 = Point(0, 2, 'point_1')
point_2 = Point(2, 5, 'point_2')
point_3 = Point(5, 2, 'point_3')
point_4 = Point(6, 6, 'point_4')
point_5 = Point(8, 3, 'point_5')


point_1.begin(point_2, point_3, point_4, point_5)

for key, value in dict_mini.items():
    count.append(key)

def func_chunk():
    i = 0
    k = int(len(all_coordinates)/len(count))
    for x in range(len(count)):
        for el in all_coordinates:
            list_coordinates.append(all_coordinates[i:k])
            i = k
            k = k+int(len(count)-1)
            break

func_chunk()
dict_list = dict(zip(count, list_coordinates))

dist_kord = []
def calculation_coordinates():
    for i in range(0, (len(count)-1)):
        for key, value in dict_list.items():
            for key_mini, value_mini in dict_mini.items():
                koord_mini = value_mini
                if key_mini == key:
                    distance = ((value[i][0] - koord_mini[0]) ** 2 + (value[i][1] - koord_mini[1]) ** 2) ** 0.5
                    dist_kord.append([value_mini, value[i], distance])


calculation_coordinates()
sort_dist_min = sorted(dist_kord, key=itemgetter(2))
start_result = []
result_dist_list = []

def start():
    for begin_point, next_point, dist in sort_dist_min:
        if begin_point[0] == point_1.x and begin_point[1] == point_1.y:
            start_result.append([begin_point, next_point, dist])
            result_dist_list.append([begin_point, next_point, dist])
            break

def next_point():
    i = len(result_dist_list) - 1
    for begin_point, next_point, dist in sort_dist_min:
        if result_dist_list[i][1] == begin_point and next_point != result_dist_list[i][0] and next_point != start_result[0][1]\
                and next_point != start_result[0][0]:
            result_dist_list.append([begin_point, next_point, dist])
            sort_dist_min.remove([begin_point, next_point, dist])
            break

def stop():
    i = len(result_dist_list) - 1
    for begin_point, next_point, dist in sort_dist_min:
        if result_dist_list[i][1] == begin_point and next_point[0] == point_1.x and next_point[1] == point_1.y:
            result_dist_list.append([begin_point, next_point, dist])
            break


def postman_distance():
    start()
    for element in range(len(count)-2):
        next_point()
    stop()
postman_distance()

def result():
    distance_for_sum = []
    print(f'{result_dist_list[0][0]}', end='')
    for begin_point, next_point, dist in result_dist_list:
        distance_for_sum.append(dist)
        print (f' --> {next_point, dist}', end='')
    print(f' == {sum(distance_for_sum)}')

result()


