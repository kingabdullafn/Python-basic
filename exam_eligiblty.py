#Take input for the student that he can attend the exam or not
medical_cause=input("did you have medical cause Y or N") 
#Take input of the attendance
atten = int(input("Tell me how much days youve been in school"))

#Checking the user input predicting output accordingly

if medical_cause == 'Y':#checking the condition one

    print("Your allowed to take the test. Good luck!")
else:
    if atten>=75: #checking conditoin 2
        print("Your allowed to take the test")

    else:
        print("Go back to your home and fakebeing sick while your using the playstation and scrolling on tiktok")