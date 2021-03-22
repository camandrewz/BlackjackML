import cv2 as cv
import numpy as np
import win32gui
from PIL import ImageGrab


class card_collector:

    def __init__(self) -> None:
        pass

    def collect():

        wind = win32gui.FindWindow(None, 'Blackjack Championship')
        win32gui.SetForegroundWindow(wind)
        dimensions = win32gui.GetWindowRect(wind)

        ImageGrab.grab(dimensions).save('Assets/game_img.jpg')

        game_img = cv.imread('Assets/game_img.jpg')

        return game_img

    def roi_selection(image_location):

        locations = []

        dealer = cv.selectROI(image_location)
        print('Dealer cards are located at: ' + str(dealer))

        player1 = cv.selectROI(image_location)
        print('Player 1 cards are located at: ' + str(player1))

        player2 = cv.selectROI(image_location)
        print('Player 2 cards are located at: ' + str(player2))

        player3 = cv.selectROI(image_location)
        print('Player 3 cards are located at: ' + str(player3))

        locations.append(dealer)
        locations.append(player1)
        locations.append(player2)
        locations.append(player3)

        return locations

    def determine(card_image):
        game_img = cv.imread('Assets/curr_board.jpg', cv.IMREAD_UNCHANGED)
        card_img = cv.imread('Assets/Card Types/' +
                             card_image, cv.IMREAD_UNCHANGED)

        result = cv.matchTemplate(game_img, card_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        threshold = 0.9

        if max_val >= threshold:

            card_w = card_img.shape[1]
            card_h = card_img.shape[0]

            top_left = max_loc

            bottom_right = (top_left[0] + card_w, top_left[1] + card_h)

            cv.rectangle(game_img, top_left, bottom_right,
                         color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

            cv.imwrite('Assets/result.jpg', game_img)

            return True

        else:

            return False
