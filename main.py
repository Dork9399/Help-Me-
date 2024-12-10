# ImpactX Submission - Help Me!
# 12/07/24
# Program Written By: Aryan Varshney

from tkinter import *

# FUNCTIONS
# ---------------------------------------------
# submit settings credentials call-back function (button) & destroy settings frame


def settingsSubmit():
    userPhoneNumber = str(phoneNumberEntry.get())
    userName = str(nameEntry.get())
    userAddress = str(addressEntry.get())
    userAge = str(ageEntry.get())

    if userPhoneNumber != "" and userName != "" and userAddress != "" and userAge != "" and tocCheckVar.get() == 1:
        window.userPhoneNumber = userPhoneNumber
        window.userName = userName
        window.userAddress = userAddress
        window.usersAge = userAge
        settingsFrame.destroy()
        mainFrame.pack()


def goToPainReport():
    mainFrame.destroy()
    painReportFrame.pack()


def submitPainReport():
    painReport = painReportEntry.get(1.0, "end-1c")
    painReportFrame.destroy()
    bigFrame.pack()
    bigLabelLine1.configure(text="REPORT SENT.")
    bigLabelLine2.configure(text="CONNECTING TO", font=("Courier", 38))
    bigLabelLine3.configure(text="MED. PROF.")
    print(window.userName + "'s Pain Report: " + painReport)


def sendAmbHome():
    if window.userAddress != "":
        mainFrame.destroy()
        bigFrame.pack()
        bigLabelLine1.configure(text="NOW SENDING")
        bigLabelLine2.configure(text="AMBULANCE TO")
        bigLabelLine3.configure(text=window.userAddress)
        print("Send an ambulance to " + window.userAddress + ".")


def sendAmbToLocation():
    mainFrame.destroy()
    bigFrame.pack()
    bigLabelLine1.configure(text="NOW SENDING")
    bigLabelLine2.configure(text="AMBULANCE TO")
    bigLabelLine3.configure(text="YOUR LOCATION")
    print("Send an ambulance to " + window.userName + "'s location.")


def call911():
    if window.userPhoneNumber != "":
        mainFrame.destroy()
        bigFrame.pack()
        bigLabelLine1.configure(text="NOW")
        bigLabelLine2.configure(text="CALLING")
        bigLabelLine3.configure(text="911")
        print("The phone number " + window.userPhoneNumber + " is calling 9-1-1.")


# submit report call-back button function (button)

# GUI
# ---------------------------------------------
# create the window
window = Tk()
# configure the window
window.title("Help Me!")
window.configure(bg="#FFE1E1", padx=10, pady=10)
window.geometry("375x667")
window.resizable(False, False)

# window variables
window.userPhoneNumber = ""
window.userName = ""
window.userAddress = ""
window.usersAge = ""

# SETTINGS FRAME (phone number, name, address, age, submit button)
settingsFrame = Frame(window, width=375, height=667, bg="#FFEAEA", padx=25, pady=25)
settingsFrame.pack()

welcomeLabel1 = Label(settingsFrame, text="Welcome to", font=("Courier", 50), bg="#FFEAEA", fg="red4")
welcomeLabel1.pack()
welcomeLabel2 = Label(settingsFrame, text="Help Me!", font=("Courier", 50), bg="#FFEAEA", fg="red4")
welcomeLabel2.pack()

settingsGapFrame1 = Frame(settingsFrame, height=30, bg="#FFEAEA")
settingsGapFrame1.pack()

phoneNumberLabel = Label(settingsFrame, text="Phone Number:", font=("Courier", 25), bg="#FFEAEA", fg="red4")
phoneNumberLabel.pack()
phoneNumberEntry = Entry(settingsFrame, font=("Courier", 20), bg="white", fg="dark blue")
phoneNumberEntry.pack()

settingsGapFrame2 = Frame(settingsFrame, height=20, bg="#FFEAEA")
settingsGapFrame2.pack()

nameLabel = Label(settingsFrame, text="Name:", font=("Courier", 25), bg="#FFEAEA", fg="red4")
nameLabel.pack()
nameEntry = Entry(settingsFrame, font=("Courier", 20), bg="white", fg="dark blue")
nameEntry.pack()

settingsGapFrame3 = Frame(settingsFrame, height=20, bg="#FFEAEA")
settingsGapFrame3.pack()

