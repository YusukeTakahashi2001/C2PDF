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
        for book_list in input_list:
            save_book_path = os.path.join(outputpath,book_list)
            os.makedirs(save_book_path)

            rollpath = os.path.join(inputpath,book_list)
            roll_list = natsorted(os.listdir(rollpath))

            for a in roll_list:
                #set filename
                fileroll = a

                #Path of folder that contains images
                mainpath = os.path.join(rollpath,fileroll)
                fltr_main_list = [filename for filename in os.listdir(mainpath) if not filename.startswith('.')]
                main_file_list = natsorted(fltr_main_list)


                #Create a new folder to combine multiple pdfs
                editpath = os.path.join(cwd,'edit')

                
                try:
                    os.makedirs(editpath)
                except :
                    shutil.rmtree(editpath)
                    os.makedirs(editpath)

        

                #Convert images in mainpath to PDF one by one
                for i in main_file_list:
                    #Set save name
                    editi = pathlib.PurePath(i).stem
                    pdf_name = editpath + "/" +  "PDF_" + str(editi) + ".pdf"

                    #Path of each image
                    img_path = os.path.join(mainpath,i)
                    #Only read image file
                    try:
                        img = Image.open(img_path)
                    except :
                        continue
                    #If the extension is '.png',convert to '.jpg'
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                        img.save(img_path, "JPEG", quality=95)
                    else:
                        pass

                    #Convert each image to pdf
                    cov_pdf = img2pdf.convert(img_path)

                    #Save pdf file to editpath
                    file = open(pdf_name, "wb")
                    file.write(cov_pdf)
                    img.close()
                    file.close()

                #Combine all PDFs in editpath.
                merge = PyPDF2.PdfFileMerger()
                for j in natsorted(os.listdir(editpath)):
                    merge.append(editpath + "/" + j)
                #Save PDF in output folder
                outputname = save_book_path + "/" + fileroll + '.pdf'
                merge.write(outputname)
                merge.close()
                #Delete edit folder
                shutil.rmtree(editpath)
                
                shutil.move(mainpath,trashpath)

                print(fileroll,'End')
            
            shutil.rmtree(rollpath)
            time.sleep(3)
            print(book_list,'FINISHED')

    
        time.sleep(3)
        print('ALL FINISHED')
        break

main()
