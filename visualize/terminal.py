import argparse
import datetime as dt
import sys


def parse_arguments(args):
    try:
        parser = argparse.ArgumentParser(
            description='Visualize Data within a time frame', prog='visualize')
        parser.add_argument('-s', '--start-date', required=True,
                            help='Start date. Date format: DD-MM-YYYY', type=date)
        parser.add_argument('-e', '--end-date', required=True,
                            help='End date. Date format: DD-MM-YYYY', type=date)

        parsed_arg = parser.parse_args(args)
        return parsed_arg
    except argparse.ArgumentError as err:
        sys.exit(err)
    except argparse.ArgumentTypeError as err:
        sys.exit(err)


def date(string):
    return dt.datetime.strptime(string, '%d-%m-%Y').date()


def main():
    args = parse_arguments(sys.argv[1:])
    return args


# if __name__ == "__main__":
#     main()
