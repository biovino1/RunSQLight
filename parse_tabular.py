"""=====================================================================================================================
This scripts parses through the log.txt file and writes each run and shoe into an individual file.

Ben Iovino  3/25/2022   RunSQLight
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
        47cde8a1-ae3b-11ec-9069-902b34362ae0: ['1943-05-16 6:02 AM', 'Easy', '9.02', '1:02:39', 'Hard day at mill']
    :return shoes: dictionary of shoes with shoe name as key i.e.
        DuctTape v3: 32
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

            # Initialize date and time
            datetime = split_line[0]
            if split_line[1] != '':
                datetime += f' {split_line[1]}'

            # Initialize type, distance, duration, note string, and shoe string
            type = split_line[3]
            distance = split_line[4]
            duration = split_line[6]
            notes = split_line[19]
            notes = notes.replace('<br>', '\t')  # Clean notes

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
            runs.update({id: [datetime, type, distance, duration, notes]})

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
        os.mkdir(path+'Runs')
        os.mkdir(path+'Shoes')
    else:
        print('Data directories already exist.')

    # Write each dictionary key and values into text file
    for key in dict.keys():
        with open(f'{path}Runs/{key}.txt', 'w') as file:
            runstring = ' \n'.join(dict[key])
            file.write(runstring)

    for key in dict1.keys():
        with open(f'{path}Shoes/{key}.txt', 'w') as file:
            shoestring = str(dict1[key])
            file.write(shoestring)


def main():
    """=================================================================================================================
    The main function is used to define the tabular file being parsed and run parse_tabular(). The returned dictionaries
    are written to separate text files using write_dictionaries().
    ================================================================================================================="""

    file = 'log.txt'
    runs, shoes = parse_tabular(file)
    write_dictionaries(runs, shoes)


main()
