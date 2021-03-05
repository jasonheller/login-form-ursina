from ursina import *
main = Ursina()

window.fps_counter.enabled = True
window.exit_button.visible = False
window.borderless = False
window.show_ursina_splash = True
window.fullscreen = False

bg = load_texture('bg.png')

class Background(Entity):
    def __init__(self):
        super().__init__(
            model = 'quad',
            texture = bg,
            parent = scene,
            scale = 15
        )

# Login - Button
login = Button(text='Login', color=color.black, model='quad', collider='quad', origin=(4,1.8,0), scale=0.08)

# Text - Password and Input Field
text1 = Text(text='Password:', color=color.white, origin=(1.57,3.95,0), scale=1)
password = InputField(position=(0,-0.15,0), hide_content=True)

# Text - Username and Username Text
text2 = Text(text='Username:', color=color.white, origin=(1.50,-0.25,0), scale=1)
username = InputField(position=(0,-0.05,0), hide_content=False)

# Text - Title
text3 = Text(text='Login Form', color=color.white, origin=(0,-8,0), scale=2)

background = Background()
main.run()