import os
import sys
import speech_recognition as sr
from nltk.corpus import wordnet
from gtts import gTTS
from playsound import playsound
import os.path
import os

list_synonyms = []
list_antonyms = []

while True:
    os.system('cls')
    print ("""
    ||_______________________||
    ||1.Thuc thi chuong trinh||
    ||2.Thoat                ||
    ||_______________________||
    """)   
    #playsound('output1.mp3')
    ans = input("Nhap lua chon: ")
    if ans == "1":
        list_antonyms.clear()
        list_synonyms.clear()
        print("Bạn muốn dùng giọng nói hay nhập văn bản")
        print ("""
            3.Giọng nói
            4.Văn bản
            """) 
        ans1=input("Nhập vào lựa chọn:")
        if ans1 == "3":
            while True:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Mời bạn nói: ")
                    audio = r.listen(source)
                try:
                    text = r.recognize_google(audio,language="en-us")
                    print("Bạn -->: {}".format(text))
                    a=format(text)
                    break
                except:
                    print("Xin lỗi! tôi không nhận được voice!")
        elif ans1=="4":
            a=input("Nhập từ:")
        for syn in wordnet.synsets(a):
            for lemm in syn.lemmas():
                list_synonyms.append(lemm.name())
        for syn in wordnet.synsets(a):
            for lemm in syn.lemmas():1
            if lemm.antonyms():
                    list_antonyms.append(lemm.antonyms()[0].name())
        if (list_synonyms == []):
            print("Dong nghia: Khong tim thay tu dong nghia phu hop.")
        else:
            print("Dong nghia: ", set(list_synonyms))
        if (list_antonyms == []):
            print("Trai nghia: Khong tim thay tu trai nghia phu hop.")
        else:
            print("Trai nghia: ", set(list_antonyms))
            
    elif (ans=="2"):
        print("==> CHƯƠNG TRÌNH TÌM TỪ ĐỒNG NGHĨA, TRÁI NGHĨA ĐÃ DỪNG LẠI!!!!!!")
        exit()
    else:
        print("Khong co lua chon, vui long nhap lai!")
    os.system('pause')