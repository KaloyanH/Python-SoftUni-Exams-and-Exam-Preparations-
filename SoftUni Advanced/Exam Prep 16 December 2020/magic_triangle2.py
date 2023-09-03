def get_magic_triangle(number):

    triangle = [[1], [1, 1]]
    for idx in range(2, number):
        my_list = [1]
        counter = 0
        for j in range(1, idx):
            my_list.append(triangle[idx - 1][counter] + triangle[idx - 1][counter + 1])
            counter += 1
        my_list.append(1)
        triangle.append(my_list)
    return triangle




get_magic_triangle(5)