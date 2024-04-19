import csv

import messages
from queries.cypherbuilder import QueryBuilder
from queries.typedefs import Properties
from csvcontentsmanager import csvContentsManager
# from dfcontentsmanager import dfContentsManager
import assetmodelutilities as amu
from queries.query import Neo4jQuery
import uuid
##json import pandas as pdf

#max_payload_size = 9500000

class FileProcessor():

    def __init__(self, filename, config, inline_query=False):
        self.filename = filename
        self.inline_query = inline_query

        self.primary_property = config.get_primary_property()
        self.add_system_properties = not config.get_no_system_properties()

        self.required_labels = config.get_required_labels()
        self.required_properties = config.get_required_properties_dict()
        self.unrequired_properties = config.get_unrequired_properties_list()
        self.unique_id_property = config.get_unique_id_property()
        self.creation_time_property = config.get_creation_time_property()
        self.update_time_property = config.get_update_time_property()
        self.header_mappings = config.get_header_mappings()
        self.default_data_type = config.get_default_data_type()

        self.label_alias = config.get_label_alias()
        self.node_alias = config.get_node_alias()
        self.from_node_alias = config.get_from_alias()
        self.from_label_alias = config.get_from_label_alias()
        self.to_node_alias = config.get_to_alias()
        self.to_label_alias = config.get_to_label_alias()
        self.relationship_alias = config.get_relationship_alias()
        self.ignore_nodes = config.get_ignore_nodes()

        self.separator = config.get_separator()
        self.def_path = config.get_default_path()
        self.validate_only = config.in_validation_mode()
        self.summarise = config.in_summary_mode()
        self.show_query = config.get_show_query()

        self.output_file = config.get_query_output()
        self.results_file = config.get_results_output()

        self.allow_blanks = config.get_allow_blanks()
        self.batch_rate = config.get_batch_rate()
        self.last_row = config.get_end_at()

        # Define special types that are used by the Neo4j importer
        # They are also used in Java asset model builder
        # Could add these to the config file at some point, but they are unlikely to change
        self.node_types = ['ID']
        self.from_types = ['START_ID']
        self.to_types = ['END_ID']
        self.relation_types = ['TYPE']
        self.label_types = ['LABEL', 'ALABEL']
        self.all_types = self.node_types + self.from_types + self.to_types + self.relation_types + self.label_types

    def get_label_lists(self, labels):
        unique_labels = []
        for label in list(set(labels)):
            for split_label in label.replace(',', ':').split(':'):
                unique_labels.append(split_label)
        label_list = []
        unwanted_label_list = []
        remove_label_list = []
        for label in unique_labels:
            if label:
                if not ('!'+label in self.required_labels or label.startswith('!') or label == '') or (label.startswith('!!')):
                    label_list.append(amu.remove_leading_chars(label, '!'))
                elif label.startswith('!'):
                    remove_label_list.append(amu.remove_leading_chars(label, '!'))
                else:
                    unwanted_label_list.append('!'+amu.remove_leading_chars(label, '!'))

        return list(set(label_list)), list(set(unwanted_label_list)), list(set(remove_label_list))

    def merge_labels(self, required_labels, unrequired_labels, remove_labels):
        merged_labels = [i for i in self.required_labels + required_labels if (not ('!' + i in unrequired_labels) and not (i in remove_labels) and not (i.startswith('!')))]
        return merged_labels

    def get_last_row(self, num_rows):
        if self.last_row < 0:
            last_row = num_rows
        else:
            last_row = min(num_rows, self.last_row)
        return last_row

    def split_node(self, value, property):
        split_node = value.split('::')
        if len(split_node) == 1:
            if property == '':
                key = self.primary_property
            else:
                key = property
            name = split_node[0]
        else:
            key = split_node[0]
            name = split_node[1]
        return key, name

    def determine_file_type(self, file_type):

        file_name = amu.find_file(self.def_path, self.filename)
        if file_name is None:
            return 'fnf', []

        match file_type:
            case 'csv':
                try:
                    with open(file_name, encoding='utf8') as csv_file:
                        csv_data = csv.reader(csv_file, delimiter=self.separator)
                        self.contents = csvContentsManager(csv_data, self.header_mappings, self.default_data_type)
                except:
                    try:
                        with open(file_name) as csv_file:
                            csv_data = csv.reader(csv_file, delimiter=self.separator)
                            self.contents = csvContentsManager(csv_data, self.header_mappings, self.default_data_type)
                    except:
                       return 'incorrect file format', []

