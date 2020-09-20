import pygame


class Ship:

    def __init__(self, ai_settings, screen):  # 相当于继承别的类
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图形并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船图像放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中储存小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新飞船的center值，而不是rect,因为rect移动是像素个数只能为整数
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象，因为控制飞船移动的rect.centerx被换成小数的center,
        # 所以将移动后变化的center值再赋给centerx，据此来绘画出飞船新的位置
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船，因为图像元素已经与屏幕指定位置对齐，只需将飞船元素绘制出来即可"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船再屏幕中央"""
        # self.rect.centerx = self.screen_rect.centerx  不可以
        # 原因在于center只是作为小数来传递数字变化的，参见def update(self)
        # 此处将屏幕的x中间值传给cnter后，center会再后续的update()函数这将该值传递给飞船的rect.centerx

        self.center = self.screen_rect.centerx