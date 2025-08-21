from langchain.schema.runnable import RunnableLambda


def word_counter(text):
    return len(text.split())    # to count words

runnable_word_counter = RunnableLambda(word_counter)

print(runnable_word_counter.invoke('hi thre how are you ?'))