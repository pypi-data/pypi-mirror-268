class Config:
    FIREBASE_API_KEY = 'AIzaSyDBbIiCyAFkz_bZQb0hbP5wFB-ioF6xOyw'
    FIREBASE_AUTH_DOMAIN = 'trail-ml-9e15e.firebaseapp.com'
    ENDPOINT_URL = ''
    PRESIGNED_ENDPOINT = '/generate_presigned_bucket_url'
    GQL_ENDPOINT = '/graphql'

    PRIMARY_USER_CONFIG_PATH = 'trail_config.yml'

    TRAIL_SIGN_UP_URL = "https://www.trail-ml.com/sign-up"

    @property
    def presigned_endpoint_url(self):
        return self.ENDPOINT_URL + self.PRESIGNED_ENDPOINT

    @property
    def gql_endpoint_url(self):
        return self.ENDPOINT_URL + self.GQL_ENDPOINT


class ProductionConfig(Config):
    ENDPOINT_URL = 'https://trail-ml-9e15e.ew.r.appspot.com'


class DevelopmentConfig(Config):
    ENDPOINT_URL = 'http://127.0.0.1:5002'
