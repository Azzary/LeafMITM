
import numpy
import heapq
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# heuristic function for path scoring




def heuristic(a, b):
    return numpy.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


# path finding function

def astar(array, start, goal, combat = False):
    if combat:
        # original one
        neighbors = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # based on y value
        odd_neighbors =  [(0, 1), (0, -1),(1, 1), (1, -1)] # non (1,0)
        pair_neighbors = [(0, 1), (0, -1),(-1, 1), (-1, -1)]
    else:#(-1, 1),(-1, -1)
        # original one
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1),(0 ,2), (0, -2)]

        # based on y value
        odd_neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1),(0 ,2), (0, -2)]
        pair_neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1),(0 ,2), (0, -2)]


    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:

        current = heapq.heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            data.append(start)
            data = data[::-1]
            return data

        close_set.add(current)

        if current[1] % 2 == 0:
            pimp_neighbors = pair_neighbors
        else:
            pimp_neighbors = odd_neighbors

        for i, j in pimp_neighbors:
            neighbor = current[0] + i, current[1] + j

            multiply = 1

            # if current_line_simetry == 'pair':
            if abs(i) == 1 and j == 0:
                multiply = 1.2
            if abs(i + j) == 2:
                multiply = 0.7

            tentative_g_score = gscore[current] + heuristic(current, neighbor) * multiply

            try:
                if 0 <= neighbor[0] < array.shape[0]:
                    if 0 <= neighbor[1] < array.shape[1]:
                        if array[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        # array bound y walls
                        continue
                else:
                    # array bound x walls
                    continue
            except:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False







#import app.tools.crypt as Crypt

def from_array_map_to_numpy(map_array, width_):

    new_map = numpy.empty((0, width_))
    for line in map_array:
        new_map = numpy.append(new_map, [line], axis=0)

    # Swap axes else y will become y >.>!
    new_map = numpy.swapaxes(new_map, 0, 1)
    return new_map

def find_direction(start_cell, end_cell):
    dirs = {'e': 0, 'se' : 1, 's' : 2, 'sw' : 3, 'w' : 4, 'nw' : 5, 'n' : 6, 'ne' : 7 }
    t_ = ''

    is_start_cell_on_pair_line = True if ( start_cell[1] % 2 == 0 ) else False
    is_end_cell_on_pair_line = True if (end_cell[1] % 2 == 0) else False
    # North or south
    if start_cell[1] - end_cell [1] > 0:
        t_ += 'n'
    elif start_cell[1] - end_cell[1] < 0:
        t_ += 's'

    # if t_ has not N or S , it means it's only vertical deplacement
    if t_ == '':
        if start_cell[0] - end_cell[0] < 0:
            t_ += 'e'
        elif start_cell[0] - end_cell[0] > 0:
            t_ += 'w'
    else:
        # care the user is not trying to go 2 cases down and then we don't care about x.
        if is_start_cell_on_pair_line and is_end_cell_on_pair_line is False:
            if start_cell[0] - end_cell[0] == 0:
                t_ += 'e'
            elif start_cell[0] - end_cell[0] > 0 :
                t_ += 'w'
            elif start_cell[0] - end_cell[0] < 0:
                print('ERROR THIS SHOULNT BE ALLOWED')
        elif is_start_cell_on_pair_line is False and is_end_cell_on_pair_line is True:
            if start_cell[0] - end_cell[0] == 0:
                t_ += 'w'
            elif start_cell[0] - end_cell[0] > 0 :
                print('ERROR THIS SHOULNT BE ALLOWED')
            elif start_cell[0] - end_cell[0] < 0:
                t_ += 'e'
    value = dirs[t_]

    return value

def from_cell_id_to_x_y_pos(cell_id, width):
    pos_y =  ( cell_id // (((width )*2)-1 ))*2
    if ( cell_id % (((width )*2)-1 )) >= width:
        pos_y += 1
    if cell_id > ( width -1 ) *2:
        add = 1
        pos_x = (cell_id + (pos_y // 2)) % (width ) + add
    else:
        pos_x = cell_id % (width) + 1
    return pos_x - 1, pos_y


def from_pos_x_y_to_cell_id(x, y, map_width):
    sous = (y // 2)
    cell_id = (y * map_width) + (x ) - sous
    return cell_id

def convert_astar_path_to_dofus_path(path, map_width):
    le_path = ''
    last_dir = None
    last_cell = None
    for i in range(1, len(path)):
        last_cell = path[i-1]
        cell = path[i]
        dir = find_direction(last_cell, cell)
        if i == 1:
            last_dir = dir
        if dir != last_dir:
            cell_id = from_pos_x_y_to_cell_id(last_cell[0], last_cell[1], map_width)
            le_path += cell_dir_to_char(cell_id, last_dir)
            
            last_dir = dir
    # add the end
    last_cell = path[-1]
    cell_id = from_pos_x_y_to_cell_id(last_cell[0], last_cell[1], map_width)
    le_path += cell_dir_to_char(cell_id, last_dir)
    return  le_path, 0




def cell_dir_to_char(cell_id,last_dir):
    hash = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    z = str(hash[last_dir])
    charCode2 = (cell_id % len(hash))
    charCode1 = (cell_id - charCode2) // len(hash)
    t = str(hash[charCode1] + hash[charCode2])
    return z+t

def char_to_cell_dir(cell):
    liste = []
    start = 0
    for i in range(3,len(cell),3):
        hash = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        z = hash.index(cell[start:i][0])
        charCode2 = hash.index(cell[start:i][1]) * len(hash)
        charCode1 = hash.index(cell[start:i][2])
        t = charCode1 + charCode2
        start = i
        liste.append((z,t))
    return liste

DEPLACEMENT_TIMING_RUN = {
'horizontal': 0.3,
'vertical': 0.2,
'diagonal': 0.2
}
DEPLACEMENT_TIMING_WALK = {
'horizontal': 0.75,
'vertical' : 0.5,
'diagonal': 0.5
}

def timing(astar_path):
    run_time = 0
    if len(astar_path) > 2:
        time = DEPLACEMENT_TIMING_RUN
    else:
        time = DEPLACEMENT_TIMING_WALK
    for i in range(len(astar_path)-1):
        dir = find_direction(astar_path[i],astar_path[i+1])
        if dir == 2 or dir == 6:
            run_time += time['vertical']
        elif dir == 0 or dir == 4:
            run_time += time['horizontal']
        else:
            run_time += time['diagonal']
    return (run_time+0.4)

if __name__ == "__main__":
    x = [
[1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
[0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],



[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1]]
    a = from_cell_id_to_x_y_pos(109,15)
    b = from_cell_id_to_x_y_pos(24,15)
    s= from_pos_x_y_to_cell_id(0,0,15)
    z = from_array_map_to_numpy(x,15)
    y = [(8,22),(8,23),(8,24),(8,25),(8,26)]#astar(z,a,b,False)
    if y != False:
        for cell in y:
            print(cell[0],cell[1],from_pos_x_y_to_cell_id(cell[0],cell[1],15))
        print(y[:5])
        pa = convert_astar_path_to_dofus_path(y,15)


