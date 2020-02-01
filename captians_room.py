#https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter


def find_captian_room(room_number):
    """ Group of families consisting of k members stay at a hotel with infinite number of rooms.
        we know that group size (k) = 5.
        Only the Captian has a seperate room.

        Takes in an unordered list of room numbers at the hotel.
        eg: 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
        These room numbers belong to the group of families and the Captain.
        Each room number can be grouped together.
        eg: Counter {(1: 5, 2: 5, 3: 5, 8: 1 ...... }
        
        Since only the Captian has a seperate room, 
        therefore the occurrence of 1 belongs to the Captian.
        eg: 8 occoures only 1 time so it has to be the Captian's room.
            8 is key (room number), 1 is value (number of people)
    """
    count_rooms = Counter(room_number)

    for key, value in count_rooms.items():
        if value == 1:
            print(key)
       

input_group_size = int(input())
input_room_numbers = list(map(int, input().split()))
find_captian_room(input_room_numbers)