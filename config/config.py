import logging

import yaml


class Config:

    # load the config file
    def __init__(self, config_file):
        # load yaml file
        with open(config_file, 'r') as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logging.error(exc)


config = Config('config/dev.yaml')
