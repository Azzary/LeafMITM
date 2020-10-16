
from character.path_finding import *
from threading import Thread
import time

class Deplacement():

    def __init__(self, socket_to_server):
        self.ismouving = False
        self.socket_to_server = socket_to_server

    def deplacement(self,cell_base, cell_clic, width, carreau, binairemap, sun, resource, pm = None, combat = False):

        cell_start = from_cell_id_to_x_y_pos(cell_base,width)
        cell_end = from_cell_id_to_x_y_pos(carreau[cell_clic]["cell"].CellID,width)
        if cell_start == cell_end:
            return True
        if carreau[cell_clic]["cell"].CellID in sun:
            binairemap[cell_end[1]][cell_end[0]] = 0
        elif carreau[cell_clic]["cell"].CellID in resource:
            binairemap[cell_end[1]][cell_end[0]] = 1
            
        numpy_ = from_array_map_to_numpy(binairemap,width)
        astar_path = astar(numpy_,cell_start,cell_end,combat)
        if astar_path != False:
            if pm:
                astar_path = astar_path[:pm+1]

            run_timing = timing(astar_path)
            dofus_path = convert_astar_path_to_dofus_path(astar_path,width)
            self.ismouving = True
            if combat:
                self.wait(dofus_path,run_timing,from_pos_x_y_to_cell_id(astar_path[-1][0],astar_path[-1][1],width))
            else:
                Thread(None,self.wait,args=[dofus_path,run_timing,from_pos_x_y_to_cell_id(astar_path[-1][0],astar_path[-1][1],width)]).start()
            return (True,run_timing)

        return (False,0)


    def wait(self,dofus_path, run_timing, last_cell):
        print(f"Depacement du personnage vers {last_cell} (temps {run_timing})")
        packet = "GA001"+dofus_path[0]+"\n\x00"
        self.socket_to_server.send(packet.encode())
        time.sleep(run_timing)
        self.socket_to_server.send(("GKK0"+"\n\x00").encode())
        self.ismouving = False
        print(f"Fin du depacement")