import imutils
import pyautogui
import cv2
import numpy as np
import os

# try:
#     os.remove("./screenshots/screenshot.jpg")
#     os.remove("screenshot.jpg)")
# except FileNotFoundError:
#     print()

# pyautogui.screenshot("./screenshots/screenshot.jpg")
# pyautogui.screenshot("./screenshots/screenshot.jpg")

font = cv2.FONT_HERSHEY_PLAIN

img_rgb = cv2.imread("./screenshots/full_inventory_copper_top_zoom.jpg")
# img_rgb = cv2.imread("screenshot.jpg")
# img_rgb = cv2.imread("./screenshots/screenshot.jpg")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

east_rock_template = cv2.imread('./screenshots/lumbride_east_copper_rock_full.png', 0)
south_rock_template = cv2.imread('./screenshots/lumbride_south_copper_rock_full.png', 0)
inventory_ore_template = cv2.imread('./screenshots/copper_ore.png', 0)

east_rock_w, east_rock_h = east_rock_template.shape[::-1]
south_rock_w, south_rock_h = south_rock_template.shape[::-1]
inventory_ore__w, inventory_ore__h = inventory_ore_template.shape[::-1]

# east_rock_mineable = False
# south_rock_mineable = False

east_res = cv2.matchTemplate(img_gray, east_rock_template, cv2.TM_CCOEFF_NORMED)
threshold = 0.75
# threshold = 0.90
east_loc = np.where( east_res >= threshold)
if len(east_loc) / 2 == True:
    east_rock_mineable = True

# print(east_rock_mineable)
# print(east_res >= 0.9)

# east_rock_mineable = bool(east_loc)
# print("East Rock Minable = " + str(east_rock_mineable))
    # print("Right rock can be mined")

for pt in zip(*east_loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + east_rock_w, pt[1] + east_rock_h), (255, 255, 255), 1)
    # cv2.putText(img_rgb,'Copper Rock', (pt[0] , pt[1]), font, 3, (255,255,255), 1, cv2.LINE_AA)

south_res = cv2.matchTemplate(img_gray, south_rock_template, cv2.TM_CCOEFF_NORMED)
threshold = 0.75
# threshold = 0.9
south_loc = np.where( south_res >= threshold)

# south_rock_mineable = bool(south_loc)
# print("South Rock Minable = " + str(south_rock_mineable))

# if south_loc == 1:
#     print("South rock can be mined")

for pt in zip(*south_loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + south_rock_w, pt[1] + south_rock_h), (255, 255, 255), 1)
    # cv2.putText(img_rgb,'Copper Rock', (pt[0] , pt[1]), font, 3, (255,255,255), 1, cv2.LINE_AA)

inventory_ore_res = cv2.matchTemplate(img_gray, inventory_ore_template, cv2.TM_CCOEFF_NORMED)
threshold = 0.75
# threshold = 0.9
inventory_ore_loc = np.where( inventory_ore_res >= threshold)

for pt in zip(*inventory_ore_loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + inventory_ore__w, pt[1] + inventory_ore__h), (255, 255, 255), 1)
    # cv2.putText(img_rgb,'Copper Ore', (pt[0] , pt[1]), font, 3, (255,255,255), 1, cv2.LINE_AA)

cv2.imshow("Lumby Mine", imutils.resize(img_rgb, width=1000))
# cv2.imshow("Lumby Mine", img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()