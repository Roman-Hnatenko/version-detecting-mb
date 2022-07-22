from hashlib import md5

import requests


def make_hash(script_link: str) -> str:
    response = requests.get(script_link)
    return md5(response.content).hexdigest()


if __name__ == '__main__':
    hash = make_hash('https://static-common.isoftbet.com/games/html/html5/pulse_ghosts_n_gold/pulse_ghosts_n_gold_r44/pulse_ghosts_n_gold/js/vendor.js')

