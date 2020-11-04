"""
created_by : Ketulkumar Suthar
creatde_date : 1st
"""
import sys
import json
import jsonschema
from jsonschema import validate
from collections import defaultdict
from SortableChallenge.src.auction.settings import CONFIG_FILE_PATH, SCHEMA_CONFIG_PATH, SCHEMA_INPUT_PATH


def read_file(type):
    """

    :param type:
    :return:
    """
    try:
        file_name = ''
        if type.upper() == "CONFIG":
            file_name = CONFIG_FILE_PATH
        elif type.upper() == "SCHEMA_CONFIG":
            file_name = SCHEMA_CONFIG_PATH
        elif type.upper() == "SCHEMA_INPUT":
            file_name = SCHEMA_INPUT_PATH

        if file_name:
            with open(file_name, 'r') as f:
                return json.load(f)
        else:
            print(f"Error : Check config file path. [load_configuration]")
    except Exception as err:
        print(f"Error : {err} [read_file]")


def load_configuration():
    """
    This function will load config file
    :return:
    """
    return read_file('CONFIG')


def is_valid_config(sites_bidders):
    """

    :param sites_bidders:
    :param type:
    :return:
    """
    config_schema = read_file('SCHEMA_CONFIG')
    try:
        validate(sites_bidders, config_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(f"Error : {err} [is_valid_config]")
        return False
    else:
        return True


def is_valid_input(auctions):
    """

    :param auctions:
    :return:
    """
    input_schema = read_file('SCHEMA_INPUT')

    try:
        validate(auctions, input_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(f"Error : {err} [is_valid_input]")
        return False
    else:
        return True


def get_sites(sites_bidders):
    """
    This function extract sites
    :param sites_bidders:
    :return: dict
    """
    sites = {}
    for site in sites_bidders:
        sites[site['name']] = {
            'bidders': site['bidders'],
            'floor': site['floor']
        }
    return sites


def get_bidders(sites_bidders):
    """
    This function extract sites
    :param sites_bidders:
    :return: dict
    """
    bidders = {}
    for bidder in sites_bidders:
        bidders[bidder['name']] = {
            'adjustment': bidder['adjustment']
        }
    return bidders


def get_input():
    """
    This fucntion return user input in json format
    :return: list or None
    """
    try:
        return json.loads(''.join(sys.stdin.readlines()))
    except:
        return None


def initialise_units(ad_units):
    """this funtion initialize dict with unit.
    :type ad_units: object
    """
    if not ad_units:
        return None

    b = defaultdict(list)

    for ad in ad_units:
        b[ad]

    return b


def validate_bidder(bidder, sites_bidders, adj_bidders):
    """"This function validate bidder
    :param adj_bidders:
    :param sites_bidders:
    :type bidder: object
    :return: bool
    """
    if bidder and sites_bidders and adj_bidders:
        if bidder not in sites_bidders or bidder not in adj_bidders:
            return False
        else:
            return True
    return False


def validate_bid(bid, ad_unit, ad_floor):
    """This function validate bid value
    :param ad_floor:
    :param ad_unit:
    :type bid: object
    """
    if not bid or not ad_unit or not ad_floor:
        return False

    if bid['unit'] not in ad_unit:
        return False

    if bid['adjusted_bid'] < ad_floor:
        return False

    return True