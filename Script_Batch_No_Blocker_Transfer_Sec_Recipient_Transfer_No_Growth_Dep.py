# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:15:56 2024

@author: deept
"""

from CellModeller.Regulation.ModuleRegulator import ModuleRegulator
from CellModeller.Biophysics.BacterialModels.CLBacterium import CLBacterium
from CellModeller.GUI import Renderers
import numpy
import random

#---------------------------------------------------------------------------------
##Deepthi's modification to include invar for batch
invar_Donor=0
invar_Recipient=0
invar_Blocker=0

#Deepthis modifications- function that sets number of donors, recipients and blocker based on argument passed from file
def set_invar(invar):
    global invar_Donor
    global invar_Recipient
    global invar_Blocker
    invar_Donor=invar['Donor']
    invar_Recipient= invar['Recipient']
    invar_Blocker=invar['Blocker']
    print('Defining set-up: Donor='+str(invar_Donor)+'Recipient: '+str(invar_Recipient)+'Blocker: '+str(invar_Blocker))
#-------------------------------------------------------------------------------


# Simulation Parameters
saveEvery = 50 # time-steps between saving pickle
renderEvery = 20 # time-steps between visualization in user interface
max_population = 50000 # Maximum number of cells in the system


# DONOR PARAMETERS TYPE 0
lenD = 2.68 # length
initialVolD = lenD # Cell Volume
targetVolD = 2*initialVolD # Volume that triggers cell division
growD = 1 # Growth rate, at the moment no cost

# RECIPIENT PARAMETERS TYPE 1
lenR = 2.68 # length
initialVolR = lenR # Cell Volume
targetVolR = 2*initialVolR # Volume that triggers cell division
growR = 1 # Growth rate

# TRANSCONJUGANT PARAMETERS TYPE 2
lenT = 2.68 # Same length as recipient
initialVolT = lenT # cell volume
targetVolT = 2*initialVolT #  Volume that triggers cell division
growT = growD # Growth rate, same as donor

# NEW CELL TYPE: BLOCKER PARAMETERS TYPE 3
lenB = 2.68 # length
initialVolB = lenB # Cell Volume
targetVolB = 2*initialVolB # Volume that triggers cell division
growB = 1 # Growth rate

# PROBAILITY OF CONJUGATION
con_prob = 0.4

# cell types and properties
number_of_types = 4
# Type 0 cells correspond to the DONOR, Blue
# Type 1 cells correspond to the RECIPIENT, Yellow
# Type 2 cells correspond to the TRANSCONJUGANT, Green
# Type 3 cells correspond to the BLOCKER, Red
# Create arrays to store information previously defined
cell_colors = {0:[0.0, 0.0, 1.0], 1:[1.0, 1.0, 0.0],2:[0.0, 1.0, 0.0], 3:[1.0, 0.0, 0.0]} # Array for color of cells: https://www.glowscript.org/docs/VPythonDocs/color.html
cell_lengths = {0:lenD, 1:lenR, 2:lenT, 3:lenB} # Array for cell lengths
cell_tarVol = {0:targetVolD, 1:targetVolR, 2:targetVolT, 3:targetVolB} # Array for target volumes
cell_growthRate = {0:growD, 1:growR, 2:growT, 3:growB} # Array for growth rates


# Function that creates random position inside of a circle
def randomXY(L,R,ktype):
    R2 = R * R
    L2 = L * L
    if ktype == 1:    ####### inside
        while True:
            x = numpy.random.uniform(-1, 1)
            y = numpy.random.uniform(-1, 1)
            x = x * L
            y = y * L
            r2 = x * x + y * y
            if r2 < R2 :
                break
    else:
        while True:
            x = numpy.random.uniform(-1, 1)
            y = numpy.random.uniform(-1, 1)
            x = x * L
            y = y * L
            r2 = x * x + y * y
            if r2 < L2 and r2 > R2:
                break
    return x,y

# Function that initializes the simulation, here the initial cells are placed in the grid
def setup(sim,invar=None):
    #Deepthi's modification to include invar for batch
    global TimeStep
    
    set_invar(invar)#Deepthi's modification to include invar for batch
    # Set biophysics and regulation models
    biophys = CLBacterium(sim, max_cells=max_population, jitter_z=False,compNeighbours=True)
    regul = ModuleRegulator(sim)

    # add biophysics, regulation, CDK and EPS objects to simulator
    sim.init(biophys, regul, None, None)
    
    # Set plasmid transfer counter to 0
    sim.countHGT = True
    sim.HGTevents = 0
    
    # Dimensions of the intial circle
    R1 =100.6
    R2 =100.5
    n_Donor=invar_Donor
    n_Recipient=invar_Recipient
    n_Blocker=invar_Blocker
    # loop to add n_Donor cells of type 0 (Donor) inside the circle
    for i in range(n_Donor):
        x1,y1 = randomXY(R1,R2,1)
        x2,y2 = randomXY(R1,R2,2)
        x = numpy.random.uniform(-1, 1)
        y = numpy.random.uniform(-1, 1)
        sim.addCell(cellType=0, length=lenD, pos=(x1,y1,0), dir=(x,y,0))
    # loop to add n_Recipient cells of type 1 (Recipient) inside the circle
    for i in range(n_Recipient):
        x1,y1 = randomXY(R1,R2,1)
        x2,y2 = randomXY(R1,R2,2)
        x = numpy.random.uniform(-1, 1)
        y = numpy.random.uniform(-1, 1)
        sim.addCell(cellType=1,length=lenR, pos=(x1,y1,0), dir=(x,y,0))
    # loop to add n_Blocker cells of type 3 (Blocker) inside the circle
    for i in range(n_Blocker):
        x1,y1 = randomXY(R1,R2,1)
        x2,y2 = randomXY(R1,R2,2)
        x = numpy.random.uniform(-1, 1)
        y = numpy.random.uniform(-1, 1)
        sim.addCell(cellType=3, length=lenB, pos=(x1,y1,0), dir=(x,y,0))

    # add some objects to draw the models
    mainRenderer = Renderers.GLBacteriumRenderer(sim)
    sim.addRenderer(mainRenderer)

    # specify how often we output data to the GUI / to file
    sim.renderEveryNSteps = renderEvery
    sim.pickleSteps = saveEvery
    TimeStep = sim.dt
    print('Timestep:',TimeStep)

# Function that adds information of each cell from the arrays
def init(cell):
    cell.length = cell_lengths[cell.cellType]
    cell.color = cell_colors[cell.cellType]
    cell.targetVol = cell_tarVol[cell.cellType]
    cell.growthRate = cell_growthRate[cell.cellType]

# Function that updates the population
def update(cells, sim):
    #Iterate through each cell and flag cells that reach target size for division
    for (id, cell) in cells.items():
       
    # Test whether the cell is ready to divide
        if cell.volume > cell.targetVol:
            cell.divideFlag = True
    
    # Add conjugation event
        if cell.cellType == 0: #if a cell is a donor
            surrounding_types=[cells[index] for index in cell.neighbours]
            if surrounding_types:
                cell_chosen_to_conjugate=random.choice(surrounding_types)
                if random.random() < con_prob and cell_chosen_to_conjugate.cellType==1:
                    cell_chosen_to_conjugate.cellType=2
                    sim.HGTevents += 1    
                    
        if cell.cellType == 2: #if a cell is a transconjugant
            surrounding_types=[cells[index] for index in cell.neighbours]
            if surrounding_types:
                cell_chosen_to_conjugate=random.choice(surrounding_types)
                if random.random() < con_prob and cell_chosen_to_conjugate.cellType==1:
                    cell_chosen_to_conjugate.cellType=2
                    sim.HGTevents += 1 
    
        cell.length = cell_lengths[cell.cellType]
        cell.color = cell_colors[cell.cellType]
        cell.targetVol = cell_tarVol[cell.cellType]
        cell.growthRate = cell_growthRate[cell.cellType]   

# Function that determines properties of daughter cells
def divide(parent, d1, d2):
    if parent.cellType == 0:
        d1.targetVol = targetVolD
        d1.length = lenD
        d1.growthRate = growD
        d2.targetVol = targetVolD
        d2.length = lenD
        d2.growthRate = growD
    if parent.cellType == 1:
        d1.targetVol = targetVolR
        d1.length = lenR
        d1.growthRate = growR
        d2.targetVol = targetVolR
        d2.length = lenR
        d2.growthRate = growR
    if parent.cellType == 2:
        d1.targetVol = targetVolT
        d1.length = lenT
        d1.growthRate = growT
        d2.targetVol = targetVolT
        d2.length = lenT
        d2.growthRate = growT
    if parent.cellType == 3:
        d1.targetVol = targetVolB
        d1.length = lenB
        d1.growthRate = growB
        d2.targetVol = targetVolB
        d2.length = lenB
        d2.growthRate = growB