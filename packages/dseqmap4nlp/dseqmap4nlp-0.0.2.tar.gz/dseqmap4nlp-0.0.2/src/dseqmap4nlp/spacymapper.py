import sys
import spacy
from spacy.language import Language
from dseqmap4nlp import BaseMapper

class SpacySequenceMapper(BaseMapper):
    spacy_cache = {}

    def __init__(self, text: str, nlp: str | Language = None):
        if text is None:
            raise ValueError("Parameter text is None.")

        if nlp is None:
            print("Assuming English NLP object...", file=sys.stderr)
            nlp = "en"

        # try to load from cache
        if isinstance(nlp, str):
            nlp = SpacySequenceMapper.spacy_cache.get(nlp, nlp)

        if isinstance(nlp, str):
            try:
                id = nlp
                nlp = spacy.load(nlp)
                SpacySequenceMapper.spacy_cache[id] = nlp
            except: pass
        if isinstance(nlp, str):
            try:
                id = nlp
                nlp = spacy.blank(nlp)
                SpacySequenceMapper.spacy_cache[id] = nlp
            except: pass

        if not isinstance(nlp, Language):
            raise ValueError("Spacy object is not a language: {}".format(repr(nlp)))

        self.text = text
        self.dseq = []

        self.txt2seq = []
        self.seq2txt = []

        # use Spacy tokenizer
        doc = nlp(text)

        charitm_idx = 0
        for token_idx, token in enumerate(doc):
            # add token first
            self.dseq.append(token.text)
            self.txt2seq += [ token_idx for _ in token.text ]
            self.seq2txt += [ charitm_idx ]
            charitm_idx += len(token.text)

            # add whitespace
            self.txt2seq += [ -1 for _ in token.whitespace_ ]
            charitm_idx += len(token.whitespace_)

    @classmethod
    def flush_cache(cls):
        SpacySequenceMapper.spacy_cache = {}

if __name__ == "__main__":
    # Some tests...
    text = "Das ist ein beeindruckender Text."

    mapper = SpacySequenceMapper(text, nlp="de")
    print("Input text: {}".format(repr(mapper.getText())), file=sys.stderr)
    print("Parsed sequence: {}".format(repr(mapper.getDSeq())), file=sys.stderr)
    print("DSeq span {} -> {} (={})".format(
        (3,4),
        mapper.mapDSeqSpanToTextSpan((3,4)),
        repr(mapper.getText()[slice(*mapper.mapDSeqSpanToTextSpan((3,4)))])
    ), file=sys.stderr)
