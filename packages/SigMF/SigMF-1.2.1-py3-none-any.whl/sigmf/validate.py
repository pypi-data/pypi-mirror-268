# Copyright: Multiple Authors
#
# This file is part of sigmf-python. https://github.com/sigmf/sigmf-python
#
# SPDX-License-Identifier: LGPL-3.0-or-later

'''SigMF Validator'''

import argparse
import json
import logging

import jsonschema

from . import __version__ as toolversion
from . import error, schema, sigmffile


def extend_with_default(validator_class):
    '''
    Boilerplate code from [1] to retrieve jsonschema default dict.

    References
    ----------
    [1] https://python-jsonschema.readthedocs.io/en/stable/faq/
    '''
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, topschema):
        for property, subschema in properties.items():
            if "default" in subschema:
                instance.setdefault(property, subschema["default"])

        for error in validate_properties(
            validator, properties, instance, topschema,
        ):
            yield error

    return jsonschema.validators.extend(
        validator_class, {"properties": set_defaults},
    )


def get_default_metadata(ref_schema=schema.get_schema()):
    '''
    retrieve defaults from schema
    FIXME: not working yet
    '''
    default = {}
    validator = extend_with_default(jsonschema.Draft7Validator)
    validator(ref_schema).validate(default)
    return default


def validate(metadata, ref_schema=schema.get_schema()):
    '''
    Check that the provided `metadata` dict is valid according to the `ref_schema` dict.
    Walk entire schema and check all keys.

    Parameters
    ----------
    metadata : dict
        The SigMF metadata to be validated.
    ref_schema : dict, optional
        The schema that holds the SigMF metadata definition.
        Since the schema evolves over time, we may want to be able to check
        against different versions in the *future*.

    Returns
    -------
    None, will raise error if invalid.
    '''
    jsonschema.validators.validate(instance=metadata, schema=ref_schema)

    # assure capture and annotation order
    # TODO: There is a way to do this with just the schema apparently.
    for key in ['captures', 'annotations']:
        count = -1
        for item in metadata[key]:
            new_count = item['core:sample_start']
            if new_count < count:
                raise jsonschema.exceptions.ValidationError(f'{key} has bad order')
            else:
                count = new_count


def main():
    parser = argparse.ArgumentParser(description='Validate SigMF Archive or file pair against JSON schema.',
                                     prog='sigmf_validate')
    parser.add_argument('filename', help='SigMF path (extension optional).')
    parser.add_argument('--skip-checksum', action='store_true', help='Skip reading dataset to validate checksum.')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('--version', action='version', version=f'%(prog)s {toolversion}')

    args = parser.parse_args()

    level_lut = {
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG,
    }
    log = logging.getLogger()
    logging.basicConfig(level=level_lut[min(args.verbose, 2)])

    try:
        signal = sigmffile.fromfile(args.filename, skip_checksum=args.skip_checksum)
    except error.SigMFFileError as err:
        # this happens if checksum fails
        log.error(err)
        exit(1)
    except IOError as err:
        log.error(err)
        log.error('Unable to read SigMF, bad path?')
        exit(1)
    except json.decoder.JSONDecodeError as err:
        log.error(err)
        log.error('Unable to decode malformed JSON.')
        exit(1)
    signal.validate()
    log.info('Validation OK!')


if __name__ == "__main__":
    main()
