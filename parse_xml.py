"""=====================================================================================================================
This scripts parses through a xml file.

Ben Iovino  3/25/2022   RunSQLight
====================================================================================================================="""

from time import sleep

def parse_xml(xml):
    """=================================================================================================================
    This function accepts an xml file and parses it, returning a list of each values for each attribute.

    :param file: file name e.g. run.xml
    ================================================================================================================="""

    with open(xml, 'r') as file:

        for line in file:

            print(line)


def main():
    """=================================================================================================================
    The main function is used to define the xml file being parsed and run parse_xml().
    ================================================================================================================="""

    file = 'log.xml'

    parse_xml(file)


main()
