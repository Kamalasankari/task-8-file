class Television:
    price = 20000
    inches = 40
    On = 1
    OFF = 0

    def __init__(self, brand, tvp, volume=50, chanel=1):
        self.bnd = brand
        self.vol = volume
        self.cnl = chanel
        self.tvt = tvp

    def vol(self):
        if self.vol < 0 or self.vol > 100:
            self.vol = 50
        else:
            return

    def cnl(self):
        if self.cnl < 1 or self.cnl > 50:
            self.cnl = 1
        else:
            return

    def reset(self):
        self.vol = 50
        self.cnl = 1

    def status(self):
        print(self.bnd, " at channel", self.cnl, ", volume ", self.vol)


tv = Television("Panasonic", "plasma", 70, 20)
tv.vol
tv.cnl
tv.status()
tv.reset()
tv.status()


class Tvtype(Television):

    def __init__(self, brand, tvp):
        self.bnd = brand
        self.tvt = tvp

    def plasma(self):

        print("(screen_thickness = 6 inches, energy_usage = 150-200 watts, lifespan = 60,000 hours,")
        print("/n refresh_rate = 600 Hz, viewing_angle = 70 degrees , backlight = No Backlight")
        print("/n display_details = Bright up to 3.8 metres")

    def led(self):

        print("(screen_thickness = 3 inches, energy_usage = 50-60 watts, lifespan = 60,000 hours,")
        print("refresh_rate = 80 Hz, viewing_angle = 70 degrees , backlight = Light emitting diodes")
        print("display_details = 450 nits")

    def display(self):
        if self.tvt == "plasma":
            self.plasma()
        if self.tvt == "led":
            self.led()


a = Tvtype("Panasonic", "plasma",)

a.display()
