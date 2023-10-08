import pygame
import sys
import math
from datetime import datetime

pygame.init()

pygame.display.set_caption("Det bedste ur")
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))

run_flag = True
while run_flag:

    # Ur data
    nutid = datetime.now()
    timer = datetime.now().hour
    minutter = datetime.now().minute
    sekunder = datetime.now().second

    # Tegn ur
    firkant_farve = (0, 0, 0)
    firkant_size = 300
    firkant_x = (500 - firkant_size) // 2
    firkant_y = (500 - firkant_size) // 2
    pygame.draw.rect(screen, firkant_farve, (firkant_x, firkant_y, firkant_size, firkant_size), 2)


    # Tegn ur linjer i rammen
    ur_outline = (0, 0, 0)
    ur_center = (250, 250)
    ur_radius = firkant_size // 2 - 10  # radius af linjer

    # minutter, timer, sekundviser
    hour_angle = math.radians(90 - (timer % 12) * 360 / 12 - (minutter / 60) * 360 / 12)
    hour_x = ur_center[0] + ur_radius * 0.5 * math.cos(hour_angle)
    hour_y = ur_center[1] - ur_radius * 0.5 * math.sin(hour_angle)
    pygame.draw.line(screen, ur_outline, ur_center, (hour_x, hour_y), 6)

    minute_angle = math.radians(90 - minutter * 360 / 60)
    minute_x = ur_center[0] + ur_radius * 0.7 * math.cos(minute_angle)
    minute_y = ur_center[1] - ur_radius * 0.7 * math.sin(minute_angle)
    pygame.draw.line(screen, ur_outline, ur_center, (minute_x, minute_y), 4)

    second_angle = math.radians(90 - sekunder * 360 / 60)
    second_x = ur_center[0] + ur_radius * 0.9 * math.cos(second_angle)
    second_y = ur_center[1] - ur_radius * 0.9 * math.sin(second_angle)
    pygame.draw.line(screen, (255, 0, 0), ur_center, (second_x, second_y), 2)

    for hour in range(1, 13):
        angle = math.radians(90 - (hour % 12) * 360 / 12)
        x1 = ur_center[0] + (ur_radius - 10) * math.cos(angle)
        y1 = ur_center[1] - (ur_radius - 10) * math.sin(angle)
        x2 = ur_center[0] + ur_radius * math.cos(angle)
        y2 = ur_center[1] - ur_radius * math.sin(angle)
        pygame.draw.line(screen, ur_outline, (x1, y1), (x2, y2), 4)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False


    # fyld skærm med hvid
    screen.fill((255, 255, 255))

pygame.quit()
sys.exit()