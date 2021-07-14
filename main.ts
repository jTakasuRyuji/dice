input.onButtonPressed(Button.A, function () {
	
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.SmallSquare)
    basic.showIcon(IconNames.Square)
    basic.showNumber(randint(0, 9))
    basic.pause(5000)
    basic.clearScreen()
})
basic.showString("Hello!")
basic.clearScreen()
basic.forever(function () {
	
})
