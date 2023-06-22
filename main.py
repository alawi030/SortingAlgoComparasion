import time
import matplotlib.pyplot as plt

data = open("data.txt", "r")
data = data.read()

bubble_sort = []
cycle_sort = []


def bubble_sort_data(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        bubble_sort.append(data.copy())
    return bubble_sort

def cylce_sort_data(data):
    for cycleStart in range(0, len(data) - 1):
        item = data[cycleStart]
        pos = cycleStart
        for i in range(cycleStart + 1, len(data)):
            if data[i] < item:
                pos += 1
        if pos == cycleStart:
            continue
        while item == data[pos]:
            pos += 1
        data[pos], item = item, data[pos]
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(data)):
                if data[i] < item:
                    pos += 1
            while item == data[pos]:
                pos += 1
            data[pos], item = item, data[pos]
        cycle_sort.append(data.copy())
    return cycle_sort

def measure_sort(sort, message, *args):
    start = time.time()
    sort(*args)
    end = time.time()
    print(f"{message} took {end - start} seconds")
    return end - start

def compare_sorting_algorithms():
    bubble_sort_time = measure_sort(bubble_sort_data, "Bubble sort", data.copy())
    cycle_sort_time = measure_sort(cylce_sort_data, "Cycle sort", data.copy())
    
    if cycle_sort_time > bubble_sort_time:
        print(f'Bubble sort is {cycle_sort_time / bubble_sort_time} times faster than Cycle sort')
    else:
        print(f'Cycle sort is {bubble_sort_time / cycle_sort_time} times faster than Bubble sort')

def draw_data(array):
    fix, ax = plt.subplots()
    ax.plot(array)
    ax.invert_yaxis()
    ax.invert_xaxis()
    plt.ylabel('Iterations')
    plt.xlabel('Data')
    plt.show()

def main():
    draw_data(data)
    compare_sorting_algorithms()
    draw_data(data)


if __name__ == "__main__":
    main()