## json            case 'json':
## json                with open(file_name, encoding='utf8') as json_file:
## json                    json_data = pdf.read_json(json_file)
## json                    self.contents = dfContentsManager(json_data.fillna('').convert_dtypes(), self.header_mappings, self.default_data_type)
            case _:
                pass

#        print(self.node_alias, self.node_types)
        num_node_columns = self.contents.get_column_count(self.node_alias, self.node_types)
#        print(self.from_node_alias, self.from_types)
        num_from_columns = self.contents.get_column_count(self.from_node_alias, self.from_types)
#        print(self.to_node_alias, self.to_types)
        num_to_columns = self.contents.get_column_count(self.to_node_alias, self.to_types)
#        print(self.relationship_alias, self.relation_types)
        num_relation_columns = self.contents.get_column_count(self.relationship_alias, self.relation_types)
#        print(num_node_columns, num_from_columns, num_to_columns, num_relation_columns)

        incomplete_rows = self.contents.get_incomplete_rows()
        if len(incomplete_rows) > 0:
            return 'incomplete row(s)', incomplete_rows

        # If there is a least one Node (including aliases) column, this could be a Node file
        if num_node_columns > 0:
            could_be_node = True
            if num_node_columns > 1:
                messages.warning_message(f'Multiple node columns found in ', f'{self.filename}')
        else:
            could_be_node = False

        # Check if there are at least one each of From, To and Relationship (including aliases) columns
        # If so, this could be a Relationship file
        if num_from_columns > 0 and num_to_columns > 0 and num_relation_columns > 0:
            could_be_relations = True
        else:
            could_be_relations = False

        if could_be_node:
            if could_be_relations:
                if self.ignore_nodes:
                    file_type = 'relationships'
                else:
                    file_type = 'both'
            else:
                file_type = 'nodes'
        else:
            if could_be_relations:
                file_type = 'relationships'
            else:
                file_type = 'neither'

        return file_type, []

    def process_node_file(self, start_from):

        # For each line in the file, build a cypher query to MERGE a node
        # Each query is added to a list of queries, which are returned to the caller. They are NOT actioned here

        num_data_rows = self.contents.get_row_count()
        node_columns = self.contents.get_column_numbers_list(self.node_alias, self.node_types)
        label_columns = self.contents.get_column_numbers_list(self.label_alias, self.label_types)
        property_columns = self.contents.get_other_column_numbers_list(self.node_alias + self.label_alias, self.all_types)

        queries = []

        num_rows = num_data_rows - start_from + 1
        this_row = start_from-1
        last_row = self.get_last_row(num_data_rows)
        property_ref = 'n'
        property_ref_dot = property_ref + '.'

        while this_row < last_row:
            wanted_labels, unwanted_labels, remove_labels = self.get_label_lists(self.contents.get_column_values_list(this_row, label_columns))
            labels = [i for i in self.required_labels if (not('!'+i in unwanted_labels) and not(i.startswith('!')))]
            new_labels = [i for i in wanted_labels if i not in labels]
            properties = self.contents.get_property_values_dict(this_row, property_columns, allow_blanks=self.allow_blanks)
            if len(self.required_properties) > 0:
                properties = {**self.required_properties, **properties}
            # Remove any properties we don't want
            for property in self.unrequired_properties:
                try:
                    properties.pop(property)
                except:
                    pass
            for k in list(properties):
                properties[property_ref_dot + k] = properties.pop(k)

            for node_name in self.contents.get_column_values_list_with_properties(this_row, node_columns, self.node_types):
                time_now = amu.get_formatted_time_now()
                node_value, node_property = list(node_name.items())[0]
                key, name = self.split_node(node_value, node_property)
                primary_property = {key: name}

                # Build a simple MERGE query using queries
                query_text = (QueryBuilder()
                              .merge()
                              .node(labels=labels, ref_name=property_ref, properties=Properties(primary_property))
                              )

                # Add in System properties if required
                if self.add_system_properties:
                    new_uuid = str(uuid.uuid4())
                    create_time = property_ref_dot + self.creation_time_property + '=datetime("' + time_now + '")'
                    id_property = property_ref_dot + self.unique_id_property
                    update_id = id_property + '= CASE WHEN ' + id_property + ' IS null THEN "' + new_uuid + '" ELSE ' + id_property + ' END,' +\
                                property_ref_dot + self.update_time_property + '=datetime("' + time_now + '")'
                    query_text = query_text.on_create().set_literal(create_time).set_literal(update_id)

                if len(new_labels) > 0:
                    query_text = query_text.set_labels(ref_name=property_ref, labels=new_labels)
                if len(remove_labels) > 0:
                    query_text = query_text.remove_literal(f'{property_ref}:{":".join(remove_labels)}')
                if len(properties) > 0:
                    query_text = query_text.set(properties=properties)

                query_text = query_text.toStr()

                query = Neo4jQuery('node', query_text, time_now, labels, new_labels, primary_property, properties)

                if self.validate_only and not self.summarise:
                    print(query.text)

                queries.append(query)

            this_row += 1
            messages.message_no_cr(f'Generating queries... {100 * (this_row - start_from + 1) / num_rows:.0f}%{chr(13)}')

        messages.message('', False)
        return queries

    def process_node_file_batch(self, start_from):

        # For each line in the file, build a cypher query to MERGE a node
        # Each query is added to a list of queries, which are returned to the caller. They are NOT actioned here

        num_data_rows = self.contents.get_row_count()
        node_columns = self.contents.get_column_numbers_list(self.node_alias, self.node_types)
        label_columns = self.contents.get_column_numbers_list(self.label_alias, self.label_types)
        property_columns = self.contents.get_other_column_numbers_list(self.node_alias + self.label_alias, self.all_types)

        queries = []

        num_rows = num_data_rows - start_from + 1
        this_row = start_from-1
        last_row = self.get_last_row(num_data_rows)
        dict_size = 0
        property_ref = 'n'
        property_ref_dot = property_ref + '.'
        payload_ref = 'payload'
        payload_ref_dot = payload_ref + '.'

        time_now = amu.get_formatted_time_now()

        # For best optimisation, we need to create a batch query for all the update with the same labels
        # So we will create a dictionary of queries based on the labels for each query
        # Since the dictionary key can't be a list, we will create a list (of lists) and use the index in that list as the key
        # When we have worked through all the input and grouped the queries by label combination, we will create the queries

        list_of_label_combinations = []
        query_dictionary = {}
        labels = [i for i in self.required_labels if (not (i.startswith('!')))]
        id_property = property_ref_dot + self.unique_id_property
        creation_property = property_ref_dot + self.creation_time_property

        while this_row < last_row:
            wanted_labels, unwanted_labels, remove_labels = self.get_label_lists(self.contents.get_column_values_list(this_row, label_columns))
            label_list = [i for i in labels if (not('!'+i in unwanted_labels))]
            new_labels = [i for i in wanted_labels if i not in label_list]

