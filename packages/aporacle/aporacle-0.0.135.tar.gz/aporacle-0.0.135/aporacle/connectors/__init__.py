from pydantic import BaseModel

from aporacle import conf


class EventData(BaseModel):
    chain: str = conf.chain
    reward_epoch: int = 0
    event: str
    block_number: int
    timestamp: str


class VotingRound(EventData):
    voting_round: int
    voting_round_start: int