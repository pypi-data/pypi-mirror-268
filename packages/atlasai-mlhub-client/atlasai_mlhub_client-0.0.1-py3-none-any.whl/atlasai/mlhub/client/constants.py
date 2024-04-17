from types import SimpleNamespace

HTTP = 'http'
BATCH = 'batch'

DEPLOYMENT_TYPES = SimpleNamespace(
    http=HTTP,
    batch=BATCH
)

DEFAULT_POLLING_TIMEOUT = 3600

POLLING_INTERVAL = 10