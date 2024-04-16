from io import BytesIO
from wrapchain import WrapChain

if __name__ == "__main__":

    wc = WrapChain()

    with open("test.jpg", "rb") as image_file:
        input_image = image_file.read()

        prompt_text = """
        アップロードされる画像の日本語を読み取って下さい.わからないまたは不明な場合は正直にその旨を返答して下さい.
        """
        result = wc.document(
            image_file=input_image,
            prompt=prompt_text,
        )

        print(result)
