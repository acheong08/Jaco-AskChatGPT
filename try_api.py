import os

from revChatGPT.ChatGPT import Chatbot

from jacolib import assistant

# ==================================================================================================

filepath = os.path.dirname(os.path.realpath(__file__)) + "/"
assist: assistant.Assistant

# ==================================================================================================


def main():
    global assist, url

    assist = assistant.Assistant(repo_path=filepath)
    auth_data = dict(assist.get_config()["user"])
    auth_data = {k: v for k, v in auth_data.items() if v != "" and v is not False}
    print("Authdata:", auth_data)

    # Use conversation_id and parent_id to start a custom conversation
    chatbot = Chatbot(auth_data, conversation_id=None, parent_id=None)

    # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation.
    prompt = "What is the meaning of life? Answer in one sentence."
    response = chatbot.ask(prompt, conversation_id=None, parent_id=None)

    print(response)
    # {
    #   "message": message,
    #   "conversation_id": conversation_id,
    #   "parent_id": parent_id,
    # }


# ==================================================================================================

if __name__ == "__main__":
    main()
