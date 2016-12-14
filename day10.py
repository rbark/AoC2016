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
not_done = True
sum = 0
while not_done:
    for bot, chips in bot_storage.items():
        print(str(bot) + ':' + str(chips) )
        if len(chips) == 2 and bot in instructions:
            instruction = instructions[bot]
            min = sorted(chips)[0]
            max = sorted(chips)[1]
            if instruction[1] == 'bot':
                bot_storage[instruction[0]].append(min)
            else:
                print(instruction[0])
                if instruction[0] not in output_storage:
                    output_storage[instruction[0]] = [min]
                else:
                    output_storage[instruction[0]].append(min)
                print(output_storage)
            if instruction[3] == 'bot':
                bot_storage[instruction[2]].append(max)
            else:
                if instruction[2] not in output_storage:
                    output_storage[instruction[2]] = [max]
                else:
                    output_storage[instruction[2]].append(max)

            bot_storage[bot] = []
            if output_storage.get(0) and output_storage.get(1) and output_storage.get(2):
                print(output_storage)
                sum = output_storage[0][0] * output_storage[1][0] * output_storage[2][0]
                not_done = False
            
            # botnummer : till vem låg, bot/output, till vem hög, bot/output
print('svar:' + str(sum))