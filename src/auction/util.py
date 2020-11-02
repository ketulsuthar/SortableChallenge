"""
created_by : Ketulkumar Suthar
creatde_date : 1st
"""
import sys
import json
from SortableChallenge.src.auction.settings import CONFIG_FILE_PATH


def load_configuration():
    """
    This function will load config file
    :return:
    """
    try:
        if CONFIG_FILE_PATH:
            with open(CONFIG_FILE_PATH,'r') as f:
                print(f)
                return json.load(f)
        else:
            print(f"Error : Check config file path. [load_configuration]")
    except Exception as err:
        print(f"Error : {err} [load_configuration]")


def get_sites(sites_bidders):
    """
    This function extract sites
    :param sites_bidders:
    :return:
    """
    sites= {}
    for site in sites_bidders:
        sites[site['name']] = {
            'bidders' : site['bidders'],
            'floor' : site['floor']
        }
    return sites


def get_bidders(sites_bidders):
    """
    This function extract sites
    :param sites_bidders:
    :return:
    """
    bidders = {}
    for bidder in sites_bidders:
        bidders[bidder['name']] = {
            'adjustment' : bidder['adjustment']
        }
    return bidders