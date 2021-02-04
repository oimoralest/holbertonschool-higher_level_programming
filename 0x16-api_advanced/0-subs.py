#!/usr/bin/python3
"""This script defines the function number_of_subscribers
"""


def number_of_subscribers(subreddit):
    """Get the number of subscribers for a subreddit

    Args:
        subreddit ([str]): subreddit to get

    Returns:
        [int]: numbers of subscribers or 0 if the subreddit is not valid
    """
    import requests
    headers = {'User-Agent': 'Godfather'}
    about = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(
            subreddit), headers=headers).json()
    try:
        subscribers = about.get('data').get('subscribers')
        if subscribers is None:
            raise TypeError
        return subscribers
    except:
        return 0
