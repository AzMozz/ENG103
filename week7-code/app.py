from flask import Flask
from gpiozero import LED

app = Flask(__name__)

# Define the LEDs connected to GPIO17, GPIO26, and GPIO16
bedroom_led = LED(17)  # GPIO17 for Bedroom Light
livingroom_led = LED(26)  # GPIO26 for Living Room Light
kitchen_led = LED(16)  # GPIO16 for Kitchen Light


# Create a function to control the LEDs
@app.route("/led/<int:pin>/<state>")
def control_led(pin, state):
    # Control the Bedroom Light (GPIO17)
    if pin == 17:
        if state == "on":
            bedroom_led.on()
            return "Bedroom Light (GPIO17) is ON"
        elif state == "off":
            bedroom_led.off()
            return "Bedroom Light (GPIO17) is OFF"

    # Control the Living Room Light (GPIO26)
    elif pin == 26:
        if state == "on":
            livingroom_led.on()
            return "Living Room Light (GPIO26) is ON"
        elif state == "off":
            livingroom_led.off()
            return "Living Room Light (GPIO26) is OFF"

    # Control the Kitchen Light (GPIO16)
    elif pin == 16:
        if state == "on":
            kitchen_led.on()
            return "Kitchen Light (GPIO16) is ON"
        elif state == "off":
            kitchen_led.off()
            return "Kitchen Light (GPIO16) is OFF"

    else:
        return "Invalid GPIO pin."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
