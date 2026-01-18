from flask import Flask, render_template, request
import tensorflow as tf
import pickle
import re
import numpy as np
# Updated import for compatibility with newer Keras/TensorFlow versions
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load the model and tokenizer
model = tf.keras.models.load_model('sentiment_model.h5')
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

def clean_text(text):
    """
    Match the cleaning logic used in your Kaggle notebook
    """
    if not isinstance(text, str):
        return ""
    # Remove non-alphabet characters and lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower().strip()

@app.route('/')
def home():
    """Renders the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the sentiment analysis logic"""
    if request.method == 'POST':
        # Get the review from the HTML form
        user_review = request.form['review']
        
        # 1. Clean the input text
        cleaned_review = clean_text(user_review)
        
        # 2. Tokenize and Pad
        sequence = tokenizer.texts_to_sequences([cleaned_review])
        padded = pad_sequences(sequence, maxlen=200)
        
        # 3. Get model prediction
        prediction = model.predict(padded)[0][0]
        
        # 4. Determine Sentiment and Emoji formatting
        if prediction > 0.5:
            sentiment = "Positive"
            # Show how sure the model is
            confidence = f"{prediction * 100:.1f}%"
        else:
            sentiment = "Negative"
            confidence = f"{(1 - prediction) * 100:.1f}%"
        
        # 5. Return results back to index.html
        return render_template('index.html', 
                               sentiment=sentiment, 
                               confidence=confidence, 
                               review=user_review)

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)