import time
from cawdrey.level_dict import LevelDict

import json

def benchmark(dict_class="dict"):
	if dict_class == "level":
		data = LevelDict("test_dict.ld")
	else:
		data = dict()

	start_time = time.time()

	# Add 150000 keys to the dictionary.
	for i in range(50000):
		data["cat" + str(i)] = str(i)
		data["ca" + str(i)] = str(i)
		data["c" + str(i)] = str(i)

	# Add tested key last.
	data["cat"] = "100"

	print(f"{time.time() - start_time:f}")

	start_time = time.time()

	# Loop up the key that was added last to the dictionary.
	for i in range(1000):
		if "cat" not in data:
			break

	print(f"{time.time() - start_time:f}")

	start_time = time.time()

	if dict_class == "dict":
		with open("test_dict.json", "w") as fp:
			json.dump(data, fp)

		del data

		with open("test_dict.json") as fp:
			data = json.load(fp)

	elif dict_class == "level":
		data.db.close()
		data = LevelDict("test_dict.ld")


	# Loop up the key that was added last to the dictionary.
	for i in range(1000):
		if "cat" not in data:
			break

	print(f"{time.time() - start_time:f}")

	#
	# if dict_class == "level":
	# 	data = LevelDict("test_dict.ld")
	# else:
	# 	data = dict()
	#
	# # Add tested key first.
	# data["cat"] = 100
	#
	# # Add 150000 keys to the dictionary.
	# for i in range(50000):
	# 	data["cat" + str(i)] = i
	# 	data["ca" + str(i)] = i
	# 	data["c" + str(i)] = i
	#
	# start_time = time.time()
	#
	# # Loop up the key that was added first to the dictionary.
	# for i in range(10000000):
	# 	if "cat" not in data:
	# 		break
	#
	# print(f"{time.time() - start_time:f}")

# print("Normal Dict")
# benchmark("dict")
#
# print("LevelDict")
# benchmark("level")
#
# data = LevelDict("test_dict.ld")
# data["foo"] = "bar"
# assert "foo" in data
#
# print("JSON")
# start_time = time.time()
# for i in range(10000000):
# 	json.loads("123.456")
# print(f"{time.time() - start_time:f}")
#
# print("Casting")
# start_time = time.time()
# for i in range(10000000):
# 	float("123.456")
# print(f"{time.time() - start_time:f}")


from cawdrey.level_dict import TypedLevelDict


class MyDict(TypedLevelDict[str, int]):
	key_type = str
	value_type = int
