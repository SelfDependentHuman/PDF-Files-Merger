###Imported Libraries##########################################################
import os
import PyPDF2

###Functions Definition########################################################
def list_of_PDFs(loc, file_type):
    """
    Function to return a Python List of all files of any given file type input as
    argument file_type, all of which are found in location stated in argument loc.

    Variables:
        loc: directory to loop in to search for files of type file_type
        file_type: file extension i.e., ".pdf"
        Uses os libary

    Based on user Gulzar´s response to "how to iterate over files in a given directory" on StackOverflow:
    https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory?newreg=6230eb0aa56f4a5b89884ee857652c97

    User Gulzar:
    https://stackoverflow.com/users/913098/gulzar
    """
    PDFsList=[]
    tmpList=[]
    directory = os.fsencode(loc)
    PDFsList.append(str(os.fsdecode(directory)) + "\\")

    for file in os.listdir(directory):
         filename = os.fsdecode(file)
         if filename.endswith(file_type):
             tmpList.append(str(os.fsdecode(directory)) + "\\" + str(filename))
             continue
         else:
             continue
    tmpList.sort()
    PDFsList=PDFsList+tmpList
    return PDFsList

def merge_PDFs(files_arr):
    """
    Function to merge an array of PDF files into a single PDF file.

    Arguments:
        files_arr: list of strings, each representing a PDF file location.
    """
    mergeFile=PyPDF2.PdfFileMerger()
    filesloc=files_arr[1:]
    for i in filesloc:
        mergeFile.append(PyPDF2.PdfFileReader(i))
    mergeFile.write(files_arr[0]+"Merged Files.pdf")

####Main Routine###############################################
print("Enter a directory pointing ")
list_of_files=list_of_PDFs(input(),".pdf")
merge_PDFs(list_of_files)
