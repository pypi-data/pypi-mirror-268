from typing import AsyncIterable
import numpy as np
import ramda as R
from haskellian.core import pipe
import haskellian.iterables as hk
import haskellian.asyn.iter as AI
from .succs import Node, Child

@R.curry
def reconstruct(node: Node, max_depth: int | None = None, with_probs: bool = True) -> list[tuple[str, float]] | list[str]:
  """Reconstruct backwards from `node` (keeping log-probs as they are)
  - `max_depth`: limit of backward steps
  """
  match node:
    case Child():
      curr = [(node.san, node.logp) if with_probs else node.san]
      if max_depth is None or max_depth > 0:
        return reconstruct(node.parent, max_depth=max_depth and max_depth-1, with_probs=with_probs) + curr
      else:
        return curr
    case _:
      return []
    
def exp(preds_logps: list[tuple[str, float]]) -> list[tuple[str, float]]:
  """Exponentiate log-probabilities"""
  preds, logps = hk.unzip(preds_logps)
  exps = np.exp(logps)
  return list(zip(preds, exps))

def convergence(beam: list[Node], max_depth: int | None = None) -> int:
  """Convergence point: ply back to which all lines of the `beam` agree on the best move
  - `max_depth`: limit of backward steps (from the current beam's ply)
  """
  return pipe(
    map(reconstruct(max_depth=max_depth, with_probs=False), beam), # line of every beam
    hk.transpose, # moves at every ply
    hk.map(set), # aka uniq
    hk.take_while(lambda uniq_preds: len(uniq_preds) == 1),
    list, len
)
  
async def decode(beams: AsyncIterable[list[Node]]) -> AsyncIterable[list[tuple[str, float]]]:
  last_converged = 0
  beam = None
  async for ply, beam in AI.enumerate(beams):
    converged = convergence(beam, max_depth=ply-last_converged)
    if converged > 0:
      yield exp(reconstruct(beam[0], max_depth=ply-last_converged)[:converged])
      last_converged += converged
  if beam is not None:
    yield exp(reconstruct(beam[0], max_depth=max(ply-last_converged, 0)))