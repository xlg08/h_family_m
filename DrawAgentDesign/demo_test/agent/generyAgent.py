from llm.llm_text_to_text import textToText
from llm.llm_text_to_iamge import textToImage, textToImage_02
from llm.llm_text_to_audio import textToAudio, textToAudio_02

from demo_test.text_process.enter_information import generyContext


charater = "段誉"
content = generyContext(charater)
storyContent = textToText(content)
for idx, story in enumerate(storyContent, 1):
    picture = textToImage_02(idx, story)
    audio = textToAudio_02(idx, story)
