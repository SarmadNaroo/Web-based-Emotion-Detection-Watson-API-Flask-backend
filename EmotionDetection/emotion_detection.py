import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    # Access the status code of the server response
    status_code = response.status_code

    # Check for a successful response (status code 200)
    if status_code == 200:
        result = json.loads(response.text)
        emotions = result.get('emotionPredictions', [])[0].get('emotion', {})

        # Find the dominant emotion
        dominant_emotion = max(emotions, key=lambda e: emotions[e])

        # Create the output dictionary
        output = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }

        return output

    # Handle the case when status code is 400
    elif status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return 'Emotion detection failed'

# Test your function with the provided text
if __name__ == "__main__":
    text_to_analyze = "I am so happy I am doing this."
    detected_emotion = emotion_detector(text_to_analyze)
    print(detected_emotion)
