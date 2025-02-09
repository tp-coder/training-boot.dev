# Export CSV
# Doc2Doc should be able to prepare and export a CSV file of whatever data you input. 
# Comma-Separated Values are a ubiquitous text format that allows for information to 
# be structured in a table. There is usually a header row, followed by data rows. Within 
# rows, items are separated by commas.
# 
# Assignment
# Complete the get_csv_status function. It should use a match case statement to select the 
# correct response depending on the status of the export operation. Create functions to handle 
# each operation as follows:
# 
# PENDING:
# Return a tuple with the string "Pending..." and the data converted from a list of lists of anything, 
# to a list of lists of strings. Try to use nested map functions to convert the data items into strings. 
# Remember to convert from a map object back into a list.
# 
# PROCESSING:
# Return a tuple with the string "Processing..." and the data converted from a list of lists of strings 
# into one string in CSV format.
#  - For each list of strings, combine the strings with join with commas inbetween to form a row.
#  - For each row string, combine the strings with join with newlines "\n" inbetween to form a table.
#
# SUCCESS:
# Return a tuple with the string "Success!" and simply return the data as is.
# 
# FAILURE:
# Return a tuple with the string "Unknown error, retrying..." and the data after it has been prepared 
# and processed into a CSV string, by combining the steps for Pending and Processing.
# 
# Any Other Status:
# If the input status is none of the above, raise an Exception with the string "unknown export status".

from enum import Enum

class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4

def pending(data):
    converted_data = list(
        map(
            lambda row: list(map(str, row)),
            data
        )
    )
    return ("Pending...", converted_data)

def processing(data):
    row_strings = [",".join(row) for row in data]
    csv_string = "\n".join(row_strings)
    return ("Processing...", csv_string)


def failure(data):
    pending_data = pending(data)
    processing_data = processing(pending_data[1])
    return ("Unknown error, retrying...", processing_data[1])

def sucess(data):
    return ("Success!", data)

def get_csv_status(status, data):
    match (status):
        case (CSVExportStatus.PENDING):
            return pending(data)
        case (CSVExportStatus.PROCESSING):
            return processing(data)
        case (CSVExportStatus.SUCCESS):
            return sucess(data)
        case (CSVExportStatus.FAILURE):
            return failure(data)
        case _:
            raise Exception("unknown export status")
        