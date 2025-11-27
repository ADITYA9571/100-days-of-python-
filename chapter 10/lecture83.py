# Write a program to pronounce list of names using win32 API. 
# If you are given a list l as follows:
# l = ["Rahul", "Nishant", "Harry"]
# Your program should pronouce:
# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry
# Note: If you are not using windows, try to figure out how to do the same thing 
# using some other package
# using win32 API module SAPI (Speech Application Programming Interface) 
"""
import win32com.client as voice
print(dir(voice))
speak = voice.Dispatch("SAPI.SpVoice")
speak.Speak("WOOW")
"""
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
speak.Speak("Now its time for shoutouts: ") #Titles are working 
l = []
number = int(input("Enter number of persons: "))
print("Enter ",number,"names: ")
for i in range(number):
    name = input(str(f"Person {i+1}: "))
    l.append(name)
for names in l:
    speak.Speak(names)

speak.Speak("thats it ...")