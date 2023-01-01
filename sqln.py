import random
import sys
from turtle import color
from PIL import Image
import itertools
import csv

height = 1200
width = 675
min_size = 25
max_size = 300
num_square = 250

ans_list = [] # [[x,y,l], ...]
color_list = []

def calc_square():
    i = 0
    while True:
    	p_x = random.randint(0, width)
    	p_y = random.randint(0, height)
    	length = random.randint(min_size, max_size)
    	if p_x + length > width or p_y + length > height:
    		continue
    	ans_list.append([p_x, p_y, length])
    	i += 1
    	if i == num_square:
    		break
    return
    
def lay_square():
    color_list = [[int('0xFFFFFF', 16)]*width for i in range(height)]
    for square in ans_list:
        color = int('0x000000', 16)
        line_color = gen_color()
        for y in range(square[1], square[1] + square[2], 1):
            for x in range(square[0], square[0] + square[2], 1):
                if y == square[1] or y == square[1] + square[2] - 1 or x == square[0] or x == square[0] + square[2] -1:	
                  color_list[y][x] = line_color

    img = Image.new('RGB', (width, height), "white")
    img.putdata(list(itertools.chain.from_iterable(color_list)))
    img.save('output.png')
    img.show()
    return

def gen_color():
    red = hex(random.randint(0, 255))
    green = hex(random.randint(0, 255))
    blue = hex(random.randint(0, 255))
    hex_color = red[2:] + green[2:] + blue[2:]
    return int(hex_color, 16)

if __name__ == "__main__":
    calc_square()
    lay_square()
