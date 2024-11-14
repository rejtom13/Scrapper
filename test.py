# from datetime import datetime
# from time import sleep
#
# from Allegro.AllegroList import AllegroList
# from Allegro.AllegroPhoneListing import AllegroPhoneListing
# from Utils.DbConnection import DbConnection
# from Utils.Discord import DiscordWebhookSender
#
#
# if __name__ == "__main__":
#     db = DbConnection()
#     discord = DiscordWebhookSender('https://discord.com/api/webhooks/961347407789047853/nuYwUGTLDc_4x7pDHMr1uuie19lOp--oVWqGfv2c2uYQ5Ggp18FxhkAdZVeXa2rVMZhg')
#     existing_listings_id = db.get_all_listing_ids()
#     urls = [
#         'https://allegrolokalnie.pl/oferty/smartfony-i-telefony-komorkowe/apple-48978/q/iphone%20?typ=kup-teraz&typ=ogloszenie&page=13'
#     ]
#     while(True):
#         for olx_url in urls:
#             if 'allegro' in olx_url:
#                 listings = AllegroList.get_alegroLokalnie_listings_for_monitor(olx_url)
#                 for listing in listings:
#                     ad = AllegroPhoneListing(listing['item'])
#                     if str(ad.listing_id) not in existing_listings_id:
#                         ad.get_phone_details()
#                         # ad.save_to_db(db)
#                         # existing_listings_id.append(str(ad.listing_id))
#                         # i = i+1
#                         # print(f'Dodano {i} ogłoszeń do bazy')
#                         # if ad.isDeal:
#                         #     discord.send_phone_listing(ad)
#                         print(ad)
#                         sleep(3)
#
#                 print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Sprawdzono nowe ogłoszenia AllegroLokalnie')
#         sleep(15)
import json

import requests


