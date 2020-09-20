import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()   # Group功能类似于列表，为游戏开发提供额外功能
    aliens = Group()
    # 在gf中的create_fleet（）函数中调用create_alien中的aliens.add(alien)来实现将各个alien写入aliens中
    # 当然在使用alien前需要创建Alien()类的实例，Alien()类需要继承Sprite()类才可以传入Group()类中，实现编组以及对编组使用方法

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始循环游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 任何时候，都需要不断监测鼠标键盘的活动情况
        # 任何时候，都需要不断刷新屏幕
        # 只有游戏开始后，才执行if内部的代码
        if stats.game_active:
            ship.update()  # 飞船移动  个人认为这块内容放在gf中也可以
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # update是说明该元素需要根据玩家控制，控制会改变元素的位置，从而需要不断更新元素的位置；
            # 更新位置通常先小数话坐标，再通过自加自减来更新位置，最后再将小数坐标整数化返回给self.rect，接着用blit来传输图像

            # 为什么ship直接调用本身的update,而bullets和aliens需要借助gf?
            # 后两者是编组

            # 更新外星人位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
