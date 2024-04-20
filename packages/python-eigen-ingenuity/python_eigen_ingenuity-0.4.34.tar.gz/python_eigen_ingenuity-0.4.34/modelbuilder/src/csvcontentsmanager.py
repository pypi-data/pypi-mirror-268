import assetmodelutilities as amu

class csvContentsManager:

    # Manages the contents of a .CSV file
    # Returns the data requested by the Processor classes

    def __init__(self, csv_data, header_mappings, default_data_type):
        file_headers = next(csv_data)
        header_names = [(header_mappings[i.split(':')[0]] if i.split(':')[0] in header_mappings.keys() else i.split(':')[0]).replace('\ufeff', '') for i in file_headers]
        self.header_names = [amu.validate_property(i) for i in header_names]
        self.header_types = [i.split(':')[1] if len(i.split(':')) > 1 else default_data_type for i in file_headers]
        self.headers = [self.header_names[i].split(':')[0] + ':' + self.header_types[i] if self.header_types[i] != '' else self.header_names[i] + ':' + j if j != '' else self.header_names[i] for i, j in enumerate(self.header_types)]
        self.data_list = list(csv_data)
        # Remove any blank lines
        while [] in self.data_list:
            self.data_list.remove([])

    def get_row_count(self):
        return len(self.data_list)

    def get_column_count(self, column_name, type_list=[]):
        # Find the number of columns in the files whose heading is in the provided list
        return len(self.get_column_numbers_list(column_name, type_list))

    def get_column_numbers_list(self, column_name, type_list=[]):
        # Return a List containing the column numbers for each column in the given list of column names
        if not(isinstance(column_name, list)):
            name_list = [column_name]
        else:
            name_list = column_name
        column_list = [i for i, j in enumerate(self.header_names) if j in name_list or self.header_types[i] in type_list]
        return column_list

    def get_other_column_numbers_list(self, column_name, type_list=[]):
        # Return a List containing the column numbers for each column NOT in the given list of column names
        if not(isinstance(column_name, list)):
            name_list = [column_name]
        else:
            name_list = column_name
        column_list = [i for i, j in enumerate(self.header_names) if not(j in name_list or self.header_types[i] in type_list)]
        return column_list

    def get_incomplete_rows(self):
        num_headers = len(self.headers)
        incomplete_rows = []
        row_count = 0
        for a_row in self.data_list:
            row_count += 1
            if len(a_row) < num_headers:
                incomplete_rows.append(row_count)
        return incomplete_rows

    def get_column_values(self, row_number, column_numbers, delimiter=''):
        # This one is not currently used
        # Return the values in the given row, for the columns in the provided list (skipping empty values)
        # Returned as string, with an optional delimiter between values
        this_row = self.data_list[row_number]
        columns = delimiter.join([this_row[column] for column in column_numbers if this_row[column]])
        return columns

    def get_column_values_list(self, row_number, column_numbers):
        # Return the values in the given row, for the columns in the provided list (skips empty values)
        # Returned as a List (of strings)
        # Also validate the returned values to ensure they are legal Cypher names
        this_row = self.data_list[row_number]
        columns_list = [amu.validate_labels_and_relationships([this_row[i]]) for i in column_numbers if len(this_row[i]) > 0]
        return columns_list

    def get_column_values_list_with_properties(self, row_number, column_numbers, node_types):
        # Return the values in the given row, for the columns in the provided list (skips empty values)
        # Returned as a List (of strings)
        this_row = self.data_list[row_number]
#        columns_list = [this_row[i] for i in column_numbers if len(this_row[i]) > 0]
        properties_list = [{this_row[i]:self.header_names[i]} if self.header_types[i] in node_types else {this_row[i]: ''} for i in column_numbers if len(this_row[i])]
        return properties_list

    def get_property_values(self, row_number, column_numbers):
        # This one is not currently used
        # Return key:values pairs from the given row, for the columns in the provided list (skips empty values)
        # Returned as a comma separated string e.g. 'key1:value1, key2:value2'
        # Treat everything as a string here (using " as a delimiter). Actual data types will be determined later - see queries.typedefs.py
        delimiter = '"'
        this_row = self.data_list[row_number]
        columns = ','.join([self.headers[column] + ':' + delimiter + this_row[column] + delimiter for column in column_numbers if this_row[column]])
        return columns

    def get_property_values_dict(self, row_number, column_numbers, prefix='', allow_blanks=False):
        # Return key:values pairs from the given row, for the columns in the provided list (skips empty values)
        # Returned as a Dict (assumes all columns are unique (which they should be!))
        this_row = self.data_list[row_number]
        this_dict = {prefix + self.headers[column]: this_row[column] for column in column_numbers if this_row[column] or allow_blanks}
        return this_dict
