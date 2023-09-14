from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def analyze_emotion():
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None
    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."})

    # Return the detected emotion scores and dominant emotion in JSON format
    return jsonify(result)

# Your emotion_detector function here

if __name__ == "__main__":
    app.run(debug=True)
