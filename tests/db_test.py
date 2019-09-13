import unittest
import sys

sys.path.append('/home/pengfei/xweb')

from app.models import db

class DbTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_a(self):
        db.create_all()

        fly = User(id=1,name='fly',age=30)
        db.session.add(fly)
        db.session.commit()

        self.assertTrue(db.query.all().count,1)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
