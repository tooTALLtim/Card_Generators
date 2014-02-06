# Please install Pillow and its libraries
# (and uninstall PIL if you are using it)

# While experimenting with placement, font size, ect, I would ^C out of the
# program so it wouldn't create all 180 cards I had in my file

from PIL import ImageFont, Image, ImageDraw
import textwrap, datetime

# I sized these images 120 x 120 pixels
unicorn_black = Image.open("shaved_unicorns(smaller,black).png")
unicorn_white = Image.open("shaved_unicorns(smaller).png")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def make_cards(line, background_color, text_color, border_color, icon, name):
    
    # This takes the text from the opened file, and wraps it.
    # The bigger the number, the wider the text on the card.
    text = textwrap.wrap(line, width = 20)
    
    # Had to go down the the microseconds so the program wouldn't time out.
    date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")

    # Size is in pixels, corresponds roughly to a 2.25" x 3.5" card.
    card_width, card_height = 747, 1122
    
    # RGB works better with some fonts. '.new' takes parameters only in 
    # "width, height" order, can't switch.
    img = Image.new("RGB", (card_width, card_height), background_color)
    draw = ImageDraw.Draw(img)
    
    # The number is the size of the font
    font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 60)
    footer_font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 20)
    
    # This is key to keeping the line height consistent by making the line 
    # height equal to the size of the tallest character that will be produced
    # for that font size.  The number added onto the end increases the
    # line spacing and keeps the text from getting too close to each 
    # other between lines.
    line_spacing = draw.textsize('A', font=font)[1] + 30

    # "0" starts the text writing at the top of the card, bigger numbers
    # lower the starting coordinate.
    current_height = 100
    
    for line in text:
        # This computes the width of the lines to be drawn on the card
        # so that the text wraps correctly as defined above.
        w, h = draw.textsize(line, font = font)
        # Dividing by a larger number moves the text to the left, as 
        # '(card_width-w)/2, current_height)' is the coordinates of
        # where the text drawing will start.
        draw.text(((card_width-w)/2, current_height), line, text_color,
             font = font)
        # This is how far down the next line will be written at.
        current_height += line_spacing

    # Or whatever you like for your footer
    footer = "F*cking Unicorns Against Humanity"
    # The numbers are the coordinates of the placement of the text on the card
    draw.text((230, 980), footer, text_color, font = footer_font)
    
    # Must save image before pasting the icon on the card.
    img.save("2014.png")
    # And must reopen it too!
    card = Image.open("2014.png")
    # Paste the icon at the numbered coordinates.
    card.paste(icon, (100, 950))
    # This creates individual cards with a nice date stamp on them.
    card.save(name + date_string + ".png", timestamp=3, boldfont=1, textpos='bc')


# Program starts prompting here.
background_color = raw_input("What background color? \nwhite or black? ----> ")

# The user can name their set, and I made sure it gets turned into a string
name = str(raw_input("What shall we name this set?\n---> "))

# This sets the parameters that make_cards calls.
if background_color in ("White", "white", "w"):
    # Open file as read only.
    w = open("List_whites.txt", "r")
    text_color = BLACK
    background_color = WHITE
    border_color = "black"
    icon = unicorn_white
    
if background_color in ("Black", "black", "b"):
    w = open("List_blacks.txt")
    text_color = WHITE
    background_color = BLACK
    border_color = "white"
    icon = unicorn_black

# Will create a card for each line in the file.
for line in w.readlines():
    make_cards(line, background_color, text_color, border_color, icon, name)
