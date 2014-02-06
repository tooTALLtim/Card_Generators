from PIL import ImageFont, Image, ImageDraw, ImageOps
import textwrap, datetime

unicorn_black = Image.open("shaved_unicorns(smaller,black).png")
unicorn_white = Image.open("shaved_unicorns(smaller).png")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def make_cards(line, background_color, text_color, border_color, icon):
    
    # this takes the text from the opened file, and wraps it.
    # The bigger the number, the wider the text on the card.
    text = textwrap.wrap(line, width = 20)
    
    # Had to go down the the microseconds so the program wouldn't time out
    date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")

    # Size is in pixels
    card_width, card_height = 747, 1122
    
    # RGB works better with some fonts. .new takes dimensions only in 
    # "width, height" order. Can't switch :P
    img = Image.new("RGB", (card_width, card_height), background_color)
    draw = ImageDraw.Draw(img)
    
    # The number is the size of the font
    font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 60)
    footer_font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 20)
    
    line_spacing = draw.textsize('A', font=font)[1] + 1

    # Starts the text writing at the top of the card for "0"
    current_height = 100
    
    for line in text:
        w, h = draw.textsize(line, font = font)
        draw.text(((card_width-w)/2, current_height), line, text_color, font = font)
        current_height += line_spacing + 30
    
    footer = "F*cking Unicorns Against Humanity"
    draw.text((230, 980), footer, text_color, font = footer_font)
    
    img.save("2014.png")
    card = Image.open("2014.png")
    card.paste(icon, (100, 950))
    card.save(date_string + ".png", timestamp=3, boldfont=1, textpos='bc')


# Program starts prompting here.
background_color = raw_input("What background color? \n----> ")

# I love the code below! Makes things easier
if background_color in ("White", "white", "w"):
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
    
for line in w.readlines():
    make_cards(line, background_color, text_color, border_color, icon)
    

