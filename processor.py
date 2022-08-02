from actions import Actions
from re import match

action = {
    Actions.play: ["play*"],
    Actions.get_wiki: ["wikipedia*"],
    Actions.tell_joke: ["tell(.*?)joke", "say(.*?)joke", "joke"],
    Actions.change_volume: ["set volume*", "volume*", "change volume*", "change loudness*", "set loudness*", "loudness*"],
    Actions.set_gender: ["set gender*", "change gender*", "gender*", "sex*", "set sex*", "change sex*"]
}

action_keys = list(action.keys())

def process(command):
    for action_key in action_keys:
        for matchable in action[action_key]:
            if match(matchable, command):
                action_key(command)
                break

"""
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who the heck is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('please say the command again')
        """