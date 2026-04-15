"""Flask server for the Emotion Detector application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyze the emotion of the given text and return the result."""
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, 'sadness': {result['sadness']}. "
        f"The dominant emotion is <strong>{result['dominant_emotion']}</strong>"
    )


@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)