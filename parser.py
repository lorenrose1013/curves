from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    file_contents = f.readlines()
    i = 0
    while (i < len(file_contents) ):
        line = file_contents[i]
        if ("line" in line):
            args = file_contents[i+1]
            args = args.split(" ")
            draw.add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
            i += 1
        elif("circle" in line):
            #case circle
        elif("hermite" in line):
            #case hermite
        elif("b" in line):
            #case bezier
        elif("ident" in line):
            #case identity
        elif("scale" in line):
            #case scale
        elif("translate" in line):
            #case translate
        elif("xrotate" in line):
            #case xrotate       
        elif("yrotate" in line):
            #case yrotate       
        elif("zrotate" in line):
            #case zrotate       
        elif("apply" in line):
            #case apply       
        elif("display" in line):
            #case display       
        elif("save" in line):
            #case save       

