# Importing Image class from PIL module
from PIL import Image
import os

directory = 'image folder here'

def list_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if ".png" in file:
                file_list.append(os.path.join(root, file))
    return file_list

def cropper(filelist, nocrops, directory):
    directory += '/processedimgs'
    print(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for file in filelist:
        
        im = Image.open(file)
        width, length = im.size
        wdth, lnth, wdths, lnths = 0,0,[],[]
       
        while wdth < width:
            wdths.append(round(wdth))
            wdth += width/nocrops
        
        while lnth < length:
            lnths.append(round(lnth))
            lnth += length/nocrops
        
        for x in wdths:
            for y in lnths:
                im1 = im.crop((x, y, x + width/nocrops -1, y + length/nocrops -1 ))
                im2 = im1.save(f"{directory}/image{filelist.index(file)} {wdths.index(x)} {lnths.index(y)}.png")

cropper(list_files(directory), round(float(input("input"))**0.5), directory)
