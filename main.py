from PIL import Image, ImageDraw, ImageFont
import textwrap
import pandas as pd


## CSV FILE ##
csv_file = 'Excel/Book1.csv'
try:
    df = pd.read_csv(csv_file, encoding='ISO-8859-1')
except UnicodeDecodeError:
    print("Error: Could not read the file")

fontName = 'Fonts/Plumpfull.ttf'


## EDIT THE TEXT AND THE FONT OF SECTIONS ##

column_City = df['City'].tolist()
column_Country = df['Country'].tolist()

# Loop over the values in the column_Values variable
for i in range(len(column_City)):
    
    city = column_Country[i] 
    City = city
    City_fontName = fontName

    country = column_City[i]
    Country = country
    Country_fontName = fontName

    S1 = "I'M NELSON NIGEL & THIS IS MY KIDMOTO JOURNEY"
    S1_fontName = fontName

    S3 = "THANK YOU FOR YOUR BUSINESS AND SAFE TRAVELS"
    S3_fontName = fontName

    S4 = "DOWNLOAD THE KIDMOTO APP"
    S4_fontName = fontName


    ## BACKGROUND PICTURE ##
    backGroundimg = 'Images/Background_img/road.jpg'


    ## OPEN THE BACKGROUND IMAGE, GET THE SIZE OF THE IMAGE ##
    img = Image.open(backGroundimg)
    width, height = img.size
    draw = ImageDraw.Draw(img)


    ## S1 TEXT ##
    S1_font = ImageFont.truetype(S1_fontName, int(height*0.023))
    text = S1
    text_width, text_height = draw.textsize(text, font=S1_font)
    x = (width - text_width) / 2
    y = int(height*0.027)
    draw.text((x, y), text, font = S1_font, fill = (0, 0, 0))

    ## City Text ##

    city_font_size_max = 400
    city_font_size_min = 250
    city_fontName = fontName

    # Calculate font size based on string length
    city_font_size = max(min(city_font_size_max, int(city_font_size_max * 10 / len(City))), city_font_size_min)

    city_font = ImageFont.truetype(city_fontName, city_font_size)
    text = City
    text_width, text_height = draw.textsize(text, font=city_font)
    max_width = int(width*0.9)  # maximum width for the text
    if text_width > max_width:
            lines = textwrap.wrap(text, width=int(max_width/text_width*len(text)))
    else:
        lines = [text]
    y = int(height*0.25) - (text_height*(len(lines)-1))/2  # center the text vertically with equal spacing
    for line in lines:
        text_width, text_height = draw.textsize(line, font=city_font)
        x = (width - text_width) / 2
        draw.text((x, y), line, font=city_font, fill=(0, 0, 0))
        y += text_height


    ## COUNTRY TEXT ##
    country_font_size = int(city_font_size * 0.8)
    country_font = ImageFont.truetype(Country_fontName, country_font_size)
    text = Country
    text_width, text_height = draw.textsize(text, font=country_font)
    x_country = (width - text_width) / 2 + int(width*0.016)
    y_country = int(height*0.366) + int(city_font_size * 1.2)  # adjust the y-coordinate based on the size of City Text letters
    draw.text((x_country, y_country), text, font = country_font, fill = (255, 255, 255))


    ## S3 TEXT ##
    S3_font = ImageFont.truetype(S3_fontName, int(height*0.023))
    lines = textwrap.wrap(S3, width=30)
    text_width, line_heights = [], []
    spacing = int(height*0.005)
    for line in lines:
        line_width, line_height = draw.textsize(line, font=S3_font)
        text_width.append(line_width)
        line_heights.append(line_height)
    text_height = sum(line_heights) + spacing * (len(lines) - 1)
    x = (width - max(text_width)) / 2
    y = int(height*0.82) - (len(lines)-1)*max(line_heights) / 2 # center the text vertically
    for i, line in enumerate(lines):
        line_width, line_height = draw.textsize(line, font=S3_font)
        x = (width - line_width) / 2  # center the line horizontally
        draw.text((x, y), line, font=S3_font, fill=(0, 0, 0))
        y += line_heights[i] + spacing

    
    ## S4 TEXT
    S4_font = ImageFont.truetype(S4_fontName, int(height * 0.023))
    text = S4
    text_width, text_height = draw.textsize(text, font=S4_font)
    x = (width - text_width) / 2
    y = int(height * 0.92)
    draw.text((x, y), text, font=S4_font, fill=(0, 0, 0))

    ## SAVE THE IMAGE

    #img.show()
    img.save('Images/'+City+'.jpg')
        



