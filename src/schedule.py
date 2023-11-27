from mistral import Mistral

ghost = "files/schedule.txt"
mistral = Mistral(ghost)


def Schedule():
    question = "Write the introduction statements for each speaker. Each speaker should be in separate parts " \
               "separated by $$$. In the introduction, no need to thank the " \
               "previous one or mention the previous context. Stick to the schedule provided, don't add any extra " \
               "information or new speakers. "
    print("Question:", question)
    answer = mistral(question)
    print("Answer:", answer)
    with open('transcript.txt', 'a') as f:
        f.write(answer + "\n")


if __name__ == '__main__':
    Schedule()
