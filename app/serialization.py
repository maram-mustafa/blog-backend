from app import ma


# step3: create schema for model to determine a return values
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ("id", "posted_by", "title", "body", "date", "image")


article_schema = ArticleSchema()  # create schema object
articles_schema = ArticleSchema(many=True)  # to return query set
