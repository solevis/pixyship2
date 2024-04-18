class DefaultConfig:
    # Database URI
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg://postgres:postgres@localhost:5432/pixyship"

    # Enable features specific to development
    DEV_MODE = True

    # Frontend domain
    DOMAIN = "localhost:8080"

    # Directory that will contain downloaded sprites, must be served by the web server as static content
    SPRITES_DIRECTORY = "../sprites"

    # Savy PSS API urls
    FORCED_PIXELSTARSHIPS_API_URL = None
    USE_STAGING_API = False

    # Maximum of changes to be returned by PixyShip API and displayed in front
    CHANGES_MAX_ASSETS = 5000

    # Generated with `python -c 'import os; print(os.urandom(16))'`, must be kept secret
    SECRET_KEY = "dev"

    # Generated from PSS website (only available for Savy trusted third-party developers),
    # if None, classic token will be generated by PixyShip
    SAVY_PUBLIC_API_TOKEN = None
    DEVICE_LOGIN_CHECKSUM_KEY = None

    # Session cookie security
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"

    # Sentry DSN (https://sentry.io)
    SENTRY_DSN = None
