from kulka import Kulka
import time


ADDR = 'XX:XX:XX:XX:XX:XX'


def main():
    with Kulka(ADDR) as kulka:
        blink_rate = 0.001

        for _ in range(10):
            kulka.set_rgb(255, 255, 255)
            time.sleep(blink_rate)
            kulka.set_rgb(0, 0, 0)
            time.sleep(blink_rate)


main()
