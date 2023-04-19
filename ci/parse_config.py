import json
import sys


def main():
    key = sys.argv[1]

    with open("ci/config.json") as config_file:
        config = json.load(config_file)

    if key == "user_id":
        print(config["user_id"])
    elif key == "suite_id":
        print(config["suite_id"])
    elif key == "docker_tag":
        print(config["docker_tag"])
    else:
        print(json.dumps(config["testcases"]))


if __name__ == "__main__":
    main()
