import os
from openai import BadRequestError
from modelConfig import client
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()

file_object = client.files.create(file=Path(rf"{os.getenv("PROJECT_PATH")}\第01章_青衫磊落险峰行.txt"), purpose="file-extract")
FILE_ID = file_object.id
print(FILE_ID)


CLASS_SIZE = os.getenv("SCENE_SIZE")

def generyContext(charater):
    try:
        # 初始化messages列表
        completion = client.chat.completions.create(
            model="qwen-long",
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                # 请将 '{FILE_ID}'替换为您实际对话场景所使用的 fileid
                {'role': 'system', 'content': f'fileid://{FILE_ID}'},
                {'role': 'user', 'content': f'请根据故事发展顺序对不同的故事情节进行分类，分为{CLASS_SIZE}类(每一类中不需要再进行细分，只需要概括内容)，并分别概括与{charater}相关的故事情节。禁止主动虚构情节。'}
            ],
            # 所有代码示例均采用流式输出，以清晰和直观地展示模型输出过程。如果您希望查看非流式输出的案例，请参见https://help.aliyun.com/zh/model-studio/text-generation
            stream=True,
            stream_options={"include_usage": True}
        )

        full_content = ""
        for chunk in completion:
            if chunk.choices and chunk.choices[0].delta.content:
                # 拼接输出内容
                full_content += chunk.choices[0].delta.content
                # print(chunk.model_dump())

        print(full_content)
        return full_content

    except BadRequestError as e:
        print(f"错误信息：{e}")
