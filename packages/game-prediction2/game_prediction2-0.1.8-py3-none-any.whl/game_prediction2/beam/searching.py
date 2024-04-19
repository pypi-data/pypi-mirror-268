from typing import Protocol, Iterable, AsyncIterable, Unpack, NotRequired
import haskellian.iterables as hk
import haskellian.asyn.iter as AI
import chess
import lcz
from ..util import logprobs as logps
from .succs import AggregateLogps, SuccParams, Logprob, successors, Node

class UCIPrior(Protocol):
  """Evaluates a batch of `fens` into `UCI -> Probability` mappings"""
  def __call__(self, fens: Iterable[str]) -> list[dict[str, float]]:
    ...
    
class BeamWidth(Protocol):
  def __call__(self, ply: int) -> int:
    ...

class SearchParams(SuccParams):
  uci_prior: NotRequired[UCIPrior]
  agg_logp: NotRequired[AggregateLogps]
  beam_width: NotRequired[BeamWidth]
  fen: NotRequired[str|None]
  
Beam = Iterable[Node]

async def search(logprobs: AsyncIterable[Logprob], **p: Unpack[SearchParams]) -> AsyncIterable[Beam]:
  """Beam search across the forest of moves stemming from `start_fens`
  - `logprobs[ply](san, piece)`: (OCR) log-probability of `san` (which captures `piece`) at `ply`
  - `uci_prior(fens)`: batched prior distribution of legal moves (defaults to using `MaiaChess` with `Leela Chess Zero`)
  - `agg_logp(logp, logq)`: aggregation function of the OCR and prior log-probabilities. Defaults to a weighted geometric average giving the OCR probabilities 10x the importance. I.e. `(p^10 * q)^(1/11)` (but in log-space, ofc)
  """
  uci_prior = p.get('uci_prior', lcz.eval)
  agg_logp = p.get('agg_logp', lambda logp_ocr, logp_prior: logps.weighted_geo_mean(logp_ocr, logp_prior, a=10, b=1))
  beam_width = p.get('beam_width', lambda _: 4)
  fen = p.get('fen') or chess.STARTING_FEN

  beam: Beam = [Node(fen)]
  priors = uci_prior([fen])
  async for i, lp in AI.enumerate(logprobs):
    inputs = zip(beam, priors)
    nested_succs = hk.starmap(lambda node, prior: successors(node, prior, lp, agg_logp))(inputs)
    succs = list(hk.flatten(nested_succs))
    if succs == []:
      return
    else:
      beam = sorted(succs, key=lambda x: x.sum_logp, reverse=True)[:beam_width(i)]
      priors = uci_prior(n.fen for n in beam)
      yield beam