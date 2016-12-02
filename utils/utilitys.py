def get_word_array(puzzle_word):
    puzzle_word = puzzle_word.replace(" ", "")
    return puzzle_word.split(",")

def get_lines_from_file_text(file_text):
    return file_text.splitlines()