#            # Remove any unwanted labels (marked with '!' in the settings file)
            properties = self.contents.get_property_values_dict(this_row, property_columns, allow_blanks=self.allow_blanks)

            for node_name in self.contents.get_column_values_list_with_properties(this_row, node_columns, self.node_types):
                node_value, node_property = list(node_name.items())[0]
                key, name = self.split_node(node_value, node_property)
#                primary_property = {key: name}
                if len(self.required_properties) > 0:
                    properties = {**self.required_properties, **properties}
                # Remove any properties we don't want
                for property in self.unrequired_properties:
                    try:
                        properties.pop(property)
                    except:
                        pass
                properties[key] = name

                query_data = [properties, time_now]

                # So now we know all about this particular update. Let's put it in the query dictionary
                # We'll group these by unique combinations of labels and primary key type
                dictionary_key = [new_labels, key, label_list, remove_labels]
                try:
                    dictionary_index = list_of_label_combinations.index(dictionary_key)
                    query_dictionary[dictionary_index].append(query_data)
                except:
                    dictionary_index = len(list_of_label_combinations)
                    query_dictionary[dictionary_index] = [query_data]
                    list_of_label_combinations.append(dictionary_key)
                dict_size += 1

            this_row += 1
            messages.message_no_cr(f'Analysing file... {100 * (this_row - start_from + 1) / num_rows:.0f}%{chr(13)}')

        messages.message('', False)

        # Right, so now we have a dictionary of updates grouped by labels. Let's create the queries
        query_count = 0
        for new_labels, updates in query_dictionary.items():
            num_updates_for_this_label = len(updates)
            num_batches = int((num_updates_for_this_label-1)/self.batch_rate) + 1

            batch_num = 1
            while batch_num <= num_batches:
                if batch_num == num_batches:
                    # Last batch, so
                    batch_size = 1 + (num_updates_for_this_label-1) % self.batch_rate
                else:
                    batch_size = self.batch_rate

                this_size = 0
                payload = []
