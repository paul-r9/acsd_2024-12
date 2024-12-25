import unittest

from gilded_rose import Item, GildedRose
from approvaltests import verify, verify_all_combinations, verify_all_combinations_with_namer

class TestApprovals(unittest.TestCase):

    # Similar to a pytest unit test but uses the Approval Tests verify instead of assert
    # the results of this test are captured in a file named TestApprovals.test_single_item.received.txt
    # and compared to the expected results in TestApprovals.test_single_item.approved.txt
    # The test passes when the contents of the received file match the approved file.
    # When the test passes, the received file is deleted.
    def test_single_item(self):
        items = [Item("normal item", 10, 6)]
        sut = GildedRose(items)

        # Act
        sut.update_quality()
        actual_updated_item = items[0]

        # Assert
        verify(actual_updated_item)

    # Generates combinations of sell_in and fixed quality for a legendary item.
    # Compares the received out to TestApprovals.test_legendary_items_sell_in_and_quality_unchanged.approved.txt
    def test_legendary_items_sell_in_and_quality_unchanged(self):
        def update_legendary_item(item):
            sut = GildedRose([item])
            sut.update_quality()
            output = f"{item.name} {item.sell_in} {item.quality}"
            return output

        verify_all_combinations(update_legendary_item,
    [
                [
                    Item("Sulfuras, Hand of Ragnaros", sell_in, 80)
                    for sell_in in range(-10, 10)
                ]
            ])

    # This test will generate all combinations of name/sell_in/quality and compare the results
    # to the contents in TestApprovals.test_multiple_items_via_combinations.approved.txt
    def test_multiple_items_via_combinations(self):
        item_names     = ["normal item", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert" ]
        sell_in_values = [ -1, 0, 5, 10, 11 ]
        quality_values = [ 0, 1, 49, 50 ]

        def update_single_item(name, sell_in, quality):
            items = [Item(name, sell_in, quality)]
            sut = GildedRose(items)
            sut.update_quality()
            output = f"{items[0].name} {items[0].sell_in} {items[0].quality}"
            return output

        verify_all_combinations(update_single_item, [item_names, sell_in_values, quality_values])

