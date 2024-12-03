from datetime import datetime
import random
from time import sleep


from OpenAi import OpenAIAgent
from Proxy import Proxy
from Utils.DbConnection import DbConnection
from OLX.OlxList import OlxList
from OLX.PhoneListing import PhoneListing
from Utils.Discord import DiscordWebhookSender
from Vinted.VintedList import VintedList
from Vinted.VintedPhoneListing import VintedPhoneListing

if __name__ == "__main__":
    db = DbConnection()
    discord = DiscordWebhookSender('https://discord.com/api/webhooks/1283777137924374628/f9-WYqGPWaajevct0le5TDCey0ZRFlUULvwpc8iG0xbkrw0qPAdas7YWAxntf9YyIMZk')
    # discord = DiscordWebhookSender('https://discord.com/api/webhooks/961347407789047853/nuYwUGTLDc_4x7pDHMr1uuie19lOp--oVWqGfv2c2uYQ5Ggp18FxhkAdZVeXa2rVMZhg')
    existing_listings_id = db.get_all_listing_ids()
    urls = [
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/?search%5Border%5D=created_at:desc',
        'https://www.vinted.pl/api/v2/catalog/items?page=1&per_page=96&time=1731756901&search_text=&catalog_ids=2999&order=newest_first&brand_ids=54661,109048,201078&brand_collection_ids=&status_ids=&color_ids=&internal_memory_capacity_ids=&sim_lock_ids=&cosmetic_condition_with_screen_ids=&cosmetic_condition_no_screen_ids='
    ]
    p = Proxy()
    v = VintedList(p.proxy_list)
    o = OpenAIAgent()
    i = 0
    while(True):
        for olx_url in urls:
            if 'olx' in olx_url:
                listings = OlxList.get_olx_listings_for_monitor(olx_url)
                for listing in listings:
                    ad = PhoneListing(listing)
                    if str(ad.listing_id) not in existing_listings_id:
                        existing_listings_id.append(str(ad.listing_id))
                        i = i+1
                        print(f'Dodano {i} ogłoszeń do bazy')
                        if ad.isDeal and ad.isDelivery == 'BuyWithDelivery':
                            ad.rate = o.rate_ad_without_photo(ad.description, ad.phonemodel, ad.title,)
                            ad.get_user()
                            discord.send_phone_listing(ad)
                        ad.save_to_db(db)
                print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] OLX: Sprawdzono: {len(listings)} ogłoszeń')
            elif 'vinted' in olx_url:
                listings = v.get_vinted_list(olx_url)
                if listings:
                    for listing in listings:
                        ad = VintedPhoneListing(listing)
                        if str(ad.listing_id) not in existing_listings_id:
                            ad.get_phone_details(v.cookies, v.proxy)
                            i = i + 1
                            print(f'Dodano {i} ogłoszeń do bazy')
                            existing_listings_id.append(str(ad.listing_id))
                            if ad.isDeal:
                                discord.send_phone_listing(ad)
                                ad.rate = o.rate_ad_without_photo(ad.description, ad.phonemodel, ad.title, )
                                discord.send_phone_listing(ad)
                            ad.save_to_db(db)
                    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Vinted: Sprawdzono: {len(listings)} ogłoszeń')
        sleep(2)