import os
import subprocess

from revChatGPT.ChatGPT import Chatbot

from jacolib import assistant

# ==================================================================================================

filepath = os.path.dirname(os.path.realpath(__file__)) + "/"
assist: assistant.Assistant

request_running = False
chatbot: Chatbot

# ==================================================================================================


def callback_ask_question(message):
    """Callback to handle current weather request"""
    global request_running, chatbot

    if request_running:
        result_sentence = assist.get_random_talk("request_running")
    else:
        answer = assist.publish_question(
            "",
            question_intents=["Jaco/Intents/GreedyText"],
            satellite=message["satellite"],
        )

        if answer != {}:
            if answer["intent"]["name"] == "greedy_text":
                result_sentence = assist.get_random_talk("wait_for_answer")
                assist.publish_answer(result_sentence, message["satellite"])

                prompt = answer["greedy"]
                try:
                    response = chatbot.ask(prompt, conversation_id=None, parent_id=None)
                    result_sentence = response["message"]
                except Exception:
                    result_sentence = assist.get_random_talk("an_error_occured")

                assist.publish_answer(result_sentence, message["satellite"])
                request_running = False


# ==================================================================================================


def main():
    global assist, chatbot

    assist = assistant.Assistant(repo_path=filepath)

    # Start virtual display
    # For some reason this will throw an error that a display is already existing, but it's working.
    display_id = ":123"
    os.environ["DISPLAY"] = display_id
    subprocess.Popen(["Xvfb", display_id, "-screen", display_id, "1280x1024x16"])

    # Filter authentication data
    auth_data = dict(assist.get_config()["user"])
    auth_data = {k: v for k, v in auth_data.items() if v != "" and v is not False}

    # Use conversation_id and parent_id to start a custom conversation
    chatbot = Chatbot(auth_data, conversation_id=None, parent_id=None)

    assist.add_topic_callback("ask_question", callback_ask_question)
    assist.run()


# ==================================================================================================

if __name__ == "__main__":
    main()
