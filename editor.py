def init_game(sender, message):
    print ("game got " + message + " from " + sender)
    nextcmd = ''
    if find_player(sender):
        game_state = load_game(sender)
        play(sender, game_state)
    else:
        create_player(sender)
        nextcmd = play(sender,'new')
    if nextcmd == 'quit':
        save_game(sender)
        return False
    else return True

def find_player(sender):
    if sender in ['oscar', 'j', 'angus']:
        return True
    else return False

def load_game(sender):
    return "Oakland"

def play(player_name, game_status):
    while nextcmd != 'quit':
        pass
    return nextcmd

def create_player(sender):
    return sender
