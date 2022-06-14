import time
import numpy as np

from gym_xiangqi.agents import AlphaBetaAgent
from gym_xiangqi.constants import (     # NOQA
    RED, BLACK, PIECE_ID_TO_NAME, ALLY
)
from gym_xiangqi.utils import action_space_to_move
from gym_xiangqi.envs import XiangQiEnv


def main():
    # Pass in the color you want to play as (RED or BLACK)
    env = XiangQiEnv(RED)
    env.render()
    agent = AlphaBetaAgent()

    done = False
    round = 0
    while not done:
        if env.turn == ALLY:
            _, _, done, info = env.step_user()

            if "exit" in info and info["exit"]:
                break

            player = "You"
            piece, start, end = env.user_move_info
            piece = PIECE_ID_TO_NAME[piece]
        else:
            time.sleep(1)
            action_i = agent.move(env)
            actions = (env.ally_actions if env.turn == ALLY
                   else env.enemy_actions)
            legal_moves = np.where(actions == 1)[0]
            action = legal_moves[action_i]
            _, _, done, _ = env.step(action)

            player = "Agent"
            move = action_space_to_move(action)
            piece = PIECE_ID_TO_NAME[move[0]]
            start = move[1]
            end = move[2]

        env.render()
        round += 1
        print(f"Round: {round}")
        print(f"{player} made the move {piece} from {start} to {end}.")
        print("================")

    print("Closing Xiangqi environment")
    env.close()


if __name__ == '__main__':
    main()
