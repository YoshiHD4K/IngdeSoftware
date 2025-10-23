def is_valid_date(d, m, y):
    try:
        import datetime as dt
        dt.date(y, m, d)
        return True
    except Exception:
        return False