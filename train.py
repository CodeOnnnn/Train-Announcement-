import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext= str(text)
    language= 'en'
    myobj=gTTS(text=mytext, lang= language, slow= True)
    myobj.save(filename)

def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+= AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton(filename):
    # May i have your attention please train no
    # from
    # to
    # is arriving shortly on platform no.
    df= pd.read_excel(filename)
    for index, item in df.iterrows():
        textToSpeech(item['first']  , '1.mp3')
        textToSpeech(item['second']  , '4.mp3')
        textToSpeech(item['third']  , '6.mp3')
        textToSpeech(item['fourth']  , '8.mp3')
   

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        textToSpeech(item['trainno']  , '2.mp3')
        textToSpeech(item['trainname']  , '3.mp3')
        textToSpeech(item['city1'], '5.mp3')
        textToSpeech(item['city2'], '7.mp3')
        textToSpeech(item['platno'], '9.mp3')
        audios = [f"{i}.mp3" for i in range(1, 10)]
        announcement = mergeAudios(audios)
        announcement.export(f"announcement{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton("skull.xlsx")
    print("Now Generating Announcement...")
    generateAnnouncement("Train list.xlsx")