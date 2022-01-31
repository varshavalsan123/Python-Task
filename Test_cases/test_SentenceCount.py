
from SentenceCount import count_Sentence

def test_countSentence():
        out = count_Sentence("Hello How u? I'm fine. Thankyou!")
        assert out == 3
