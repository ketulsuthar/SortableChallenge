"""
create_by : Ketulkumar Suthar
created_date : 1st November 2020
"""
from SortableChallenge.src.auction.util import load_configuration, get_bidders, get_sites, is_valid_config, get_input,is_valid_input

if __name__ == "__main__":
    # load config file
    sites_bidders = load_configuration()
    if is_valid_config(sites_bidders):
        # filter all the sites
        sites = get_sites(sites_bidders.get('sites',[]))
        # filter all the bidders
        bidders = get_bidders(sites_bidders.get('bidders',[]))

        auctions = get_input()

        if is_valid_input(auctions):
            for auction in auctions:
                site_auction = sites.get(auction['site'],None)
                if site_auction:
                    ad_unit = auction['units']
                else:
                    print(f"{auction['site']} does not exist in configuration.")
        else:
            print(f"Invalid Auction : {auctions}")

