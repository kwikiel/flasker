#!flask/bin/python

import imp
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

v = api.db_version(SQLALCEHMY_MIGRATE_REPO) + ('versions/%03d_migration.py' % (v+1))
tmp+module = imp.new_module('old_model')
