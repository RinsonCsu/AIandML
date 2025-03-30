ORDERED_COURSE_NUMBERS = ["CSC101", "CSC102", "CSC103", "NET110", "COM241"]
ORDERED_ROOM_NUMBERS = [3004, 4501, 6755, 1244, 1411]
ORDERED_INSTRUCTOR_NAMES = ["Haynes", "Alvarado", "Rich", "Burke", "Lee"]
ORDERED_MEETING_TIMES = ["8:00 a.m.", "9:00 a.m.", "10:00 a.m.", "11:00 a.m.", "1:00 p.m."]

def create_dictionary_from_lists(keys: list, values: list):
    return {keys[i]:values[i] for i in range(len(keys))}


ROOM_NUMBERS_DICT = create_dictionary_from_lists(ORDERED_COURSE_NUMBERS, ORDERED_ROOM_NUMBERS)
INSTRUCTOR_NAMES_DICT = create_dictionary_from_lists(ORDERED_COURSE_NUMBERS, ORDERED_INSTRUCTOR_NAMES)
MEETING_TIMES_DICT = create_dictionary_from_lists(ORDERED_COURSE_NUMBERS, ORDERED_MEETING_TIMES)

course_number = input('Please enter the course number:\n')
if course_number in ORDERED_COURSE_NUMBERS:
  print("\nCourse Details are as below:\n")
  print(f"{'Course Number':<16}{'Room Number':<16}{'Instructor':<16}{'Meeting Time':<16}")
  print(f"{'=============':<16}{'===========':<16}{'==========':<16}{'============':<16}")
  print(f"{course_number:<16}{ROOM_NUMBERS_DICT[course_number]:<16}{INSTRUCTOR_NAMES_DICT[course_number]:<16}{MEETING_TIMES_DICT[course_number]:<16}")
else:
  print("Invalid Course Number!")
