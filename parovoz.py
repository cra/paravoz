import pyxel


class App:
    def __init__(self):
        self.X0 = 16
        self.Y0 = 61
        self.N = 6
        self.show_debug = False
        self.kolbas = 4

        pyxel.init(256, 128, title="Parovoz")
        pyxel.load('parovoz.pyxres')
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.Y0 -= 3
            self.Y0 = max(50, self.Y0)
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.Y0 += 3
            self.Y0 = min(self.Y0, 100)
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.X0 -= 3
            self.X0 = max(self.X0, 10)
        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.X0 += 3
            self.X0 = min(self.X0, 46)

        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.KEY_SPACE):
            pyxel.playm(1)
        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btnp(pyxel.KEY_D):
            self.show_debug = True
        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) or pyxel.btnp(pyxel.KEY_A):
            self.N += 1
            self.N = min(self.N, 7)
        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y) or pyxel.btnp(pyxel.KEY_B):
            self.N -= 1
            self.N = max(self.N, 2)

    def draw(self):
        pyxel.cls(1)

        pyxel.text(6, 6, f"edet", 7)
        if self.show_debug: pyxel.text(6, 12, f"x{self.X0},y{self.Y0},N{self.N}", 7)

        for i in range(self.N):
            x = self.X0 + i * 32 + (16 if i > 0 else 0)
            y = self.Y0 + pyxel.sin(pyxel.frame_count * 5.73 + i * 120.3) * self.kolbas
            col = 15
            pyxel.pal(1, col)
            if i == 0:
                pyxel.blt(x, y, 0, 32, 40, 48, 16, 0)
            else:
                pyxel.blt(x, y, 0, 40, 56, 32, 16, 0)
        pyxel.pal()


App()
