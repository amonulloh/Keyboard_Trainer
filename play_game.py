import pygame, pyjokes, time

pygame.init()
clock = pygame.time.Clock()

# 700x500
width = 900
height = 600

# background and icon img
bg_img = 'background_keyboard.jpg'
icon_img = 'icon.png'
start_img = 'start_png.png'

# header screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Keyboard Trainer')
icon = pygame.image.load(icon_img)
pygame.display.set_icon(icon)
bg = pygame.image.load(bg_img)
bg = pygame.transform.scale(bg, (width, height))
start = pygame.image.load(start_img)
start = pygame.transform.scale(start, (200, 64))

# font of texts
text_font = pygame.font.SysFont("georgia", 20)

header_font = pygame.font.SysFont('berlinsansfb', 60)
header_text = header_font.render('KEYBOARD TRAINER', True, 'white')
header_font_2 = pygame.font.SysFont('berlinsansfb', 60)
header_text_2 = header_font_2.render('KEYBOARD TRAINER', True, 'black')

finish_font = pygame.font.SysFont('georgia', 15)
finish_key = finish_font.render('Press ENTER for finish!', True, 'white')

joke_font = pygame.font.SysFont('georgia', 20)
joke = joke_font.render('Are you ready?', True, 'yellow')
joke2 = joke_font.render('Are you ready?', True, 'black')

result_font = pygame.font.SysFont('georgia', 30)

# parameters
user_text = ''
user_joke = ''
time_start = 0
total_time = 0
res = 'Time:0   Accuracy:0 %    WpM:0'
results = result_font.render(res, True, 'red')
results2 = result_font.render(res, True, 'black')
game_over = True

# function random sentebces(jokes)
def get_jokes():
    global joke, joke2, jokes
    jokes = pyjokes.get_joke()
    print_jokes = jokes[:90]
    joke = joke_font.render(print_jokes, True, 'yellow')
    joke2 = joke_font.render(print_jokes, True, 'black')


# function results
def result():
    global results, results2

    # calculate time
    total_time = time.time() - time_start

    accuracy = 0
    wpm = 0

    if not game_over:

        # calculate accuracy
        count = 0
        for i, j in enumerate(jokes):
            try:
                if user_text[i] == j:
                    count += 1
            except:
                pass
        try:
            accuracy = count / len(user_text) * 100
            
            # calculate wpm (words per minutes)
            wpm = len(user_text) * 60 / (5 * total_time)
        except:
            pass

        # 'Time:1   Accuracy:100 %    Wpm:1'
        res = 'Time:' + str(round(total_time)) + " secs   Accuracy:" + str(round(accuracy)) + "%" + '   WpM: ' + str(round(wpm))
        results = result_font.render(res, True, 'green')
        results2 = result_font.render(res, True, 'black')

    # pygame.display.update()


# function runnig
def testing():
    global time_start
    global user_text, game_over
    play = True
    active = False
    rect_color = 'red'
    len_rect = 10
    start_color = 'red'

    while play:
        # pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

            # mousebutton for reStart
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 350 <= x <= 550 and 400 <= y <= 464:
                    get_jokes()
                    user_text = ''
                    active = True
                    game_over = False
                    time_start = time.time()
                    rect_color = 'green'
                    start_color ='green'
                    len_rect = 10

            # KEYDOWN for word processing
            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    active = False
                    # saved result on consol
                    print('1. ' + user_text)
                    print(res + '\n')
                    rect_color = 'red'
                    start_color = 'red'

                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                    if len_rect < 400:
                        len_rect -= 5
                else:
                    if len_rect < 440:
                        len_rect += 5
                    user_text += event.unicode
                    result()

        # background
        screen.blit(bg, (0, 0))

        # rect for input text
        len_rect1 = max((len_rect), 150)
        pygame.draw.rect(screen, 'black', (width / 2 - len_rect1, 160, 2*len_rect1, 50))
        pygame.draw.rect(screen, rect_color, (width / 2 - len_rect1, 160, 2*len_rect1, 50), 3)

        # start button
        pygame.draw.rect(screen, start_color, (345, 395, 210, 74))
        screen.blit(start, (350, 400))

        # text display
            # header text
        screen.blit(header_text_2, header_text.get_rect(center=(width / 2 + 4, 50 + 4)))
        screen.blit(header_text, header_text.get_rect(center=(width / 2, 50)))
            # output text (random text, joke)
        screen.blit(joke2, joke.get_rect(center=(width / 2 + 1, 105 +1)))
        screen.blit(joke, joke.get_rect(center=(width / 2, 105)))
            # input text
        text = text_font.render(user_text, True, 'white')
        screen.blit(text, text.get_rect(center=(width / 2, 185)))
            # result text
        screen.blit(results2, results.get_rect(center=(width / 2 + 1, 310 + 1)))
        screen.blit(results, results.get_rect(center=(width / 2, 310)))
            # finish rext
        screen.blit(finish_key, finish_key.get_rect(center=(width / 2, 500)))

        pygame.display.update()
        clock.tick(80)

# running functions
result()
testing()
