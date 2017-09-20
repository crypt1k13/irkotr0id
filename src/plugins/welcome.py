#/usr/bin/env python
# -*- coding: Utf8 -*-

import event
import random

class Plugin:

    def __init__(self, client):
        self.client = client

    @event.join()
    def welcome(self, e):
        nick = e.values['nick']
        if nick[0] in ('&', '~', '+', '@'):
            nick = nick[1:]
        chan = e.values['chan']
		# If the nick is the same as the bot, do nothing.
        if nick != self.client.nick_name:
			welcome = random.choice([
				"Hi, <NAME>",
				"Hey, <NAME>",
				"Hello, <NAME>",
				"Heyo, <NAME>",
				"Welcome <NAME>",
				"Greetings <NAME>!",
				"What's up <NAME>?",
				"Hello there <NAME>",
				"Speak of the devil",
				"How are you <NAME>?",
				"Hey, what's up <NAME>?",
				"Well, Hello there <NAME>",
				"Well, look who showed up!",
				"Look what the cat dragged in.",
				"Aloha, <NAME>",
				"Hola, <NAME>",
				"Bounjour, <NAME>",
				"Guten Tag, <NAME>",
				"Konnichiwa, <NAME>"
			])
			message = welcome.replace("<NAME>", nick)
			self.client.priv_msg(chan, message)

    def help(self, target):
        message = "The 'welcome' plugin greets everyone that joins the channel"
        self.client.priv_msg(target, message)
