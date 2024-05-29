
# Arabic Dialect Detection App
![image](https://github.com/mohamedelsayed10/Arabic-Dialect-Detection/assets/87568101/2838d316-57d0-4276-aa55-c07cd693f9b8)


This is a Streamlit application that predicts the dialect of Arabic text input and provides a Text-to-Speech (TTS) feature to play the detected dialect.

## Features

- Predicts the dialect of Arabic text.
- Displays the flag of the country associated with the detected dialect.
- Generates and plays audio of the detected dialect using Google Text-to-Speech (gTTS).

## Models Used

- **Multinomial Naive Bayes**
- **Bernoulli Naive Bayes**
- **Complement Naive Bayes**
- **Logistic Regression**
- **Random Forest Classifier**

These models are combined in a voting classifier to provide the best prediction.

## Preprocessing

- Text is preprocessed using custom functions to clean and prepare the Arabic text for classification.
- TF-IDF vectorization is used to convert text into numerical features.

## Setup

### Prerequisites

- Python 3.7 or later
- Streamlit
- scikit-learn
- joblib
- gTTS
- pydub

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/arabic-dialect-detection.git
    cd arabic-dialect-detection
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Run the App

1. Ensure you have the necessary model and preprocessing files:

    - `best_model.pkl`
    - `vectorizer.pkl`
    - `label_encoder.pkl`

2. Place the flag images (`EG.png`, `LB.png`, etc.) in the working directory.

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Enter Arabic text in the provided text area.
2. Click the "Predict" button.
3. The app will display the predicted dialect and the corresponding country flag.
4. The app will generate and play an audio file of the detected dialect.

## File Structure

- `app.py`: Main Streamlit application script.
- `fun_pre.py`: Preprocessing functions for text data.
- `best_model.pkl`: Serialized voting classifier model.
- `vectorizer.pkl`: Serialized TF-IDF vectorizer.
- `label_encoder.pkl`: Serialized label encoder.
- `requirements.txt`: List of Python dependencies.


