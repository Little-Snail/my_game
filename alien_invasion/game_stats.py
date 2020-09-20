class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化信息"""
        self.ai_settings = ai_settings
        self.ships_left = self.reset_stats()
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):     # 方便初始化__init__对reset的调用，也方便其他代码对该方法的调用
        """初始化在游戏运行期间可能变化的统计信息"""
        ships_left = self.ai_settings.ship_limit   # 当前存在的一条统计信息
        return ships_left