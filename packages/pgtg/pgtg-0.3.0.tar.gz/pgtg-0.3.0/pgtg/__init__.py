from gymnasium.envs.registration import register

from pgtg.environment import PGTGEnv

__version__ = "0.3.0"

register(id="pgtg-v2", entry_point="pgtg.environment:PGTGEnv")
