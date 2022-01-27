class Person:
    def __init__(self, name, nationality='GBR'):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f'{self.name}({self.nationality})'


class Player(Person):
    SCORE_TRANSLATOR = {
        0: 'love',
        1: 'fifteen',
        2: 'thirty',
        3: 'forty',
    }

    score = 0

    def translate_score(self):
        try:
            return self.SCORE_TRANSLATOR[self.score]
        except KeyError:
            raise Exception('Invalid score')


class TennisGame:
    def __init__(self, player_one, player_two):
        # Player 1 assumed to be serving (read first in score)
        self.player_one = player_one
        self.player_two = player_two
        self.winner = None

    def get_score(self):
        winner = self.find_winner()

        if winner:
            return f'{winner} wins'

        advantage = self.find_advantage()

        if advantage:
            return f'Advantage {advantage}'

        if self.is_deuce():
            return 'Deuce'

        if self.player_one.score == self.player_two.score:
            return f'{self.player_one.translate_score()} all'

        return '{} - {}'.format(
            self.player_one.translate_score(),
            self.player_two.translate_score()
        )

    def is_deuce(self):
        return (
            self.player_one.score >= 3 and
            self.player_two.score == self.player_one.score
        )

    def find_winner(self):
        if (
            self.player_one.score >= 4 and
            (self.player_one.score - self.player_two.score) >= 2
        ):
            self.winner = self.player_one

        elif (
            self.player_two.score >= 4 and
            (self.player_two.score - self.player_one.score) >= 2
        ):
            self.winner = self.player_two

        return self.winner

    def find_advantage(self):
        if (
            self.player_one.score >= 4 and
            (self.player_one.score - self.player_two.score) == 1
        ):
            return self.player_one

        if (
            self.player_two.score >= 4 and
            (self.player_two.score - self.player_one.score) == 1
        ):
            return self.player_two

    def __score(self, player):
        if self.winner:
            return f'{self.winner} has already won'

        player.score += 1
        return self.get_score()

    def player_one_scores(self):
        return self.__score(self.player_one)

    def player_two_scores(self):
        return self.__score(self.player_two)


tennis = TennisGame(Player('Henry'), Player('Franki'))