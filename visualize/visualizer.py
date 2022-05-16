import sys
import datetime as dt
from tracemalloc import start
import plotext as plt
from . import api
from . import terminal

# local_data = {
#     "01-01-2022": 300,
#     "02-01-2022": 500,
#     "03-01-2022": 700,
#     "04-01-2022": 1300,
#     "05-01-2022": 2000,
#     "06-01-2022": 3000,
#     "07-01-2022": 3500,
#     "08-01-2022": 4000,
#     "09-01-2022": 4500,
#     "10-01-2022": 5000,
#     "11-01-2022": 20000,
#     "12-01-2022": 35000,
#     "13-01-2022": 46000,
#     "14-01-2022": 70000,
#     "15-01-2022": 90000
# }

url = "http://sam-user-activity.eu-west-1.elasticbeanstalk.com"


def visualize_data(data):
    # data = get_data(args)

    plt.date_form('d/m/Y')
    plt.title("Userbase Growth Graph")
    plt.ylabel("Number of Users")
    plt.xlabel("Dates")
    no_of_users = data.get("Y-Axis")
    dates = plt.datetimes_to_string(data.get("X-Axis"))

    plt.bar(dates, no_of_users)
    plt.yticks(no_of_users)

    plt.show()


def get_data(args):
    # arguments = terminal.main()
    res = api.main(url)
    # res = local_data
    start_date = args.start_date
    end_date = args.end_date

    coordinates = get_coordinates(start_date, end_date, res)

    data = {
        "X-Axis": coordinates.get("X"),
        "Y-Axis": coordinates.get("Y")
    }

    return data


def get_coordinates(start_date, end_date, res):
    x_values = []
    y_values = []
    coordinates = {}

    if start_date.strftime('%d-%m-%Y') in res and end_date.strftime('%d-%m-%Y') in res:
        for key, value in res.items():
            if format_date(key) >= start_date and format_date(key) <= end_date:
                # print(key, value)
                x_values.append(format_date(key))
                y_values.append(value)
    elif start_date.strftime('%d-%m-%Y') not in res:
        sys.exit("Given start date is not available")
    elif end_date.strftime('%d-%m-%Y') not in res:
        sys.exit("Given end date is not available")
    else:
        sys.exit("An error occurred. Please check your input")

    coordinates = {
        "X": x_values,
        "Y": y_values
    }
    return coordinates


def format_date(date):
    return dt.datetime.strptime(date, '%d-%m-%Y').date()


def main():
    args = terminal.main()
    data = get_data(args)
    visualize_data(data)


if __name__ == "__main__":
    main()
