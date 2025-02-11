# Complete the create_html_table function. It takes a list of lists of strings, 
# data_rows, and returns a function, create_table_headers. create_table_headers 
# should take a list of strings, headers, and convert them into the header row of 
# the table, then return the complete HTML table as a string without any added 
# whitespace or indentation.
#
# Use the provided functions to complete the create_html_table function. Within the create_table_headers function:
#
# 1. Access the nonlocal rows string.
# 2. Accumulate the strings in the headers list as header cells in a single table row.
# 3. Add the row of headers to the beginning of the rows string.
# 4. Add the final tag, "table", around all of the rows.
# 5. Return one single string containing the HTML table.

from functools import reduce

def create_tagger(tag):
    def tagger(content):
        return f"<{tag}>{content}</{tag}>"
    return tagger

def create_accumulator(tagger):
    def accumulate(items):
        return reduce(lambda acc, item: acc + tagger(item), items, "")
    return accumulate

tag_data = create_tagger("td")
tag_header = create_tagger("th")
tag_row = create_tagger("tr")
tag_table = create_tagger("table")

accumulate_data_cells = create_accumulator(tag_data)
accumulate_rows = create_accumulator(tag_row)
accumulate_headers = create_accumulator(tag_header)

# don't touch above this line

def create_html_table(data_rows):
    rows = accumulate_rows(map(accumulate_data_cells, data_rows))

    def create_table_headers(headers):
        nonlocal rows

        header_row = tag_row(accumulate_headers(headers))
        rows = header_row + rows
        table = tag_table(rows)

        return table

    return create_table_headers

Data_Rows= [['Scooby Doo', 'Lassie'], ['Blue', 'Wishbone']]
Headers = ['Cartoon TV Dogs', 'Real TV Dogs']
create_html = create_html_table(Data_Rows)(Headers)
print(create_html)