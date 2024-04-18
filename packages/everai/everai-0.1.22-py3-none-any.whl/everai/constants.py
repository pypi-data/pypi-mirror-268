import os
import sys

from everai.utils.bool import str_to_bool
from dotenv import load_dotenv

load_dotenv('.env')

EVERAI_ENDPOINT = os.getenv('EVERAI_ENDPOINT') or 'https://hub.everai.com'

default_home = os.path.join(os.path.expanduser("~"), '.cache')

EVERAI_HOME = os.path.expanduser(
    os.getenv(
        'EVERAI_HOME',
        os.path.join(
            os.getenv('XDG_CACHE_HOME', default_home),
            'everai',
        )
    )
)

EVERAI_VOLUME_ROOT = os.getenv('EVERAI_VOLUME_ROOT') or os.path.join(EVERAI_HOME, 'volumes')

EVERAI_TOKEN_PATH = os.path.join(EVERAI_HOME, 'token')
EVERAI_TOKEN = 'EVERAI_TOKEN'

EVERAI_FORCE_PULL_VOLUME = str_to_bool(os.getenv('EVERAI_FORCE_PULL_VOLUME'))

HEADER_REQUEST_ID = 'X-everai-request-id'
HEADER_SETUP_PATH = 'X-everai-setup-path'

COMMAND_ENTRY = os.path.basename(sys.argv[0])

BUILDER = 'everai'

PUSH_DELETE_FILE_LIMIT = 0.5

MAX_SINGLE_FILE_SIZE = 5 * 1024 * 1024

DEFAULT_PART_SIZE = 32 * 1024 * 1024

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

PART_NUMBER_KEY = 'partNumber'
