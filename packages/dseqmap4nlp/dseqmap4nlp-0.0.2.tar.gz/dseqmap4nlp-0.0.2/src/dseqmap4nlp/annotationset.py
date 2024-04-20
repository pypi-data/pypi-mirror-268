from .basemapper import BaseMapper
from typing import List, Literal, Tuple, Dict
from functools import reduce
import sys

class AnnotationSet:
    def __init__(self, entries: List[Tuple[int, int, str]], level: Literal["text", "dseq"], mapper: BaseMapper = None):
        if not level in ["text", "dseq"]:
            raise ValueError("Unknown level {}, one of {} expected.".format(
                repr(level),
                repr(["text", "dseq"])
            ))
        if mapper is None and level == "dseq":
            raise ValueError("No mapper provided. Cannot handle sequence entries appropriately.")

        # sort by lowest end, then by lowest start
        self.entries = list(sorted(sorted(entries, key=lambda x: x[1]), key=lambda x: x[0]))
        self.level = level
        self.mapper = mapper

    def toTextSpans(self) -> "AnnotationSet":
        if self.level == "text": return self
        text_entries = [ (*self.mapper.mapDSeqSpanToTextSpan((e_start, e_stop)), e_lbl) for e_start, e_stop, e_lbl in self.entries ]
        return AnnotationSet(text_entries, "text", self.mapper)

    def toDSeqSpans(self, strategy: List[Literal["strict", "expand", "contract"]] = "expand", mapper: BaseMapper = None) -> "AnnotationSet":
        if isinstance(strategy, str): strategy = [strategy]
        if not all([s in ["strict", "expand", "contract"] for s in strategy ]):
            raise ValueError("One of the strategy is unknown: {}".format(
                repr(strategy)
            ))

        if self.mapper is None and mapper is None:
            raise ValueError("No mapper found or given.")
        if mapper is None: mapper = self.mapper

        dseq_entries = []
        for e_start, e_stop, e_lbl in self.entries:
            new_span = None
            next_strategies = strategy
            while next_strategies:
                next_strategy, *next_strategies = next_strategies
                new_span = mapper.mapTextSpanToDSeqSpan((e_start, e_stop), mode=next_strategy)
                if new_span is not None:
                    dseq_entries.append((*new_span, e_lbl))
                    break
            if new_span is None:
                print("Span entry {} failed to align. Dropping entry".format(
                    (e_start, e_stop, e_lbl)
                ), file=sys.stderr)

        return AnnotationSet(dseq_entries, "dseq", mapper)

    def filterEntries(self, condition) -> "AnnotationSet":
        return AnnotationSet([ e for e in self.entries if condition(e)], self.level, self.mapper)

    def getLabels(self) -> List[str]:
        return list(set([ e[2] for e in self.entries ]))

    def renameLabels(self, labelmap: Dict[str, str]) -> "AnnotationSet":
        return AnnotationSet([ (start, stop, labelmap.get(lbl, lbl)) for start, stop, lbl in self.entries ], self.level, self.mapper)

    def withoutOverlaps(self, strategy: Literal["prefer_longest", "prefer_shortest"] = "prefer_longest", merge_same_classes: bool = False) -> "AnnotationSet":
        if not strategy in ["prefer_shortest", "prefer_longest"]:
            ValueError("Unsupported strategy: {}. One of {}".format(
                strategy,
                ['prefer_longest', 'prefer_shortest']
            ))

        def overlapsWith(entries: List[Tuple[int,int,str]]) -> List[int]:
            # determine ranges (works also without mapper)
            pmin = 0
            pmax = max([ entry[1] for entry in entries ] + [pmin]) # add pmin list to avoid issues with empty lists
            fields_used = [ set() for _ in range(pmin, pmax)]

            # mark field positions
            for entry_idx, (start, stop, lbl) in enumerate(entries):
                for field_idx in range(start, stop):
                    fields_used[field_idx].add(entry_idx)

            # accumulate all overlapping entry idxs for each entry
            return [ reduce(lambda acc, new: acc.union(new), [
                    fields_used[field_idx] for field_idx in range(start, stop)
                ], set())
                for (start, stop, lbl) in entries
            ]

        def mergeOverlappingEntries(entries: List[Tuple[int,int,str]]) -> List[Tuple[int,int,str]]:
                # filter for one label
                merged_entries = []
                overlaps = overlapsWith(entries)
                seen_entry_idxs = set()

                for entry_idx,_ in enumerate(entries):
                    if entry_idx in seen_entry_idxs:
                        continue
                    # aggregate mergeable entries
                    overlap_idxs = overlaps[entry_idx]
                    overlap_entries = [ oentry for oidx, oentry in enumerate(entries) if oidx in overlap_idxs ]
                    merged_entry = (
                        min([ e[0] for e in overlap_entries ]),
                        max([ e[1] for e in overlap_entries ]),
                        lbl
                    )
                    merged_entries.append(merged_entry)
                    seen_entry_idxs.update(overlap_idxs)

                # update and reorder merged entries
                return list(sorted(sorted(merged_entries, key=lambda x: x[1]), key=lambda x: x[0]))

        def removeByPriority(entries: List[Tuple[int,int,str]], strategy) -> List[Tuple[int,int,str]]:
            # prioritize entries
            if strategy == "prefer_longest":
                priority = [ (entry[1]-entry[0]) for entry in entries ]
            elif strategy == "prefer_shortest":
                priority = [ -(entry[1]-entry[0]) for entry in entries ]
            else: raise Exception(f"Unknown strategy: {strategy}")

            # determine overlaps and keep by priority
            overlaps = overlapsWith(entries)
            nonoverlapping_entries = []
            seen_entry_idxs = set()
            for entry_idx, entry in sorted(enumerate(entries), key=lambda x: priority[x[0]], reverse=True):
                if entry_idx in seen_entry_idxs: continue
                seen_entry_idxs.update(overlaps[entry_idx])
                nonoverlapping_entries.append(entry)
            return list(sorted(sorted(nonoverlapping_entries, key=lambda x: x[1]), key=lambda x: x[0]))

        entries = self.entries
        # merge first, if we are prioritiize longer sequences
        if merge_same_classes and strategy == "prefer_longest":
            entries_merged = []
            # merge only per label
            for lbl in self.getLabels():
                entries_merged += mergeOverlappingEntries([
                    entry for entry in entries if entry[2] == lbl
                ])
            entries = list(sorted(sorted(entries_merged, key=lambda x: x[1]), key=lambda x: x[0]))

        entries = removeByPriority(entries, strategy)

        # merge last, if we are prioritiize shorter sequences
        if merge_same_classes and strategy == "prefer_shortest":
            merged_entries = []
            # merge only per label
            for lbl in self.getLabels():
                merged_entries += mergeOverlappingEntries([
                    entry for entry in entries if entry[2] == lbl
                ])
            entries = list(sorted(sorted(merged_entries, key=lambda x: x[1]), key=lambda x: x[0]))

        return AnnotationSet(entries, self.level, self.mapper)

    def countOverlaps(self) -> int:
        ctr = 0
        cursor = 0
        for start, stop, _ in self.entries:
            if start < cursor:
                # overlap found -> discard
                ctr += 1
            else:
                cursor = stop
        return ctr

    def ontoMapper(self, mapper: BaseMapper) -> "AnnotationSet":
        if not isinstance(mapper, BaseMapper):
            raise ValueError("Unknown mapper given.")

        if self.level == "dseq":
            raise Exception("Convert AnnotationSet to text spans first.")

        # validate if no mapper is given
        if self.mapper is not None:
            if self.mapper.getText() != mapper.getText():
                raise Exception("Text of mappers do not match.")
        else:
            print("Cannot validate text of annotation data because no previous mapper was set.", file=sys.stderr)
        return AnnotationSet(self.entries, self.level, mapper)

    def toFormattedSequence(self, schema: Literal["IOB2", "plain"] = "IOB2"):
        if self.level != "dseq":
            raise ValueError("Convert to dseq spans first.")
        if self.mapper is None:
            raise ValueError("No mapper is set.")
        if not schema in ["IOB2", "plain"]:
            raise ValueError("Unknown schema: {}, one of {}".format(
                schema,
                ["IOB2", "plain"]
            ))

        n_overlaps = self.countOverlaps()
        if n_overlaps > 0:
            raise ValueError("Entries have {} overlaps -> remove overlaps first.".format(
                n_overlaps
            ))

        fseq = []
        n_seq = len(self.mapper.dseq) if self.level == "dseq" else len(self.mapper.text)
        cursor = 0
        if schema == "IOB2":
            for start, stop, label in self.entries:
                fseq += [ "O" for _ in range(start-cursor)] +\
                    [ "B-" + label ] +\
                    [ "I-" + label for _ in range(stop-start-1) ]
                cursor = stop
            fseq += [ "O" for _ in range(n_seq-cursor)]
        if schema == "plain":
            for start, stop, label in self.entries:
                fseq += [ None for _ in range(start-cursor)] +\
                    [ label for _ in range(stop-start) ]
                cursor = stop
            fseq += [ None for _ in range(n_seq-cursor)]
        return fseq

    def toEntities(self, with_text: bool = None):
        if self.entries is None:
            raise ValueError("Entries are None.")
        if with_text:
            if self.mapper is None:
                raise ValueError("No mapper assigned.")
            {"text": self.mapper.getText(), "label": self.entries}