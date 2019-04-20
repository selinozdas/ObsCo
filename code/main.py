#!/bin/python3

from readfile import read_data
from readfile import read_labels
from util import quick_sort
from util import calculate_variance


def get_variance(data, ci):
    column_data = []

    for ri in range(len(data)):
        if data[ri][ci] >= 0:
            column_data.append(data[ri][ci])

    return calculate_variance(column_data)


def get_variances(data):
    var = []

    for ci in range(len(data[0])):
        var.append(get_variance(data, ci))

    return var


def convert_to_int(data):
    int_data = []

    for ri in range(len(data)):
        int_data.append([])

        for ci in range(len(data[0])):
            int_data[ri].append(int(data[ri][ci]))

    return int_data


if __name__ == '__main__':
    table = convert_to_int(read_data("data.txt"))
    column_names = read_labels("skills.txt", to_lower=True)
    row_names = read_labels("users.txt")

    num_of_users = len(table)
    num_of_skills = len(table[0])

    variances = get_variances(table)

    column_name_map = {}
    for i in range(len(column_names)):
        column_name_map[column_names[i]] = i

    while True:
        skills = input("Enter skills: ").strip().lower().split()

        if skills[0] == "quit":
            break

        skill_indexes = []
        for i in range(len(skills)):
            if skills[i] in column_name_map:
                skill_indexes.append(column_name_map[skills[i]])

        if len(skill_indexes) == 0:
            print("No skills found")
            continue

        ranks = []

        for i in range(num_of_users):
            rank = 0

            for s in skill_indexes:
                rank += table[i][s] * variances[s]

            ranks.append(rank)

        rank_index = quick_sort(ranks, is_ascending=False)

        skill_str = "".join(column_names[s] + " " for s in skill_indexes)
        print("Recommended for : " + skill_str)

        for i in range(3):
            print("{} : {}".format(row_names[rank_index[i]], ranks[i]))
