# Please install Pillow and its libraries
# (and uninstall PIL if you are using it)

from PIL import ImageFont, Image, ImageDraw, ImageOps
import textwrap, datetime


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# The text for the card
line = "F*cking Unicorns Against Humanity"

def make_cards(line, background_color, text_color, border_color, name):

    # This takes the text from the opened file, and wraps it.
    # The bigger the number, the wider the text on the card.
    # I wanted it to be only one word per line, so I kept it small.
    text = textwrap.wrap(line, width = 10)
    
    # Had to go down the the microseconds so the program wouldn't time out.
    date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")

    # Size is in pixels, corresponds roughly to a 2.25" x 3.5" card.
    card_width, card_height = 747, 1122
    
    # RGB works better with some fonts. '.new' takes parameters only in 
    # "width, height" order, can't switch.
    img = Image.new("RGB", (card_width, card_height), background_color)
    draw = ImageDraw.Draw(img)
    
    # The number is the size of the font
    font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 120)

    # This is key to keeping the line height consistent by making the line 
    # height equal to the size of the tallest character that will be produced
    # for that font size.  The number added onto the end increases the
    # line spacing and keeps the text from getting too close to each 
    # other between lines.
    line_spacing = draw.textsize('A', font=font)[1] + 1

    # "0" starts the text writing at the top of the card, bigger numbers
    # lower the starting coordinate.
    current_height = 100
    
    for line in text:
        # I liked having the text start at the left side of the card, but
        # not at the edge, so it starts at 100 pixels away from the 
        # left side of the card, remember: (width, height).
        draw.text((100, current_height), line, text_color, font = font)
        # This is how far down the next line will be written at.
        current_height += line_spacing + 30
        
    # This creates individual cards with a nice date stamp on them.
    img.save(name + "back" +date_string + ".png", timestamp=3, boldfont=1,
         textpos='bc')


background_color = raw_input("What background color? \n----> ")

# This sets the parameters that make_cards calls.
if background_color in ("White", "white", "w"):
    text_color = BLACK
    background_color = WHITE
    border_color = "black"
    name = "white_"
    make_cards(line, background_color, text_color, border_color, name)
    
if background_color in ("Black", "black", "b"):
    text_color = WHITE
    background_color = BLACK
    border_color = "white"
    name = "black_"
    make_cards(line, background_color, text_color, border_color, name)# Please install Pillow and its libraries
# (and uninstall PIL if you are using it)

from PIL import ImageFont, Image, ImageDraw, ImageOps
import textwrap, datetime


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# The text for the card
line = "F*cking Unicorns Against Humanity"

def make_cards(line, background_color, text_color, border_color, name):

    # This takes the text from the opened file, and wraps it.
    # The bigger the number, the wider the text on the card.
    # I wanted it to be only one word per line, so I kept it small.
    text = textwrap.wrap(line, width = 10)
    
    # Had to go down the the microseconds so the program wouldn't time out.
    date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")

    # Size is in pixels, corresponds roughly to a 2.25" x 3.5" card.
    card_width, card_height = 747, 1122
    
    # RGB works better with some fonts. '.new' takes parameters only in 
    # "width, height" order, can't switch.
    img = Image.new("RGB", (card_width, card_height), background_color)
    draw = ImageDraw.Draw(img)
    
    # The number is the size of the font
    font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 120)

    # This is key to keeping the line height consistent by making the line 
    # height equal to the size of the tallest character that will be produced
    # for that font size.  The number added onto the end increases the
    # line spacing and keeps the text from getting too close to each 
    # other between lines.
    line_spacing = draw.textsize('A', font=font)[1] + 1

    # "0" starts the text writing at the top of the card, bigger numbers
    # lower the starting coordinate.
    current_height = 100
    
    for line in text:
        # I liked having the text start at the left side of the card, but
        # not at the edge, so it starts at 100 pixels away from the 
        # left side of the card, remember: (width, height).
        draw.text((100, current_height), line, text_color, font = font)
        # This is how far down the next line will be written at.
        current_height += line_spacing + 30
        
    # This creates individual cards with a nice date stamp on them.
    img.save(name + "back" +date_string + ".png", timestamp=3, boldfont=1,
         textpos='bc')


background_color = raw_input("What background color? \n----> ")

# This sets the parameters that make_cards calls.
if background_color in ("White", "white", "w"):
    text_color = BLACK
    background_color = WHITE
    border_color = "black"
    name = "white_"
    make_cards(line, background_color, text_color, border_color, name)
    
if background_color in ("Black", "black", "b"):
    text_color = WHITE
    background_color = BLACK
    border_color = "white"
    name = "black_"
    make_cards(line, background_color, text_color, border_color, name)
