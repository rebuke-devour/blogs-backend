"""Providers Configuration File."""

from masonite.providers import (
    AppProvider,
    CorsProvider,
    RequestHelpersProvider,
    AuthenticationProvider,
    BroadcastProvider,
    CacheProvider,
    CsrfProvider,
    HelpersProvider,
    MailProvider,
    QueueProvider,
    RouteProvider,
    SessionProvider,
    StatusCodeProvider,
    UploadProvider,
    ViewProvider,
    WhitenoiseProvider,
    
)
from masonite.logging.providers import LoggingProvider
from masonite.validation.providers import ValidationProvider
from masoniteorm.providers import ORMProvider

"""Providers List
Providers are a simple way to remove or add functionality for Masonite
The providers in this list are either ran on server start or when a
request is made depending on the provider. Take some time to can
learn more more about Service Providers in our documentation
"""

PROVIDERS = [
    # Framework Providers
    AppProvider,
    CorsProvider,
    RequestHelpersProvider,
    CsrfProvider,
    AuthenticationProvider,
    SessionProvider,
    RouteProvider,
    StatusCodeProvider,
    WhitenoiseProvider,
    ViewProvider,
    # Optional Framework Providers
    MailProvider,
    UploadProvider,
    QueueProvider,
    CacheProvider,
    BroadcastProvider,
    HelpersProvider,
    ValidationProvider,
    # Third Party Providers
    LoggingProvider,
    ValidationProvider,
    ORMProvider,
     
    # Application Providers
]
CORS = {
    'Access-Control-Allow-Origin': "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Max-Age": "3600",
    "Access-Control-Allow-Credentials": "true"
}