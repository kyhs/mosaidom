import random

height = 1200
width = 675

ul_list = [] # upper left points list
ans_list = [] # [[x,y,l], ...]

def calc_square():
    ul_list.append([0, 0])

    while True:
        min_x = 1000
        min_y = 1000
        for ul_point in ul_list:
            if min_y > ul_point[1]:
                min_y = ul_point[1] # min_y is minimum y-axis value in ul_point
                if min_x > ul_point[0]:
                    min_x = ul_point[0] # min_x is minimum x-axis value in min_y line
        
        # upper left point in this loop
        p_x = min_x
        p_y = min_y
        print(p_x, p_y)

        max_l = 100000 # TODO consider the case of stick out
        length = random.randint(5, 10)  # TODO when margin is less than 5
        break
    return

if __name__ == "__main__":
    calc_square()
    # draw
