import { Item, GildedRose } from '@/gilded-rose';


describe("Gilded Rose", function () {
  it("Legendary Item quality does not decrease", () => {
    // Arrange
    const sut = new GildedRose([new Item("Sulfuras, Hand of Ragnaros", 20, 80)]);

    // Act
    const items = sut.updateQuality();

    // Assert
    expect(items[0].quality).toBe(80);
  });

  it("Legendary Item never has to be sold", () => {
    const sut = new GildedRose([new Item("Sulfuras, Hand of Ragnaros", 1, 80)]);

    const items = sut.updateQuality();

    expect(items[0].sellIn).toBe(1);
  });

  it("Legendary Item quality does not change after sellin", () => {
    const sut = new GildedRose([new Item("Sulfuras, Hand of Ragnaros", -1, 80)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(80);
  });


  it("Generic item SellIn decreases each update", () => {
    const sut = new GildedRose([new Item("generic item", 8, 8)]);

    const items = sut.updateQuality();

    expect(items[0].sellIn).toBe(7);
  });

  // TODO - can the tests for `negative after sellIn date reached` be parameterized for several items?? 
  it("Generic item SellIn will be negative after sellIn date reached", () => {
    const sut = new GildedRose([new Item("generic item", 0, 10)]);

    const items = sut.updateQuality();

    expect(items[0].sellIn).toBe(-1);
  });

  it("Generic item quality decreases by 1 before sellIn date reached", () => {
    const sut = new GildedRose([new Item("generic item", 5, 10)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(9);
  });

  it("Generic item quality decreases twice as fast after sellIn date reached", () => {
    const sut = new GildedRose([new Item("generic item", 0, 10)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(8);
  });

  it("Generic item quality never decreases below 0", () => {
    const sut = new GildedRose([new Item("generic item", 5, 0)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(0);
  });

  it("Aged Brie item SellIn decreases each update", () => {
    const sut = new GildedRose([new Item("Aged Brie", 5, 5)]);

    const items = sut.updateQuality();

    expect(items[0].sellIn).toBe(4);
  });

  it("Aged Brie SellIn will be negative after sellIn date reached", () => {
    const sut = new GildedRose([new Item("Aged Brie", 0, 25)]);

    const items = sut.updateQuality();

    expect(items[0].sellIn).toBe(-1);
  });

  it("Aged Brie quality improves with age", () => {
    const sut = new GildedRose([new Item("Aged Brie", 5, 30)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(31);
  });

  it("Aged Brie quality improves twice as fast after sellIn date reached", () => {
    const sut = new GildedRose([new Item("Aged Brie", 0, 30)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(32);
  });

  // TODO: can all items which improve with and have cap be tested together? 
  it("Aged Brie improves with age, quality is capped at 50 before sellIn date reached", () => {
    const sut = new GildedRose([new Item("Aged Brie", 10, 50)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(50);
  });

  it("Aged Brie quality capped at 50 even when really old", () => {
    const sut = new GildedRose([new Item("Aged Brie", -10, 50)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(50);
  });


  // TODO - there are several items whose Sellin decreases each update.. can we make it dat driven? 
  it("Backstage passes SellIn decreases each update", () => {
    const sut = new GildedRose([new Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]);

    const items = sut.updateQuality();

    expect(items[0].sellIn).toBe(9);
  });

  it("Backstage passes SellIn will be negative after sellIn date reached", () => {
    const sut = new GildedRose([new Item("Backstage passes to a TAFKAL80ETC concert", 0, 25)]);

    const items = sut.updateQuality();

    expect(items[0].sellIn).toBe(-1);
  });

  it("Backstage pass quality increases when concert is far in the future", () => {
    const sut = new GildedRose([new Item("Backstage passes to a TAFKAL80ETC concert", 30, 23)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(24);
  });

  it("Backstage pass quality increases more when concert is 10 days away", () => {
    const sut = new GildedRose([new Item("Backstage passes to a TAFKAL80ETC concert", 10, 23)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(25);
  });

  it("Backstage pass quality increases even more when concert is 5 days away", () => {
    const sut = new GildedRose([new Item("Backstage passes to a TAFKAL80ETC concert", 5, 23)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(26);
  });


  it("Backstage passes improves with age, quality is capped at 50", () => {
    const sut = new GildedRose([new Item("Backstage passes to a TAFKAL80ETC concert", 10, 50)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(50);
  });

  it("Backstage pass quality drops to zero when concert has passed", () => {
    const sut = new GildedRose([new Item("Backstage passes to a TAFKAL80ETC concert", 0, 23)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(0);
  });

  it("Backstage pass quality is capped at 50 when concert is about to happen", () => {
    const sut = new GildedRose([new Item("Backstage passes to a TAFKAL80ETC concert", 1, 49)]);

    const items = sut.updateQuality();

    expect(items[0].quality).toBe(50);
  });

  it("Shop can contain multiple items and each is updated", () => {
    const sut = new GildedRose([new Item("Sulfuras, Hand of Ragnaros", 0, 80),
    new Item("generic item", 10, 5)]);

    const items = sut.updateQuality();

    // jest doesn't have a mechanism to ensure all expectations are verified
    // Is there any other way to do this? 
    expect(items[0].sellIn).toBe(0);
    expect(items[1].sellIn).toBe(9);
  });

});

