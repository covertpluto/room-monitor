import json
import datetime



def get_day_of_year(date=None):
    if date is None:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
    return datetime.datetime.strptime(date, "%Y-%m-%d").timetuple().tm_yday


def store_load_ops(read=False, write=None):
    if not read and write is None:
        print("No data provided. Doing nothing.")
        return
    if read:
        with open("/home/pi/.p_stor/data.json", "r") as f:
            data = json.load(f)
        return data
    with open("/home/pi/.p_stor/data.json", "w") as f:
        json.dump(write, f)
    return


def possible(data):
    prev = store_load_ops(read=True)
    high = prev["high"]["temp"]
    low = prev["low"]["temp"]
    hday = prev["high"]["day"]
    lday = prev["low"]["day"]
    if data > high:
        print("High temp detected. Prev high: {}. Current: {}".format(high, data))
        high = data
        hday = get_day_of_year()
    elif data < low:
        print("Low temp detected. Prev low: {}. Current: {}".format(low, data))
        low = data
        lday = get_day_of_year()
    elif get_day_of_year() - hday > 5 or get_day_of_year() - lday > 5:
        print("High temp is greater than 5 days old.")
        print("Updating the temperatures anyways")
        high = data
        low = data
        hday = get_day_of_year()
        lday = get_day_of_year()
    else:
        return
    data_to_write = {
        "high": {
            "temp": high,
            "day": hday
        },
        "low": {
            "temp": low,
            "day": lday
        }
    }
    print("data:", data_to_write)
    store_load_ops(write=data_to_write)


def check():
    prev = store_load_ops(read=True)
    high = prev["high"]["temp"]
    low = prev["low"]["temp"]
    hday = prev["high"]["day"]
    lday = prev["low"]["day"]
    print("High:", high, "Low:", low)
    print("High day:", hday, "Low day:", lday)

    duration_between_high_low = abs(hday - lday)
    print("Duration between high and low:", duration_between_high_low)
    if duration_between_high_low > 2:
        print("High and low are more than 2 days apart. High: {}. Low: {}".format(high, low))
    else:
        print("High and low are less than 2 days apart. High: {}. Low: {}".format(high, low))
    return round(high - low, 0)
