from main_util import main_util as mutil

# testing dates
operation_mode = mutil.get_operation_mode_input()
current_day = mutil.real_or_test_dates_day(operation_mode)
current_week = mutil.real_or_test_dates_week(operation_mode)