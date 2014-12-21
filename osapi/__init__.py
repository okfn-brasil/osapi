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
import json
try:
    # Python 3
    from urllib.parse import urljoin
except:
    # Python 2
    from urlparse import urljoin


def auth_header(apikey):
    return { 'Authorization': 'ApiKey {key}'.format( key=apikey )}

class OpenSpendingAPI(object):
    """Interacts with the OpenSpending API"""
    def __init__(self, url, apikey):
        self.url = url
        self.apikey = apikey

    #def create_resource_package(self, budget_url):
    #    """docstring for create_resource"""
    #    create_url = urljoin(self.url, '/api/2/new')
    #    parameters = {'budget_data_package': budget_url}
    #    response = requests.post(create_url, params=parameters,
    #                             headers=auth_header(self.apikey))

    def create_dataset(self, csv_file, metadata):
        """Creates a Dataset based on the csv_file in metadata. Returns it."""
        create_url = urljoin(self.url, '/api/2/new')
        parameters = {
            'csv_file': csv_file,
            'metadata': metadata,
        }
        response = requests.post(create_url, params=parameters,
                                 headers=auth_header(self.apikey))
        print(response.text)
        # TODO: Error check!
        dataset_name = json.loads(response.text)['name']
        return Dataset(dataset_name, self.url, self.apikey)

class Dataset(object):
    """Interacts with an OpenSpending Dataset"""
    def __init__(self, name, url, apikey):
        self.name = name
        self.url = url
        self.apikey = apikey

    def delete_dataset(self):
        """Deletes the dataset"""
        url = urljoin(self.url, self.name + "/editor/delete")
        response = requests.post(url, headers=auth_header(self.apikey))
        #open("a.html", 'w').write(response.text)

    def list_sources(self):
        pass
        #https://openspending.org/02o2do982o2do982/sources.json
    def delete_source(self, source):
        pass
        #https://openspending.org/02o2do982o2do982/sources/10832/delete
    def retract_all(self):
        pass
        #https://openspending.org/02o2do982o2do982/editor/retract
    def delete_loaded(self):
        pass
        #https://openspending.org/02o2do982o2do982/editor/drop
