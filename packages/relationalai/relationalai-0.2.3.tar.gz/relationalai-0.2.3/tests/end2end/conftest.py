import os
import random
import pytest
import relationalai as rai
from relationalai.clients import config as cfg


@pytest.fixture(scope="session")
def engine_config():
    # If there's a local config file, use it, including
    # the engine specified there.
    config = cfg.Config()
    if config.file_path is not None:
        yield config
        return

    # Otherwise, create a new engine and delete it afterwards.
    random_number = random.randint(1000000000, 9999999999)
    engine_name = f"pyrel_test_{random_number}"

    config = make_config(engine_name)

    sf_compute_pool = os.getenv("SF_TEST_COMPUTE_POOL", config.get("compute_pool", ""))

    print(f"Creating engine {engine_name}")
    provider = rai.Resources(config=config)
    provider.create_engine(name=engine_name, size="XS", pool=sf_compute_pool)

    yield config

    print(f"Deleting engine {engine_name}")
    provider.delete_engine(engine_name)


def make_config(engine_name: str) -> cfg.Config:
    cloud_provider = os.getenv("RAI_CLOUD_PROVIDER")

    match cloud_provider:
        case None:
            raise ValueError("RAI_CLOUD_PROVIDER must be set")
        case "azure":
            client_id = os.getenv("RAI_CLIENT_ID")
            client_secret = os.getenv("RAI_CLIENT_SECRET")
            if client_id is None or client_secret is None:
                raise ValueError(
                    "RAI_CLIENT_ID, RAI_CLIENT_SECRET must be set if RAI_CLOUD_PROVIDER is set to 'azure'"
                )
            # Running against prod
            return cfg.Config(
                {
                    "platform": "azure",
                    "host": "azure.relationalai.com",
                    "port": "443",
                    "region": "us-east",
                    "scheme": "https",
                    "client_credentials_url": "https://login.relationalai.com/oauth/token",
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "engine": engine_name,
                }
            )
        case "snowflake":
            sf_username = os.getenv("SF_TEST_ACCOUNT_USERNAME")
            sf_password = os.getenv("SF_TEST_ACCOUNT_PASSWORD")
            sf_account = os.getenv("SF_TEST_ACCOUNT_NAME")
            sf_warehouse = os.getenv("SF_TEST_WAREHOUSE_NAME")
            sf_app_name = os.getenv("SF_TEST_APP_NAME")
            sf_compute_pool = os.getenv("SF_TEST_COMPUTE_POOL")
            if sf_username is None or sf_password is None:
                raise ValueError(
                    "SF_TEST_ACCOUNT_USERNAME, SF_TEST_ACCOUNT_PASSWORD, SF_TEST_ACCOUNT_NAME must be set if RAI_CLOUD_PROVIDER is set to 'snowflake'"
                )
            return cfg.Config(
                {
                    "platform": "snowflake",
                    "user": sf_username,
                    "password": sf_password,
                    "account": sf_account,
                    "role": "rai_integration_consumer",
                    "warehouse": sf_warehouse,
                    "rai_app_name": sf_app_name,
                    "engine": engine_name,
                    "compute_pool": sf_compute_pool,
                }
            )
        case _:
            raise ValueError(f"Unsupported cloud provider: {cloud_provider}")
