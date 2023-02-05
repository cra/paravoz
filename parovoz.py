import pyxel


class App:
    def __init__(self):
        pyxel.init(256, 128, title="Parovoz")
        pyxel.load('parovoz.pyxres')
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


    def draw(self):
        pyxel.cls(1)

        pyxel.text(6, 6, "edet", 7)

        for i in range(7):
            x = 16 + i * 32 + (16 if i > 0 else 0)
            y = 61 + pyxel.sin(pyxel.frame_count * 5.73 + i * 120.3) * 4
            col = 15
            pyxel.pal(1, col)
            if i == 0:
                pyxel.blt(x, y, 0, 32, 40, 48, 16, 0)
            else:
                pyxel.blt(x, y, 0, 40, 56, 32, 16, 0)
        pyxel.pal()


App()
