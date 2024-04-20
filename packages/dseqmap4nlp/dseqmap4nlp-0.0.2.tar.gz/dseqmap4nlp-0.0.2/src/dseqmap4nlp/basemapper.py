from typing import List, Tuple, Literal, Optional

class BaseMapper():
    def __init__(self, text: str, dseq: List[str], txt2seq: List[int], seq2txt: List[int]) -> None:
        self.text = text
        self.dseq = dseq
        self.txt2seq = txt2seq
        self.seq2txt = seq2txt

    def getText(self):
        return self.text

    def getDSeq(self):
        return self.dseq

    def mapDSeqSpanToTextSpan(self, dseq_span: Tuple[int,int]) -> Tuple[int,int]:
        start, stop = dseq_span
        n_dseq = len(self.dseq)

        if start >= stop:
            raise ValueError("Start ({}) is not lower than stop ({}).".format(
                repr(start),
                repr(stop)
            ))
        if start < 0 or start >= n_dseq:
            raise ValueError("Start of dseq span ({}) is out of known dseq ({}).".format(
                repr((start, stop)),
                repr(0, n_dseq)
            ))
        if stop < 0 or stop > n_dseq:
            raise ValueError("Stop of dseq span ({}) is out of known dseq ({}).".format(
                repr((start, stop)),
                repr(0, n_dseq)
            ))

        text_start = self.seq2txt[start]
        # use end of previous dseq entry
        text_stop = self.seq2txt[stop-1] + len(self.dseq[stop-1])
        return (text_start, text_stop)


    def mapTextSpanToDSeqSpan(self, text_span: tuple[int,int], mode: Literal["strict", "contract", "expand"] = "strict") -> Optional[Tuple[int,int]]:
        if mode not in ["strict", "contract", "expand"]:
            raise ValueError("Unknown mode {}. Use one of: {}".format(
                repr(mode),
                repr(["strict", "contract", "expand"])
            ))

        start, stop = text_span
        n_text = len(self.text)

        # do not yield any span if empty span is given
        #if start == stop: return None
        if start >= stop: return None
        if stop == 0: return None

        if start < 0 or start >= n_text:
            raise ValueError("Start of text span ({}) is out of known text ({}).".format(
                repr((start, stop)),
                repr((0, n_text))
            ))
        if stop < 0 or stop > n_text:
            raise ValueError("Stop of text span ({}) is out of known text ({}).".format(
                repr((start, stop)),
                repr((0, n_text))
            ))

        if mode == "strict":
            dseq_start = self.txt2seq[start]
            if dseq_start == -1:
                # no dseq hit
                return None
            elif start > 0 and self.txt2seq[start-1] == dseq_start:
                # no strict begin border
                return None
            dseq_pre_stop = self.txt2seq[stop-1]
            if dseq_pre_stop == -1:
                return None
            elif stop-1 < n_text-1 and self.txt2seq[stop] == dseq_pre_stop:
                # no strict end border
                return None
            return (dseq_start, dseq_pre_stop+1)

        if mode == "expand":
            # find exact txt spans and call in strict mode

            if self.txt2seq[start] == -1:
                # contract start to right, if we are outside
                while start < n_text and self.txt2seq[start] == -1:
                    start += 1
            else:
                # expand start to left, because we are in sequence item
                current_seq = self.txt2seq[start]
                while True:
                    if start == 0: break # edge case
                    if self.txt2seq[start-1] == current_seq: # left side has something
                        start -= 1
                    else:
                        break # we found the left border edge

            pre_stop = stop-1
            if self.txt2seq[pre_stop] == -1:
                # contract to left, because we are in empty position
                while pre_stop > 0 and self.txt2seq[pre_stop] == -1:
                    pre_stop -= 1
            else:
                # expand stop to right
                current_seq = self.txt2seq[pre_stop]
                while True:
                    if pre_stop == n_text-1: break # edge case
                    if self.txt2seq[pre_stop+1] == current_seq: # right side has something
                        pre_stop += 1
                    else:
                        break # we found the right border edge

            return self.mapTextSpanToDSeqSpan((start, pre_stop+1), mode='strict')
        if mode == "contract":
            # again: find exact txt spans and call in strict mode

            # contract start to right to leave the half-way sequence item
            if start != 0 and self.txt2seq[start-1] == self.txt2seq[start]:
                # we are not at the edge of sequence item yet
                while start < n_text and self.txt2seq[start] == self.txt2seq[start-1]:
                    start += 1

            # contract to next right sequence item, if we are outside the dseq items
            if self.txt2seq[start] == -1:
                while start < n_text and self.txt2seq[start] == -1:
                    start += 1

            pre_stop = stop-1
            # contract (pre-stop) to left to leave the half-way sequence item
            if pre_stop != n_text-1 and self.txt2seq[pre_stop] == self.txt2seq[pre_stop+1]:
                # we are not at the edge of sequence item
                current_seq = self.txt2seq[pre_stop]
                while pre_stop > 0 and self.txt2seq[pre_stop] == current_seq:
                    pre_stop -= 1

            # contract to next left sequence item, if we are outside the dseq items
            if self.txt2seq[pre_stop] == -1:
                while pre_stop > 0 and self.txt2seq[pre_stop] == -1:
                    pre_stop -= 1

            return self.mapTextSpanToDSeqSpan((start, pre_stop+1), mode='strict')
