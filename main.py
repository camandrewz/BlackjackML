import os
import cv2 as cv
from card_collection import card_collector


def main():

    collector = card_collector
    game_board = collector.collect()

    #locations = collector.roi_selection(game_board)
    locations = [(350, 37, 342, 134), (37, 111, 298, 156),
                 (333, 213, 383, 126), (639, 88, 401, 188)]

    print("Are you player 1, 2, or 3?")
    player_num = input()

    dealer_cards = []
    my_cards = []
    other_cards = []

    for index, loc in enumerate(locations):
        board_crop = game_board[int(loc[1]):int(loc[1]+loc[3]), int(loc[0]):int(loc[0]+loc[2])]

        cv.imwrite('Assets/curr_board.jpg', board_crop)

        for thing in os.walk('Assets/Card Types'):
            for image in thing[2]:
                if (index == 0):
                    if (card_collector.determine(image) == True):
                        dealer_cards.append(image[:-4])
                elif (index == int(player_num)):
                    if (card_collector.determine(image) == True):
                        my_cards.append(image[:-4])
                else:
                    if (card_collector.determine(image) == True):
                        other_cards.append(image[:-4])

    print('My cards: ' + str(my_cards))
    print('Dealer\'s cards: ' + str(dealer_cards))
    print('Other cards: ' + str(other_cards))


main()
