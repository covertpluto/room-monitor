from flask import Flask, render_template, redirect
import random
from gpiozero import CPUTemperature

import debug_led

import sensors

cpu = CPUTemperature()
app = Flask(__name__)


@app.route("/")
def hello_world():
    debug_led.success()
    room_name = open("config/room_name.txt", 'r')
    output = render_template("index.html", rn=room_name.readline(),
                             temperature=sensors.temp(),
                             humidity=sensors.hum(),
                             airQuality=0,
                             lights=sensors.light(),
                             cpu=cpu.temperature,
                             heatloss=sensors.heatloss())
    room_name.close()
    return output


@app.errorhandler(404)
def page_not_found(e):
    debug_led.page_access_error()
    return redirect("/")

@app.route("/settings")
def settings():
    return 'You have reached the settings page. To return, click <a href="/">Here</a>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
