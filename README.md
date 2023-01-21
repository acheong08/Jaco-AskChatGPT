# Jaco-AskChatGPT

Ask arbitrary questions to [ChatGPT](https://chat.openai.com/). \
Uses [reverse engineered python-api](https://github.com/acheong08/ChatGPT) as interface.

<br>

**Setup**:

Requires an _OpenAI_-Account. \
Follow the [setup-guide](https://github.com/acheong08/ChatGPT/wiki/Setup#authentication) to get your authentication data. \
Save it in the `config.yaml` file afterwards.

<br>

**Debugging**:

```bash
docker build -t skill_jaco_askchatgpt - < skills/skills/Jaco-AskChatGPT/Containerfile_amd64

# Run without display
docker run --network host --rm \
  --volume `pwd`/skills/skills/Jaco-AskChatGPT/:/Jaco-Master/skills/skills/Jaco-AskChatGPT/:ro \
  --volume `pwd`/skills/skills/Jaco-AskChatGPT/skilldata/:/Jaco-Master/skills/skills/Jaco-AskChatGPT/skilldata/ \
  --volume `pwd`/userdata/config/:/Jaco-Master/userdata/config/:ro \
  -it skill_jaco_askchatgpt

# Run with real display
xhost + && docker run --network host --rm \
  --volume `pwd`/skills/skills/Jaco-AskChatGPT/:/Jaco-Master/skills/skills/Jaco-AskChatGPT/:ro \
  --volume `pwd`/skills/skills/Jaco-AskChatGPT/skilldata/:/Jaco-Master/skills/skills/Jaco-AskChatGPT/skilldata/ \
  --volume `pwd`/userdata/config/:/Jaco-Master/userdata/config/:ro \
  --volume /tmp/.X11-unix:/tmp/.X11-unix \
  --env DISPLAY --env QT_X11_NO_MITSHM=1 \
  --privileged \
  -it skill_jaco_askchatgpt

# Create a virtual display in the docker container
export DISPLAY=:123
Xvfb $DISPLAY -screen $DISPLAY 1280x1024x16 &

# Try loading a webpage only
python3 /Jaco-Master/skills/skills/Jaco-AskChatGPT/try_chrome.py

# Try an example question
python3 /Jaco-Master/skills/skills/Jaco-AskChatGPT/try_api.py

# Start the skill's action
python3 /Jaco-Master/skills/skills/Jaco-AskChatGPT/action_answer.py
```
