from ursina import *

app = Ursina()
window.title = 'Mini Clicker - JSJ'
window.borderless = False
window.color = color._20

gold = 0
gold_text = Text(text = str(gold), y = 0.2, scale = 2, background = True)
button = Button(text = '1', color = color.light_gray, text_color = color.black, scale = .2)

def button_click():
    global gold
    gold += 1

button.on_click = button_click

# auto gold generator
auto_button_1 = Button(text = '1G/sec\n(Price: 10G)', x = 0.25, scale = 0.2, disabled = True, cost = 10, earn = 1)

def auto_earn_gold(earn = 1, interval = 1):
    global gold
    gold += earn

    invoke(auto_earn_gold, earn, delay = interval)

def get_auto_gold(button, earn = 1):
    global gold

    if gold >= button.cost:
        gold -= button.cost
        invoke(auto_earn_gold, earn = earn, interval = 1)

#auto_button_1.on_click = get_auto_gold
auto_button_1.on_click = Func(get_auto_gold, auto_button_1)

def update():
    global gold

    gold_text.text = str(gold)
    if gold >= auto_button_1.cost:
        auto_button_1.disabled = False
        auto_button_1.color = color.green
        auto_button_1.text_color = color.black
    else:
        auto_button_1.disabled = True
        auto_button_1.color = color.black
        auto_button_1.text_color = color.white

app.run()   # opens a window and starts the game.