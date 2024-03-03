from typing import NamedTuple

class Sentence(NamedTuple):
    id: int  # the unique identifier of the unit
    start: int  # represents the start index of your unit
    end: int  # represents the end index of your unit

class Span(NamedTuple):
    id: int
    start: int
    end: int
    sentence: int

def map_documents(
    document_a: tuple[list[Sentence], list[Span]], 
    document_b: tuple[list[Sentence], list[Span]]
) -> tuple[list[int], list[int]]:
    sentences_a = iter(document_a[0])
    sentence_a = next(sentences_a)
    spans_a = iter(document_a[1])
    span_a = next(spans_a)

    sentences_b = iter(document_b[0])
    sentence_b = next(sentences_b)
    spans_b = iter(document_b[1])
    span_b = next(spans_b)

    sentences = []
    spans = []

    while sentence_b is not None or span_b is not None:
        if sentence_a is not None and sentence_b is not None:
            if sentence_b.start < sentence_a.end:
                sentences.append(sentence_a.id)
                sentence_b = next(sentences_b, None)
            else:
                sentence_a = next(sentences_a, None)

        if span_a is not None and span_b is not None:
            if span_b.start < span_a.end:
                spans.append(span_a.id)
                span_b = next(spans_b, None)
            else:
                span_a = next(spans_a, None)

    return sentences, spans

doc_a = (
    [Sentence(0, 0, 10), Sentence(1, 11, 20)],
    [Span(0, 0, 5, 0), Span(1, 6, 10, 0), Span(2, 11, 15, 1), Span(3, 16, 20, 1)]
)

doc_b = (
    [Sentence(0, 0, 7), Sentence(1, 8, 20)],
    [Span(0, 0, 5, 0), Span(1, 6, 7, 0), Span(2, 8, 15, 1), Span(3, 16, 20, 1)]
)

assert map_documents(doc_a, doc_b) == ([0, 0], [0, 1, 1, 3])
