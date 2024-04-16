import argparse
import os
import json


def load_and_serialize_log(logfile_path):
    with (open(logfile_path, 'r') as file):
        sandbox_indicator = "Sandbox logs:"
        activity_log_indicator = "Activities log:"
        trade_history_log_indicator = "Trade History:"

        linenum = 0
        sandbox_start, sandbox_end, trade_history_start = 0, 0, 0
        lines = file.readlines()
        for line in lines:
            if sandbox_indicator in line:
                sandbox_start = linenum + 1
            elif activity_log_indicator in line:
                sandbox_end = linenum
            elif trade_history_log_indicator in line:
                trade_history_start = linenum + 1
            linenum += 1
        sandbox_str = '[' + ''.join(lines[sandbox_start:sandbox_end]) + ']'
        trade_history_str = ''.join(lines[trade_history_start:linenum])

        # Serialize to Sandbox History
        # with open("sandbox.json", 'w') as sandbox_json_file:
        #     sandbox_json = json.loads(sandbox_str)
        #     json.dump(sandbox_json, sandbox_json_file, indent=4)

        # Serialize to trade history
        with open("../trade_history.json", 'w') as trade_history_json_file:
            trade_history_json = json.loads(trade_history_str)
            json.dump(trade_history_json, trade_history_json_file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Parse IMC prosperity log file into json")
    parser.add_argument("file_path", type=str, help="Path to the file to be read.")
    args = parser.parse_args()
    # Read and print the file content
    load_and_serialize_log(args.file_path)


if __name__ == "__main__":
    main()