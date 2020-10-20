# coding=utf-8
"""
Main bot script file
"""
import imutils
import pyautogui
import cv2
import numpy as np
import os
from time import time, sleep

font = cv2.FONT_HERSHEY_PLAIN
threshold = 0.80

try:
    os.remove("./screenshots/screenshot.png")
    os.remove("screenshot.png")
except FileNotFoundError:
    print()

pyautogui.screenshot("./screenshots/screenshot.png")

screenshot_rgb = cv2.imread("./screenshots/screenshot.png")
screenshot_gray = cv2.cvtColor(screenshot_rgb, cv2.COLOR_BGR2GRAY)

east_rock__full_template = cv2.imread('./screenshots/lumbride_east_copper_rock_full.png', 0)
south_rock__full_template = cv2.imread('./screenshots/lumbride_south_copper_rock_full.png', 0)

east_rock__full_w, east_rock_full_h = east_rock__full_template.shape[::-1]
south_rock_full_w, south_rock_full_h = south_rock__full_template.shape[::-1]

east_rock_mineable = False
east_res = cv2.matchTemplate(screenshot_gray, east_rock__full_template, cv2.TM_CCOEFF_NORMED)
east_loc = np.where( east_res >= threshold)

for pt in zip(*east_loc[::-1]):
    cv2.rectangle(screenshot_rgb, pt, (pt[0] + east_rock__full_w, pt[1] + east_rock_full_h), (255, 255, 255), 1)

south_rock_mineable = False
south_res = cv2.matchTemplate(screenshot_gray, south_rock__full_template, cv2.TM_CCOEFF_NORMED)
south_loc = np.where( south_res >= threshold)

for pt in zip(*south_loc[::-1]):
    cv2.rectangle(screenshot_rgb, pt, (pt[0] + south_rock_full_w, pt[1] + south_rock_full_h), (255, 255, 255), 1)

cv2.imshow("Lumby Mine", imutils.resize(screenshot_rgb, width=750))
cv2.imshow("Lumby Mine", screenshot_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()

try:
    os.remove("./screenshots/screenshot.png")
except FileNotFoundError:
    print()

def runLoop():
    try:
        os.remove("./screenshots/screenshot.png")
        os.remove("screenshot.jpg)")
    except FileNotFoundError:
        print()

    pyautogui.screenshot("./screenshots/screenshot.png")

    # Colour versions of the sample screenshots
    east_rock_true_south_rock_true_rgb = cv2.imread("./screenshots/east_rock_true_south_rock_true.png")
    east_rock_true_south_rock_false_rgb = cv2.imread("./screenshots/east_rock_true_south_rock_false.png")
    east_rock_false_south_rock_true_rgb = cv2.imread("./screenshots/east_rock_false_south_rock_true.png")
    east_rock_false_south_rock_false_rgb = cv2.imread("./screenshots/east_rock_false_south_rock_false.png")
    screenshot_rgb = cv2.imread("./screenshots/screenshot.png")

    # Grayscale versions of the coloured screenshots
    east_rock_true_south_rock_true_gray = cv2.cvtColor(east_rock_true_south_rock_true_rgb, cv2.COLOR_BGR2GRAY)
    east_rock_true_south_rock_false_gray = cv2.cvtColor(east_rock_true_south_rock_false_rgb, cv2.COLOR_BGR2GRAY)
    east_rock_false_south_rock_true_gray = cv2.cvtColor(east_rock_false_south_rock_true_rgb, cv2.COLOR_BGR2GRAY)
    east_rock_false_south_rock_false_gray = cv2.cvtColor(east_rock_false_south_rock_false_rgb, cv2.COLOR_BGR2GRAY)
    screenshot_gray = cv2.cvtColor(screenshot_rgb, cv2.COLOR_BGR2GRAY)

    # An example picture of the east rock being full and empty
    east_rock__full_template = cv2.imread('./screenshots/lumbride_east_copper_rock_full.png', 0)
    east_rock__empty_template = cv2.imread('./screenshots/lumbride_east_copper_rock_empty.png', 0)

    # An example picture of the south rock being full and empty
    south_rock__full_template = cv2.imread('./screenshots/lumbride_south_copper_rock_full.png', 0)
    south_rock__empty_template = cv2.imread('./screenshots/lumbride_south_copper_rock_empty.png', 0)

    # An example picture of a full inventory
    inventory_ore_template = cv2.imread('./screenshots/copper_ore.png', 0)

    # Width and height of the sample image of an east rock
    # Full
    east_rock__full_w, east_rock_full_h = east_rock__full_template.shape[::-1]
    Empty
    east_rock__empty_w, east_rock_fempty_h = east_rock__empty_template.shape[::-1]

    # Width and height of the sample image of a south rock
    # Full
    south_rock_full_w, south_rock_full_h = south_rock__full_template.shape[::-1]
    Empty
    south_rock_empty_w, south_rock_empty_h = south_rock__empty_template.shape[::-1]

    # Width and height of the image of the full inventory
    inventory_ore__w, inventory_ore__h = inventory_ore_template.shape[::-1]

    east_rock_mineable = False
    east_res = cv2.matchTemplate(screenshot_gray, east_rock__full_template, cv2.TM_CCOEFF_NORMED)
    east_loc = np.where( east_res >= threshold)

    if len(east_loc) == 2:
        for pt in zip(*east_loc[::-1]):
            cv2.rectangle(screenshot_rgb, pt, (pt[0] + east_rock__full_w, pt[1] + east_rock_full_h), (255, 255, 255), 1)
            # cv2.putText(screenshot_rgb,'Copper Rock', (pt[0] , pt[1]), font, 3, (255,255,255), 1, cv2.LINE_AA)
        east_rock_mineable = bool(east_loc)

    south_rock_mineable = False
    south_res = cv2.matchTemplate(screenshot_gray, south_rock__full_template, cv2.TM_CCOEFF_NORMED)
    south_loc = np.where( south_res >= threshold)

    if len(south_loc) == 2:
        for pt in zip(*south_loc[::-1]):
            cv2.rectangle(screenshot_rgb, pt, (pt[0] + south_rock_full_w, pt[1] + south_rock_full_h), (255, 255, 255), 1)
        south_rock_mineable = bool(south_loc)

    print("East rock is mineable " + str(east_rock_mineable))
    print("South rock is mineable " + str(south_rock_mineable))

    inventory_ore_res = cv2.matchTemplate(screenshot_gray, inventory_ore_template, cv2.TM_CCOEFF_NORMED)
    inventory_ore_loc = np.where( east_res >= threshold)
    for pt in zip(*inventory_ore_loc[::-1]):
        cv2.rectangle(screenshot_rgb, pt, (pt[0] + inventory_ore__w, pt[1] + inventory_ore__h), (255, 255, 255), 1)

    cv2.imshow("Lumby Mine", imutils.resize(img_rgb, width=1000))
    cv2.imshow("Lumby Mine", screenshot_rgb)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    sleep(2)

cv2.waitKey(0)
cv2.destroyAllWindows()