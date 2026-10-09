print("EDIZA: Hello! I'm EDIZA. Tell me what's on your mind.")
response_list = ["Please tell me more.", "How does that make you feel?",  "What makes you say that?"]
response_index = 0
keyword_responses = {"mother" : "Tell me more about your family.",
                     "father": "Tell me more about your family.",
                     "edinburgh":"What is it like living in Edinburgh?",
                     "university": "What do you think about your studies?"}
punc =  [".", ",", "!", "?"]
while True:
    message = input("You: ")
    for punctuation in punc:
        message = message.replace(punctuation, "")
    message = message.lower()
    message = message.strip()
    if message == "bye":
        print("EDIZA: Goodbye!")
        break
    elif message == "":
        print("EDIZA: Even a chatbot needs something to go on.")
    else:
        words = []
        word = ""
        for character in message + " ":
            if character == " ":
                if word != "":
                    words.append(word)  # Append the finished word to words
                    word = ""  # Set word back to an empty string
            else:
                word = word + character  # Add character to the end of word

                reply = ""
        for word in words:
            if word in keyword_responses:
                reply = keyword_responses[word]  # Look up this word's reply in the dictionary
                break  # Stop searching now that we have a reply

        if reply == "":
            reply = response_list[response_index]
            if response_index < (len(response_list) - 1):
                response_index += 1
            else:
                response_index = 0

        print(f"EDIZA: {reply}")