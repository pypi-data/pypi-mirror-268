from typing import AsyncIterable, Unpack
import haskellian.asyn.iter as AI
from .succs import Logprob
from .searching import search, SearchParams
from .decoding import decode

@AI.lift
def predict(logprobs: AsyncIterable[Logprob], **params: Unpack[SearchParams]):
  """Beam decoding across the forest of moves stemming from `start_fens`
  - Yields predictions as the beams converge (i.e. agree on a single move) or the search stops (because no legal moves have high enough probability)
    - Thus, a bigger `beam_width` can increase accuracy but also prediction time by more than a constant factor
    
  Params:
  - `logprobs[ply](san, piece)`: (OCR) log-probability of `san` (which captures `piece`) at `ply`
  - `uci_prior(fens)`: batched prior distribution of legal moves (defaults to using `MaiaChess` with `Leela Chess Zero`)
  - `agg_logp(logp, logq)`: aggregation function of the OCR and prior log-probabilities. Defaults to a weighted geometric average giving the OCR probabilities 10x the importance. I.e. `(p^10 * q)^(1/11)` (but in log-space, ofc)
  """
  beams = search(logprobs, **params)
  return decode(beams)