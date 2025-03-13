""" Emotion Analyzer Web Application """
from flask import Flask, render_template, request
from EmotionAnalysis.emotion_analysis import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/")
def render_index_page():
    """Render the index.html page for the Emotion Analyzer web application."""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotion from the given text input.
    Returns:
        str: A formatted response with emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return (f"\nFor the given statement, the system response is "
            f"'anger': {emotions['anger']:.9f}, "
            f"'disgust': {emotions['disgust']:.9f}, "
            f"'fear': {emotions['fear']:.9f}, "
            f"'joy': {emotions['joy']:.9f} and "
            f"'sadness': {emotions['sadness']:.9f}. "
            f"The dominant emotion is {emotions['dominant_emotion']}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
