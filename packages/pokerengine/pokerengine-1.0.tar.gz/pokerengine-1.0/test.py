from __future__ import annotations

from pokerengine.card import Cards, CardGenerator

from typing import Dict, Any, Type, Union, Optional
from pokerengine.engine import EngineRake01

from pokerengine.pokerengine_core.engine import EngineTraits


class Poker:
    def __init__(
        self,
        traits: EngineTraits,
        *,
        engine_class: Type[Union[EngineRake01]] = EngineRake01,
        seed: int = 1927,
    ) -> None:
        self.engine = engine_class(traits=traits)
        self.cards: Optional[Cards] = None
        self.cards_generator = CardGenerator(seed=seed)

    def information(self) -> Dict[str, Any]:
        return {
            "actions": {
                "actions": self.engine.actions.actions
            },
            "players": {
                "players": self.engine.players.players,
            },
            "positions": {
                "current": self.engine.positions.current,
                "player": self.engine.positions.player,
            },
            "pot": {
                "pot": self.engine.pot.pot(),
                "round_highest_bet": self.engine.pot.round_highest_bet,
            },
            "round": {
                "round": self.engine.round.round,
                "flop_dealt": self.engine.round.flop_dealt
            },
            "traits": {
                "sb_bet": self.engine.traits.sb_bet,
                "bb_bet": self.engine.traits.bb_bet,
                "bb_mult": self.engine.traits.bb_mult,
                "min_raise": self.engine.traits.min_raise,
            }
        }
