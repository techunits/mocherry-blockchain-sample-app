#!/usr/bin/env python
from mocherry.library.commands import BaseCommand
from mocherry.library.databases import DatabaseConnection
from mocherry.settings import CONFIG
from cms.models import Article
from faker import Faker
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args):
        print("Initialize applicaiton with dummy data")
        faker = Faker()
        for idx in range(1, 50):
            mongo_uri = CONFIG['database']['default']['uri']
            with DatabaseConnection(mongo_uri):
                article_info = Article()
                article_info.title = faker.sentence()
                article_info.description = faker.text()
                for tdx in range(0, 5):
                    article_info.tags.append(faker.name())
                article_info.modified_on = datetime.now()
                article_info.save()
                print('New Dummy Article: {} -> {}'.format(article_info.title, article_info.pk))