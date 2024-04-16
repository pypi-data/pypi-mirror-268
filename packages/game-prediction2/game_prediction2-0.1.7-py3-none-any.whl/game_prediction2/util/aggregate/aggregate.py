from collections import Counter
import numpy as np

def agg_max(preds: list[tuple[str, float]], k: int = None) -> list[tuple[str, float]]:
    """Aggregates by maxing probabilities of equal predictions"""
    acc = Counter()
    for move, prob in preds:
        cur = acc[move]
        acc[move] = max(prob, float("-inf") if cur == 0 else cur) # Counter defaults to 0, but logprob's identity is log(0) = -inf
    return acc.most_common(k)

def agg_union(preds: list[tuple[str, float]], k: int = None) -> list[tuple[str, float]]:
    """Aggregates by summing probabilities of equal predictions"""
    acc = Counter()
    for move, prob in preds:
        acc[move] += np.exp(prob)
    return [(m, np.log(p)) for m, p in acc.most_common(k)]