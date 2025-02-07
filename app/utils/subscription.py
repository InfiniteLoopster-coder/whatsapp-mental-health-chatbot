def check_subscription(user_id):
    """
    Checks if the user (identified by user_id) has an active subscription.
    (For demonstration, this dummy logic returns True if the last digit of the
    user_id is even, otherwise False.)
    """
    try:
        last_digit = int(user_id[-1])
        return last_digit % 2 == 0
    except Exception:
        return False
