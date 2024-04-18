import time
import unittest
from unittest.mock import patch
import dawnai.analytics as analytics


class TestAnalytics(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data or configurations
        analytics.write_key = "0000"
        analytics.debug_logs = True

    #  analytics.api_url = "http://localhost:3000/"

    def tearDown(self):
        # Clean up any resources or reset any state after each test
        pass

    def test_identify(self):

        user_id = "user123"
        traits = {"email": "john@example.com", "name": "John"}

        try:
            analytics.identify(user_id, traits)
        except e:
            print("Error")
        time.sleep(1)
        # No assertion needed as the SDK handles the request internally

    def test_track(self):
        user_id = "user123"
        event = "signed_up"
        properties = {"plan": "Premium"}
        analytics.track(user_id, event, properties)
        time.sleep(1)
        # No assertion needed as the SDK handles the request internally

    def test_track_ai(self):
        user_id = "user123"
        event = "ai_chat"
        model = "GPT-3"
        input_text = "Hello"
        output_text = "Hi there!"

        analytics.track_ai(
            user_id, event, model=model, user_input=input_text, output=output_text
        )

        time.sleep(1)

    def test_flush(self):
        user_id = "user123"
        event = "ai_chat"
        model = "GPT-3"
        input_text = "Hello"
        output_text = "Hi there!"

        analytics.track_ai(
            user_id, event, model=model, user_input=input_text, output=output_text
        )

        time.sleep(1)

        assert len(analytics.buffer) == 0


#  def MEGATEST(self):
#         user_id = "user123"
#         event = "1_400_test_ai_chat_test"
#         model = "gpt_3"
#         input_text = "Hello"
#         output_text = "Hi there!"

#         for _ in range(20):
#             for _ in range(20):
#                 analytics.track_ai(
#                     user_id, event, model=model, user_input=input_text, output="bloop"
#                 )

#                 analytics.track_ai(
#                     user_id,
#                     event,
#                     model=model,
#                     user_input=input_text,
#                 )

#                 analytics.track_ai(user_id, event, model=model, output=output_text)

#                 analytics.track_ai(
#                     user_id,
#                     event,
#                     model=model,
#                     user_input=input_text,
#                     output=output_text,
#                 )

#             time.sleep(0.5)

#         time.sleep(5)
