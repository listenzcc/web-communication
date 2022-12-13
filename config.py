'''
@ file: config.py
@ author: listenzcc
@ version: 0.0
@ requires: config/config.xxx

@ readme:
Parse the configure using the XML Schema
It builds XMLSchema from .xsd file,
and parse the .xml by the schema.
'''

# %%
import xmlschema
import pandas as pd
from pathlib import Path

# %%
folder = Path('./config')
cfg = 'config'

schema = xmlschema.XMLSchema(folder.joinpath(cfg + '.xsd'))
dct = schema.to_dict(folder.joinpath(cfg + '.xml'))
print(dct)

# %%
table = pd.DataFrame(dct['site'])
table

# %%
