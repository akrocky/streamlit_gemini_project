import streamlit as st
from api_calling import audio_transcription, note_generator , quizz_generator
from PIL import Image
#title
st.title("Note Summery and Quize generator")
st.markdown("upload up to 3 images to generate Note summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload the potos of your note",
        type=['jpg' ,'jpeg' ,'png'],
        accept_multiple_files=True
    )
    if images :
         if len(images) > 3 :
              st.error("upload at max 3 images")
         else :
              st.subheader("uploaded images")
              col = st.columns(len(images))
             
              for i, img in enumerate(images):
                   with col[i]:
                        st.image(img)

    #diffculty
    selected_option = st.selectbox(
         "Enter the difficulty of your quiz",
         ("Easy" , "Medium" , "Hard"),
         index= None
    )

  

    pressed =  st.button("Click the to initiate Ai", type= 'primary')

if pressed :
     if not images:
          st.error("You must upload 1 image")
     if not selected_option:
          st.error("You must select a difficulty")

     if images and selected_option :

          #note
          with st.container(border=True):
               st.subheader("Your note")
               pil_images = [Image.open(img) for img in images]
               with st.spinner("AI is writing notes for you"):
                    generated_notes= note_generator(pil_images )
                    st.markdown(generated_notes)

          #Audio Trunccript
          with st.container(border=True):
               st.subheader("Audio Transcription")
               audio = audio_transcription(generated_notes )
               st.audio(audio)
          #quiz
          with st.container(border=True):
               st.subheader(f"Quiz({selected_option})")
               with st.spinner("AI is writing notes for you"):
                    generated_quizz= quizz_generator(pil_images ,selected_option )
                    st.markdown(generated_quizz)



