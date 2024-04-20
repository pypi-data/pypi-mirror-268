import sys
from typing import List
from dseqmap4nlp import BaseMapper

class RaggedSequenceMapper(BaseMapper):
    def __init__(self, dseq: List[str], text: str = None, text_join: str = None, skippable_chars: List[str] = None):
        if text and skippable_chars is None:
            skippable_chars = [" ", "\t", "\n", "\r"]
            print("Assuming skippable chars: {}".format(
                repr(skippable_chars)
            ), file=sys.stderr)

        if not text is None and not text_join is None:
            print("Either text join element or text can be None.", file=sys.stderr)

        if text is None and text_join is None:
            text_join = " "
            print("No text was given. Trying to reconstruct the text with text join element: {}".format(
                repr(text_join)
            ), file=sys.stderr)

        self.dseq = []

        self.txt2seq = []
        self.seq2txt = []

        # try to parse and reconstruct text
        if text is None:
            self.text = ""
            n_seqitms = len(dseq)
            charitm_idx = 0

            for seqitm_idx, seqitm in enumerate(dseq):
                w_len = len(seqitm)
                self.text += seqitm

                self.txt2seq += [ seqitm_idx for _ in range(w_len)]
                self.seq2txt += [ charitm_idx ]
                self.dseq.append(seqitm)
                charitm_idx += w_len

                # append join element
                if (seqitm_idx+1) < n_seqitms:
                    j_len = len(text_join)
                    self.text += text_join

                    self.txt2seq += [ -1 for _ in range(j_len) ]
                    self.seq2txt += [ ]
                    charitm_idx += j_len

            if len(self.text) != len(self.txt2seq):
                print("Length of text: {} does not match length of charmapping: {len(self.txt2seq)}".format(
                    len(self.text)
                ), file=sys.stderr)

        else:
            # text is given -> try to align to text
            self.text = text
            n_text = len(self.text)
            n_seqitms = len(dseq)
            charitm_idx = 0

            for seqitm_idx, seqitm in enumerate(dseq):
                w_len = len(seqitm)
                # skip through skippable chars
                while not self.text[charitm_idx:].startswith(seqitm):
                    if charitm_idx >= n_text:
                        raise ValueError("Could not find sequence item {} before exceeding the text.".format(
                            repr(seqitm)
                        ))
                    if not self.text[charitm_idx] in skippable_chars:
                        raise ValueError(
                            "Char at position {} ({}) is not in list of skippable chars {}.".format(
                                charitm_idx,
                                repr(self.text[charitm_idx]),
                                repr(skippable_chars)
                            ))

                    charitm_idx += 1
                    self.txt2seq.append(-1)

                self.txt2seq += [ seqitm_idx for _ in range(w_len)]
                self.seq2txt += [ charitm_idx ]
                self.dseq.append(seqitm)
                charitm_idx += w_len

            if len(self.text) != len(self.txt2seq):
                # fill last txt2seq map
                self.txt2seq += [ -1 for _ in  range(len(self.text) - len(self.txt2seq)) ]

if __name__ == "__main__":
    # Some tests...
    dseq = ["This", "is", "a", "fancy", "text", "."]

    print("Parsing WITHOUT given text:", file=sys.stderr)
    mapper = RaggedSequenceMapper(dseq, text_join=" ")
    print("Discrete sequence: {}".format(repr(dseq)), file=sys.stderr)
    print("Reconstructed text: {}".format(repr(mapper.getText())), file=sys.stderr)
    print("DSeq span {} -> {} (={})".format(
        (3,4),
        mapper.mapDSeqSpanToTextSpan((3,4)),
        repr(mapper.getText()[slice(*mapper.mapDSeqSpanToTextSpan((3,4)))])
    ), file=sys.stderr)

    print()

    print("Parsing WITH given text:", file=sys.stderr)
    text = " This   is a\nfancy \ttext."
    mapper = RaggedSequenceMapper(dseq, text=text)
    print("Discrete sequence: {}".format(repr(dseq)), file=sys.stderr)
    print("Text: {}".format(repr(mapper.getText())), file=sys.stderr)
    print("DSeq span {} -> {} (={})".format(
        (3,4, dseq[3:4]),
        mapper.mapDSeqSpanToTextSpan((3,4)),
        repr(mapper.getText()[slice(*mapper.mapDSeqSpanToTextSpan((3,4)))])
    ), file=sys.stderr)
    print("Text span {} expand -> {}".format(
        (8,9, mapper.getText()[8:9]),
        repr(mapper.getDSeq()[slice(*mapper.mapTextSpanToDSeqSpan((8,9), mode="expand"))])
    ), file=sys.stderr)
    print("Text span {} expand -> {}".format(
        (2,9, mapper.getText()[2:9]),
        repr(mapper.getDSeq()[slice(*mapper.mapTextSpanToDSeqSpan((2,9), mode="expand"))])
    ), file=sys.stderr)
    print("Text span {} contract -> {}".format(
        (2,10, mapper.getText()[2:10]),
        repr(mapper.getDSeq()[slice(*mapper.mapTextSpanToDSeqSpan((2,10), mode="contract"))])
    ), file=sys.stderr)
