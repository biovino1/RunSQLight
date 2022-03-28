"""=====================================================================================================================
This scripts parses through the log.txt file and writes each run and piece of equipment into a file with the desired
attributes.


Ben Iovino  3/25/2022   RunSQLight
====================================================================================================================="""

import uuid

def parse_tabular(tab):
    """=================================================================================================================
    This function accepts a tabular file and parses it.

    :param file: file name e.g. log.txt
    ================================================================================================================="""

    # Initialize dictionaries
    run_dict = dict()
    shoes = dict()

    with open(tab, 'r') as file:

        # Split each line (each run) by tab character
        for line in file:

            # Give run uuid, split tabular line
            id = str(uuid.uuid1())
            split_line = line.split('\t')

            # Initialize date and time
            datetime = split_line[0]
            if split_line[1] != '':
                datetime += (f' {split_line[1]}')

            # Initialize type, distance, duration, note string, and shoe string
            type = split_line[3]
            distance = split_line[4]
            duration = split_line[6]
            notes = split_line[19]
            temp_shoe = split_line[23]+split_line[24]+split_line[27]

            # Check if line's shoe is same as previous, add distance to shoe
            if temp_shoe not in shoes.keys():
                shoes.update({temp_shoe: int(distance)})
            else:
                new_shoe = split_line[23]+split_line[24]+split_line[27]


            # Update dict
            run_dict.update({id: [datetime, type, distance, duration, notes, shoe]})


def main():
    """=================================================================================================================
    The main function is used to define the xml file being parsed and run parse_xml().
    ================================================================================================================="""

    file = 'log.txt'

    parse_tabular(file)


main()
