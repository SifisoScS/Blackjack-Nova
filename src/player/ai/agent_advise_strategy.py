from src.player.ai.basic_strategy_agent import BasicStrategyAgent
from src.ai.strategy import powerup_advisor

class AgentAdviseStrategy(BasicStrategyAgent):
    def __init__(self, deck, name = "Advise AI", bankroll = 100):
      super().__init__(deck,name, bankroll)

    def get_action(self, hand, dealer_upcard, powerups_available):
      #Use our powerup advisor
      advisor = powerup_advisor.PowerUpAdvisor(self.deck, hand, dealer_upcard)
      if advisor._evaluate_shuffle_up() > 0 and powerups_available['shuffle_up']:
          return 'shuffle_up'

      if advisor._evaluate_peek() > 0 and powerups_available['peek']:
          return 'peek'

      # Fallback: Use basic strategy if no powerups are good
      return super().get_action(hand, dealer_upcard, powerups_available)