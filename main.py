from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap


## EDIT THE TEXT AND THE FONT OF SECTIONS ##
City = "Punta Cana"
City_fontName = 'Plumpfull.ttf'

Country = "Dominican Republic"
Country_fontName = 'Plumpfull.ttf'

S1 = "I'M NELSON NIGEL & THIS IS MY KIDMOTO JOURNEY"
S1_fontName = 'Plumpfull.ttf'

S3 = "THANK YOU FOR YOUR BUSINESS AND SAFE TRAVELS"
S3_fontName = 'Plumpfull.ttf'

S4 = "DOWNLOAD THE KIDMOTO APP"
S4_fontName = 'Plumpfull.ttf'


## BACKGROUND PICTURE ##
backGroundimg = 'road.jpg'


## OPEN THE BACKGROUND IMAGE, GET THE SIZE OF THE IMAGE ##
img = Image.open(backGroundimg)
width, height = img.size
draw = ImageDraw.Draw(img)


## S1 TEXT ##
S1_font = ImageFont.truetype(S1_fontName, 70)
text = S1
text_width, text_height = draw.textsize(text, font=S1_font)
x = (width - text_width) / 2
y = 110
draw.text((x, y), text, font = S1_font, fill = (0, 0, 0))


## CITY TEXT ##
city_font = ImageFont.truetype(City_fontName, 400)
text = City
text_width, text_height = draw.textsize(text, font=city_font)
x = (width - text_width) / 2
y = 1100
draw.text((x, y), text, font = city_font, fill = (0, 0, 0))


## COUNTRY TEXT ##
country_font = ImageFont.truetype(Country_fontName, 200)
text = Country
text_width, text_height = draw.textsize(text, font=country_font)
x_country = (width - text_width) / 2 + 30
y = 1500
draw.text((x_country, y), text, font = country_font, fill = (0, 0, 0))


## S3 TEXT ##
S3_font = ImageFont.truetype(S3_fontName, 70)
lines = textwrap.wrap(S3, width=30)
text_width, line_heights = [], []
spacing = 20
for line in lines:
    line_width, line_height = draw.textsize(line, font=S3_font)
    text_width.append(line_width)
    line_heights.append(line_height)
text_height = sum(line_heights) + spacing * (len(lines) - 1)
x = (width - max(text_width)) / 2
y = 2000 - text_height / 2

for line, line_height in zip(lines, line_heights):
    line_width, _ = draw.textsize(line, font=S3_font)
    draw.text(((width - line_width) / 2, y), line, font=S3_font, fill=(0, 0, 0))
    y += line_height + spacing


## S4 TEXT ##
S4_font = ImageFont.truetype(S4_fontName, 70)
text = S4
text_width, text_height = draw.textsize(text, font=S4_font)
x = (width - text_width) / 2
y = 4000
draw.text((x, y), text, font = S4_font, fill = (0, 0, 0))



img.show()
img.save(City+'.jpg')