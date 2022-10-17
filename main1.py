import random
import time

def read(path):
    array = [int(i) for i in open('Chisla.txt').readline().split()]
    return array
def read1(path):
    array = [int(i) for i in open('Bigfile.txt').readline().split()]
    return array
def read2(path):
    array = [int(i) for i in open('TooBigfile.txt').readline().split()]
    return array
def read3(path):
    array = [int(i) for i in open('One.txt').readline().split()]
    return array


def _min(array):
    min_ = array[0]
    for z in array:
        if z < min_:
            min_ = z
    return min_

def _max(array):
    max_ = array[0]
    for z in array:
        if z > max_:
            max_ = z
    return max_

def _mult(array):
    mul_ = 1
    for z in array:
        mul_ *= z
    return mul_

def _sum(array):
    sum_ = 0
    for z in array:
        sum_ += z
    return sum_

def get_time(size):
    test = [random.randrange(-100, 100) for z in range(size)]
    start = time.time_ns()
    _mult(test)
    return (time.time_ns() - start) / 1e6

def run_time_test():
    print(get_time(1))
    print(get_time(100000))
    print(get_time(200000))
    print(get_time(300000))
    print(get_time(400000))
    print(get_time(500000))
    print(get_time(600000))
    print(get_time(700000))
    print(get_time(800000))
    print(get_time(900000))
    print(get_time(1000000))


print('В файле')
print("Минимальное:", _min(read(1)))
print('Максимальное:', _max(read(1)))
print('Сумма:', _sum(read(1)))
print("Произведение:", _mult(read(1)))

print('В big файле')
print("Минимальное:", _min(read1(1)))
print('Максимальное:', _max(read1(1)))
print('Сумма:', _sum(read1(1)))
print("Произведение:", _mult(read1(1)))

print('В too big файле')
print("Минимальное:", _min(read2(1)))
print('Максимальное:', _max(read2(1)))
print('Сумма:', _sum(read2(1)))
print("Произведение:", _mult(read2(1)))

print('В one файле')
print("Минимальное:", _min(read3(1)))
print('Максимальное:', _max(read3(1)))
print('Сумма:', _sum(read3(1)))
print("Произведение:", _mult(read3(1)))