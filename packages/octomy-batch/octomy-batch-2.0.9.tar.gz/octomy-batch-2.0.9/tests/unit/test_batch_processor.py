import logging
import octomy.batch
import octomy.db
import pytest
import os
import pathlib


logger = logging.getLogger(__name__)



@pytest.mark.asyncio
async def test_batch_processor():
	config = {
	  'db-hostname': os.environ.get("TEST_DB_HOSTNAME")
	, 'db-port':     os.environ.get("TEST_DB_PORT")
	, 'db-database': os.environ.get("TEST_DB_DATABASE")
	, 'db-username': os.environ.get("TEST_DB_USERNAME")
	, 'db-password': os.environ.get("TEST_DB_PASSWORD")
	}
	dbc, err = octomy.db.get_database(config, )
	assert dbc, err
	assert not err, err
	await dbc.state(do_online = True)
	dbc.register_query_dir("data/sql", do_preload = True, do_debug = True)

	bp = octomy.batch.Processor(config, dbc, do_debug = False)
	await dbc.state(do_online = True)
	dbc.preload_queries(do_debug = True)


def get_package_data_dir():
	path = pathlib.Path(__file__).resolve()
	logger.info(f"get_package_data_dir file: '{path}' is file: {path.is_file()}")
	path = path.parent
	logger.info(f"get_package_data_dir path: '{path}' is dir: {path.is_dir()}")

def _test_path():
	logger.info("A")
	get_package_data_dir()
	logger.info("B")
	bp = octomy.batch.Processor(config=dict(), dbc=None)
	logger.info("C")
	
