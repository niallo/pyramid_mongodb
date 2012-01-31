"""
simplified mongodb integration


1. Add two lines to  app/__init__.py ( the import and the call to initialize_mongo_db )

    import python_mongodb
    def main(global_config, **settings):
        ## ...
        # Initialize mongodb , which is a subscriber
        python_mongodb.initialize_mongo_db( config , settings )
        ## ...
        return config.make_wsgi_app()
	
2. in each of your envinronment.ini files, have:

    mongodb.use = true
    mongodb.uri = mongodb://localhost
    mongodb.name = myapp
    
if "mongodb.use" is not "true", then it won't be configured -- so you can do your local development / tests / etc without having mongodb running ( should you want to )

"""
import pymongo
from gridfs import GridFS


def initialize_mongo_db( config, settings ):
    if ( 'mongodb.use' in settings ) and ( settings['mongodb.use'] == 'true' ):
        conn = pymongo.Connection( settings['mongodb.uri'] )
        config.registry.settings['!mongodb.conn'] = conn
        config.add_subscriber(add_mongo_db, 'pyramid.events.NewRequest')


def add_mongo_db(event):
    settings = event.request.registry.settings
    db = settings['!mongodb.conn'][settings['mongodb.name']]
    event.request.mongodb = db
    event.request.gridfs = GridFS(db)
