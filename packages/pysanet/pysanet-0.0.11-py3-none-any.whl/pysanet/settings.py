from functools import cached_property

from pydantic import BaseModel, HttpUrl, SecretStr, computed_field
from pydantic_settings_toml import TomlSettings


class SanetSettings(BaseModel):
    base_url: HttpUrl
    auth_token: SecretStr
    api_version: str = ""
    api_endpoint_path: str = "rest_api/"
    portal_path: str = "web/page/"

    @computed_field
    @cached_property
    def api_url(self) -> HttpUrl:
        url = HttpUrl(f"{self.base_url}{self.api_endpoint_path}{self.api_version}")
        return url

    @computed_field
    @cached_property
    def portal_url(self) -> HttpUrl:
        url = HttpUrl(f"{self.base_url}{self.portal_path}")
        return url


class AppSettings(TomlSettings):
    pysanet: SanetSettings | None = None
