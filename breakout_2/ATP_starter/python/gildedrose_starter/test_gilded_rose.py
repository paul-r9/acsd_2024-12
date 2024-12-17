# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose


def arrange_test(name, sell_in, quality):
    items = [Item(name, sell_in, quality)]
    sut = GildedRose(items)

    return sut, items


def test_name_does_not_change_on_update():
    # Arrange
    sut, items = arrange_test("foo", 0, 0)

    # Act
    sut.update_quality()

    # Assert
    assert items[0].name == "foo"


def test_quality_decreases_by_one_with_positive_sell_in():
    sut, items = arrange_test("foo", 1, 5)

    sut.update_quality()

    assert items[0].quality == 4


def test_quality_decreases_double_when_sell_in_is_zero():
    sut, items = arrange_test("foo", 0, 6)

    sut.update_quality()

    assert items[0].quality == 4


def test_sell_in_decreases_on_update():
    sut, items = arrange_test("foo", 2, 6)

    sut.update_quality()

    assert items[0].sell_in == 1


def test_quality_always_zero_or_higher():
    sut, items = arrange_test("foo", 0, 0)

    sut.update_quality()

    assert items[0].quality == 0


def test_aged_brie_increases_in_quality_the_older_it_get():
    sut, items = arrange_test("Aged Brie", 3, 0)

    sut.update_quality()

    assert items[0].quality == 1


def test_aged_brie_quality_never_goes_above_fifty():
    sut, items = arrange_test("Aged Brie", 3, 50)

    sut.update_quality()

    assert items[0].quality == 50


def test_sulfuras_never_decreases():
    sut, items = arrange_test("Sulfuras, Hand of Ragnaros", 10, 10)

    sut.update_quality()

    assert all(
        [
            items[0].sell_in == 10,
            items[0].quality == 10,
        ]
    )


def test_backstage_passes_increases_by_2_in_quality_with_sell_in_ten_days_or_less():
    sut, items = arrange_test("Backstage passes to a TAFKAL80ETC concert", 8, 10)

    sut.update_quality()

    assert items[0].quality == 12


def test_backstage_passes_increases_by_3_in_quality_with_sell_in_five_days_or_less():
    sut, items = arrange_test("Backstage passes to a TAFKAL80ETC concert", 3, 10)

    sut.update_quality()

    assert items[0].quality == 13

def test_backstage_passes_increases_by_1_in_quality_with_sell_in_more_than_10():
    sut, items = arrange_test("Backstage passes to a TAFKAL80ETC concert", 12, 10)

    sut.update_quality()

    assert items[0].quality == 11


if __name__ == "__main__":
    pytest.main()
