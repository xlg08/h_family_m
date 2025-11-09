#  DashScope SDK 版本不低于 1.24.6
import os
from pathlib import Path

import requests
import dashscope
from dotenv import load_dotenv
from datetime import datetime

formatted = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

load_dotenv()
# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'
def textToAudio(storyContent):
    for idx, story in enumerate(storyContent, 1):
        promptContent = f'{story.strip().split("：")}'
        print(promptContent[1])
        # SpeechSynthesizer接口使用方法：dashscope.audio.qwen_tts.SpeechSynthesizer.call(...)
        response = dashscope.MultiModalConversation.call(
            model="qwen3-tts-flash",
            # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
            # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx"
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            text=promptContent,
            voice="Cherry",
            language_type="Chinese",  # 建议与文本语种一致，以获得正确的发音和自然的语调。
            stream=False
        )
        audio_url = response.output.audio.url

        audio_file_path = Path(rf"{os.getenv("STORY_FILE_PATH")}/Audios/{formatted}")
        audio_file_path.mkdir(parents=True, exist_ok=True)

        audio_file_name = f"场景{idx}.wav"  # 自定义保存路径

        audio_save_path = f"{audio_file_path}/{audio_file_name}"
        try:
            response = requests.get(audio_url)
            response.raise_for_status()  # 检查请求是否成功
            with open(audio_save_path, 'wb') as f:
                f.write(response.content)
            print(f"音频文件已保存至：{audio_save_path}")
            return response
        except Exception as e:
            print(f"下载失败：{str(e)}")


def textToAudio_02(idx, story):

    promptContent = f'{story.strip().split("：")}'
    print(promptContent[1])
    # SpeechSynthesizer接口使用方法：dashscope.audio.qwen_tts.SpeechSynthesizer.call(...)
    response = dashscope.MultiModalConversation.call(
        model="qwen3-tts-flash",
        # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key = "sk-xxx"
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        text=promptContent,
        voice="Cherry",
        language_type="Chinese",  # 建议与文本语种一致，以获得正确的发音和自然的语调。
        stream=False
    )
    audio_url = response.output.audio.url

    audio_file_path = Path(rf"{os.getenv("STORY_FILE_PATH")}/Audios/{formatted}")
    audio_file_path.mkdir(parents=True, exist_ok=True)

    audio_file_name = f"场景{idx}.wav"  # 自定义保存路径

    audio_save_path = f"{audio_file_path}/{audio_file_name}"
    try:
        response = requests.get(audio_url)
        response.raise_for_status()  # 检查请求是否成功
        with open(audio_save_path, 'wb') as f:
            f.write(response.content)
        print(f"音频文件已保存至：{audio_save_path}")
        return response
    except Exception as e:
        print(f"下载失败：{str(e)}")
