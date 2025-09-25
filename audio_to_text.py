import streamlit as st
from pydub import AudioSegment, silence
import speech_recognition as sr
recog=sr.Recognizer()
st.markdown("<h1 style='text-align:center;'>Audio To Text Converter<h1>", unsafe_allow_html=True)
st.markdown("---")
audio=st.file_uploader("upload your audio file",type=["mp3","wav"])
if audio:
    audio_segment=AudioSegment.from_file(audio)
    chunks=silence.split_on_silence(audio_segment,min_silence_len=500,silence_thresh=audio_segment.dBFS-20,keep_silence=100)
    for index,chunk in enumerate(chunks):
        chunk.export(str(index)+".wav", format="wav")
        with sr.AudioFile(str(index)+".wav") as source:
            recorded=recog.record(source)
            try:
                 recog.recognize_google(recorded)
            except:
                st.write("none")
