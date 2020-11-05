"""
create_by : Ketulkumar Suthar
created_date : 1st November 2020
"""
from src.util import load_configuration, get_bidders, get_sites, is_valid_config, get_input,is_valid_input, initialise_units, validate_bid, validate_bidder, get_auction_results, display_results, calculated_bid

if __name__ == "__main__":
    # load config file
    result = []
    bid_units = {}
    sites_bidders = load_configuration()
    if is_valid_config(sites_bidders):
        # filter all the sites
        sites = get_sites(sites_bidders.get('sites', []))
        # filter all the bidders
        # print(sites)
        bidders = get_bidders(sites_bidders.get('bidders', []))
        # print(bidders)
        # print("********************")
        auctions = get_input()
        # print(sites)
        if is_valid_input(auctions):
            for auction in auctions:
                site_auction = sites.get(auction['site'], None)
                if site_auction:
                    ad_unit = auction['units']
                    # print(ad_unit)
                    bid_units = initialise_units(ad_unit)
                    # print(bid_units)
                    for bid in auction['bids']:
                        if validate_bidder(bid['bidder'], site_auction['bidders'], bidders):
                            bid['adjusted_bid'] = calculated_bid(bid['bid'], bidders[bid['bidder']]['adjustment'])

                            if validate_bid(bid, ad_unit, site_auction['floor']):
                                bid_units[bid['unit']].append(bid)

                    result.append(get_auction_results(bid_units))
                
        else:
            #print(f"Invalid Auction : {auctions}")
            pass

    display_results(result)
