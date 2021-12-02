import unittest

from app import app, db
from app.models import Articles


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_data(self):
        article = Articles(posted_by='maram', title='title test1', body='body test1', image='image test1')
        db.session.add(article)
        db.session.commit()
        clint = app.test_client()
        res = clint.get('http://localhost:500/get')
        data = res.get_json()
        assert data[0]['posted_by'] == 'maram'
        print(data)

    def test_add_data(self):
        client = app.test_client()
        res = client.post('http://localhost:5000/add',
                          data='{"posted_by": "maram", "title": "test2", "body": "body2", "image": "image2"}',
                          headers={'Content-Type': 'application/json'})
        data = res.get_json()
        print('DATA', data)
        assert data['posted_by'] == 'maram'

    def test_update_data(self):
        article1 = Articles(posted_by='ali', title='title test3', body='body test3', image='image test3')
        db.session.add(article1)
        db.session.commit()
        client3 = app.test_client()
        # in JS: used ${} with backtick
        # in the flask without $ and ` used only f'String'
        response = client3.put(f'http://localhost:5000/update/{article1.id}',
                               data='{"posted_by": "ahmad", "title": "test3", "body": "body3", "image": "image3"}',
                               headers={'Content-Type': 'application/json'})
        # data3 = response
        # print(data3)
        data = response.get_json()
        assert data['posted_by'] == 'ahmad'

    def test_delete_data_from_database(self):
        article1 = Articles(posted_by='ali', title='title test3', body='body test3', image='image test3')
        db.session.add(article1)
        db.session.commit()
        client3 = app.test_client()
        response = client3.delete(f'http://localhost:5000/delete/{article1.id}')
        data = response.get_json()
        assert data["message"] == "Deleted"


if __name__ == '__main__':
    unittest.main(verbosity=2)
