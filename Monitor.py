from time import sleep

from Utils.DbConnection import DbConnection
from OLX.OlxList import OlxList
from OLX.PhoneListing import PhoneListing
from Utils.Discord import DiscordWebhookSender

if __name__ == "__main__":
    db = DbConnection()
    discord = DiscordWebhookSender('https://discord.com/api/webhooks/1283777137924374628/f9-WYqGPWaajevct0le5TDCey0ZRFlUULvwpc8iG0xbkrw0qPAdas7YWAxntf9YyIMZk')
    existing_listings_id = db.get_all_listing_ids()
    urls = [
        'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=900&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-13',
        'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=1400&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-13-pro',
        'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=1200&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-14',
        'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=600&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-12'


    ]
    while(True):
        for olx_url in urls:
                listings = OlxList.get_olx_listings_for_monitor(olx_url)
                for listing in listings:
                    ad = PhoneListing(listing)
                    if str(ad.listing_id) not in existing_listings_id and ad.price>0:
                        discord.send_phone_listing(ad)
                        ad.save_to_db(db)
                        existing_listings_id.append(str(ad.listing_id))
                    else:
                        print(f'Listing istnieje w bazie {ad.listing_id}')
        sleep(30)

