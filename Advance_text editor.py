from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from PIL import Image
import pytesseract
import PyPDF2 
def newFile():
    global file
    root.title("Untitled-text editor")
    file = None
    TextArea.delete(1.0, END)

def convert(file_name):
    
    audio_file=(file_name)
    
    #initilize the recognizer
    r=sr.Recognizer()
    
    
    # read audio file
    with sr.AudioFile(audio_file)as source:
        audio=r.record(source)
        
        
    try:
            #print("audio file contains: "+ r.recognize_google(audio))
        kun=r.recognize_google(audio)
        return kun  
    except sr.UnknownValueError:
        print("Google speech Recognition could not understand audio")
        # to handle error
    except sr.RequestError:
        print("couldn't get the results from Google Speech Recognition")
def audioFile():
    global file
    file=askopenfilename(defaultextension=".wav",filetypes=[("All files","*.*"),("audio file","*.wav")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " -text editor")
        TextArea.delete(1.0,END)
        f=convert(file)
        TextArea.insert(1.0,f)
def speech_female():
    u=TextArea.get(1.0,END)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',130)
    engine.say(u)
    engine.runAndWait()
def speech_male():
    u=TextArea.get(1.0,END)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',130)
    engine.say(u)
    engine.runAndWait()
def imagefile():
    global file
    file = askopenfilename(defaultextension=".jpg",
                           filetypes=[("All Files", "*.*"),
                                     ("Images", "*.jpg")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - text editor")
        TextArea.delete(1.0, END)
        pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
 
# Create an image object of PIL library
        image = Image.open(file)
 
# pass image into pytesseract module
# pytesseract is trained in many languages
        image_to_text = pytesseract.image_to_string(image, lang='eng')
 
# Print the text
        TextArea.insert(1.0, image_to_text)
def openpdf(file):
    pdfFileObj = open(file, 'rb') 
  
# creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
      
    # creating a page object 
    pageObj = pdfReader.getPage(0) 
      
    # extracting text from page 
    TextArea.insert(1.0,pageObj.extractText())
      
    # closing the pdf file object 
    pdfFileObj.close() 
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - text editor")
        TextArea.delete(1.0, END)
        if('.pdf' in file):
            openpdf(file)
        else:
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()
def save_a():
    mytext=TextArea.get(1.0,END)
    file = asksaveasfilename(initialfile = 'Untitled.mp3', defaultextension=".mp3",
                           filetypes=[("All Files", "*.*"),
                                     ("Audio file", "*.mp3")])
    
    language = 'en'
    myobj = gTTS(text=mytext, lang=language)
    myobj.save(file)
def save_asFile():
    global file
    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file =="":
        file = None

    else:
            #Save as a new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + " - text editor")
        print("File Saved")    
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - text editor")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<>"))

def copy():
    TextArea.event_generate(("<>"))

def paste():
    TextArea.event_generate(("<>"))

def about():
    showinfo("advance text editor", "advance text editor by Nihal and Gaurav")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled -text editor")
   # root.wm_iconbitmap("1.ico")
    root.geometry("644x600")

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)
    
    #FileMenu.add_command(label="Audio",command=audioFile)
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_command(label="Save as",command=save_asFile)
    FileMenu.add_command(label="Save as audio file",command=save_a)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends

    # Help Menu Starts
    AudioMenu = Menu(MenuBar, tearoff=0)
    AudioMenu.add_command(label="audio to text",command=audioFile)
    AudioMenu.add_command(label="speech loud male audio",command=speech_male)
    AudioMenu.add_command(label="speech loud female audio",command=speech_female)
    MenuBar.add_cascade(label="Audio",menu=AudioMenu)
    ImageMenu=Menu(MenuBar,tearoff=0)
    ImageMenu.add_command(label="Extract text from image",command=imagefile)
    MenuBar.add_cascade(label="Image",menu=ImageMenu)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About text editor", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    

    root.mainloop()

