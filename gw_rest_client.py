import click
import requests


class GwRestClient:
    def __init__(self):
        self.uri = 'http://localhost:8887/graphwalker/'

    def has_next(self):
        response = requests.get(self.uri + 'hasNext')
        if not self._json(response)['hasNext'] == 'true':
            return False
        return True

    def get_next(self):
        response = requests.get(self.uri + 'getNext')
        return self._json(response)['currentElementName']

    def get_data(self):
        response = requests.get(self.uri + 'getData')
        return self._json(response)['data']

    def get_statistics(self):
        response = requests.get(self.uri + 'getStatistics')
        return self._json(response)

    def restart(self):
        click.echo(requests.put(self.uri + 'restart').content)

    @staticmethod
    def _json(response):
        try:
            json_ = response.json()
            if response.status_code != 200:
                click.echo('Error retrieving response. Check inner details for more info.', err=True)
            elif json_['result'] != 'ok':
                click.echo('getNext failed. Check inner details for more info.', err=True)
            else:
                return json_
        except:
            click.echo('Error retrieving response. Check inner details for more info.', err=True)
