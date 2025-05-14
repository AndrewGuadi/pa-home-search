from flask import render_template, request
from . import property_search
from math import ceil

def fetch_listings(q=None, beds=None, baths=None, min_price=None, max_price=None, page=1, per_page=12):
    """
    Replace this with your real MLS integration.
    Should return a tuple: (list_of_listing_dicts, total_listing_count).
    """
    # TODO: integrate with real data source
    return [], 0

@property_search.route('/', methods=['GET'])
def search():
    # 1. Grab all filters from the query string
    q         = request.args.get('q', type=str, default='')
    beds      = request.args.get('beds', type=int)
    baths     = request.args.get('baths', type=int)
    min_price = request.args.get('min_price', type=int)
    max_price = request.args.get('max_price', type=int)
    page      = request.args.get('page', type=int, default=1)
    per_page  = 12

    # 2. Fetch listings + total count
    listings, total = fetch_listings(
        q=q,
        beds=beds,
        baths=baths,
        min_price=min_price,
        max_price=max_price,
        page=page,
        per_page=per_page
    )

    # 3. Compute total pages
    total_pages = ceil(total / per_page) if total else 1

    # 4. Render the unified search template
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

@property_search.route('/<city>', methods=['GET'])
def city_page(city):
    # Pre-fill the 'q' filter with the city name
    page     = request.args.get('page', type=int, default=1)
    per_page = 12

    listings, total = fetch_listings(q=city, page=page, per_page=per_page)
    total_pages     = ceil(total / per_page) if total else 1

    return render_template(
        'property_search/index.html',
        listings=listings,
        page=page,
        total_pages=total_pages,
        filters={'q': city}
    )