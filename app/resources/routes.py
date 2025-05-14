# app/resources/routes.py
from flask import render_template, request
from . import resources


@resources.route('/resources')
def resources_overview():
    # 1. pagination params
    page = request.args.get('page', 1, type=int)
    per_page = 10

    # 2. filtering/search params
    category = request.args.get('category')
    q        = request.args.get('q', '')

    # 3. Fetch your data (replace these stubs with real DB or API calls)
    categories = [
        {'slug': 'market-trends',        'name': 'Market Trends'},
        {'slug': 'neighborhood-guides',   'name': 'Neighborhood Guides'},
        {'slug': 'buying-selling-tips',   'name': 'Buying & Selling Tips'},
        {'slug': 'faq',                   'name': 'FAQ'},
    ]
    # Stubbed list of articles
    articles = [{
        'title':   f'Sample Article {i}',
        'url':     f'/resources/article-{i}',
        'image_url': '/static/images/sample.jpg',
        'date':    'May 2025',
        'category': categories[i % len(categories)]['name'],
        'excerpt': 'This is a short excerpt of the article…'
    } for i in range(per_page)]

    # Total count stub → compute total_pages
    total_articles = 42
    total_pages    = (total_articles + per_page - 1) // per_page

    # Other sidebars / featured content
    popular_posts    = articles[:5]
    tags             = [{'slug': t, 'name': t.title()} for t in ['pricing','tips','neighborhood']]
    featured_article = articles[0]
    related_resources= [
        {'url':'/resources/guide-1','title':'Beginner Guide','description':'Start here…'},
        {'url':'/resources/guide-2','title':'Selling Checklist','description':'Don’t forget…'},
        {'url':'/resources/guide-3','title':'Loan Basics','description':'Know your options…'},
    ]

    return render_template(
        'resources/index.html',  # **no** leading slash
        categories=categories,
        articles=articles,
        page=page,
        total_pages=total_pages,
        popular_posts=popular_posts,
        tags=tags,
        featured_article=featured_article,
        related_resources=related_resources,
        # also pass through any filters so pagination links preserve them:
        q=q,
        category=category
    )
    
@resources.route('/resources/market_trends')
def market_trends():
    return render_template('resources/market_trends.html')

@resources.route('/resources/neighborhood_guides')
def neighborhood_guides():
    return render_template('resources/neighborhood_guides.html')

@resources.route('/resources/buying_selling_tips')
def buying_selling_tips():
    return render_template('resources/buying_selling_tips.html')

@resources.route('/resources/faq')
def faq():
    return render_template('resources/faq.html')
