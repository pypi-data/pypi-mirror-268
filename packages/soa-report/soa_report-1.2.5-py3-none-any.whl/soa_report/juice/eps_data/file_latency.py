"""
Created on November 2023

@author: Ricardo Valles (ESAC)

This file includes a method to get data latency

Note: this module comes from OSVE

"""

import math
import logging


def get_file_latency(input_data, store_acc_col, downlink_acc_col):
    last_store_acc_value = 0.0
    last_downlink_acc_value = 0.0
    closed_files = []
    downlinking_file_idx = -1

    times = []
    latencies = []
    sizes = []

    for idx in range(len(input_data["datetime (UTC)"])):
        store_acc_value = input_data[store_acc_col][idx]
        downlink_acc_value = input_data[downlink_acc_col][idx]
        date = input_data["datetime (UTC)"][idx]

        if store_acc_value > last_store_acc_value:

            # A file has been closed
            file_size = store_acc_value - last_store_acc_value
            closed_file = {
                "idx": idx,
                "closed_date": date,
                "size": file_size,
                "downlinked": 0,
                "downlink_date": None
            }
            closed_files.append(closed_file)
            logging.debug(store_acc_col + " File " + str(idx) + " closed at " + str(date) + " with size " + str(file_size) + " Gbits")

        if downlink_acc_value > last_downlink_acc_value:

            if downlinking_file_idx < 0:
                downlinking_file_idx = 0

            downlinked_size = downlink_acc_value - last_downlink_acc_value

            while downlinked_size > 0:

                downlinking_file = closed_files[downlinking_file_idx]
                pending = downlinking_file["size"] - downlinking_file["downlinked"]

                if pending > downlinked_size:
                    downlinking_file["downlinked"] += downlinked_size
                    downlinked_size = 0.0

                else:
                    downlinked_size -= pending
                    downlinking_file["downlinked"] = downlinking_file["size"]
                    downlinking_file["downlink_date"] = date

                    latency = math.ceil((date - downlinking_file["closed_date"]).total_seconds() / (24 * 3600))
                    logging.debug(store_acc_col + " File " + str(downlinking_file["idx"]) + " downlinked at " + str(date) + " latency: " + str(latency))

                    times.append(downlinking_file["closed_date"])
                    latencies.append(latency)
                    sizes.append(downlinking_file["size"])

                    downlinking_file_idx += 1

        last_store_acc_value = store_acc_value
        last_downlink_acc_value = downlink_acc_value

    return times, latencies, sizes
