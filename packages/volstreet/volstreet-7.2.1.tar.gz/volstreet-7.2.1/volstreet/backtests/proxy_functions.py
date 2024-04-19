from datetime import datetime
from volstreet.config import EXPIRY_FREQUENCIES
from volstreet.backtests import state
from volstreet.backtests.underlying_info import UnderlyingInfo, fetch_historical_expiry


def current_time() -> datetime:
    return state.time_now


def get_symbol_token(name=None, expiry=None, strike=None, option_type=None):
    if expiry is None and strike is None and option_type is None:
        return name.upper(), name.upper()
    else:
        symbol = f"{name.upper()}{expiry.upper()}{int(strike)}{option_type.upper()}"
        return symbol, symbol


def get_expiry_dates(expiry_frequency: int):
    expiry_frequencies = {v: k for k, v in EXPIRY_FREQUENCIES.items()}
    underlying = expiry_frequencies[expiry_frequency]
    expiries = fetch_historical_expiry(
        underlying, current_time(), threshold_days=0, n_exp=4
    )
    return expiries


def get_base(name, expiry):
    return UnderlyingInfo(name).base
