import unittest

from SortableChallenge.src.auction.util import is_valid_auction
from SortableChallenge.src.auction.util import get_auction_results

mock_sites_dict = {'houseofcheese.com': {'bidders': ['AUCT', 'BIDD'], 'floor': 32}}

mock_auction_no_bids = {'site': 'houseofcheese.com', 'units': ['banner', 'sidebar'], 'bids': []}
mock_auction_unknown_site = {'site': 'UNKNOWN', 'units': ['banner', 'sidebar'], 'bids': [{'bidder': 'AUCT', 'unit': 'banner', 'bid': 35}, {'bidder': 'BIDD', 'unit': 'sidebar', 'bid': 60}, {'bidder': 'AUCT', 'unit': 'sidebar', 'bid': 55}]}
mock_auction = {'site': 'houseofcheese.com', 'units': ['banner', 'sidebar'], 'bids': [{'bidder': 'AUCT', 'unit': 'banner', 'bid': 35}, {'bidder': 'BIDD', 'unit': 'sidebar', 'bid': 60}, {'bidder': 'AUCT', 'unit': 'sidebar', 'bid': 55}]}

mock_no_bids_for_ad_unit = {'banner': []}

winning_bid_banner = {'bidder': 'AUCT', 'unit': 'banner', 'bid': 35, 'adjusted_bid_value': 32.8125}
winning_bid_sidebar = {'bidder': 'BIDD', 'unit': 'sidebar', 'bid': 60, 'adjusted_bid_value': 60}
losing_bid_sidebar = {'bidder': 'AUCT', 'unit': 'sidebar', 'bid': 55, 'adjusted_bid_value': 51.5625}
mock_bids = {'banner': [winning_bid_banner], 'sidebar': [winning_bid_sidebar, losing_bid_sidebar]}
expected_result = [{'bid': 35, 'bidder': 'AUCT', 'unit': 'banner'}, {'bid': 60, 'bidder': 'BIDD', 'unit': 'sidebar'}]

class Test_is_valid_auction(unittest.TestCase):
  def test_with_empty_sites_dict(self):
    self.assertEqual(is_valid_auction(mock_auction, {}), False)

  def test_with_empty_auction(self):
    self.assertEqual(is_valid_auction({}, mock_sites_dict), False)

  def test_with_0_bids(self):
    self.assertEqual(is_valid_auction(mock_auction_no_bids, mock_sites_dict), False)

  def test_with_unknown_site(self):
    self.assertEqual(is_valid_auction(mock_auction_unknown_site, mock_sites_dict), False)

  def test_with_correct_data(self):
    self.assertEqual(is_valid_auction(mock_auction, mock_sites_dict), True)

class Test_get_auction_results(unittest.TestCase):
  def test_with_empty_bids(self):
    self.assertEqual(get_auction_results({}), [])

  def test_no_bids_for_ad_unit(self):
    self.assertEqual(get_auction_results(mock_no_bids_for_ad_unit), [])

  def test_correct_winner(self):
    self.assertEqual(get_auction_results(mock_bids), expected_result)

if __name__ == '__main__':
  unittest.main()