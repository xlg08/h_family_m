from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath, Path
import requests
from dashscope import ImageSynthesis
import os
import sys
import dashscope
from dotenv import load_dotenv
from datetime import datetime
formatted = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# from demo_test.text_process.enter_information import full_content

load_dotenv()

# 以下为北京地域url，若使用新加坡地域的模型，需将url替换为：https://dashscope-intl.aliyuncs.com/api/v1
dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

# 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
# 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
api_key = os.getenv("DASHSCOPE_API_KEY")

print('----sync call, please wait a moment----')

def textToImage(storyContent):
    for idx, story in enumerate(storyContent, 1):
        promptContent = f'{story.strip()}'
        print(promptContent)
        rsp = ImageSynthesis.call(api_key=api_key,
                                  model="wan2.5-t2i-preview",
                                  prompt=promptContent,
                                  negative_prompt="",
                                  n=1,
                                  size='1024*1024',
                                  prompt_extend=True,
                                  watermark=False,
                                  seed=12345)
        print('图片地址为: %s' % rsp.output.results[0].url)
        if rsp.status_code == HTTPStatus.OK:
            # 在当前目录下保存图片
            for result in rsp.output.results:

                picture_file_name = f"场景{idx}.png"
                # file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]

                picture_file_path = Path(rf'{os.getenv("STORY_FILE_PATH")}/pictures/{formatted}')
                picture_file_path.mkdir(parents=True, exist_ok=True)

                with open(rf'{picture_file_path}/{picture_file_name}', 'wb+') as f:
                    f.write(requests.get(result.url).content)
                return result
        else:
            print('sync_call Failed, status_code: %s, code: %s, message: %s' %
                  (rsp.status_code, rsp.code, rsp.message))


def textToImage_02(idx, story):

    promptContent = f'{story.strip()}'
    print(promptContent)
    rsp = ImageSynthesis.call(api_key=api_key,
                              model="wan2.5-t2i-preview",
                              prompt=promptContent,
                              negative_prompt="",
                              n=1,
                              size='1024*1024',
                              prompt_extend=True,
                              watermark=False,
                              seed=12345)
    print('图片地址为: %s' % rsp.output.results[0].url)
    if rsp.status_code == HTTPStatus.OK:
        # 在当前目录下保存图片
        for result in rsp.output.results:
            picture_file_name = f"场景{idx}.png"
            # file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]

            picture_file_path = Path(rf'{os.getenv("STORY_FILE_PATH")}/pictures/{formatted}')
            picture_file_path.mkdir(parents=True, exist_ok=True)

            with open(rf'{picture_file_path}/{picture_file_name}', 'wb+') as f:
                f.write(requests.get(result.url).content)
            return result
    else:
        print('sync_call Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))