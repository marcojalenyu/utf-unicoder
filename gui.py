from tkinter import *
from tkinter import filedialog
import converter
import reverter

def convertToUTF8():
    inputText = convertInputEntry.get()
    outputText = converter.check_and_convert_to_utf8(inputText)
    outputBox.config(state="normal")
    outputBox.delete(1.0, END)
    outputBox.insert(END, outputText)
    outputBox.config(state="disabled")

def convertToUTF16():
    inputText = convertInputEntry.get()
    outputText = converter.check_and_convert_to_utf16(inputText)
    outputBox.config(state="normal")
    outputBox.delete(1.0, END)
    outputBox.insert(END, outputText)
    outputBox.config(state="disabled")

def convertToUTF32():
    inputText = convertInputEntry.get()
    outputText = converter.check_and_convert_to_utf32(inputText)
    outputBox.config(state="normal")
    outputBox.delete(1.0, END)
    outputBox.insert(END, outputText)
    outputBox.config(state="disabled")

def revertFromUTF8():
    inputText = inputEntry.get()
    outputText = reverter.check_and_revert_utf8(inputText)
    outputBox.config(state="normal")
    outputBox.delete(1.0, END)
    outputBox.insert(END, outputText)
    outputBox.config(state="disabled")

def revertFromUTF16():
    inputText = inputEntry.get()
    outputText = reverter.check_and_revert_utf16(inputText)
    outputBox.config(state="normal")
    outputBox.delete(1.0, END)
    outputBox.insert(END, outputText)
    outputBox.config(state="disabled")

def revertFromUTF32():
    inputText = inputEntry.get()
    outputText = reverter.check_and_revert_utf32(inputText)
    outputBox.config(state="normal")
    outputBox.delete(1.0, END)
    outputBox.insert(END, outputText)
    outputBox.config(state="disabled")

def exportOutput():
    # Ask user to select a file path to save the output
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    # If the user cancels the file dialog, return
    if file_path == "":
        return

    # Get the output text from the text box
    outputText = outputBox.get(1.0, END)
    with open(file_path, "w") as file:
        file.write(outputText)

root = Tk()

# Title and icon for the window
root.title("Unicode Converter/Translator")

try:
    root.iconbitmap("unicode.ico")
except:
    pass

titleLabel = Label(root, text="Unicode Converter/Translator")
titleLabel.pack()

#convert input section
inputLabel = Label(root, text="Unicode (U+) to UTF")
inputLabel.pack(pady=(5,0))

convertInputFrame = Frame(root)
convertInputFrame.pack()

convertInputLabel = Label(convertInputFrame, text="U+")
convertInputLabel.grid(row=0, column=0)

convertInputEntry = Entry(convertInputFrame, width=30)
convertInputEntry.grid(row=0, column=1)

#Convert buttons
convertButtonFrame = Frame(root)
convertButtonFrame.pack(padx=10, pady=10)

convertLabel = Label(convertButtonFrame, text="Convert to:")
convertLabel.grid(row=0, column=0)

convertButton = Button(convertButtonFrame, text="UTF-8", command=convertToUTF8)
convertButton.grid(row=0, column=1, padx = 5)

convertButton = Button(convertButtonFrame, text="UTF-16", command=convertToUTF16)
convertButton.grid(row=0, column=2, padx = 5)

convertButton = Button(convertButtonFrame, text="UTF-32", command=convertToUTF32)
convertButton.grid(row=0, column=3, padx = 5)

#revert input section

inputLabel = Label(root, text="UTF to Unicode (U+)")
inputLabel.pack(pady=(5,0))

inputEntry = Entry(root, width=30)
inputEntry.pack()

#Revert Buttons
revertButtonFrame = Frame(root)
revertButtonFrame.pack(padx=10, pady=10)

revertLabel = Label(revertButtonFrame, text="Translate from:")
revertLabel.grid(row=0, column=0)

convertButton = Button(revertButtonFrame, text="UTF-8", command=revertFromUTF8)
convertButton.grid(row=0, column=1, padx = 5)

convertButton = Button(revertButtonFrame, text="UTF-16", command=revertFromUTF16)
convertButton.grid(row=0, column=2, padx = 5)

convertButton = Button(revertButtonFrame, text="UTF-32", command=revertFromUTF32)
convertButton.grid(row=0, column=3, padx = 5)

#output section
outputLabel = Label(root, text="Output:")
outputLabel.pack(pady=(10,0))

outputBox = Text(root, width=50, height=10)
outputBox.pack(padx=10)
outputBox.config(state="disabled")

#export button
exportButton = Button(root, text="Export into Text File", command=exportOutput)
exportButton.pack(pady=10)

root.mainloop()