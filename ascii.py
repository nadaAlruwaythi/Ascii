from PIL import Image

ASCII_CHARS=['@','#','S','$','*','-']


#resize
def resize_image(image,new_width=100):
    width,height=image.size
    ratio=height/width
    new_height=int(new_width*ratio)
    resize_image=image.resize((new_width,new_height))
    return(resize_image)
    
# convert each pixcel to grayscale
def grayify(image):
    grayify_image=image.convert('L')
    return(grayify_image)

#convert pixcel to ascill
def pixcel_ascill(image):
    pixels=image.getdata()
    characters="".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return (characters)


def main():
    path= input('Enter your path:')
    try:
        image=PIL.Image.open(path)
        
    except:
        print(path,'is not valid')
        
    new_image=pixcel_ascill(grayify(resize_image(image)))
    
    pixcel_count=len(new_image)
    ascill_image='\n'.join(new_image[i:(i+new_width)] for i in range(0,pixcel_count,new_width))
    print(ascill_image)
    
    with open('ascii.txt','w') as f:
        f.write(ascill_image)
        
    