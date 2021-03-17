import os

#need to install module
import img2pdf
import PyPDF2
#######################
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import time
import shutil
from natsort import natsorted
import pathlib
import time

#######################
cwd = os.getcwd()

inputpath = os.path.join(cwd,'input')
outputpath = os.path.join(cwd,'output')
trashpath = os.path.join(cwd,'trash')
def main():

    while True:
        #Store and update the file list in input folder in the list.
        fltr_input_list = [filename for filename in os.listdir(inputpath) if not filename.startswith('.')]
        input_list = natsorted(fltr_input_list)
        for i ,a in enumerate(input_list):
            #set filename
            filename = a


            

            
            mainpath = os.path.join(inputpath,filename)
            fltr_main_list = [filename for filename in os.listdir(mainpath) if not filename.startswith('.')]
            main_list = natsorted(fltr_main_list)

            


      

            #Convert images in mainpath to PDF one by one
            for j,b in enumerate(main_list):
                #Set save name
                fname = str(i) + "_"  + str(j) + '.jpg'
                picb_path = os.path.join(mainpath,b)
                pica_path = os.path.join
                #Path of each image
                out_path = os.path.join(outputpath,str(fname))
                os.rename(picb_path,out_path)
                
            shutil.rmtree(mainpath)
            print(filename,'finished')
                

           
        time.sleep(3)
        print('ALL FINISHED')
        break

main()