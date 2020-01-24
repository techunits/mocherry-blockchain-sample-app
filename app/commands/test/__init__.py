#!/usr/bin/env python
from mocherry.library.commands import BaseCommand

class Command(BaseCommand):
    def handle(self, *args):
        print("Success: This is a test command")