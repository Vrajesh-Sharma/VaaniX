from flask import Flask, render_template, request, send_file
import pyttsx3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    gender = request.form['gender']

    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    
    # Get voices and set the selected gender
    voices = engine.getProperty('voices')
    if gender == 'female':
        engine.setProperty('voice', voices[1].id)  # Female voice
    else:
        engine.setProperty('voice', voices[0].id)  # Male voice

    # Save the audio file
    output_path = 'static/output.mp3'
    engine.save_to_file(text, output_path)
    engine.runAndWait()

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)