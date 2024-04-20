from pathlib import Path
import relationalai as rai

import pytest
import random
from gentest.exec import path_to_slug, validate_query_results
from relationalai.clients import config as cfg

test_case_dir = Path(__file__).parent / "test_cases"
test_case_files = [path for path in test_case_dir.rglob("*.py")]

# This test absorbs the latency of the engine being created
def test_engine_creation_dummy(engine_config: cfg.Config):
    pass

def randomize(name: str) -> str:
    return f"{name}_{random.randint(1000000000, 9999999999)}"


@pytest.mark.parametrize(
    "file_path", test_case_files, ids=lambda path: path_to_slug(path, test_case_dir)
)
def test_snapshots(file_path: Path, snapshot, engine_config: cfg.Config):
    # Clone the engine_config to ensure a fresh configuration for each test case
    local_config = engine_config.clone()

    test_name = file_path.stem
    db_name = randomize(test_name)
    validate_query_results(
        file_path,
        snapshot,
        {
            "name": db_name,
            "config": local_config,
        }
    )
    try:
        provider = rai.Resources(config=local_config)
        provider.delete_graph(db_name)
    except Exception as e:
        print(f"Failed to delete graph {db_name}: {e}")
        pass