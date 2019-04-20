#!/bin/python3


def read_data(filename):
    with open(filename) as file:
        content = file.readlines()

    content = [x.strip() for x in content]

    data = []

    for line in content:
        index = len(data)
        data.append([])
        for num in line.split():
            data[index].append(num)

    return data


def read_labels(filename, to_lower=False):
    with open(filename) as file:
        content = file.readlines()

    if to_lower:
        content = [x.strip().lower() for x in content]
    else:
        content = [x.strip() for x in content]

    return content


if __name__ == '__main__':
    res = read_data("data.txt")

    for i in range(len(res)):
        for j in range(len(res[i])):
            print("{},{} : {}".format(i, j, res[i][j]))
