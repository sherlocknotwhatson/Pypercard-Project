"""
This simple app demonstrates how cards can automatically advance to another
card after a certain amount of time. The auto_advance can either be a string
containing the name of the next card, or a function to call that returns the
name of the next card.
"""
from pypercard import App, Card


def auto_func(app, card):
    """
    Called while transitioning from card 2, to card 3.
    """
    count = app.datastore.setdefault("counter", 0)
    count += 1
    app.datastore["counter"] = count
    return "card3"


# The templates for these cards can be found in pypercard.html.
cards = [
    Card("card1", ),
    Card("card2", ),
    Card("card3", ),
]


# Create the app while ensuring the counter is reset.
carousel_app = App(
    name="PyperCard carousel", cards=cards
)

@carousel_app.transition("card1", "click", "next")
def go_next(app, card):
    return "card2"

@carousel_app.transition("card2", "click", "reset")
def reset(app, card):
    return "card1"


carousel_app.start("card1")
