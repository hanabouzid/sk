from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler


class MyFirstSkill(MycroftSkill):
    def __init__(self):
        super(MyFirstSkill, self).__init__(name="MyFirstSkill")

    @intent_handler(IntentBuilder("").require('ask'))
    def handle_hello_world_intent(self, message):
        self.speak_dialog('rep')

def create_skill():
    return MyFirstSkill()
