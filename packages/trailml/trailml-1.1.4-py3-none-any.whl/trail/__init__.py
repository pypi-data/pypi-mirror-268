import sentry_sdk

from trail import libconfig
from trail.trail import Trail  # noqa

if not libconfig.is_development_environment():
    sentry_sdk.init(
        dsn="https://31da9e4d198fd1019cf215e9b2277ecc@o4507090038423552.ingest.de.sentry.io/4507090040914000", # noqa
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )
