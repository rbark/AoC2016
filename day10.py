import re

instructions = {} # botnummer : till vem låg, bot/output, till vem hög, bot/output
bot_storage = {}
output_storage = {}

bot_get_value_pattern = re.compile(r'value (\d+) goes to bot (\d+)')
bot_give_instruction_pattern = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')

with open("day10.txt") as f:
    for instruction in f.readlines():
        bot_gets = re.search(bot_get_value_pattern, instruction)
        bot_gives = re.search(bot_give_instruction_pattern, instruction)

        if bot_gets:
            bot = int(bot_gets.group(2))
            chips = int(bot_gets.group(1))
            if bot in bot_storage:
                bot_storage[bot].append(chips)
            else:
                bot_storage[bot] = [chips]

        if bot_gives:
            bot = int(bot_gives.group(1))
            bot_low_number = int(bot_gives.group(3))
            bot_high_number = int(bot_gives.group(5))
            low_output = bot_gives.group(2)
            hi_output = bot_gives.group(4)

            if bot not in bot_storage:
                bot_storage[bot] = []

            instructions[bot] = [bot_low_number, low_output, bot_high_number, hi_output]

# print(instructions)


while 1:
    for bot, chips in bot_storage.items():
        if len(chips) == 2 and bot in instructions:
            done = False
            if 61 in chips and 17 in chips:
                print(bot)
                done = True
                break
            instruction = instructions[bot]
            min = sorted(chips)[0]
            max = sorted(chips)[1]
            if instruction[1] == 'bot':
                print('bot ' + str(bot) + ' gives ' + str(min) + ' to ' + str(instruction[0]))
                bot_storage[instruction[0]].append(min)
            if instruction[3] == 'bot':
                print('bot ' + str(bot) + ' gives ' + str(max) + ' to ' + str(instruction[2]))
                bot_storage[instruction[2]].append(max)

            bot_storage[bot] = []

            # botnummer : till vem låg, bot/output, till vem hög, bot/output