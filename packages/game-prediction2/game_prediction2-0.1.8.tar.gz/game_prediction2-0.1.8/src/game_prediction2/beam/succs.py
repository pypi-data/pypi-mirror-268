from typing import Protocol, Iterable, TypedDict, NotRequired
from dataclasses import dataclass
import numpy as np
import chess
from chess_utils import CapturablePiece, parse, unchecked_san, captured_piece, fen_after

class Logprob(Protocol):
  def __call__(self, san: str, captured_piece: CapturablePiece | None) -> float:
    ...
    
class AggregateLogps(Protocol):
  def __call__(self, logp_ocr: float, logp_prior: float) -> float:
    ...
    
@dataclass
class Node:
  fen: str
  sum_logp: float
  
  def __init__(self, fen: str, sum_logp = None):
    self.fen = fen
    self.sum_logp = sum_logp or 0
  
@dataclass
class Child(Node):
  sum_logp: float
  fen: str
  logp: float
  san: str
  parent: Node
  
  def __init__(self, fen: str, logp: float, san: str, parent: Node, sum_logp = None):
    self.fen = fen
    self.sum_logp = sum_logp or logp + parent.sum_logp
    self.logp = logp
    self.san = san
    self.parent = parent
    
class SuccParams(TypedDict):
  logp_min: NotRequired[float]
  ocr_logp_min: NotRequired[float]

def successors(
  node: Node, uci_priors: dict[str, float], lp: Logprob, agg_lp: AggregateLogps,
  logp_min: float = np.log(0.02), logp_ocr_min: float = np.log(0.02),
) -> Iterable[Child]:
  board = chess.Board(node.fen)
  for uci, p_prior in uci_priors.items():
    move = parse.uci(uci)
    san = unchecked_san(board, move)
    logp_prior = np.log(p_prior)
    captured = captured_piece(board, move) if 'x' in san else None
    logp_ocr = lp(san, captured)
    if logp_ocr < logp_ocr_min:
      continue
    logp = agg_lp(logp_ocr, logp_prior)
    if logp >= logp_min:
      yield Child(fen=fen_after(move, board), logp=logp, san=san, parent=node)