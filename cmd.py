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
        print("Name: %s" %(game.player.name))
        print("Money: %i" %(game.player.money))
        print("Location: %s" %(game.player.location.city_name))
        print("Loan: %i" %(game.player.loan))
    elif command_list[0] == "exit":
        print("Quitting")
        sys.exit()
    elif command_list[0] in ["help", "halp", "hjelp"]:
        if len(command_list) == 1:
            print("Available commands:")
            print("info")
            print("exit")
            print("goto")
            print("loan")
        else:
            if command_list[1] == "info":
                print("Usage: info")
                print("Shows information about your character")
            if command_list[1] == "exit":
                print("Usage: exit")
                print("Exits the game")
            if command_list[1] == "goto":
                print("Usage: goto [city]")
                print("Will transport the player to [city]")
            if command_list[1] == "loan":
                print("Usage: loan [number]")
                print("Positive number borrows, negative number repays the amount")



def get_prompt(game):
    """Returns prompt used for input"""
    prompt = str(game.player.name)
    prompt += "@"
    prompt += str(game.player.location.city_name)
    prompt += "$ "
    return prompt
