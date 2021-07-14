def on_gesture_six_g():
    basic.show_number(20)
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

def on_gesture_three_g():
    basic.show_number(10)
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

def on_gesture_eight_g():
    basic.show_number(30)
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_number(randint(0, 9))

def on_forever():
    pass
basic.forever(on_forever)
