from pypokerengine.api.game import setup_config, start_poker
from pypokerengine.players import BasePokerPlayer
from PokerAI import *

config = setup_config(max_round=5, initial_stack=1000, small_blind_amount=15)
config.register_player(name="Randy", algorithm=RandomPlayer())
config.register_player(name="Truther", algorithm=HonestPlayer())
config.register_player(name="AI", algorithm=EmulatorPlayer())
game_result = start_poker(config, verbose=1)

# print("RESULTS")
# print(game_result['players'][0]['stack'])
file = open("output.txt", "a")
file.write(str(game_result['players'][0]['stack']))
file.write(' ')
file.write(str(game_result['players'][1]['stack']))
file.write(' ')
file.write(str(game_result['players'][2]['stack']))
file.write("\n")
file.close()