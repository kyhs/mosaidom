import random

height = 1200
width = 675
max_square = 400

ul_list = [] # upper left points list
ans_list = [] # [[x,y,l], ...]

def calc_square():
    ul_list.append([0, 0])

    while True:
        min_x = 1000
        min_y = 1000
        counter = 0
        i = 0
        for ul_point in ul_list:
            if min_y > ul_point[1]:
                min_y = ul_point[1] # min_y is minimum y-axis value in ul_point
                if min_x > ul_point[0]:
                    min_x = ul_point[0] # min_x is minimum x-axis value in min_y line
                    i = counter
            counter += 1
        
        # (p_x, p_y): upper left point in this loop
        p_x = min_x
        p_y = min_y
        del ul_list[counter] # remove point p from ul_list
        print(p_x, p_y)

        max_l = min(width - p_x, height - p_y) # TODO consider the case of stick out
        length = random.randint(5, min(max_l, max_square))  # TODO when margin is less than 5
        ans_list.append([p_x, p_y, length])

        # append new ul to ul_list
        if p_x + length < width: # TODO consider the case of stick out
            ul_list.append([p_x + length + 1, p_y])
        if p_y + length < height: # TODO consider the case of stick out
            ul_list.append([p_x, p_y + length + 1])

        print(ul_list.len())
        print('\n')

        if len(ul_list) == 0:
            break
        # break
    return

if __name__ == "__main__":
    calc_square()
    # draw
