import pygame
import pyjokes
import time

from Globals import Globals as self

pygame.init()
clock = pygame.time.Clock()


class Game:
    """
    All logic is only in this class.
    It contains 5 functions, in each function, its
     action will be informed.
    We use global parameters from Globals.py
    To work with it, you need to generate an example
     of it.
    For play the game, please run main.py
    """

    @staticmethod
    def get_joke():
        """
        this function generates and get a random joke from
         the "pyjokes" module (which is already installed
         and imported)
        """
        self.joke_text = pyjokes.get_joke()
        self.joke_text = self.joke_text[:90]
        self.joke = self.joke_font.render(self.joke_text, True, 'yellow')
        self.joke2 = self.joke_font.render(self.joke_text, True, 'black')

    @staticmethod
    def result():
        """
        This function counts and check total time, accuracy
         and wpm while typing
        """
        accuracy = 0
        wpm = 0
        if not self.game_over:
            # calculate time
            self.total_time = time.time() - self.time_start
            # calculate accuracy
            count = 0
            for i, j in enumerate(self.joke_text):
                try:
                    if self.user_text[i] == j:
                        count += 1
                except:
                    pass
            try:
                accuracy = count / len(self.user_text) * 100
                # calculate wpm (words per minutes)
                wpm = len(self.user_text) * 60 / (5 * self.total_time)
            except:
                pass
            # 'Time:1   Accuracy:100 %    Wpm:1'
            self.res = 'Time:' + str(round(self.total_time)) + \
                       " secs   Accuracy:" + str(round(accuracy)) + "%" + \
                       '   WpM: ' + str(round(wpm))
        self.results = self.result_font.render(self.res, True, 'green')
        self.results2 = self.result_font.render(self.res, True, 'black')

    @staticmethod
    def testing():
        """
        This function is the main one (run the code).
        Responsible for typing, the "start" and "exit" buttons.
        """
        play = True
        active = False
        a = ''
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False

                # mouse button for reStart
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 350 <= x <= 550 and 400 <= y <= 464:
                        Game.get_joke()
                        self.user_text = ''
                        active = True
                        self.game_over = False
                        self.time_start = time.time()
                        self.rect_color = 'green'
                        self.start_color = 'green'
                        self.len_rect = 10

                # KEYDOWN for word processing
                elif event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_RETURN:
                        active = False
                        self.game_over = True
                        # saved result on console
                        print(' ' + self.user_text)
                        print(self.res + '\n')
                        self.rect_color = 'red'
                        self.start_color = 'red'

                    elif event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                        if len(a) > 0:
                            self.user_text = a[len(a) - 1] + self.user_text
                            a = a[:-1]
                        if len(self.user_text) < 80:
                            self.len_rect -= 5
                    else:
                        if self.len_rect < 440:
                            self.len_rect += 5
                        self.user_text += event.unicode
                        if len(self.user_text) > 90:
                            a = a + self.user_text[0]
                            self.user_text = self.user_text.replace(self.user_text[0], '', 1)
            Game.result()
            Game.fonts()
            pygame.display.update()
            clock.tick(80)

    @staticmethod
    def display(header_text, header_text_2, text, finish_key, rect_size,
                header2_xy, header_xy, joke2_xy, joke_xy, results2_xy,
                results_xy, finish_xy, text_xy):
        """
            This function displays widgets in a screen.
        """
        # background
        self.screen.blit(self.bg, (0, 0))

        # rect for input text
        pygame.draw.rect(self.screen, 'black', rect_size)
        pygame.draw.rect(self.screen, self.rect_color, rect_size, 3)

        # start button
        pygame.draw.rect(self.screen, self.start_color, (345, 395, 210, 74))
        self.screen.blit(self.start, (350, 400))

        # header text
        self.screen.blit(header_text_2, header2_xy)
        self.screen.blit(header_text, header_xy)
        # output text (random text, joke)
        self.screen.blit(self.joke2, joke2_xy)
        self.screen.blit(self.joke, joke_xy)
        # input text
        self.screen.blit(text, text_xy)
        # result text
        self.screen.blit(self.results2, results2_xy)
        self.screen.blit(self.results, results_xy)
        # finish rext
        self.screen.blit(finish_key, finish_xy)

    @staticmethod
    def fonts():
        """
        This function is responsible for the characteristics of widgets.
        """
        # text fonts
        text_font = pygame.font.SysFont("georgia", self.text_size)
        header_font = pygame.font.SysFont('mannerliness', self.header_size)
        header_text = header_font.render('KEYBOARD TRAINER', True, 'white')
        header_text_2 = header_font.render('KEYBOARD TRAINER', True, 'black')
        text = text_font.render(self.user_text, True, 'white')
        finish_font = pygame.font.SysFont('georgia', self.finish_size)
        finish_key = finish_font.render('Press ENTER for finish!', True, 'white')

        # blit coord
        rect = max(self.len_rect, 150)
        rect_size = (self.width / 2 - rect, 160, 2 * rect, 50)
        header2_xy = header_text.get_rect(center=(self.width / 2 + 4, 50 + 4))
        header_xy = header_text.get_rect(center=(self.width / 2, 50))
        text_xy = text.get_rect(center=(self.width / 2, 185))
        joke2_xy = self.joke.get_rect(center=(self.width / 2 + 1, 105 + 1))
        joke_xy = self.joke.get_rect(center=(self.width / 2, 105))
        results2_xy = self.results.get_rect(center=(self.width / 2 + 1, 310 + 1))
        results_xy = self.results.get_rect(center=(self.width / 2 + 1, 310 + 1))
        finish_xy = finish_key.get_rect(center=(self.width / 2, 500))

        Game.display(header_text, header_text_2, text, finish_key, rect_size,
                     header2_xy, header_xy, joke2_xy, joke_xy, results2_xy,
                     results_xy, finish_xy, text_xy)
