import base64
from getpass import getpass
import json
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic

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
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_string

    def document(self, image_file, prompt: str):
        system = prompt
        human = "{text}"
        prompt_template = ChatPromptTemplate.from_messages(
            [("system", system), ("human", human)]
        )
        chain = prompt_template | self.chat
        return chain.invoke(
            input={
                "text": json.dumps(
                    {
                        "image": self._get_base64_encoded_image(image_file),
                    }
                )
            }
        )
