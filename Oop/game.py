class GameObject:
    def __init__(self, x, y, game):
        self.y = y
        self.x = x
        self.game = game
        self.alive = True
        self.passable = True
        self.interactable = True

    def interact(self, object):
        pass

    def process(self):
        pass

    def render(self):
        raise NotImplementedError


class Coin(GameObject):
    def render(self):
        return "$"


class Wall(GameObject):
    def render(self):
        return '#'

    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.alive = True
        self.passable = False
        self.interactable = False


coin = Coin(0, 0, 'ddd')
print(coin.render())

wall = Wall(0, 0, 'wall')
print(wall)


class Player(GameObject):
    def render(self):
        return '@'


class SoftWall(GameObject):
    def render(self):
        return '%'

    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.passable = False
        self.interactable = True


class HeatWave(GameObject):
    def render(self):
        return '+'

    def process(self):
        self.alive = False
        pass

    def interact(self, object):
        if type(object) == Player or type(object) == SoftWall: object.alive = False
        pass


player = Player(3, 4, 'ddd')
heatwave = HeatWave(5, 6, 'ddd')

heatwave.interact(player)
print(player)


class Render():
    def __init__(self):
        pass

    def init_screen(self, h, w):
        raise NotImplementedError

    def add_object(self, char, x, y):
        raise NotImplementedError

    def draw_screen(self):
     raise NotImplementedError

    def get_input(self):
        raise NotImplementedError


class ShellRender(Render):
    def init_screen(self, h, w):
        self._screen = []
        for i in range(h):
            self._screen = self._screen + [w * [' ']]

    def add_object(self, char, x, y):
        self._screen[y][x] = char

    def draw_screen(self):
        [print(''.join(row)) for row in self._screen]

    def get_input(self):
        return input()


sc = ShellRender()
sc.init_screen(3, 5)
sc.add_object('&', 1, 2)
sc.draw_screen()
