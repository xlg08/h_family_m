import os
import dashscope
from dotenv import load_dotenv
import re

load_dotenv()

def textToText(full_content: str):
    messages = [
        {'role': 'system', 'content': '你是一个具有十年编剧工作经验的编导。'},
        {'role': 'user', 'content': f'将以下分类，转化为各自的场景，有几个分类生成几个场景，不要多生成也不要少生成场景，并且以各自的"场景几："开始。分类内容为{full_content}，场景内容不需要使用换行符等分隔符分割，只返回场景内容文字即可'}
    ]
    response = dashscope.Generation.call(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        model="qwen-plus",  # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=messages,
        result_format='message'
    )

    print("开始编写：")
    storyContent = response.output.choices[0].message.content
    storyContent = re.findall(r'(场景.*?)(?=场景|$)', storyContent, flags=re.S)
    print(storyContent)

    return storyContent
