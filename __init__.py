from adapt.intent import IntentBuilder
from mycroft.skills.core import intent_handler
from mycroft import MycroftSkill


class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    @intent_handler(IntentBuilder("").require('ask'))
    def handle_query_time(self):
        self.speak_dialog('rep')

def create_skill():
    return MyFirstSkill()
