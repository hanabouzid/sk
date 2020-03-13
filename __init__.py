from adapt.intent import IntentBuilder
from mycroft import MycroftSkill
from mycroft.skills.core import intent_handler


class FocusDefinition(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("").require('hana.focus'))
    def handle_focus_def(self):
        self.speak_dialog('hana.focus')


def create_skill():
    return FocusDefinition()
