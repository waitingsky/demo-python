from PIL import Image

# 定义将要解析的图片和目标文件
IMG = "test.jpg"
WIDTH = 80
HEIGHT = 60
OUTPUT = "test.txt"

# 我们定义的不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    
    # 灰度公式
    gray = int(0.299 * r + 0.587 * g + 0.114 * b)
    #gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


# 执行
im = Image.open(IMG)
im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

txt = ""

#将图片的每一个像素进行处理，类似二维数组
for i in range(HEIGHT):
    for j in range(WIDTH):
        #getpixel()函数的参数是由每个像素点在图片中的相对位置（w，h）组成的元组
        #返回值是一个代表图片像素值的(r,g,b,alpha)元组
        txt += get_char(*im.getpixel((j,i)))
    txt += '\n'

# 输出到控制台
print(txt)

#字符画输出到文件
with open(OUTPUT,'w') as f:
    f.write(txt)
