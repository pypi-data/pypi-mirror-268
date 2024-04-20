import logging
import os
import pprint
import datetime
import pathlib

logger = logging.getLogger(__name__)




class termcol:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	RED = '\u001b[31m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def random_token(length=10):
	alphabet = string.ascii_letters + string.digits
	return "".join(random.choice(alphabet) for i in range(length))


def human_bytesize(bytes: int, max: int = -1):
	if bytes == 0:
		return "0 bytes"
	if bytes < 0:
		return "negative bytes (error)"
	# fmt: off
	KiB=1024
	periods = [
		("PiB", KiB*KiB*KiB*KiB*KiB),
		("TiB", KiB*KiB*KiB*KiB),
		("GiB", KiB*KiB*KiB),
		("MiB", KiB*KiB),
		("KiB", KiB),
		("bytes", 1)
	]
	# fmt: on

	strings = []
	ct: int = 0
	for period_name, period_bytes in periods:
		if bytes > period_bytes:
			period_value, bytes = divmod(bytes, period_bytes)
			# has_s = "s" if period_value > 1 else ""
			# strings.append("%s %s%s" % (period_value, period_name, has_s))
			strings.append(f"{period_value} {period_name}")
			ct += 1
			if max >= 0 and ct > max:
				break
	return ", ".join(strings)  # + f"({td_object}, {bytes})"



def human_delta(td_object: datetime.timedelta, max: int = 0):
	ms = int(td_object.total_seconds() * 1000)
	if ms == 0:
		return "0 ms"
	sign = ""
	if ms < 0:
		ms = -ms
		sign = "-"
	# fmt: off
	periods = [
		("year",  1000 * 60 * 60 * 24 * 365),
		("month", 1000 * 60 * 60 * 24 * 30),
		("day",   1000 * 60 * 60 * 24),
		("hr",    1000 * 60 * 60),
		("min",   1000 * 60),
		("sec",   1000),
		("ms", 1)
	]
	# fmt: on

	strings = []
	ct: int = 0
	for period_name, period_ms in periods:
		if ms > period_ms:
			period_value, ms = divmod(ms, period_ms)
			# has_s = "s" if period_value > 1 else ""
			# strings.append("%s %s%s" % (period_value, period_name, has_s))
			strings.append(f"{period_value} {period_name}")
			ct += 1
			if max > 0 and ct > max:
				break
	return sign + ", ".join(strings)  # + f"({td_object}, {ms})"




def generate_tree(directory, prefix=''):
	tree_str = ""
	files = sorted(os.listdir(directory))
	for i, file in enumerate(files):
		path = os.path.join(directory, file)
		if os.path.isdir(path):
			tree_str += f"{prefix}{'├' if i < len(files) - 1 else '└'}─ {termcol.BLUE}{file}{termcol.ENDC}\n"
			extension = '│  ' if i < len(files) - 1 else '    '
			tree_str += generate_tree(path, prefix=prefix + extension)
		else:
			bytesize = human_bytesize(os.path.getsize(path), 0)
			tree_str += f"{prefix}{'├' if i < len(files) - 1 else '└'}─ {termcol.GREEN}{file}{termcol.ENDC} [{bytesize}]\n"
	return tree_str

def tree(directory):
	return f".\n{generate_tree(directory)}"



def get_package_relative_dir(do_debug=True):
	path = pathlib.Path(__file__).resolve()
	logger.info(f"get_package_relative_dir file: '{path}' is file: {path.is_file()}")
	path = path.parent
	logger.info(f"get_package_relative_dir path: '{path}' is dir: {path.is_dir()}")
	if do_debug:
		logger.info(f"\n{tree(path)}")
	return path

