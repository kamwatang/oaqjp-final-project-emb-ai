from flask import Flask, render_template, request
from oaqjp_final_project_emb_ai.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def predict():
    text = requests.get('text_to_analyze')
    response = emotion_detector(text)
    return (f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. This dominant emotion is {response['dominant_emotion']} ")

@app.route("/")
def home():
    return render_template("index.htnl")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
