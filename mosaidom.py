import random
import sys
from turtle import color
import numpy as np
from PIL import Image
import itertools
import csv

height = 1200
width = 675
max_square = 400

ul_list = [] # upper left points list
ans_list = [] # [[x,y,l], ...]

color_list = []

def calc_square():
    ul_list.append([0, 0])

    while True:
        min_x = 10000
        min_y = 10000
        counter = 0
        i = 0
        flg_suit = False

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
        # print('i:', i, ', counter:', counter)
        if len(ul_list) <= i:
            print("out of index")
            print(ul_list)
            sys.exit()
        del ul_list[i] # remove point p from ul_list
        print('p:', p_x, p_y)
        
        max_x = 10000
        if len(ans_list) > 0:
            for ans_ul_point in ans_list:
                if ans_ul_point[0] > p_x and ans_ul_point[1] < p_y < ans_ul_point[1] + ans_ul_point[2]:
                    max_x = min(max_x, ans_ul_point[0])
                elif ans_ul_point[0] == p_x and ans_ul_point[1] < p_y < ans_ul_point[1] + ans_ul_point[2]:
                    # p_x is on the other square's edge TODO
                    print("suit")
                    flg_suit = True
                elif ans_ul_point[0] < p_x < ans_ul_point[0] + ans_ul_point[2] and ans_ul_point[1] < p_y < ans_ul_point[1] + ans_ul_point[2]:
                    print("overlap")
                    flg_suit = True
        if flg_suit:
            continue

        max_l = min(max_x, min(width - p_x, height - p_y)) 

        if max_l < 5:
            print("no margin")
            break # TODO when margin is less than 5

        length = random.randint(5, min(max_l, max_square)) 

        # print(length)
        if length < 5:
            print("shorter length")
            break # TODO consider when 0 < lenght < 5 
        else:
            ans_list.append([p_x, p_y, length])

        # append new ul to ul_list
        if p_x + length < width: # TODO consider the case of stick out
            print("a")
            ul_list.append([p_x + length, p_y])
        if p_y + length < height: # TODO consider the case of stick out
            print("b")
            ul_list.append([p_x, p_y + length])
        

        # print(ul_list)
        # print(len(ul_list))
        # print('\n')
        # print(ans_list)

        if len(ul_list) == 0:
            break

        # # debug
        # if len(ans_list) > 10:
        #     break
    return

def draw_square():
    # color_list = [[int('0x000000', 16)]*width]*height
    color_list = [[int('0x000000', 16)]*width for i in range(height)]
    i = 0
    for square in ans_list:
        # print(square)
        color = gen_color()
        for y in range(square[1], square[1] + square[2], 1):
            for x in range(square[0], square[0] + square[2], 1):
                color_list[y][x] = color
        # print(x,y)
        # print(len(ans_list)-i)
        i += 1
    # print(color_list)

    # np_color_list = np.array(color_list)
    # im = Image.fromarray(np_color_list)
    # im.save('sample.png')

    with open('color_list.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(color_list)
    with open('ans_list.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(ans_list)

    img = Image.new('RGB', (width, height), "white")
    img.putdata(list(itertools.chain.from_iterable(color_list)))
    img.save('aaa.png')

def gen_color():
    red = hex(random.randint(0, 255))
    green = hex(random.randint(0, 255))
    blue = hex(random.randint(0, 255))
    hex_color = red[2:] + green[2:] + blue[2:]
    return int(hex_color, 16)

if __name__ == "__main__":
    calc_square()
    # print('ans size: ', len(ans_list))
    # print(gen_color()) # debug
    draw_square()
    # print(ans_list)
