from pydantic_settings import BaseSettings


API_ENDPOINT = "https://rest.tenzir.app/production-v1"
ISSUER_URL = "https://tenzir.eu.auth0.com/"
CLIENT_ID = "vzRh8grIVu1bwutvZbbpBDCOvSzN8AXh"


class PlatformEnvironment(BaseSettings):
    # The remote API endpoint of the platform.
    api_endpoint: str = API_ENDPOINT

    # An arbitrary short string to identify this environment
    # in the local cache directory.
    stage_identifier: str = "prod"

    # TODO: Provide a new `/oidc-config` endpoint in the public platform api
    # to load these values dynamically.
    issuer_url: str = ISSUER_URL
    client_id: str = CLIENT_ID

    # Enable more verbose print statements.
    verbose: bool = False

    @staticmethod
    def load():
        return PlatformEnvironment(
            _env_prefix="TENZIR_PLATFORM_CLI_", _env_nested_delimiter="__"
        )
