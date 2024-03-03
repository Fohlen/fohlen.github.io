from typing import NamedTuple

class Unit(NamedTuple):
    id: int  # the unique identifier of the unit
    start: int  # represents the start index of your unit
    end: int  # represents the end index of your unit


def map_documents(document_a: list[Unit], document_b: list[Unit]) -> list[int]:
    mapped_spans = []

    for span_b in document_b:
        for span_a in document_a:
            if span_b.start <= span_a.end:
                mapped_spans.append(span_a.id)
                break

    return mapped_spans

doc_a = [Unit(0, 0, 10), Unit(1, 11, 20), Unit(2, 21, 30)]
doc_b = [Unit(0, 0, 10), Unit(1, 11, 15), Unit(2, 16, 19), Unit(3, 20, 30)]
assert map_documents(doc_a, doc_b) == [0, 1, 1, 1]
