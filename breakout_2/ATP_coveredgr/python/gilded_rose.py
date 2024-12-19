# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
LEGENDARY_SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED_PREFIX = "Conjured "

MAX_QUALITY = 50
TEN_DAYS_OR_LESS = 10
FIVE_DAYS_OR_LESS = 5


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_single_item(item)

    def update_single_item(self, item):
        if item.name == LEGENDARY_SULFURAS:
            # LEGENDARY_SULFURAS never changes in quality and we always want to sell it
            return

        # By default, items decrease in quality over time
        quality_update = -1

        if item.name == BACKSTAGE_PASSES or item.name == AGED_BRIE:
            # AGED_BRIE and BACKSTAGE_PASSES increase in quality over time
            quality_update = 1
        elif item.name.startswith(CONJURED_PREFIX):
            # Conjured items decrease in quality twice as fast
            quality_update = quality_update * 2

        if item.name == BACKSTAGE_PASSES:
            if item.sell_in <= 0:
                # BACKSTAGE_PASSES are worthless after the concert
                quality_update = -item.quality
            elif item.sell_in <= FIVE_DAYS_OR_LESS:
                # BACKSTAGE_PASSES get really valuable when concert is 5 days away
                quality_update = quality_update * 3
            elif item.sell_in <= TEN_DAYS_OR_LESS:
                # BACKSTAGE_PASSES get more valuable when concert is 10 days away
                quality_update = quality_update * 2
        elif item.sell_in <= 0:
            # AGED_BRIE, Conjured, and generic items have their quality change twice as fast after sell_in
            quality_update = quality_update * 2

        # Quality must be between 0 and 50
        item.quality = max(0, min(50, item.quality + quality_update))
        item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
