from WordCount import word_Count

def test_Word_Count():
    out = word_Count("hello how are you?")
    assert out  == len("hello how are you?".split(" "))