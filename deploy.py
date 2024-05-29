import streamlit as st
import joblib
import numpy as np
import fun_pre as f
from gtts import gTTS
from io import BytesIO
from tempfile import NamedTemporaryFile
from pydub import AudioSegment
from pydub.playback import play

# Load models and necessary preprocessing objects
best_model = joblib.load('best_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Function to predict dialect using the best model
def predict_dialect(text):
    processed_text = f.preprocess_text_arabic(text)
    text_vectorized = vectorizer.transform([processed_text])
    prediction = best_model.predict(text_vectorized)[0]
    return label_encoder.classes_[prediction]

# Function to generate TTS for Arabic text
def generate_tts(text):
    tts = gTTS(text=text, lang='ar')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

# Streamlit UI components
st.title('Arabic Dialect Detection')

# Text input for user to enter Arabic text
text_input = st.text_area('Enter Arabic Text:', '')

# Predict button
if st.button('Predict'):
    if text_input:
        prediction = predict_dialect(text_input)
        st.success(f'Predicted Dialect: {prediction}')
        
        # Map prediction to country flag (simplified example)
        country_flags = {
            'EG': 'EG.png',
            'LB': 'LB.png',
            'LY': 'LY.png',
            'MA': 'MA.png',
            'SD': 'SD.png'
        }
        
        flag_image = country_flags.get(prediction, 'default_flag.png')
        st.image(flag_image, caption='Flag of Detected Dialect', use_column_width=True)
        
        # Generate TTS for the detected dialect
        tts_audio_bytes = generate_tts(f'انها الهجه {prediction}')
        
        # Save the TTS audio to a temporary file
        temp_file_path = "temp_audio.mp3"
        with open(temp_file_path, 'wb') as f:
            f.write(tts_audio_bytes.read())
        
        # Load the temporary audio file and play it
        audio = AudioSegment.from_file(temp_file_path, format='mp3')
        play(audio)

        # Clean up: Remove the temporary file
        import os
        os.remove(temp_file_path)

    else:
        st.warning('Please enter some text.')

# Display footer or additional information
st.markdown('---')
st.markdown('Built with Streamlit')
