import unittest
from EmotionDetection.emotion_detection import emotion_detectorfrom EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_statement_glad(self):
        statement = "I am glad this happened"
        expected_emotion = "joy"
        result = emotion_detector(statement)
        dominant_emotion = result['dominant_emotion']  # Extract the dominant emotion
        self.assertEqual(dominant_emotion, expected_emotion)

    def test_statement_mad(self):
        statement = "I am really mad about this"
        expected_emotion = "anger"
        result = emotion_detector(statement)
        dominant_emotion = result['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

    def test_statement_disgusted(self):
        statement = "I feel disgusted just hearing about this"
        expected_emotion = "disgust"
        result = emotion_detector(statement)
        dominant_emotion = result['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

    def test_statement_sad(self):
        statement = "I am so sad about this"
        expected_emotion = "sadness"
        result = emotion_detector(statement)
        dominant_emotion = result['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

    def test_statement_afraid(self):
        statement = "I am really afraid that this will happen"
        expected_emotion = "fear"
        result = emotion_detector(statement)
        dominant_emotion = result['dominant_emotion']
        self.assertEqual(dominant_emotion, expected_emotion)

if __name__ == "__main__":
    unittest.main()
