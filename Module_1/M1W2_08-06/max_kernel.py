# Exercise: 1

def max_kernel(lst, k):
    margin = k//2
    length = len(lst)-margin
    length = length if k % 2 == 1 else length+1

    result = []
    for i in range(margin, length):
        left = i-margin
        right = left + k
        window = lst[left: right]
        max_value = max(window)

        # print(f'{window} => max {max_value}')
        result.append(max_value)

    return result


if __name__ == '__main__':
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    print(max_kernel(num_list, 3))
