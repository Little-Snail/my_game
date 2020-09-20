import pygame
# pygame模块
from pygame.sprite import Sprite
# pygame.sprite模块  也可以不用这句，继承时用pygame.Sprite


class Bullet(Sprite):
    """一个对飞船发射子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        # 为什么此处是引用参数，而不是继承类呢？
        # 因为我们立足的是主程序，在主程序调用其他内容，而不是在其他程序中调用其他程序的内容
        # 而且这里的参数在主程序中已经定义过了，所以直接作为参数传入这里后，在主程序中调用是最合理方便的
        """在飞船所处的位置创建一个子弹"""
        super().__init__()  # super(Bullet, self).__init__()
        self.screen = screen

        # """在（0，0）处创建一个表示子弹的矩形，再设置正确的位置"""
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        # 设置子弹颜色和速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
