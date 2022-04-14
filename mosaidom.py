import random
import sys

height = 1200
width = 675
max_square = 400

ul_list = [] # upper left points list
ans_list = [] # [[x,y,l], ...]

def calc_square():
    ul_list.append([0, 0])

    while True:
        min_x = 10000
        min_y = 10000
        counter = 0
        i = 0
        for ul_point in ul_list:
            if min_y > ul_point[1]:
                if min_x > ul_point[0]:
                    min_y = ul_point[1] # min_y is minimum y-axis value in ul_point
                    min_x = ul_point[0] # min_x is minimum x-axis value in min_y line
                    i = counter
            counter += 1
        
        # (p_x, p_y): upper left point in this loop
        p_x = min_x
        p_y = min_y
        print('i:', i, ', counter:', counter)
        del ul_list[i] # remove point p from ul_list
        print('p:', p_x, p_y)
        
        max_x = 10000
        if len(ans_list):
            for ans_ul_point in ans_list:
                if ans_ul_point[0] > p_x and ans_ul_point[1] < p_y < ans_ul_point[1] + ans_ul_point[2]:
                    max_x = min(max_x, ans_ul_point[0])
                elif ans_ul_point[0] == p_x and ans_ul_point[1] < p_y < ans_ul_point[1] + ans_ul_point[2]:
                    # p_x is on the other square's edge TODO
                    print("suit")
                    return

        max_l = min(max_x, min(width - p_x, height - p_y)) 

        if max_l < 5:
            print("no margin")
            break# TODO when margin is less than 5

        length = random.randint(5, min(max_l, max_square)) 

        # print(length)
        if length < 5:
            print("shorter length")
            continue # TODO consider when 0 < lenght < 5 
        else:
            ans_list.append([p_x, p_y, length])

        # append new ul to ul_list
        if p_x + length < width: # TODO consider the case of stick out
            ul_list.append([p_x + length + 1, p_y])
            print('append_x:', p_x+length+1)
        if p_y + length < height: # TODO consider the case of stick out
            ul_list.append([p_x, p_y + length + 1])
            print('append_y:', p_y+length+1)

        print(ul_list)
        # print(len(ul_list))
        # print('\n')
        # print(ans_list)

        if len(ul_list) == 0:
            break
        # break
    return

if __name__ == "__main__":
    calc_square()
    print('ans size: ', len(ans_list))
    print(ans_list)
    # draw
