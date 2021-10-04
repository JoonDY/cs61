"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """

    ###############
    # My Solution #
    ###############

    paragraphs = list(filter(select, paragraphs))
    
    if len(paragraphs) <= k:
        return ''
    else:
        return paragraphs[k]


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC."""

    ###############
    # My Solution #
    ###############

    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'

    def select(paragraph):
        paragraph = paragraph.lower().split()
        new_paragraph = []
        for word in paragraph:
            new_paragraph.append(remove_punctuation(word))
        return any(word in new_paragraph for word in topic)
    
    return select



def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed."""

    ###############
    # My Solution #
    ###############

    typed_words = split(typed)
    reference_words = split(reference)

    if len(typed_words) == 0:
        return 0.0
    elif len(reference_words) == 0:
        return 0.0
    
    accuracy = 0
    for i in range(0, len(typed_words)):
        if len(typed_words) > len(reference_words) and len(reference_words) - i == 0:
            break
        elif typed_words[i] == reference_words[i]:
            accuracy+=1

    return accuracy/len(typed_words)*100



def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""

    ###############
    # My Solution #
    ###############

    assert elapsed > 0, 'Elapsed time must be positive'

    num_chars = len(typed)
    words = num_chars/5
    minutes = elapsed / 60

    return words / minutes



def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """

    ###############
    # My Solution #
    ###############

    if user_word in valid_words:
        return user_word
    
    valid = {}
    for word in valid_words:
        valid[word] = diff_function(user_word, word, limit)

    if (min(valid.values())) > limit:
        return user_word
    
    return min(valid, key=valid.get)




def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """

    ###############
    # My Solution #
    ###############

    len_diff = 0
    if len(start) != len(goal):
        len_diff = abs(len(goal) - len(start))

    def helper(start, goal, count):
        if count > limit:
            return count
        if len(start) == 0 or len(goal) == 0:
            return count
        else:
            if start[0] == goal[0]:
                return helper(start[1:], goal[1:], count)
            else:
                count+=1
                return helper(start[1:], goal[1:], count)
    
    return helper(start, goal, len_diff)



def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    ###############
    # My Solution #
    ###############

    if limit < 0:
        return 0

    if len(start) == 0 and len(goal) == 0:
        return 0
    elif len(start) == 0 or len(goal) == 0:
        return abs(len(start) - len(goal))
    elif start[0] == goal[0]:
        return pawssible_patches(start[1:], goal[1:], limit)
    else:
        add_diff = pawssible_patches(start, goal[1:], limit - 1)
        remove_diff = pawssible_patches(start[1:], goal, limit - 1)
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit - 1)
        return min(add_diff, remove_diff, substitute_diff) + 1



def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""

    ###############
    # My Solution #
    ###############

    correct = 0
    for i in range(0, len(typed)):
        if typed[i] == prompt[i]:
            correct+=1
        else:
            break
    
    ratio = correct / len(prompt)

    message = {"id": user_id, "progress": ratio}
    send(message)

    return ratio



def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report



def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """

    ###############
    # My Solution #
    ###############

    times = []
    for i in range(0, len(times_per_player)):
        player = []
        for j in range(0, len(times_per_player[i])):
            if times_per_player[i][j] == times_per_player[i][-1]:
                break
            player.append(times_per_player[i][j+1] - times_per_player[i][j])
        times.append(player)
    
    return game(words, times)



def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]



def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])



def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """

    ###############
    # My Solution #
    ###############

    player_indices = range(len(all_times(game)))
    word_indices = range(len(all_words(game)))

    # winners = []
    # for word in word_indices:
    #     player_times = []
    #     for player in player_indices:
    #         player_times.append(time(game, player, word))
    #     winners.append(player_times.index(min(player_times)))

    # for player in player_indices:
    #     wins = []
    #     for i in range(0, len(winners)):
    #         if player == winners[i]:
    #             wins.append(word_at(game, i))
    #     results.append(wins)

    results = []
    for player in player_indices:
        wins = []
        for word in word_indices:
            winner = all_times(game).index(min(all_times(game), key=lambda x: x[word]))
            if player == winner:
                wins.append(word_at(game, word))
        results.append(wins)

    return results



enable_multiplayer = True

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)