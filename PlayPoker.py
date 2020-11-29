from pypokerengine.api.game import setup_config, start_poker
from pypokerengine.players import BasePokerPlayer
from PokerAI import *

config = setup_config(max_round=5, initial_stack=100, small_blind_amount=5)
config.register_player(name="Randy", algorithm=RandomPlayer())
config.register_player(name="Truther", algorithm=HonestPlayer())
config.register_player(name="AI", algorithm=EmulatorPlayer())
game_result = start_poker(config, verbose=1)


print(game_result)