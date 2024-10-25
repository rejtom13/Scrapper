from time import sleep

from Utils.DbConnection import DbConnection
from OLX.OlxList import OlxList
from OLX.PhoneListing import PhoneListing

if __name__ == "__main__":
    db = DbConnection()
    existing_listings_id = db.get_all_listing_ids()
    urls = [
        'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-16-plus&search%5Bfilter_enum_phonemodel%5D%5B10%5D=iphone-16-pro-max&search%5Bfilter_enum_phonemodel%5D%5B11%5D=iphone-11&search%5Bfilter_enum_phonemodel%5D%5B12%5D=iphone-8-plus&search%5Bfilter_enum_phonemodel%5D%5B13%5D=iphone-12-pro&search%5Bfilter_enum_phonemodel%5D%5B14%5D=iphone-12&search%5Bfilter_enum_phonemodel%5D%5B15%5D=iphone-14&search%5Bfilter_enum_phonemodel%5D%5B16%5D=iphone-14-plus&search%5Bfilter_enum_phonemodel%5D%5B17%5D=iphone-15-pro-max&search%5Bfilter_enum_phonemodel%5D%5B18%5D=iphone-xs&search%5Bfilter_enum_phonemodel%5D%5B19%5D=iphone-xs-max&search%5Bfilter_enum_phonemodel%5D%5B1%5D=iphone-8&search%5Bfilter_enum_phonemodel%5D%5B20%5D=iphone-xr&search%5Bfilter_enum_phonemodel%5D%5B21%5D=iphone-16pro&search%5Bfilter_enum_phonemodel%5D%5B22%5D=iphone-14-pro-max&search%5Bfilter_enum_phonemodel%5D%5B23%5D=iphone-12-pro-max&search%5Bfilter_enum_phonemodel%5D%5B24%5D=iphone-11-pro&search%5Bfilter_enum_phonemodel%5D%5B25%5D=iphone-13-pro&search%5Bfilter_enum_phonemodel%5D%5B26%5D=iphone-13-pro-max&search%5Bfilter_enum_phonemodel%5D%5B27%5D=iphone-14-pro&search%5Bfilter_enum_phonemodel%5D%5B28%5D=iphone-13&search%5Bfilter_enum_phonemodel%5D%5B29%5D=iphone-13-mini&search%5Bfilter_enum_phonemodel%5D%5B2%5D=iphone-15-pro&search%5Bfilter_enum_phonemodel%5D%5B3%5D=iphone-15&search%5Bfilter_enum_phonemodel%5D%5B4%5D=iphone-12-mini&search%5Bfilter_enum_phonemodel%5D%5B5%5D=iphone-16&search%5Bfilter_enum_phonemodel%5D%5B6%5D=iphone-se&search%5Bfilter_enum_phonemodel%5D%5B7%5D=iphone-x&search%5Bfilter_enum_phonemodel%5D%5B8%5D=iphone-15-plus&search%5Bfilter_enum_phonemodel%5D%5B9%5D=iphone-11-pro-max&search%5Border%5D=created_at%3Adesc'
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-16-plus&search%5Bfilter_enum_phonemodel%5D%5B1%5D=iphone-16pro&search%5Bfilter_enum_phonemodel%5D%5B2%5D=iphone-16&search%5Bfilter_enum_phonemodel%5D%5B3%5D=iphone-16-pro-max',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-15&search%5Bfilter_enum_phonemodel%5D%5B1%5D=iphone-15-plus',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-15-pro',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-15-pro-max',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-14&search%5Bfilter_enum_phonemodel%5D%5B1%5D=iphone-14-plus',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_builtinmemory_phones%5D%5B0%5D=32gb&search%5Bfilter_enum_builtinmemory_phones%5D%5B1%5D=64gb&search%5Bfilter_enum_builtinmemory_phones%5D%5B2%5D=128gb&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-14-pro',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_builtinmemory_phones%5D%5B0%5D=256gb&search%5Bfilter_enum_builtinmemory_phones%5D%5B1%5D=1tb&search%5Bfilter_enum_builtinmemory_phones%5D%5B2%5D=512gb&search%5Bfilter_enum_builtinmemory_phones%5D%5B3%5D=others&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-14-pro',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-14-pro-max',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-13&search%5Bfilter_enum_builtinmemory_phones%5D%5B0%5D=32gb&search%5Bfilter_enum_builtinmemory_phones%5D%5B1%5D=64gb&search%5Bfilter_enum_builtinmemory_phones%5D%5B2%5D=128gb',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_builtinmemory_phones%5D%5B0%5D=256gb&search%5Bfilter_enum_builtinmemory_phones%5D%5B1%5D=512gb&search%5Bfilter_enum_builtinmemory_phones%5D%5B2%5D=others&search%5Bfilter_enum_builtinmemory_phones%5D%5B3%5D=1tb&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-13',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-13-mini',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_float_price:to%5D=2400&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-13-pro',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_float_price:from%5D=2400&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-13-pro',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-13-pro-max',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_float_price:to%5D=1400&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-12',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_float_price:from%5D=1400&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-12',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-12-mini',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-12-pro',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-12-pro-max',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_float_price:to%5D=750&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-11',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_float_price:from%5D=750&search%5Bfilter_float_price:to%5D=950&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-11',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_float_price:from%5D=950&search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-11',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-11-pro',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-11-pro-max',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-se',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-x&search%5Bfilter_enum_phonemodel%5D%5B1%5D=iphone-xs',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-xs-max&search%5Bfilter_enum_phonemodel%5D%5B1%5D=iphone-xr',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-8&search%5Bfilter_enum_phonemodel%5D%5B1%5D=iphone-8-plus',
        # 'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/q-iphone/?search%5Bfilter_enum_phonemodel%5D%5B0%5D=iphone-7&search%5Bfilter_enum_phonemodel%5D%5B1%5D=iphone-7-plus'
         ]
    for olx_url in urls:
        pages = 2
        i=0
        while (i<=pages):
            sleep(5)
            i = i +1
            listings, pages = OlxList.get_olx_listings(olx_url, i)
            for listing in listings:
                ad = PhoneListing(listing)
                if str(ad.listing_id) not in existing_listings_id and ad.price>0:
                    print(ad.listing_id)
                    ad.save_to_db(db)
                    existing_listings_id.append(str(ad.listing_id))
                else:
                    print(f'Listing istnieje w bazie {ad.listing_id}')

