import tkinter as tk
from map_gestion.cell import Cell
import logging
from map_gestion.entity import Entity
from map_gestion.click_simulation import ClickSimulation


class Table(tk.Frame):
    def __init__(self, parent, rows, columns):
        self.clicksimulation = ClickSimulation()
        tk.Frame.__init__(self, parent)
        self._widgets = []
        self.cells = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                if column == 0 and row%2 == 0:
                    label = tk.Label(self, text=" ", borderwidth=0, width=5)
                else:
                    label = tk.Label(self, text=" ", borderwidth=0, width=5)
                if row % 2  == 0:
                    label.grid(row=row, column=column, sticky="nsew", padx=0, pady=0)
                else:
                    label.grid(row=row, column=column, sticky="nsew", padx=0, pady=0)
                current_row.append(label)
            self._widgets.append(current_row)
            
            

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set_background(self, row, column, color):
        widget = self._widgets[row][column]
        widget.configure(background=color)

    def set_data(self, cells: [[Cell]]):
        self.cells = cells
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                
                cell = cells[i][j]
                self.cells[i][j].max_x = len(cells[i])

                self.cells[i][j].max_y = len(cells)
                self.cells[i][j].x = j
                self.cells[i][j].y = i
                widget = self._widgets[i][j]
                widget.configure(background=cell.color, text=str(cell.CellID))
                widget.bind('<Button-1>', lambda e, a=i, b=j: self.debug_cell(a, b))
                
                
    def set_entities(self, entitys, entitys_remove):
       
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                
                for entity_remove in entitys_remove:
                    if (self.cells[i][j].CellID == entity_remove.cell):
                        widget = self._widgets[i][j]
                        widget['background'] = self.cells[i][j].color
                        
                for entity in entitys:
                    if(self.cells[i][j].CellID == entity.cell):
                        widget = self._widgets[i][j]
                        widget['background'] = self.cells[i][j].color
                        #widget.(background=cell.color , text=str(cell.CellID))
                        #self._widgets[i][j]. .bind('<Button-1>', lambda e, a=i, b=j: self.debug_cell(a, b))
                
                                
                
            
            
        


    def debug_cell(self, i, j):
        print(self.cells[i][j].__dict__)

        self.clicksimulation.click(self.cells[i][j].__dict__)