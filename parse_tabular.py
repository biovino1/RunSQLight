"""=====================================================================================================================
This scripts parses through the log.txt file and writes each run and piece of equipment into a file with the desired
attributes.


Ben Iovino  3/25/2022   RunSQLight
====================================================================================================================="""

def parse_tabular(tab):
    """=================================================================================================================
    This function accepts a tabular file and parses it.

    :param file: file name e.g. log.txt
    ================================================================================================================="""

    # Initialize dictionary where date + time is key
    run_dict = dict()
    with open(tab, 'r') as file:

        # Split each line by tab character
        for line in file:
            split_line = line.split('\t')
            date = split_line[0]
            time = split_line[1]
            print(date+time)

def main():
    """=================================================================================================================
    The main function is used to define the xml file being parsed and run parse_xml().
    ================================================================================================================="""

    file = 'log.txt'

    parse_tabular(file)


main()
