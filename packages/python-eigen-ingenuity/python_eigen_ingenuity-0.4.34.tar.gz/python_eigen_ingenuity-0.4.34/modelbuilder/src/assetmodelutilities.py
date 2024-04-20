from pathlib import Path
import datetime
from datetime import timezone
import re

def find_file(path, filename):
    # try the provided path file first, then with the current path. Otherwise, return None to indicate file not found
    if Path(path + filename).is_file():
        full_name = path + filename
    elif Path(filename).is_file():
        full_name = filename
    else:
        full_name = None
    return full_name

def get_formatted_time_now():
#    now = datetime.datetime.now(pytz.timezone('Europe/Oslo')).strftime("%Y-%m-%dT%H:%M:%S.%f[%z]")
    now = datetime.datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    return now

def get_formatted_time_now_noms():
    now = datetime.datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")
    return now

def get_formatted_future_time():
    future = datetime.datetime(2199, 12, 31).strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    return future

def get_time_for_filename():
    now = datetime.datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H-%M-%S-%f")[0:-3]
    return now

def remove_leading_chars(string, chars):
    if string:
        while string[0] in chars:
            string = string[1:]
    return string

def validate(input, prefix = ''):
    output = f'{prefix}{input}'
    if input:
        if ''.join(re.findall("[A-Za-z0-9_]", input)) != input or ''.join(re.findall("[A-Za-z]", input[0])) != input[0]:
            output = f'{prefix}`{input.replace("`","")}`'
        return output

def validate_property(typed_property):
    validated = ''
    property_name = typed_property.split(':')[0]
    if property_name:
        validated += validate(property_name)
        try:
            validated += ':' + typed_property.split(':')[1]
        except:
            pass
    else:
        validated = typed_property

    return validated

def validate_properties(properties):
    validated = {}
    unwanted = []
    if properties:
        for property in properties:
            for prop in property.strip().split(','):
                split_prop = prop.replace('=', ':').split(':')
##                print(f'vp SP: {split_prop}')
                valid_key = validate(remove_leading_chars(split_prop[0], '!'))
                try:
                    validated[valid_key] = split_prop[1]
                except:
                    unwanted.append(valid_key)

    return validated, unwanted

def validate_labels_and_relationships(label_list):
    validated = ''
    if label_list:
        required = []
        unwanted = []
        override = []
        for labels in label_list:
            for label in labels.replace(':', ',').split(','):
                if label:
                    if label.startswith('!!'):
                        override.append(validate(label[2:].strip(), ''))
                    elif label.startswith('!'):
                        unwanted.append(validate(label[1:].strip(), ''))
                    else:
                        required.append(validate(label.strip(), ''))

        combined = [':!!'+i for i in override if i not in unwanted and i not in required]
        combined += [':!'+i for i in unwanted if i not in override and i not in required]
        combined += [':'+i for i in required if i not in override and i not in unwanted]
        validated = ''.join(combined)

    return validated

def combine_required_labels(config_labels, override_labels):
    valid_config_labels = validate_labels_and_relationships(config_labels)[1:].split(':')
    valid_override_labels = validate_labels_and_relationships(override_labels)[1:].split(':')
    required_labels = [i for i in valid_config_labels if (not(i.startswith('!') and ('!'+i not in valid_config_labels)) and ('!'+i not in valid_override_labels))] + [i for i in valid_override_labels if (not(i.startswith('!')) and ('!'+i not in valid_override_labels))]
    unwanted_labels = [i for i in valid_config_labels if ((i.startswith('!') and (i[1:] not in valid_override_labels) and ('!' + i not in valid_override_labels)))] + [i for i in valid_override_labels if i.startswith('!') and not i.startswith('!!')]

    combined_list = list(set(required_labels + unwanted_labels))
    if '' in combined_list:
        combined_list.remove('')

    return combined_list

def combine_required_properties(config_properties, override_properties):
    valid_config_properties, unwanted_config_properties = validate_properties(config_properties)
    valid_override_properties, unwanted_override_properties = validate_properties(override_properties)

    config_properties = {i: valid_config_properties[i] for i in valid_config_properties if i not in unwanted_override_properties}
    override_properties = {i: valid_override_properties[i] for i in valid_override_properties}
    required_properties = {**config_properties, **override_properties}

    unwanted_properties = [i for i in unwanted_override_properties] + [i for i in unwanted_config_properties if i not in valid_override_properties.keys()]

    return required_properties, unwanted_properties