#                payload_len = 0
#                while this_size < batch_size and payload_len < max_payload_size:
                while this_size < batch_size:
                    # Combine all the update data...
                    update = updates[(batch_num-1)*self.batch_rate + this_size]
                    update_properties = update[0] or {}
                    if self.add_system_properties:
                        update_properties[self.update_time_property] = update[1]
                    payload.append(update_properties)
#                    payload_len += len(Properties(update_properties).format())
                    this_size += 1
                    query_count += 1

                formatted_payload = []
                property_count = 0
                for a_payload in payload:
                    formatted_payload.append(Properties(a_payload).format())
                    property_count += len(a_payload)

                # Build a MERGE query using queries
                node_labels = list_of_label_combinations[new_labels][2]
                remove_labels = list_of_label_combinations[new_labels][3]
                if list_of_label_combinations[new_labels][0]:
                    node_labels += list_of_label_combinations[new_labels][0]
                query_text = (QueryBuilder()
                              .unwind_list_as(formatted_payload, payload_ref)
                              .merge()
                              .node_batch(labels=list(set(node_labels)), ref_name=property_ref, properties=list_of_label_combinations[new_labels][1]+':'+payload_ref_dot+list_of_label_combinations[new_labels][1])
                              .set_literal(property_ref + ' += ' + payload_ref)
                              )
                if len(remove_labels) > 0:
                    query_text = query_text.remove_literal(f'{property_ref}:{":".join(remove_labels)}')
                if self.add_system_properties:
                    query_text = query_text.set_literal(id_property + '= CASE WHEN ' + id_property + ' IS null THEN randomUUID() ELSE ' + id_property + ' END')
                    query_text = query_text.set_literal(creation_property + '= CASE WHEN ' + creation_property + ' IS null THEN ' + property_ref_dot + self.update_time_property + ' ELSE ' + creation_property + ' END')

                query_text = query_text.toStr()
                query = Neo4jQuery('batch node', query_text, time_now, batch_size=this_size, property_count=property_count)
                queries.append(query)
                messages.message_no_cr(f'Generating queries... {100 * query_count / dict_size:.0f}%{chr(13)}')

                if self.validate_only and not self.summarise:
                    print(query.text)

                batch_num += 1

        messages.message('', False)
        return queries

    def process_relationship_file(self, start_from):

        # For each line in the file, build a cypher query to MERGE a relationship
        # Each query is added to a list of queries, which are returned to the caller. They are NOT actioned here

        num_data_rows = self.contents.get_row_count()
        from_columns = self.contents.get_column_numbers_list(self.from_node_alias, self.from_types)
        from_label_columns = self.contents.get_column_numbers_list(self.from_label_alias)
        to_columns = self.contents.get_column_numbers_list(self.to_node_alias, self.to_types)
        to_label_columns = self.contents.get_column_numbers_list(self.to_label_alias)
        relation_columns = self.contents.get_column_numbers_list(self.relationship_alias, self.relation_types)
        other_columns = self.from_node_alias + self.from_label_alias + self.to_node_alias + self.to_label_alias + self.relationship_alias
        property_columns = self.contents.get_other_column_numbers_list(other_columns, self.all_types)

        queries = []
        from_ref = 'from'
        relation_ref = 'rel'
        to_ref = 'to'
        relation_ref_dot = relation_ref + '.'

        num_rows = num_data_rows - start_from + 1
        this_row = start_from-1
        last_row = self.get_last_row(num_data_rows)
        while this_row < last_row:

            relationships = self.contents.get_column_values_list(this_row, relation_columns)
            properties = self.contents.get_property_values_dict(this_row, property_columns, relation_ref_dot, self.allow_blanks)
            # If there are multiple From or To nodes, create a relationship query for each combination
            for from_properties in self.contents.get_column_values_list_with_properties(this_row, from_columns, self.from_types):
                from_value, from_property = list(from_properties.items())[0]
                key, name = self.split_node(from_value, from_property)
                from_node = {key: name}
                required_from_labels, unrequired_from_labels, remove_from_labels = self.get_label_lists(self.contents.get_column_values_list(this_row, from_label_columns))
                from_labels = self.merge_labels(required_from_labels, unrequired_from_labels, remove_from_labels)
                for to_properties in self.contents.get_column_values_list_with_properties(this_row, to_columns, self.to_types):
                    to_value, to_property = list(to_properties.items())[0]
                    key, name = self.split_node(to_value, to_property)
                    to_node = {key: name}
                    required_to_labels, unrequired_to_labels, remove_to_labels = self.get_label_lists(self.contents.get_column_values_list(this_row, to_label_columns))
                    to_labels = self.merge_labels(required_to_labels, unrequired_to_labels, remove_to_labels)

                    # We need to create sets of updates that have the same label combinations, and relationship

                    # Build a MERGE query for the relationship(s)
                    for relationship in relationships:
                        for relation in relationship.split(':'):
                            if relation:

                                time_now = amu.get_formatted_time_now()
                                query_text = (QueryBuilder()
                                              .match()
                                              .node(labels=from_labels, ref_name=from_ref, properties=Properties(from_node))
                                              .match()
                                              .node(labels=to_labels, ref_name=to_ref, properties=Properties(to_node))
                                              .merge()
                                              .node(ref_name=from_ref)
                                              .related_to(label=relation, ref_name=relation_ref)
                                              .node(ref_name=to_ref)
                                              )

                                # Add in System properties
                                if self.add_system_properties:
                                    create_time = relation_ref_dot + self.creation_time_property + '=datetime("' + time_now + '")'
                                    update_time = relation_ref_dot + self.update_time_property + '=datetime("' + time_now + '")'
                                    query_text = query_text.on_create().set_literal(create_time).set_literal(update_time)

                                if len(properties) > 0:
                                    query_text = query_text.set(properties=properties)
                                query_text = query_text.toStr()
                                query = Neo4jQuery('relationship', query_text, time_now)

                                if self.validate_only and not self.summarise:
                                    print(query.text)

                                queries.append(query)

            this_row += 1
            messages.message_no_cr(f'Generating queries... {100 * (this_row - start_from + 1) / num_rows:.0f}%{chr(13)}')

        messages.message('', False)
        return queries

    def process_relationship_file_batch(self, start_from):

        # For each line in the file, build a cypher query to MERGE a relationship
        # Each query is added to a list of queries, which are returned to the caller. They are NOT actioned here

        num_data_rows = self.contents.get_row_count()
        from_columns = self.contents.get_column_numbers_list(self.from_node_alias, self.from_types)
        from_label_columns = self.contents.get_column_numbers_list(self.from_label_alias)
        to_columns = self.contents.get_column_numbers_list(self.to_node_alias, self.to_types)
        to_label_columns = self.contents.get_column_numbers_list(self.to_label_alias)
        relation_columns = self.contents.get_column_numbers_list(self.relationship_alias, self.relation_types)
        other_columns = self.from_node_alias + self.from_label_alias + self.to_node_alias + self.to_label_alias + self.relationship_alias
        property_columns = self.contents.get_other_column_numbers_list(other_columns, self.all_types)

        queries = []
        from_ref = 'from'
        relation_ref = 'rel'
        to_ref = 'to'
        relation_ref_dot = relation_ref + '.'
        payload_ref = 'payload'
        payload_ref_dot = payload_ref + '.'

        time_now = amu.get_formatted_time_now()

        # For best optimisation, we need to create a batch query for all the update with the same labels
        # So we will create a dictionary of queries based on the labels and relationships for each query
        # Since the dictionary key can't be a list, we will create a list (of lists) and use the index in that list as the key
        # When we have worked through all the input and grouped the queries by label and relationship combinations, we will create the queries

        list_of_combinations = []
        query_dictionary = {}
        dict_size = 0

        num_rows = num_data_rows - start_from + 1
        this_row = start_from-1
        last_row = self.get_last_row(num_data_rows)
        while this_row < last_row:
            relationships = self.contents.get_column_values_list(this_row, relation_columns)
            properties = self.contents.get_property_values_dict(this_row, property_columns, '', self.allow_blanks)
            # If there are multiple From or To nodes, create a relationship query for each combination
            for from_properties in self.contents.get_column_values_list_with_properties(this_row, from_columns, self.from_types):
                from_value, from_property = list(from_properties.items())[0]
                key, name = self.split_node(from_value, from_property)
                from_node = [key, name]
                required_from_labels, unrequired_from_labels, remove_from_labels = self.get_label_lists(self.contents.get_column_values_list(this_row, from_label_columns))
                from_labels = self.merge_labels(required_from_labels, unrequired_from_labels, remove_from_labels)
                for to_properties in self.contents.get_column_values_list_with_properties(this_row, to_columns, self.to_types):
                    to_value, to_property = list(to_properties.items())[0]
                    key, name = self.split_node(to_value, to_property)
                    to_node = [key, name]
                    required_to_labels, unrequired_to_labels, remove_to_labels = self.get_label_lists(self.contents.get_column_values_list(this_row, to_label_columns))
                    to_labels = self.merge_labels(required_to_labels, unrequired_to_labels, remove_to_labels)

                    # Build a MERGE query for the relationship(s)
                    for relationship in relationships:
                        for relation in relationship.split(':'):
                            if relation:

                                new_labels = [from_labels, to_labels, relation, from_node[0], to_node[0]]
                                query_data = [from_node[1], to_node[1], properties, time_now]

                                # So now we know all about this particular update. Let's put it in the query dictionary
                                try:
                                    dictionary_index = list_of_combinations.index(new_labels)
                                    query_dictionary[dictionary_index].append(query_data)
                                except:
                                    dictionary_index = len(list_of_combinations)
                                    query_dictionary[dictionary_index] = [query_data]
                                    list_of_combinations.append(new_labels)
                                dict_size += 1

            this_row += 1
            messages.message_no_cr(f'Analysing file... {100 * (this_row - start_from + 1) / num_rows:.0f}%{chr(13)}')

        messages.message('', False)

        # Right, so now we have a dictionary of updates grouped by labels. Let's create the queries
        query_count = 0
        for from_to_labels, updates in query_dictionary.items():
            num_updates_for_this_label = len(updates)
            num_batches = int((num_updates_for_this_label - 1) / self.batch_rate) + 1
            from_labels = list_of_combinations[from_to_labels][0]
            to_labels = list_of_combinations[from_to_labels][1]
            relationship = list_of_combinations[from_to_labels][2]
            from_key = list_of_combinations[from_to_labels][3]
            to_key = list_of_combinations[from_to_labels][4]

            batch_num = 1
            while batch_num <= num_batches:
                if batch_num == num_batches:
                    # Last batch, so
                    batch_size = 1 + (num_updates_for_this_label - 1) % self.batch_rate
                else:
                    batch_size = self.batch_rate

                this_size = 0
                payload = []
                while this_size < batch_size:
                    # Combine all the update data...
                    update = updates[(batch_num - 1) * self.batch_rate + this_size]
                    update_properties = update[2] or {}  # In case update_properties[2] is {}
                    update_properties[from_ref] = update[0]
                    update_properties[to_ref] = update[1]
                    if self.add_system_properties:
                        update_properties[self.update_time_property] = update[3]
                    payload.append(update_properties)
                    this_size += 1
                    query_count += 1

                formatted_payload = []
                for a_payload in payload:
                    formatted_payload.append(Properties(a_payload).format())

                # Build a MERGE query using queries
                from_property = " {" + from_key + ":" + payload_ref_dot + from_ref + "}"
                to_property = " {" + to_key + ":" + payload_ref_dot + to_ref + "}"
                create_time = relation_ref_dot + self.creation_time_property + '=datetime("' + time_now + '")'
                update_time = relation_ref_dot + self.update_time_property + '=datetime("' + time_now + '")'

                query_text = (QueryBuilder()
                              .unwind_list_as(formatted_payload, payload_ref)
                              .match()
                              .node(labels=from_labels, ref_name=from_ref, properties_literal=from_property)
                              .match()
                              .node(labels=to_labels, ref_name=to_ref, properties_literal=to_property)
                              .merge()
                              .node(ref_name=from_ref)
                              .related_to(label=relationship, ref_name=relation_ref)
                              .node(ref_name=to_ref)
                              )

                if self.add_system_properties:
                    query_text = query_text.on_create().set_literal(create_time)

                query_text = query_text.set_literal(relation_ref + ' += ' + payload_ref)

                if self.add_system_properties:
                    query_text = query_text.set_literal(update_time)

                query_text = query_text.remove_literal(relation_ref_dot + from_ref + ', ' + relation_ref_dot + to_ref)
                query_text = query_text.toStr()

                query = Neo4jQuery('batch relationship', query_text, time_now, batch_size=this_size)

                if self.validate_only and not self.summarise:
                    print(query.text)

                queries.append(query)
                messages.message_no_cr(f'Generating queries... {100 * query_count / dict_size:.0f}%{chr(13)}')

                batch_num += 1

        messages.message('', False)
        return queries

    def process_cypher_file(self, start_from):

        queries = []
        try:
            cypher_file_name = amu.find_file(self.def_path, self.filename)
            cypher_file = open(cypher_file_name, 'r', encoding='UTF8')
            cypher_list = list(cypher_file)
            file_queries = 0
            next_query = ''
            cypher_file_size = len(cypher_list)
            entry_count = 0
            while entry_count < cypher_file_size:
                this_entry = cypher_list[entry_count].strip()
                if not this_entry.startswith('#') and not this_entry == '\n':
                    next_query += this_entry + '\n'
                    if not this_entry.endswith(',') and not this_entry.endswith('\\'):
                        while next_query.endswith('\n'):
                            next_query = next_query[0:-1]
                        query = Neo4jQuery('cypher', next_query.replace('\\', '').strip())
                        next_query = ''
                        if self.validate_only and not self.summarise:
                            print(query.text)
                        queries.append(query)
                        file_queries += 1
                entry_count += 1

            # Process any leftover query at the end of the file
            # This shouldn't normally happen, but will if the last entry ends with a comma or backslash
            # Any trailing backslash is removed, so the query may be OK but will be missing any continuation clause(s)
            # But a trailing comma will be left - result is a query that will generate an error if executed!
            # This is done intentionally as the query in the input file is incomplete
            if next_query != '':
                query = Neo4jQuery('cypher', next_query[0:-1].replace('\\', '').strip())
                if self.validate_only and not self.summarise:
                    print(query.text)
                queries.append(query)
                file_queries += 1

            cypher_file.close()
        except:
            print(f'{self.filename} not found')

        return queries

    def process_query_list(self, start_from):

        queries = []
        query = Neo4jQuery('query', self.filename)
        if self.validate_only and not self.summarise:
            print(query.text)
        queries.append(query)
        return queries

    def get_filename(self):
        return self.filename

    def is_inline_query(self):
        return self.inline_query
