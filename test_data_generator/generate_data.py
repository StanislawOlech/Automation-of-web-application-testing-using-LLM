import random

def generate_test_data(spec):
    # TODO Do it with LLM
    # recives a table of touples (bool if_is_button, an class: requirement)
    # return a table of all moves
    # move should be a touple (index of button/text_box, input)

    test_data = []
    num_of_test  = 5
    num_of_moves = 3

    for _ in range(num_of_test):
        move = []
        for _ in range(num_of_moves):
            index = random.randint(0, len(spec)-1)
            if spec[index][0]: # button
                input = random.choice([True, False])
            else: # text box
                input = random.choice(["test", "Test1", "12345", "Admin", "hello", "HELLO", "user123", "no_numbers", "123456", "A1b2C3", "short", "thisisaverylonginput"])
            move.append((index, input))
        test_data.append(move)

    return test_data