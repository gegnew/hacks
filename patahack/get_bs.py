##
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
##

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as response:
            if is_good_response(response):
                return(response.content)
            else:
                return(None)

    except RequestException as err:
        log_error('Fricken error during requests to {0} : {1}'.format(url,
                                                                      str(err)))
        return(None)


def is_good_response(response):
    """
    Returns True if the response is HTML, False otherwise.
    """
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200) and content_type is not None and content_type.find('html') > -1

def log_error(err):
    """
    Log dem errs, bud
    """
    print(err)
    save('patahack_log.txt', err)


