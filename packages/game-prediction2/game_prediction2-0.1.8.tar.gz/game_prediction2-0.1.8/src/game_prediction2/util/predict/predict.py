from typing import Protocol, Awaitable, AsyncIterable, TypedDict, NotRequired, Unpack
import haskellian.asyn.promises as P
import haskellian.asyn.iter as AI
from ..logprobs import logprob, Annotations
from ...beam.succs import Logprob

class PredictFn(Protocol):
  """Batched predictions of plies `[from_ply, to_ply)` for all (1 or 2) players
  - Must return an array of shape `BATCH x PLAYERS x TOP_PREDS` of `(pred, logprob)` tuples
  """
  def __call__(self, from_ply: int, to_ply: int) -> Awaitable[list[list[list[tuple[str, float]]]]]:
    ...

class BatchedParams(TypedDict):
  max_moves: int
  start_ply: NotRequired[int]
  batch_size: NotRequired[int]

class PrefetchedParams(BatchedParams):
  prefetch: NotRequired[int]

@AI.lift
async def batched_logprobs(predict: PredictFn, annotations: list[Annotations] | None = None, *, max_moves: int, start_ply: int = 0, batch_size: int = 8) -> AsyncIterable[list[Logprob]]:
  for i in range(start_ply, max_moves, batch_size):
    preds = await P.wait(predict(i, i+batch_size))
    yield [logprob(ps, annotations) for ps in preds]

@AI.lift
def prefetched_logprobs(predict: PredictFn, annotations: list[Annotations] | None = None, *, prefetch: int = 2, **p: Unpack[BatchedParams]) -> AsyncIterable[Logprob]:
  """Async iterable of `Logprob`s by calling `predict`. Prefetches and batches requests"""
  prefetched = batched_logprobs(predict, annotations, **p) \
    .prefetch(prefetch)
  return AI.flatten(prefetched)
  