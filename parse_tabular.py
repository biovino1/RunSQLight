"""=====================================================================================================================
This scripts parses through the log.txt file and writes runs and shoes into separate files.

Ben Iovino  4/9/22   RunSQLight
====================================================================================================================="""

import uuid
import os


def parse_tabular(tab):
    """=================================================================================================================
    This function accepts a tabular file, parses it, and returns two dictionaries. The 'runs' dict contains a uuid
    for each run as the key, then desired info as values. The 'shoes' dict contains a shoe name as a key and total
    distance run on that shoe as its value.

    :param tab: file name e.g. log.txt
    :return runs: dictionary of runs with uuid as key i.e.
        47cde8a1-ae3b-11ec-9069-902b34362ae0: ['1943-05-16 6:02 AM', 'Easy', '9.02', '1:02:39', '7:37', 'Fun run']
    :return shoes: dictionary of shoes with shoe name as key i.e. DuctTape v3: 32
    ================================================================================================================="""

    # Initialize dictionaries
    runs = dict()
    shoes = dict()

    with open(tab, 'r') as file:

        # Split each line (each run) by tab character
        for line in file:

            # Give run uuid, split tabular line
            split_line = line.split('\t')
            id = str(uuid.uuid1())

            # Pass entries that aren't runs
            if split_line[2] != 'Run':
                continue

            # Initialize date and time
            datetime = split_line[0]
            if split_line[1] != '':
                datetime += f' {split_line[1]}'

            # Initialize type, distance, duration, note string, and shoe string
            type = split_line[3]
            distance = split_line[4]

            # Format duration string so time matches 00:00:00 (H:M:S)
            duration = split_line[6].split(":")
            hours, minutes, seconds = duration[0], duration[1], duration[2].split('.')[0]
            if len(minutes) == 1:
                duration = f'0{hours}:0{minutes}:{seconds}'
            if len(minutes) == 2:
                duration = f'0{hours}:{minutes}:{seconds}'

            notes = split_line[19]
            notes = notes.replace('<br>', '\t')  # Clean notes

            # Calculate pace from distance and duration
            duration_sec = sum(x * int(t) for x, t in zip([3600, 60, 1], duration.split(":")))
            pace_sec = duration_sec/float(distance)
            pace_min = pace_sec // 60
            pace_sec = pace_sec % 60
            if pace_sec < 10:
                pace = f'{int(pace_min)}:0{int(pace_sec)}'
            else:
                pace = f'{int(pace_min)}:{int(pace_sec)}'

            # Check line for no shoe entry
            if split_line[23] != '':
                shoe = split_line[23]+split_line[24]+split_line[27]

                # Check if shoe is already a key, add distance to the value
                if shoe not in shoes.keys():
                    shoes.update({shoe: float()})
                    if distance != '':
                        shoes[shoe] += round(float(distance))
                else:
                    if distance != '':
                        shoes[shoe] += round(float(distance))

            # Update dict
            runs.update({id: [datetime, type, distance, duration, pace, notes]})

        return runs, shoes


def write_dictionaries(dict, dict1):
    """=================================================================================================================
    This function accepts dictionaries and prints them into text files.

    :param dict: Dict object
    ================================================================================================================="""

    # Create directories for individual files
    path = 'C:/Users/biovi/PycharmProjects/RunSQLight/Data/'
    if not os.path.isdir(path):
        os.mkdir(path)
    else:
        print('Data directories already exist.')

    # Write dictionary key and values into text file
    with open(f'{path}runs.txt', 'w') as file:
        for key in dict.keys():
            runstring = ' \t'.join(dict[key])
            file.write(key+'\t'+runstring+'\n')

    with open(f'{path}shoes.txt', 'w') as file:
        for key in dict1.keys():
            shoestring = str(dict1[key])
            file.write(key+'\t'+shoestring+'\n')


def main():
    """=================================================================================================================
    The main function is used to define the tabular file being parsed and run parse_tabular(). The returned dictionaries
    are written to separate text files using write_dictionaries().
    ================================================================================================================="""

    file = 'log.txt'
    runs, shoes = parse_tabular(file)
    write_dictionaries(runs, shoes)


main()
