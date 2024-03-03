from typing import NamedTuple
import bisect

class Sentence(NamedTuple):
    id: int  # the unique identifier of the unit
    start: int  # represents the start index of your unit
    end: int  # represents the end index of your unit

class Span(NamedTuple):  # unfortunately inheriting NamedTuple comes with complications
    id: int
    start: int
    end: int
    sentence: int

doc_a = (
    [Sentence(0, 0, 10), Sentence(1, 11, 20)],
    [Span(0, 0, 5, 0), Span(1, 6, 10, 0), Span(2, 11, 15, 1), Span(3, 16, 20, 1)]
)

doc_b = (
    [Sentence(0, 0, 7), Sentence(1, 8, 20)],
    [Span(0, 0, 5, 0), Span(1, 6, 7, 0), Span(2, 8, 15, 1), Span(3, 16, 20, 1)]
)

sentence_mapping = {sentence.start: sentence.id for sentence in doc_a[0]}
sentence_mapping.update({sentence.end: sentence.id for sentence in doc_a[0]})
sentence_starts = sorted([sentence.start for sentence in doc_a[0]])
sentence_ends = sorted([sentence.end for sentence in doc_a[0]])

# get the sentence for span 3 in document a by ascending ordering
span_3_ascending_sentence = sentence_mapping[sentence_ends[bisect.bisect_left(sentence_ends, doc_b[1][3].start)]]
assert span_3_ascending_sentence == 1

# get the sentence for span 2 in document a by descending ordering
span_2_descending_sentence = sentence_mapping[sentence_starts[bisect.bisect_right(sentence_starts, doc_b[1][2].start)]]
assert span_2_descending_sentence == 1
