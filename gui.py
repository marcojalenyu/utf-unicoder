from tkinter import *
import converter
import reverter

def convertToUTF8():
    inputText = inputEntry.get()
    outputText = converter.check_and_convert_to_utf8(inputText)
    outputBox.config(state="normal")
    outputBox.delete(1.0, END)
    outputBox.insert(END, outputText)
    outputBox.config(state="disabled")

def convertToUTF16():
    inputText = inputEntry.get()
    outputText = converter.check_and_convert_to_utf16(inputText)
    outputBox.config(state="normal")
    outputBox.delete(1.0, END)
    outputBox.insert(END, outputText)
    outputBox.config(state="disabled")

def convertToUTF32():
    inputText = inputEntry.get()
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
    outputText = outputBox.get(1.0, END)
    with open("output.txt", "w") as file:
        file.write(outputText)

root = Tk()

titleLabel = Label(root, text="Unicode Converter/Translator")
titleLabel.pack()

#input section
inputLabel = Label(root, text="Input:")
inputLabel.pack()

inputEntry = Entry(root, width=50)
inputEntry.pack()

#Convert buttons
convertButtonFrame = Frame(root)
convertButtonFrame.pack(padx=10, pady=10)

convertLabel = Label(convertButtonFrame, text="Convert from Unicode to UTF:")
convertLabel.grid(row=0, column=0, columnspan=3)

convertButton = Button(convertButtonFrame, text="UTF-8", command=convertToUTF8)
convertButton.grid(row=1, column=0, padx = 5)

convertButton = Button(convertButtonFrame, text="UTF-16", command=convertToUTF16)
convertButton.grid(row=1, column=1, padx = 5)

convertButton = Button(convertButtonFrame, text="UTF-32", command=convertToUTF32)
convertButton.grid(row=1, column=2, padx = 5)


#Revert Buttons
revertButtonFrame = Frame(root)
revertButtonFrame.pack(padx=10, pady=10)

revertLabel = Label(revertButtonFrame, text="Revert from UTF to Unicode:")
revertLabel.grid(row=0, column=0, columnspan=3)

convertButton = Button(revertButtonFrame, text="UTF-8", command=revertFromUTF8)
convertButton.grid(row=1, column=0, padx = 5)

convertButton = Button(revertButtonFrame, text="UTF-16", command=revertFromUTF16)
convertButton.grid(row=1, column=1, padx = 5)

convertButton = Button(revertButtonFrame, text="UTF-32", command=revertFromUTF32)
convertButton.grid(row=1, column=2, padx = 5)

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