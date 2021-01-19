from ursina import *

app = Ursina()
window.title = 'Mini Clicker - JSJ'
window.borderless = False
window.color = color._20

gold = 0
gold_text = Text(text = str(gold), y = .2, scale = 2, background = True)
button = Button(text = '1', x = -.5, color = color.light_gray, text_color = color.black, scale = .2)

def button_click():
    global gold
    gold += 1

button.on_click = button_click

# auto gold generator
def auto_earn_gold(earn = 1, interval = 1):
    global gold
    gold += earn

    invoke(auto_earn_gold, earn, delay = interval)

def get_auto_gold(button, earn = 1):
    global gold

    if gold >= button.cost:
        gold -= button.cost
        invoke(auto_earn_gold, earn = earn, interval = 1)

auto_settings = [
    {
        'cost': 10,
        'earn': 1,
        'upgrade': 0,
    },
    {
        'cost': 100,
        'earn': 5,
        'upgrade': 0,
    },
    {
        'cost': 1000,
        'earn': 25,
        'upgrade': 0,
    },
    {
        'cost': 10000,
        'earn': 125,
        'upgrade': 0,
    },
]

auto_buttons = []

for i, setting in enumerate(auto_settings):
    b = Button(
        text = f'{setting["earn"]}G/sec\n(Price: {setting["cost"]}G)',
        x = .25 * (i + 1) - .5,
        scale = 0.2,
        disabled = True,
        cost = setting['cost'],
        earn = setting['earn'],
        upgrade = setting['upgrade']
    )

    b.on_click = Func(get_auto_gold, b, b.earn)
    auto_buttons.append(b)

def update():
    global gold

    gold_text.text = str(gold)
    for button in auto_buttons:
        if gold >= button.cost:
            button.disabled = False
            button.color = color.green
            button.text_color = color.black
        else:
            button.disabled = True
            button.color = color.black
            button.text_color = color.white

app.run()   # opens a window and starts the game.