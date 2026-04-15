from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    text_to_analyse = request.args.get('textToAnalyze')
    r = emotion_detector(text_to_analyse)

    if r['dominant_emotion'] is None:
        return "Invalid text! Please try again"
    else:
        return (
            f"For the given statement, the system response is "
            f"'anger': {r['anger']}, 'disgust': {r['disgust']}, 'fear': {r['fear']}, "
            f"'joy': {r['joy']}, 'sadness': {r['sadness']}. "
            f"The dominant emotion is <strong>{r['dominant_emotion']}</strong>"
        )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)