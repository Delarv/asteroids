def write(screen, font, text, location, color=(255,255,255)):
    screen.blit(font.render(text, True, color), location)