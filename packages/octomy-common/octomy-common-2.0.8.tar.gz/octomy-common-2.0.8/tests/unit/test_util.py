import logging
import octomy.db
import pprint

logger = logging.getLogger(__name__)

# fmt: off
configs = {
	"empty:":(
		{}
		,""
		,""
	)
	, "hello:":(
		{
			"db-hostname":"hello.com"
			,"db-port":1234
			,"db-username":"arnold"
			,"db-password":"secret123"
			,"db-database":"mydb"
		}
		,"F12F52B73358C297F47A80768ABDFADF20D021F6A20E9929178908F981B75FA1"
		,"postgres://arnold:secret123@hello.com:1234/mydb"
	)
}
# fmt: on

def test_db_get_config_hash():

	for name, pack in configs.items():
		logger.info(f"NAME:{name}")
		config, expected, _ = pack
		logger.info(f"config:{config}")
		logger.info(f"expected:{expected}")
		actual = octomy.db.get_config_hash(config)
		logger.info(f"actual:{actual}")
		assert actual == expected
	return True


def test_db_uri_to_and_from_config():
	for name, pack in configs.items():
		logger.info(f"NAME:{name}")
		expected_config, _, expected_uri = pack
		logger.info(f"expected_config:{expected_config}")
		logger.info(f"expected_uri:   {expected_uri}")
		actual_uri, actual_uri_err = octomy.db.db_uri_from_conf(expected_config, do_online=False)
		actual_config = octomy.db.db_uri_to_config(expected_uri, do_online=False)
		if None == actual_uri:
			logger.info(f"actual_uri_err={actual_uri_err}")
		else:
			assert actual_uri == expected_uri
			assert actual_config == expected_config

