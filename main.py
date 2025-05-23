import data
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1200, 400))
pygame.display.set_caption("TP2")
FRAME_DURATION = 0.12

x, y = 600, 200

def parado():
    global x, y
    frame = pygame.image.load(f'sprites/parado.png')
    frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))

def direita():
    global x, y
    for frame in [pygame.image.load(f'sprites/direita/{i}.png') for i in range(0, 9)]:
        frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        screen.fill((0, 0, 0))
        screen.blit(frame, (x, y))
        pygame.display.flip()
        time.sleep(FRAME_DURATION)
        x = x + 12

def esquerda():
    global x, y
    for frame in [pygame.image.load(f'sprites/esquerda/{i}.png') for i in range(0, 9)]:
        frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        screen.fill((0, 0, 0))
        screen.blit(frame, (x, y))
        pygame.display.flip()
        time.sleep(FRAME_DURATION)
        x = x - 12

def defesa():
    global x, y
    for frame in [pygame.image.load(f'sprites/defesa/{i}.png') for i in range(0, 3)]:
        frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        screen.fill((0, 0, 0))
        screen.blit(frame, (x, y))
        pygame.display.flip()
        time.sleep(FRAME_DURATION)
        x += 1

def pulo():
    global x, y
    for frame in [pygame.image.load(f'sprites/pulo/{i}.png') for i in range(0, 4)]:
        frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        screen.fill((0, 0, 0))
        screen.blit(frame, (x, y))
        pygame.display.flip()
        time.sleep(FRAME_DURATION)
        y -= 15
    for frame in [pygame.image.load(f'sprites/pulo/{i}.png') for i in range(4, 8)]:
        frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        screen.fill((0, 0, 0))
        screen.blit(frame, (x, y))
        pygame.display.flip()
        time.sleep(FRAME_DURATION)
        y += 15

def ataquepadrao():
    global x, y
    for frame in [pygame.image.load(f'sprites/ataquepadrao/{i}.png') for i in range(0, 7)]:
        frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        screen.fill((0, 0, 0))
        screen.blit(frame, (x, y))
        pygame.display.flip()
        time.sleep(FRAME_DURATION)
        x += 12

def especial():
    global x, y
    for frame in [pygame.image.load(f'sprites/especial/{i}.png') for i in range(0, 17)]:
        frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        screen.fill((0, 0, 0))
        screen.blit(frame, (x, y))
        pygame.display.flip()
        time.sleep(FRAME_DURATION)
        x += 12

move = {
    0: lambda: screen.blit(parado),
    1: esquerda,
    2: pulo,
    3: direita,
    4: ataquepadrao,
    5: defesa,
    6: ataquepadrao,
    7: especial
}

def get_text_input():
    font = pygame.font.SysFont(None, 40)
    user_input = ""
    input_active = True

    while input_active:
        screen.fill((0, 0, 0))
        prompt = font.render("Digite a string de entrada e pressione Enter:", True, (255, 255, 255))
        input_text = font.render(user_input, True, (0, 255, 0))
        screen.blit(prompt, (50, 50))
        screen.blit(input_text, (50, 100))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

    return user_input

if __name__ == "__main__":
    afd = data.importXml("afd.jff")
    entrada = get_text_input()  # Captura entrada no Pygame
    afd.limpaAfd()
    afd.move(entrada, move)

    font = pygame.font.SysFont(None, 30)
    text = font.render("Digite qualquer tecla para encerrar", True, (255, 255, 255))
    screen.blit(text, (800, 350))
    pygame.display.flip()

    # Espera qualquer tecla
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN:
                waiting = False
