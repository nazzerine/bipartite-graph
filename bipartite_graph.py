#This is a turtle graphics program that given 2 sets of coordinates will
#draw a complete bipartite graph (lines connect all the points in one set with
#all the points in the other set).

#The coordinates depict where the vertices are in space.
#The program will go to one vertex in the first list and draw an edge to each
#vertex in the second list. X and Y represent the two lists of vertices.

import turtle

def turtle_setup():
    global my_screen
    global my_turtle
    my_screen = turtle.Screen()
    my_turtle = turtle.Turtle()

#listX and listY should be entered as a list of lists
def bipartite_graph(listX, listY):
    turtle_setup()
    for X_vertex in listX:
        my_turtle.setposition(X_vertex)
        for Y_vertex in listY:
            my_turtle.pd()
            my_turtle.setposition(Y_vertex)
            my_turtle.pu()
            my_turtle.setposition(X_vertex)
            
