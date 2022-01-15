def max_in_2d_arr(numbers):
    sum_list = []
    for i in range(0,len(numbers)):
        sum_list.append(sum(numbers[i]))
    return max(sum_list)


if __name__ == '__main__':
    numbers = [[0, 0, 1, 0, 0, 1], [0, 1, 0, 88, 0, 0], [0, 0, 2, 0, 0, 1], [0, 1, 0, 3, 0, 0], [0, 0, 0, 0, 4, 0]]

    # arr = [[23, 4, 56, 55, 4, 43, 22, 11, 1]]
    print(max_in_2d_arr(numbers))
