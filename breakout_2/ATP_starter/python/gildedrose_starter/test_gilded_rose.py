# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose


def test_needs_a_better_name():
    # Arrange
    items = [Item("foo", 0, 0)]
    sut = GildedRose(items)

    # Act
    sut.update_quality()

    # Assert
    assert "fixme" == items[0].name


if __name__ == "__main__":
    pytest.main()
