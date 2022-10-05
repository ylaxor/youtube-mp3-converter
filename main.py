import streamlit as st
from pytube import YouTube
import datetime
import os
from pathlib import Path

Path("tempouts").mkdir(parents=True, exist_ok=True)


st.markdown("# Youtube MP3 converter")

url = st.text_input("Video URL", "https://www.youtube.com/watch?v=o3ZWB0hnJW0")
convert_btn = st.button("Convert")

if convert_btn:
        try:
            yt = YouTube(url)
        
            st.markdown("")
            st.markdown("### {}".format(yt.title))
            st.write("Published by {}, on: {}".format(yt.author, yt.publish_date.strftime("%d %b, %Y.")))
            st.image(yt.thumbnail_url, width=312)
            video = yt.streams.filter(only_audio=True).first()
            downloaded_file = video.download("tempouts")
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
            with open('./tempouts/'+new_file.split("/")[-1], 'rb') as f:
                download = st.download_button('Download mp3', f, file_name=yt.title+'.mp3')  # Defaults to 'application/octet-stream'
                
                if download:
                    st.experimental_rerun() 
        except:
            st.markdown("")
            st.markdown("")
            st.error("Wrong url format or video no longer available!")
        
else:
        st.markdown("")
        st.markdown("")
        st.info("Video details and download options will be shown here.")