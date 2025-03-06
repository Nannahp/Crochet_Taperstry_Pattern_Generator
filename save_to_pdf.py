#%pip install reportlab

from reportlab.lib.pagesizes  import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def ansi_to_colours(ansi_code):
    color_map = {
        "\x1b[31m": colors.red,        
        "\x1b[32m": colors.green,      
        "\x1b[33m": colors.yellow,     
        "\x1b[34m": colors.blue,       
        "\x1b[35m": colors.magenta,    
        "\x1b[36m": colors.cyan,       
        "\x1b[37m": colors.white,      
        "\x1b[0m": colors.black,       
    }
    
    return color_map.get(ansi_code, colors.black) 
    
def create_pdf(pattern, colour_map, size, filename ="pattern.pdf"):

    c = canvas.Canvas(filename, pagesize=letter)
    title = "Generated Crochet Tapestry Pattern"
    description = f"Here is your {size} pattern"
    
    #set font for title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100,750, title)
    
    #set font for description 
    c.setFont("Helvetica", 12)
    c.drawString(100,730, description)
    
    #position for pattern
    x_position = 100 #start position
    y_position =650 #start postion
    font_size=12
    
    for row in pattern:
        for x in row:
            colour_code = colour_map.get(x, "\033[0m")
            reportLab_color = ansi_to_colours(colour_code)
            c.setFillColor(reportLab_color)
            c.drawString(x_position, y_position, "X")
            x_position += 20 # move right for the next x
       
        y_position -= 20 # move down for the next row
        x_position = 100 # reset x position
    c.save()
    
#create_pdf(pattern,colour_map)