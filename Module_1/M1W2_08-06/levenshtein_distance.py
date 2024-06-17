def levenshtein_distance(source, target):
    m = len(source)
    n = len(target)

    # Tạo ma trận với kích thước (m+1) x (n+1)
    d = [[0] * (n + 1) for _ in range(m + 1)]

    # Khởi tạo giá trị cho hàng và cột đầu tiên
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j

    # Tính toán khoảng cách Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + cost
            )

    return d[-1][-1]


if __name__ == '__main__':
    print(levenshtein_distance('holla', 'hello'))
