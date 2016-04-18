# -*- coding: utf-8 -*-

from eve import Eve

app = Eve()

if __name__ == '__main__':
    with app.app_context():
        result = app.data.driver.db['users'].find({})
        print([item for item in result])
    app.run()
