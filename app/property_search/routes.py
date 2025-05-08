# app/property_search/routes.py
from flask import render_template, request
from . import property_search
from math import ceil

def fetch_listings(q=None, beds=None, baths=None, min_price=None, max_price=None, page=1, per_page=12):
    """
    Replace this with your real MLS integration.
    Should return (list_of_listing_dicts, total_listing_count).
    """
    # Example stub: return empty + zero total
    return [], 0

@property_search.route('/property_search')
def search():
    # 1. Grab all your filters from the querystring
    q         = request.args.get('q', type=str, default='')
    beds      = request.args.get('beds', type=int)
    baths     = request.args.get('baths', type=int)
    min_price = request.args.get('min_price', type=int)
    max_price = request.args.get('max_price', type=int)
    page      = request.args.get('page', type=int, default=1)
    per_page  = 12

    # 2. Fetch your listings + total count
    listings, total = fetch_listings(
        q=q,
        beds=beds,
        baths=baths,
        min_price=min_price,
        max_price=max_price,
        page=page,
        per_page=per_page
    )

    # 3. Compute total pages for pagination
    total_pages = ceil(total / per_page) if total else 1

    # 4. Render with everything the template needs
    return render_template(
        'property_search/index.html',
        listings=listings,
        page=page,
        total_pages=total_pages,
        filters={
            'q': q,
            'beds': beds,
            'baths': baths,
            'min_price': min_price,
            'max_price': max_price
        }
    )

@property_search.route('/property_search/<city>')
def city_page(city):
    # If you want to pre‐filter by city in the same general UI:
    page      = request.args.get('page', type=int, default=1)
    per_page  = 12

    # You could pass city into the same fetch_listings or a separate function:
    listings, total = fetch_listings(q=city, page=page, per_page=per_page)
    total_pages     = ceil(total / per_page) if total else 1

    return render_template(
        'property_search/index.html',   # reuse the same layout
        listings=listings,
        page=page,
        total_pages=total_pages,
        filters={'q': city}
    )
