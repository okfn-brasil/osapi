#!/usr/bin/env python
# coding: utf-8

#-----------------------------------------------------------------------------
# Copyright 2014 Andrés Mantecon Ribeiro Martano
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-----------------------------------------------------------------------------


import requests
import urllib


APIKEY = open("apikey").read().strip()


class OpenSpendingAPI(object):
    """Interacts with the OpenSpending API"""
    def __init__(self, url, apikey):
        self.url = url
        self.apikey = apikey

    def get_header(self):
        return { 'Authorization': 'ApiKey {key}'.format( key=self.apikey )}

    def create_resource_package(self, budget_url):
        """docstring for create_resource"""
        create_url = urllib.parse.urljoin(self.url, '/api/2/new')
        parameters = {'budget_data_package': budget_url}
        response = requests.post(create_url, params=parameters,
                                 headers=self.get_header())

    def create_resource_csv(self, csv_file, metadata):
        """docstring for create_resource"""
        create_url = urllib.parse.urljoin(self.url, '/api/2/new')
        parameters = {
            'csv_file': csv_file,
            'metadata': metadata,
        }
        response = requests.post(create_url, params=parameters,
                                 headers=self.get_header())
        open("a.html", 'w').write(response.text)

class Dataset(object):
    """Interacts with an OpenSpending Dataset"""
    def __init__(self, name, apikey):
        self.name = name
        self.apikey = apikey

    def delete_dataset(self):
        """Deletes the dataset"""
        url = urllib.parse.urljoin(self.url, self.name + "/editor/delete")
        response = requests.post(url, headers=self.get_header())
        #open("a.html", 'w').write(response.text)

    def list_sources(self):
        https://openspending.org/02o2do982o2do982/sources.json
    def delete_source(self, source):
        https://openspending.org/02o2do982o2do982/sources/10832/delete
    def retract_all(self):
        https://openspending.org/02o2do982o2do982/editor/retract
    def delete_loaded(self):
        https://openspending.org/02o2do982o2do982/editor/drop
        
osapi = OpenSpendingAPI("https://openspending.org", APIKEY)
json = "https://devcolab.each.usp.br/owncloud/public.php?service=files&t=f4a2b677b00fd7f286c6276a9aef155c&download"
csv = "http://mk.ucant.org/info/data/sample-openspending-dataset.csv"
#osapi.create_resource_csv(csv, json)
osapi.delete_dataset("02o2diiiiiiiiiii")
