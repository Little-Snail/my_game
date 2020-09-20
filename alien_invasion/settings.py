class Settings:
    """储存《外星人入侵》的所有重要设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船移速,大于1就会移动的更快
        self.ship_speed_factor = 1
        self.ship_limit = 3

        # 外星人移速
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动，为-1表示向左
        self.fleet_direction = 1

        # 子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60   # 这是一个元组,元组可以不带括号
        self.bullets_allowed = 3
