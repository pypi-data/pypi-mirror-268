import argparse
import logging
import sys

from difflib import SequenceMatcher
from meteo_hr import cache, __version__
from meteo_hr.api import fetch_forecast_html
from meteo_hr.output import bold, print_chart, print_forecast
from meteo_hr.parse import parse_forecast
from meteo_hr.places import list_3d, list_7d


def make_parser():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("place", nargs="*", type=str)
    parser.add_argument("-l", "--list", action="store_true", help="list places for which forecast is available")
    parser.add_argument("-d", "--debug", action="store_true", help="print debug info")
    parser.add_argument("-7", "--week", action="store_true", help="show weekly forecast instad of 3-day")
    parser.add_argument("-c", "--clear-cache", action="store_true", help="clear cached data")
    parser.add_argument("-v", "--version", action="store_true", help="print version and exit")
    return parser


def main():
    parser = make_parser()
    args = parser.parse_args()

    if args.version:
        print(f"meteo_hr version {__version__}")
        return

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    if args.clear_cache:
        cache.clear()

    places = list_7d() if args.week else list_3d()

    if args.list:
        for place in places:
            print(place.name)
        return

    place_name = " ".join(args.place).lower()

    if not place_name:
        place_name = cache.load_last_place()

    if not place_name:
        print("Place is required.", file=sys.stderr)
        sys.exit(1)

    place = max(places, key=lambda p: name_diff(p.name, place_name))
    diff = name_diff(place.name, place_name)

    if diff < 0.5:
        print("Place not found", file=sys.stderr)
        sys.exit(1)

    cache.save_last_place(place.name)
    forecast_html = fetch_forecast_html(place)
    forecasts = list(parse_forecast(forecast_html))

    print(bold(place.name))
    print()
    print_chart(forecasts)
    print_forecast(place, forecasts)


def name_diff(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()
