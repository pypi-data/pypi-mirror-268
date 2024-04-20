from typing import List
from dseqmap4nlp import BaseMapper

class CharSequenceMapper(BaseMapper):
    def __init__(self, dseq: List[str] = None, text: str = None):
        if text is None and dseq is None:
            raise ValueError("Text and DSeq parameters are None")

        textFromDSeq = "".join(dseq) if dseq is not None else None
        textFromText = text if text is not None else None

        if textFromText is not None and textFromDSeq is not None:
            if textFromDSeq != textFromText:
                raise ValueError("Given Text and DSeq text does not match.")

        self.text = textFromText if textFromText is not None else textFromDSeq

        n_text = len(self.text)
        self.dseq = [ c for c in self.text ]
        self.txt2seq = [ i for i in range(n_text)]
        self.seq2txt = [ i for i in range(n_text)]
