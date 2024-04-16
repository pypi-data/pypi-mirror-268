from wrapchain import WrapChain

if __name__ == "__main__":

    wc = WrapChain()

    # with open("test.png", "rb") as image_file:
    #     result = wc.document(
    #         image_file=image_file,
    #         prompt="""
    #         アップロードされる画像の日本語を読み取って下さい.わからないまたは不明な場合は正直にその旨を返答して下さい.
    #         """,
    #     )
    result = wc.joke()

    print(result)
