basic.showString("Ready")
basic.pause(500)
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        basic.showString("" + input.lightLevel())
    } else if (input.buttonIsPressed(Button.B)) {
        basic.showString("" + input.compassHeading())
    } else if (input.buttonIsPressed(Button.AB)) {
        basic.showString("" + input.acceleration(Dimension.X))
    } else if (input.temperature() < 25 && input.temperature() > 10) {
        basic.showIcon(IconNames.Happy)
        music.playTone(262, music.beat(BeatFraction.Eighth))
    } else if (input.temperature() > 25) {
        basic.showIcon(IconNames.Angry)
        music.playTone(262, music.beat(BeatFraction.Eighth))
    } else {
        basic.showIcon(IconNames.Sad)
        music.playTone(262, music.beat(BeatFraction.Eighth))
    }
})
