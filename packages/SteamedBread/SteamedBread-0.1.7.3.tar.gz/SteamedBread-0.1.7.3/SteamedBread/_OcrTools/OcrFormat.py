"""
@Author: 馒头 (chocolate)
@Email: neihanshenshou@163.com
@File: OcrFormat.py
@Time: 2024/2/2 21:36
"""

import requests
from PIL import Image

from .OriginOcrTool import OcrTool


class OcrFormat:

    @staticmethod
    def ocr_code(filename: str = "", img: Image = None, show=True):
        """
        识别动态变化的验证码(前端登录), 非GIF文件(准确度会稍微低一些)

        img: 如果使用该参数, 则这样传递 show_word(img=Image.open("file.png"))
        filename: 如果使用该参数, 则这样传递 show_word(filename="file.png")
        """
        if img:
            img_file = img
        elif filename:
            img_file = Image.open(filename)
        else:
            raise AttributeError("Please Use The Picture That Needs To Be Recognized.")
        ocr = OcrTool()
        word = ocr.classification(img_file)
        if show and word:
            print(f"识别到的验证码: {word}")
        return word

    @staticmethod
    def ocr_word(filename: str = "", show=True):
        """
        识别图片中的文字
        :param filename: 图片的文件路径
        :param show: 展示结果
        :return:
        """

        response = requests.post(
            url="https://api.oioweb.cn/api/ocr",
            files={"file": open(file=filename, mode="rb", encoding=None)},
            verify=False
        )
        try:
            word = response.json().get("result", [])
        except Exception as e:
            word = [] and e

        if show and word:
            print(f"识别到的字符: {word}")
        return word
