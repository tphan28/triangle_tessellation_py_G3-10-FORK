import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""
    
    # Fill the background
    sg.fill_background("white")
    
    # make some variables available
    # the color name "green" does not give correct shade of green, so used hex code instead
    colors = ["red", "#00ff00", "blue", "cyan", "magenta", "yellow"]

    # sizes of triangles are based on canvas size
    # we want to fit in 3 horizontally and 5 vertically.
    TRIANGLE_HEIGHT = height / 5
    TRIANGLE_WIDTH = width / 3

    # ==================================================================
    # Draw the tesselation (you should only edit code below this part!)
    # ==================================================================
    
    # code for RED triangles
    sg.set_fill_color(colors[0]) # set fill color to red
    
    for i in range(5):   # fill_triangle(x1, y1, x2, y2, x3, y3)
        sg.fill_triangle(2*TRIANGLE_WIDTH, i*TRIANGLE_HEIGHT, 3*TRIANGLE_WIDTH, i*TRIANGLE_HEIGHT, 3*TRIANGLE_WIDTH, (i+1)*TRIANGLE_HEIGHT) 
        
    
    # code for BLUE triangles
    sg.set_fill_color(colors[2])
    for i in range(5):   # fill_triangle(x1, y1, x2, y2, x3, y3)
        sg.fill_triangle(2*TRIANGLE_WIDTH, i*TRIANGLE_HEIGHT, 2*TRIANGLE_WIDTH, (i+1)*TRIANGLE_HEIGHT, 3*TRIANGLE_WIDTH, (i+1)*TRIANGLE_HEIGHT) 
    
    # code for YELLOW triangles
    sg.set_fill_color(colors[5])

    for i in range(5):
        sg.fill_triangle(
            TRIANGLE_WIDTH, i * TRIANGLE_HEIGHT,
            2 * TRIANGLE_WIDTH, i * TRIANGLE_HEIGHT,
            2 * TRIANGLE_WIDTH, (i + 1) * TRIANGLE_HEIGHT
        )
   
    # code for GREEN triangles
 
    sg.set_fill_color(colors[1])

    for i in range(5):
        sg.fill_triangle(
            TRIANGLE_WIDTH, i * TRIANGLE_HEIGHT,
            TRIANGLE_WIDTH, (i + 1) * TRIANGLE_HEIGHT,
            2 * TRIANGLE_WIDTH, (i + 1) * TRIANGLE_HEIGHT)
 
    # code for MAGENTA triangles
    sg.set_fill_color(colors[4])
    
    for i in range(5):   # fill_triangle(x1, y1, x2, y2, x3, y3)
        sg.fill_triangle(0, i*TRIANGLE_HEIGHT, TRIANGLE_WIDTH, i*TRIANGLE_HEIGHT, TRIANGLE_WIDTH, (i+1)*TRIANGLE_HEIGHT)
    
    # code for CYAN triangles
    sg.set_fill_color(colors[3]) # set fill color to red
    
    for i in range(5):   # fill_triangle(x1, y1, x2, y2, x3, y3)
        sg.fill_triangle(0*TRIANGLE_WIDTH, i*TRIANGLE_HEIGHT, 0*TRIANGLE_WIDTH, (i+1)*TRIANGLE_HEIGHT, 1*TRIANGLE_WIDTH, (i+1)*TRIANGLE_HEIGHT) 
    
    

if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
