# symbolx
Dealling with multiple scenarios data?  This tool helps collecting several scenarios data such as multidimentional variables and parameters for reporting and visualization


Initial setting to be able to collect scenarios info. The following example uses parser and loader for GAMS-dieterpy output. For CSV and Arrow file formats see the test folder in https://gitlab.com/diw-evu/symbolx/-/tree/main/test

```python
import os
import symbolx as syx
from symbolx import DataCollection, SymbolsHandler, Symbol
import karray as ka


folder = "project_files/data_output"
# Next two lines allows to compress or unzip the current scenarios folders
# syx.compress_subdirs(folder=folder, zip_extension='7z', delete=True)
# syx.unzip_all(folder=folder, zip_extension='7z', delete=True)

# This example is for dieterpy users as this considers gams path, GDX parser and loader
DC = DataCollection()
DC.add_collector(collector_name='gdx_collector', parser=syx.symbol_parser_gdx, loader=syx.load_gdx)
DC.add_folder('gdx_collector', folder)
# These atrributes are arguments of the loader function. It may vary depending on the loader we use. This exmaple is for syx.load_gdx
DC.add_custom_attr(collector_name='gdx_collector', inf_to_zero=True, verbose=False)
# Use zip_extension='7z', if we consider scenario folders compresed with '.7z'. 
# Use serializer='yml' if using scenario folders created with dieterpy.__version__ < (1.6.0)
DC.adquire(id_integer=False, serializer='json', gams_dir=None, zip_extension=None)

SH = SymbolsHandler(method='object', obj=DC)
ka.settings.order = ['id','n','g','s','l','h']
# Resulting symbols will follow this order. This should be addapted to the actual dimension names of your variables
```

You can create the symbols and make operations.

```python

Z = Symbol("Z", symbol_handler=SH)

PRICE = Symbol("eq_nodalbalance", "m", symbol_handler=SH)*-1

G_L = Symbol("G_L", symbol_handler=SH)

STO_OUT = Symbol("STO_OUT", symbol_handler=SH)

# Some relevant methods
Z.df

Z.dfc

Z.dfm

G_L.items

G_L.array # this shows the karray attribute of symbolx

STO_OUT.rename_dim(**{'s':'g'})

G_L.dimreduc('h')

Z.add_dim('n','DE')

G_L.shrink(g=['wind','pv'])

# Symbols operations
BILL = G_L*PRICE

```
