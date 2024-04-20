from .basemapper import BaseMapper
from .annotationset import AnnotationSet
from typing import List, Literal, Tuple
import sys, re

class LabelLoader:
    @classmethod
    def from_tagged_sequence(cls, dseq_tag: List[str], schema: Literal["IOB2"] = "IOB2", mapper: BaseMapper = None, dseq_text: List[str] = None, on_mismatch: Literal["warn", "error"] = "warn"):
        if not on_mismatch in ["warn", "error"]:
            raise ValueError("Unknown on_mismatch value: {}. Should be one of {}".format(
                on_mismatch,
                repr(["warn", "error"])
            ))
        if not isinstance(mapper, BaseMapper):
            raise ValueError("Unknown mapper given.")

        if not schema in ["IOB2"]:
            raise ValueError("Schema {} is not supported yet.".format(schema))

        if dseq_text is None:
            print("No sequence text was given. No checks can be provided.", file=sys.stderr)
            dseq_text = [None for _ in dseq_tag]

        if len(dseq_tag) != mapper.getDSeq():
            raise ValueError("Given sequence length ({}) does not match to discret sequence of mapper ({}).".format(
                len(dseq_tag),
                len(mapper.getDSeq())
            ))

        # parse schema
        ptn = re.compile(r"^\s*(?P<action>[IB])\-(?P<lbl>.+)\s*$")
        entries = []
        if schema == "IOB2":
            buffer = []
            for dseq_idx, (tag, txt) in enumerate(zip(dseq_tag, dseq_text)):
                # check sequence text match
                if txt is not None:
                    if mapper.dseq[dseq_idx] != txt:
                        if on_mismatch == "warn":
                            print("At {} tag, sequence text {} does not match expected mapper text {}.".format(
                                dseq_idx,
                                repr(txt),
                                repr(mapper.dseq[dseq_idx])
                            ))
                        else:
                            raise ValueError("At {} tag, sequence text {} does not match expected mapper text {}.".format(
                                dseq_idx,
                                repr(txt),
                                repr(mapper.dseq[dseq_idx])
                            ))

                if tag == "O":
                    # flush buffer
                    if buffer:
                        entries.append((buffer[0][0], buffer[-1][0]+1, buffer[0][1]))
                        buffer = []
                else:
                    m = ptn.match(tag)
                    if m is None:
                        raise ValueError("Could not parse tag {}.".format(repr(tag)))
                    action = m.group("action")
                    label = m.group("lbl")
                    # validate buffer
                    if action == "I" and not buffer:
                        raise ValueError("Unexpected action entry {} received at empty buffer.".format(repr(tag)))
                    if action == "B":
                        # write back buffer first
                        if buffer:
                            entries.append((buffer[0][0], buffer[-1][0]+1, buffer[0][1]))
                            buffer = []
                    # add to buffer for I and B actions
                    buffer += [(dseq_idx, label)]

            # handle last action tails
            if buffer:
                entries.append((buffer[0][0], buffer[-1][0]+1, buffer[0][1]))

    @classmethod
    def from_text_spans(cls, text_entries: List[Tuple[int, int, str]], mapper: BaseMapper = None):
        if not isinstance(mapper, BaseMapper):
            raise ValueError("Unknown mapper given.")

        # validate first
        n_text = len(mapper.getText())
        for start, stop, _ in text_entries:
            if not (start >= 0 and start < n_text):
                raise ValueError("Item {} does not match to text length {}.".format(
                    (start, stop),
                    n_text
                ))
            if not (stop > 0 and stop <= n_text):
                raise ValueError("Item {} does not match to text length {}.".format(
                    (start, stop),
                    n_text
                ))

        return AnnotationSet(text_entries, "text", mapper)
