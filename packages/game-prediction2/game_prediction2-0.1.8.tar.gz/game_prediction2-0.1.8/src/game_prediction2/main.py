from typing import Unpack
from chess import STARTING_FEN
from chess_utils.fens import position_idx
from .beam import predict as beam_predict, SearchParams
from .util.predict import prefetched_logprobs, PredictFn, Annotations

def predict(
  predict: PredictFn, annotations: list[Annotations] | None = None, *,
  max_moves: int, batch_size: int = 8,
  prefetch: int = 2, **params: Unpack[SearchParams]
):
  """Beam decoding across the forest of moves stemming from `start_fens`
  - Yields predictions as the beams converge (i.e. agree on a single move) or the search stops (because no legal moves have high enough probability)
    - Thus, a bigger `beam_width` can increase accuracy but also prediction time by more than a constant factor
  """
  start_ply = position_idx(params.get('fen') or STARTING_FEN)
  return beam_predict(
    prefetched_logprobs(predict, annotations, max_moves=max_moves, start_ply=start_ply, batch_size=batch_size, prefetch=prefetch),
    **params
  )