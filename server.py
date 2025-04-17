"""
server.py - A Flask-based server providing emotion detection functionality.

This module defines two endpoints:
1. /emotionDetector: Accepts text input (via 'textToAnalyze' query parameter)
   and returns emotion predictions.
2. /: Renders a home page (index.html).
"""

from flask import Flask, render_template, request
from oaqjp_final_project_emb_ai.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def predict():
    """
    Handle GET requests to analyze user-provided text and return emotion scores.

    Query Parameter:
        textToAnalyze (str): The text to be analyzed.

    Returns:
        str: A formatted string listing various emotion scores and the dominant emotion.
             If 'dominant_emotion' is None, an error string is returned.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid Text. Please try again."

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"This dominant emotion is {response['dominant_emotion']}"
    )

@app.route("/", methods=["GET"])
def home():
    """
    Render the home page template.

    Returns:
        str: The rendered 'index.html' template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
