import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    # Check for a successful response
    if response.status_code == 200:
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

    return 'Emotion detection failed'

# Test your function with the provided text
if __name__ == "__main__":
    text_to_analyze = "I am so happy I am doing this."
    detected_emotion = emotion_detector(text_to_analyze)
    print(detected_emotion)
