from flask import jsonify, request
from app import app, db
from app.models import Articles
from app.serialization import article_schema, articles_schema
from flask_cors import cross_origin


# to get all articles
@app.route('/get', methods=['GET'])
@cross_origin()
def get_articles():
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)


# to get specific article to specific id
@app.route('/get/<id>/', methods=['GET'])
@cross_origin()
def post_details(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)


# step2: create add method to add new article
@app.route('/add', methods=['POST'])
@cross_origin()
def add_article():
    data = request.get_json()
    posted_by = request.json['posted_by']
    title = request.json['title']
    body = request.json['body']
    image = request.json['image']
    articles = Articles(posted_by, title, body, image)
    if len(posted_by) > 4 and len(body) > 99 and len(image) > 0:
        db.session.add(articles)
        db.session.commit()
        return article_schema.jsonify(articles)
    else:
        return article_schema.jsonify({"Error": "Can't Added"})


# update on article

@app.route('/update/<id>', methods=['PUT'])
@cross_origin()
def update_article(id):
    article = Articles.query.get(id)

    posted_by = request.json['posted_by']
    title = request.json['title']
    body = request.json['body']
    image = request.json['image']

    article.posted_by = posted_by
    article.title = title
    article.body = body
    article.image = image

    db.session.commit()
    return article_schema.jsonify(article)


# delete specific article
@app.route('/delete/<id>', methods=['DELETE'])
@cross_origin()
def article_delete(id):
    article = Articles.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return jsonify({"message": "Deleted"})

