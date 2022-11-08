basic.show_string("Ready")
basic.pause(500)

def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_string("" + str((input.light_level())))
    elif input.button_is_pressed(Button.B):
        basic.show_string("" + str((input.compass_heading())))
    elif input.button_is_pressed(Button.AB):
        basic.show_string("" + str((input.acceleration(Dimension.X))))
    else:
        if input.temperature() < 25 and input.temperature() > 10:
            basic.show_icon(IconNames.HAPPY)
            music.play_tone(659, music.beat(BeatFraction.EIGHTH))
        else:
            if input.temperature() > 25:
                basic.show_icon(IconNames.ANGRY)
                music.play_tone(988, music.beat(BeatFraction.EIGHTH))
            else:
                basic.show_icon(IconNames.SAD)
                music.play_tone(196, music.beat(BeatFraction.EIGHTH))
basic.forever(on_forever)
