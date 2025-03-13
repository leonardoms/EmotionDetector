import requests
import json

emotions_none = { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None,   'dominant_emotion': None}

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return emotions_none

    response_dict = json.loads(response.text)

    emotion_predictions = response_dict.get("emotionPredictions", [])
    
    emotions = emotion_predictions[0].get("emotion", {})
    dominant_emotion = max(emotions, key=emotions.get)

    result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }

    return result