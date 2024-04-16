from PIL import Image
import base64
from getpass import getpass
from io import BytesIO
import json
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage


load_dotenv()


def _set_if_undefined(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass(f"Please provide your {var}")


class WrapChain:
    def __init__(self):
        self.chat = ChatAnthropic(temperature=0.1, model_name="claude-3-opus-20240229")
        _set_if_undefined("ANTHROPIC_API_KEY")
        pass

    @staticmethod
    def _get_base64_encoded_image(image_file):
        encoded_string = base64.b64encode(image_file).decode("utf-8")
        return encoded_string

    def document(self, image_file, prompt: str, max_size=4 * 1024 * 1024, quality=85):
        system = (
            "You are an AI assistant that analyzes images based on the given prompt."
        )
        human = "{text}"
        prompt_template = ChatPromptTemplate.from_messages(
            [("system", system), ("human", human)]
        )
        compressed_image = self._compress_image(image_file, max_size, quality)
        messages = [
            HumanMessage(
                content=[
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{compressed_image}",  # noqa: E501
                        },
                    },
                    {"type": "text", "text": prompt},
                ]
            )
        ]
        return self.chat.invoke(messages)

    def _compress_image(self, image_file, max_size, quality):
        with Image.open(BytesIO(image_file)) as img:
            img.thumbnail((1092, 1092))
            output_buffer = BytesIO()
            img.save(output_buffer, format="JPEG", optimize=True, quality=quality)
            compressed_image = output_buffer.getvalue()

            encoded_image = self._get_base64_encoded_image(compressed_image)

            # 圧縮後の画像サイズがmax_sizeを超える場合、再帰的に圧縮
            if len(encoded_image) > max_size:
                quality -= 5
                if quality < 5:
                    raise ValueError("画像の圧縮率が限界に達しました")
                return self._compress_image(compressed_image, max_size, quality)

            return encoded_image

    def joke(self):
        prompt_template = ChatPromptTemplate.from_template(
            """
            プログラミングに関するブラックジョークを述べて下さい.
            """
        )
        chain = prompt_template | self.chat
        response = chain.invoke(input={})
        serializable_response = {
            "content": response.content,
            "metadata": dict(response.response_metadata),
        }
        return json.dumps(serializable_response, ensure_ascii=False)
