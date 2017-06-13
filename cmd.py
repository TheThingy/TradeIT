#! /usr/bin/env python3
import sys


def decode_command(game, command):
    """Decode command and do action based on command"""
    command_list = command.split()
    
    if command_list[0] == "goto":
        if len(command_list) < 2:
            print("Error! Please specify city to go to.")
            return
        game.player.set_location(game.city_list.get_city(command_list[1]))
        game.do_step()
    elif command_list[0] == "info":
        infolist = ["Name: %s" %(game.player.name),
                    "Money: %i" %(game.player.money),
                    "Location: %s" % (game.player.location.city_name),
                    "Loan: %i" % (game.player.loan.get_loan())
                ]
        return infolist

    elif command_list[0] == "exit":
        sys.exit()

    elif command_list[0] in ["help", "halp", "hjelp"]:
        if len(command_list) == 1:
            helplist = ["info", "exit", "goto", "loan"]
            return helplist
        else:
            if command_list[1] == "info":
                hilist = ["Usage: info", "Shows information about your character"]
                return hilist
            if command_list[1] == "exit":
                helist = ["Usage: exit", "Exits the game"]
                return helist
            if command_list[1] == "goto":
                hglist = ["Usage: goto [city]", "Will transport the player to [city]"]
                return hglist
            if command_list[1] == "loan":
                hllist = ["Usage: loan [number]", "Positive number borrows, negative number repays the amount"]
                return hllist



def get_prompt(game):
    """Returns prompt used for input"""
    prompt = str(game.player.name)
    prompt += "@"
    prompt += str(game.player.location.city_name)
    prompt += "$ "
    return prompt
