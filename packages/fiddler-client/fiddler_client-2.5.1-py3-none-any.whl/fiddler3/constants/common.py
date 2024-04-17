JSON_CONTENT_TYPE = 'application/json'
FIDDLER_CLIENT_VERSION_HEADER = 'X-Fiddler-Client-Version'
CLIENT_NAME = 'python-sdk'
LOGGER_NAME = 'fiddler3'
LOG_FORMAT = '%(asctime)s [%(name)s:%(lineno)d] %(levelname)s: %(message)s'
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

# Headers
CONTENT_TYPE_HEADER_KEY = 'Content-Type'
CONTENT_TYPE_OCTET_STREAM = 'application/octet-stream'
CONTENT_TYPE_OCTET_STREAM_HEADER = {CONTENT_TYPE_HEADER_KEY: CONTENT_TYPE_OCTET_STREAM}

# Multi-part upload
MULTI_PART_UPLOAD_SIZE_THRESHOLD = 5 * 1024 * 1024  # 5MB in bytes
MULTI_PART_CHUNK_SIZE = 100 * 1024 * 1024  # 100MB in bytes
