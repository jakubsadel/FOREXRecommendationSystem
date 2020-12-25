from datetime import datetime, timedelta


def get_today_date():
    date_today = datetime.today().strftime('%Y-%m-%d')
    return date_today


def get_2weeks_date():
    date_2weeks_ago = (datetime.today() - timedelta(days=14)).strftime('%Y-%m-%d')
    return date_2weeks_ago
