#    Copyright 2010, 2011 Red Hat Inc.
#
#    This file is part of StratoSource.
#
#    StratoSource is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    StratoSource is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with StratoSource.  If not, see <http://www.gnu.org/licenses/>.
#    
from django.core.management.base import BaseCommand, CommandError
from suds.client import Client
import os
import base64
import sys
import httplib, urllib
import json
import time
import datetime
from stratosource.admin.management import CSBase
from stratosource.admin.management import Utils
from stratosource.user import rallyintegration


__author__="jkruger"
__date__ ="$Nov 1, 2011 10:41:44 AM$"



class Command(BaseCommand):

    def handle(self, *args, **options):

        rallyintegration.refresh()
