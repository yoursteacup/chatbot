from vk_api.api_methods import messages_history, continuous_messages_generator, messages_history_generator

dishka = 441515260
me = 678562910
messages_retrieving_step = 200


def chat_history_to_dialogue_generator(user_id: int):
    generator = messages_history_generator(offset=0, count=5, user_id=user_id)
    input_txt = ""
    target_txt = ""
    initiator = me

    while True:
        message = next(generator)
        if message.from_id == me:
            if initiator == dishka:
                yield input_txt, target_txt
                input_txt = ""
                target_txt = ""

            input_txt += message.text.replace('\n', '. ') + ". "
        elif message.from_id == dishka:
            target_txt += message.text.replace('\n', '. ') + ". "

        initiator = message.from_id


if __name__ == "__main__":
    dialogue_generator = chat_history_to_dialogue_generator(user_id=dishka)

    # Test property: Generate dialogue
    def test1():
        print("Testing property: Generate dialogue")
        count = 0
        for dialogue in dialogue_generator:
            if count == 20:
                return
            print(dialogue)
            count += 1

    test1()
