"""
create_by : Ketulkumar Suthar
created_date : 1st November 2020
"""
from SortableChallenge.src.auction.util import load_configuration, get_bidders, get_sites

if __name__ == "__main__":
    # load config file
    sites_bidders = load_configuration()
    if sites_bidders:
        # filter all the sites
        sites = get_sites(sites_bidders.get('sites',[]))
        # filter all the bidders
        bidders = get_bidders(sites_bidders.get('bidders',[]))

