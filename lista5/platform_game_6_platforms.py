import pygame, os
import game_module as gm

os.environ['SDL_VIDEO_CENTERED'] = '1'          # centrowanie okna
pygame.init()


## ustawienia ekranu i gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
pygame.display.set_caption('Prosta gra platformowa...')
clock = pygame.time.Clock()


# klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = set()
        self.movement_x = 0
        self.movement_y = 0
        self.count = 0
        self.lifes = 3
        self.level = None
        self.direction_of_movement = 'right'

    def _gravitation(self):
        if self.movement_y == 0:
            self.movement_y = 1
        else:
            self.movement_y +=0.4

    def jump(self):
        if self.movement_y == 0:
            self.movement_y = -20

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_right(self):
        self.movement_x = 15
        self.direction_of_movement = 'right'

    def turn_left(self):
        self.movement_x = -15
        self.direction_of_movement = 'left'

    def stop(self):
        self.movement_x = 0

    # 10_10_10_10_10_10_10_10_10_10_10_10_10 metoda strzelania
    def shoot(self):
        if len(self.items) > 0:
            bullet = Bullet(gm.BULLET_R, self.direction_of_movement)
            if self.direction_of_movement == 'right':
                bullet.rect.x = self.rect.x + 50
            else:
                bullet.rect.x = self.rect.x 
            bullet.rect.y = self.rect.y + 50
            self.level.set_of_bullets.add(bullet)

    def update(self):
        self._gravitation()
        self.rect.x += self.movement_x

        cp = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)

        for p in cp:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right

        if self.movement_x > 0:
            self._move(gm.IMAGES_R)

        if self.movement_x < 0:
            self._move(gm.IMAGES_L)


        self.rect.y += self.movement_y

        cp = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)

        for p in cp:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
            if self.movement_y < 0:
                self.rect.top = p.rect.bottom
            self.movement_y = 0

        if self.movement_y > 0:
            if self.direction_of_movement == 'right':
                self.image = gm.FALL_R
            else:
                self.image = gm.FALL_L
        if self.movement_y < 0:
            if self.direction_of_movement == 'right':
                self.image = gm.JUMP_R
            else:
                self.image = gm.JUMP_L
        if self.movement_y == 0 and self.movement_x == 0:
            if self.direction_of_movement == 'right':
                self.image = gm.STAND_R
            else:
                self.image = gm.STAND_L

        # 999999999999999999999999999999999999999 wykrywanie kolizji z Itemami
        cp = pygame.sprite.spritecollide(self, self.level.set_of_items, False)

        for p in cp:
            self.items.add(p.name)
            p.kill()


    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.turn_right()
            if event.key == pygame.K_a:
                self.turn_left()
            if event.key == pygame.K_w:
                self.jump()

            # 11_11_11_11_11_11_11_11_11_11_11_11_11_11_11 wywłowanie metody strzelania
            if event.key == pygame.K_SPACE:
                self.shoot()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.movement_x > 0:
                self.stop()
                #self.image = gm.STAND_R
            if event.key == pygame.K_a and self.movement_x < 0:
                self.stop()
                #self.image = gm.STAND_L

    def _move(self, image_list):
        if self.count < 4:
            self.image = image_list[0]
        elif self.count < 8:
            self.image = image_list[1]
        if self.count >= 8:
            self.count = 0
        else:
            self.count += 1

# 111111111111111111111111 klasa Item
class Item(pygame.sprite.Sprite):
    def __init__(self,image,name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
    

# 2222222222222222222222222 klasa Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self,image,direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.direction_of_movement = direction
        self.rect = self.image.get_rect()

    def update(self):
        if self.direction_of_movement == 'right':
            self.rect.x +=15
        elif self.direction_of_movement == 'left':
            self.rect.x -= 15

class Platform(pygame.sprite.Sprite):
    def __init__(self,colour,width,height,rect_x,rect_y):
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.image.fill(colour)

    def draw(self, surface, listOfImages):

        if self.width == 70:
            surface.blit(listOfImages[0], self.rect)
        else:
            surface.blit(listOfImages[1], self.rect)

        for i in range(70, self.width - 70, 70):
            surface.blit(listOfImages[2], [self.rect.x + i, self.rect.y])

        surface.blit(listOfImages[3], [self.rect.x + self.width - 70, self.rect.y])



class Level():
    def __init__(self,player):
        self.player = player
        self.set_of_platforms = set()
        self.world_shift = 0

        # 33333333333333333333333 dodatkowe atrybuty
        self.set_of_items = pygame.sprite.Group()
        self.set_of_bullets = pygame.sprite.Group()

    def update(self):
        for i in self.set_of_platforms:
            i.update()

        # 4444444444444444444444444 uaktualnienie metody update
        for i in self.set_of_bullets:
            i.update()

        #shift when player close to the right edge
        if self.player.rect.right > 400:
            diff = self.player.rect.right - 400
            self.player.rect.right = 400
            self._shift_world(-diff)

        #close to the left edge
        if self.player.rect.left < 100:
            diff = 100 - self.player.rect.left
            self.player.rect.left = 100
            self._shift_world(diff)
        
        #  777777777777777777777777777777777777777 usuwanie pocisków
        self._delete_bullets()

    def _shift_world(self, world_shift):
        self.world_shift += world_shift

        for p in self.set_of_platforms:
            p.rect.x += world_shift

    # 6666666666666666666666666666666 metoda usuwania pocisków
    def _delete_bullets(self):
        for i in self.set_of_bullets:
            for j in self.set_of_platforms:
                if i.direction_of_movement == 'right':
                    if pygame.sprite.collide_rect(i,j)==True:
                        i.kill()
                elif i.direction_of_movement == 'left':
                    if pygame.sprite.collide_rect(j,i)==True:
                        i.kill()



    def draw(self,surface):
        for i in self.set_of_platforms:
            i.draw(surface, gm.GRASS_LIST)

        # 55555555555555555555555555 uaktualnienie metody draw
        for i in self.set_of_items:
            surface.blit(gm.SHOTGUN, i.rect)

        for i in self.set_of_bullets:
            if i.direction_of_movement == 'right':
                surface.blit(gm.BULLET_R, i.rect)
            elif i.direction_of_movement == 'left':
                surface.blit(gm.BULLET_L, i.rect)

class Level_1(Level):
    def __init__(self,player):
        super().__init__(player)
        list_p = ((7000,70,0,gm.HEIGHT-70),
                  (280,70,800,500),(140,70,200,500),
                  (70, 70,100,700))
        for i in list_p:
            p = Platform(gm.DARKGREEN,*i)
            self.set_of_platforms.add(p)

        # 8888888888888888888888888888888888 dodanie shotguna
        shotgun = Item(gm.SHOTGUN, "shotgun")
        for p in self.set_of_platforms:
            shotgun.rect.y = 650
            shotgun.rect.x = 100
            break
        self.set_of_items.add(shotgun)



# konkretyzacja obiektów
player = Player(gm.STAND_R)
player.rect.center = screen.get_rect().center
level_1 = Level_1(player)
player.level = level_1


# głowna pętla gry
window_open = True
while window_open:
    screen.fill(gm.LIGHTBLUE)
    # pętla zdarzeń
    for event in pygame.event.get():
        player.get_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        elif event.type == pygame.QUIT:
            window_open = False

    # rysowanie i aktualizacja obiektów
    player.update()
    player.draw(screen)
    level_1.update()
    level_1.draw(screen)

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(30)

pygame.quit()