addressLabel = Label(settingsFrame, text="Address:", font=("Courier", 25), bg="#FFEAEA", fg="red4")
addressLabel.pack()
addressEntry = Entry(settingsFrame, font=("Courier", 20), bg="white", fg="dark blue")
addressEntry.pack()

settingsGapFrame4 = Frame(settingsFrame, height=20, bg="#FFEAEA")
settingsGapFrame4.pack()

ageLabel = Label(settingsFrame, text="Age:", font=("Courier", 25), bg="#FFEAEA", fg="red4")
ageLabel.pack()
ageEntry = Entry(settingsFrame, font=("Courier", 20), bg="white", fg="dark blue")
ageEntry.pack()

settingsGapFrame5 = Frame(settingsFrame, height=25, bg="#FFEAEA")
settingsGapFrame5.pack()

tocCheckVar = IntVar()

tocCheckbutton = Checkbutton(settingsFrame, text="I agree to the Terms and Conditions.", bg="#FFEAEA", fg="black", font=("Rockwell", 15), onvalue=1, offvalue=0, variable=tocCheckVar)
tocCheckbutton.pack()

settingsGapFrame6 = Frame(settingsFrame, height=25, bg="#FFEAEA")
settingsGapFrame6.pack()

settingsSubmitButton = Button(settingsFrame, font=("Courier", 30), bg="white", fg="dark blue", text="SUBMIT", command=settingsSubmit)
settingsSubmitButton.pack()

# BIG TEXT FRAME (acting as place-holders for certain screens)
bigFrame = Frame(window, width=375, height=667, bg="#FFC7F0", padx=25, pady=25)

bigLabelLine1 = Label(bigFrame, text="Line 1", font=("Courier", 40), bg="#FFC7F0", fg="red4")
bigLabelLine1.pack()
bigLabelLine2 = Label(bigFrame, text="Line 2", font=("Courier", 40), bg="#FFC7F0", fg="red4")
bigLabelLine2.pack()
bigLabelLine3 = Label(bigFrame, text="Line 3", font=("Courier", 40), bg="#FFC7F0", fg="red4")
bigLabelLine3.pack()

# MAIN FRAME (option buttons: call 911, send ambulance to home, send ambulance to location, pain report)

mainFrame = Frame(window, width=375, height=667, bg="#FFC7F0", padx=25, pady=25)

painReportButton = Button(mainFrame, font=("Courier", 25), bg="white", fg="dark blue", text="SEND PAIN REPORT", command=goToPainReport)
painReportButton.pack()

mainGapFrame1 = Frame(mainFrame, height=150, bg="#FFC7F0")
mainGapFrame1.pack()

sendAmbHomeButton = Button(mainFrame, font=("Courier", 20), bg="white", fg="dark blue", text="SEND AMBULANCE HOME", command=sendAmbHome)
sendAmbHomeButton.pack()

mainGapFrame2 = Frame(mainFrame, height=150, bg="#FFC7F0")
mainGapFrame2.pack()

sendAmbLocationButton = Button(mainFrame, font=("Courier", 18), bg="white", fg="dark blue", text="SEND AMBULANCE TO LOCATION", command=sendAmbToLocation)
sendAmbLocationButton.pack()

mainGapFrame3 = Frame(mainFrame, height=150, bg="#FFC7F0")
mainGapFrame3.pack()

call911Button = Button(mainFrame, font=("Courier", 25), bg="white", fg="dark blue", text="CALL 911", command=call911)
call911Button.pack()

# PAIN REPORT FRAME (title label, text widget, submit button)

painReportFrame = Frame(window, width=375, height=667, bg="#FFC7F0", padx=25, pady=25)

painReportTitleLabel = Label(painReportFrame, text="Describe your pain:", font=("Courier", 25), bg="#FFC7F0", fg="red4")
painReportTitleLabel.pack()
painGapFrame1 = Frame(painReportFrame, height=30, bg="#FFC7F0")
painGapFrame1.pack()
painReportEntry = Text(painReportFrame, font=("Arial Black", 20), bg="#FFC7F0", fg="dark blue", wrap=WORD, height=15)
painReportEntry.pack()
painGapFrame2 = Frame(painReportFrame, height=50, bg="#FFC7F0")
painGapFrame2.pack()
painReportSubmitButton = Button(painReportFrame, font=("Courier", 40), bg="white", fg="dark blue", text="SUBMIT", command=submitPainReport)
painReportSubmitButton.pack()

# run the window
window.mainloop()