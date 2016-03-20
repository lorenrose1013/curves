from display import *
from draw import *
import parser
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parser.parse_file( 'script_nocurves', edges, transform, screen, color )
