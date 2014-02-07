# This is the program to use if you want to print cards out on 
# a home printer or at Kinko's.
# Simply save your card ideas in separate .txt files labled:
# "List_whites.txt" and "List_blacks.txt" in the working directory
# and the prompts will do the rest!

# Please install Pillow and its libraries
# (and uninstall PIL if you are using it)

from PIL import ImageFont, Image, ImageDraw, ImageOps
import textwrap
import datetime

def generate_cards():
    text = ""
    border_color = ""
    base = Image.new("RGB", (632, 825), "white")
     
    line01 = ""
    line02 = ""
    line03 = ""
    line04 = ""
    line05 = ""
    line06 = ""
    line07 = ""
    line08 = ""
    line09 = ""
    line10 = ""
    line11 = ""
    line12 = ""
    line13 = ""
    line14 = ""
    line15 = ""
    line16 = ""
    line17 = ""
    line18 = ""
    line19 = ""
    line20 = ""
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    background_color = raw_input("""What background color would you like, 
        white or black?----> """)
    name = str(raw_input("What shall we name this set?\n----> "))
    
    if background_color in ("White", "white", "w"):
        text = open("List_whites.txt", "r")
        border_color = "black"
        text_color = BLACK
        
    if background_color in ("Black", "black", "b"):
        text = open("List_blacks.txt")
        border_color = "white"
        text_color = WHITE
        
    def make_cards(background_color, text_color, border_color, name):

        ########## Make Card 01 ###############
        text01 = textwrap.wrap(line01, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")

        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text01:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing

        img.save("a1.png")
        x = Image.open("a1.png")
        # I put borders around these cards to make them easier to cut out
        # The border is one pixel wide on EACH side, take that into 
        # consideration when calculating total dimensions and 
        # paste coordinates
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("a1.png")


        ########## Make Card 02 ######### 
        text02 = textwrap.wrap(line02, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text02:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing

        img.save("a2.png")
        x = Image.open("a2.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("a2.png")


        ########## Make Card 03 ############
        text03 = textwrap.wrap(line03, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text03:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing

        img.save("a3.png")
        x = Image.open("a3.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("a3.png")



        ########## Make Card 04 #############
        text04 = textwrap.wrap(line04, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text04:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("a4.png")
        x = Image.open("a4.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("a4.png")
        

        ########## Make Card 05 #############
        text05 = textwrap.wrap(line05, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text05:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("b1.png")
        x = Image.open("b1.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("b1.png")


        ########## Make Card 06 #############
        text06 = textwrap.wrap(line06, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text06:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("b2.png")
        x = Image.open("b2.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("b2.png")


        ########## Make Card 07 #############
        text07 = textwrap.wrap(line07, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text07:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("b3.png")
        x = Image.open("b3.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("b3.png")


        ########## Make Card 08 #############
        text08 = textwrap.wrap(line08, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text08:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("b4.png")
        x = Image.open("b4.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("b4.png")


        ########## Make Card 09 #############
        text09 = textwrap.wrap(line09, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text09:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("c1.png")
        x = Image.open("c1.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("c1.png")


        ########## Make Card 10 #############
        text10 = textwrap.wrap(line10, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text10:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("c2.png")
        x = Image.open("c2.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("c2.png")


        ########## Make Card 11 #############
        text11 = textwrap.wrap(line11, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text11:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("c3.png")
        x = Image.open("c3.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("c3.png")


        ########## Make Card 12 #############
        text12 = textwrap.wrap(line12, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text12:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("c4.png")
        x = Image.open("c4.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("c4.png")


        ########## Make Card 13 #############
        text13 = textwrap.wrap(line13, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text13:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("d1.png")
        x = Image.open("d1.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("d1.png")


        ########## Make Card 14 #############
        text14 = textwrap.wrap(line14, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text14:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("d2.png")
        x = Image.open("d2.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("d2.png")


        ########## Make Card 15 #############
        text15 = textwrap.wrap(line15, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text15:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("d3.png")
        x = Image.open("d3.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("d3.png")


        ########## Make Card 16 #############
        text16 = textwrap.wrap(line16, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text16:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("d4.png")
        x = Image.open("d4.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("d4.png")


        ########## Make Card 17 #############
        text17 = textwrap.wrap(line17, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text17:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("e1.png")
        x = Image.open("e1.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("e1.png")


        ########## Make Card 18 #############
        text18 = textwrap.wrap(line18, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text18:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("e2.png")
        x = Image.open("e2.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("e2.png")


        ########## Make Card 19 #############
        text19 = textwrap.wrap(line19, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text19:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("e3.png")
        x = Image.open("e3.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("e3.png")


        ########## Make Card 20 #############
        text20 = textwrap.wrap(line20, width = 20)
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S:%f")
        card_width, card_height = 156, 163
        img = Image.new("RGB", (card_width, card_height), background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("/usr/share/fonts/Helvetica_Bold.ttf", 13)

        line_spacing = draw.textsize('A', font=font)[1] + 10

        current_height = 10
        for line in text20:
            w, h = draw.textsize(line, font = font)
            draw.text(((card_width-w)/2, current_height), line, text_color,
                font = font)
            current_height += line_spacing
            
        img.save("e4.png")
        x = Image.open("e4.png")
        y = ImageOps.expand(x, border = 1, fill = border_color)
        y.save("e4.png")


        # I found out this is key.  I thought just saving them 
        # would keep them open, but they must reopened after saving.
        card01 = Image.open("a1.png")
        card02 = Image.open("a2.png")
        card03 = Image.open("a3.png")
        card04 = Image.open("a4.png")
        card05 = Image.open("b1.png")
        card06 = Image.open("b2.png")
        card07 = Image.open("b3.png")
        card08 = Image.open("b4.png")
        card09 = Image.open("c1.png")
        card10 = Image.open("c2.png")
        card11 = Image.open("c3.png")
        card12 = Image.open("c4.png")
        card13 = Image.open("d1.png")
        card14 = Image.open("d2.png")
        card15 = Image.open("d3.png")
        card16 = Image.open("d4.png")
        card17 = Image.open("e1.png")
        card18 = Image.open("e2.png")
        card19 = Image.open("e3.png")
        card20 = Image.open("e4.png")

        # This pastes the "cards" in the correct position.
        # All numbers are pixel coordinates.
        base.paste(card01, (0, 0))
        base.paste(card02, (158, 0))
        base.paste(card03, (316, 0))
        base.paste(card04, (474, 0))
        base.paste(card05, (0, 165))
        base.paste(card06, (158, 165))
        base.paste(card07, (316, 165))
        base.paste(card08, (474, 165))
        base.paste(card09, (0, 330))
        base.paste(card10, (158, 330))
        base.paste(card11, (316, 330))
        base.paste(card12, (474, 330))
        base.paste(card13, (0, 495))
        base.paste(card14, (158, 495))
        base.paste(card15, (316, 495))
        base.paste(card16, (474, 495))
        base.paste(card17, (0, 660))
        base.paste(card18, (158, 660))
        base.paste(card19, (316, 660))
        base.paste(card20, (474, 660))
        
        
        # Saving base with date_string so it creates unique files
        base.save(name + date_string + ".png", timestamp=3, boldfont=1, textpos='bc')


    # So this while loop reads twenty lines from the file at a time,
    # and saves them with an individual name.  Keeping the break 
    # after line01 allows bases to be created with less than twenty images
    while True:
        line01 = text.readline()
        if not line01:
            break
        
        line02 = text.readline()
        line03 = text.readline()
        line04 = text.readline()
        line05 = text.readline()
        line06 = text.readline()
        line07 = text.readline()
        line08 = text.readline()
        line09 = text.readline()
        line10 = text.readline()
        line11 = text.readline()
        line12 = text.readline()
        line13 = text.readline()
        line14 = text.readline()
        line15 = text.readline()
        line16 = text.readline()
        line17 = text.readline()
        line18 = text.readline()
        line19 = text.readline()
        line20 = text.readline()
        # Ok, now I can do something with the variables I have named
        print line01, line02, line03, line04, "ect...\n======"
        make_cards(background_color, text_color, border_color, name)           

generate_cards()
