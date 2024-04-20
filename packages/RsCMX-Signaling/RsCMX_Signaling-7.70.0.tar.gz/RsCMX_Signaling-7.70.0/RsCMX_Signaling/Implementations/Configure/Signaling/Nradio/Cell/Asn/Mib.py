from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MibCls:
	"""Mib commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mib", core, parent)

	def set(self, cell_name: str, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:ASN:MIB \n
		Snippet: driver.configure.signaling.nradio.cell.asn.mib.set(cell_name = 'abc', message = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:param message: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('message', message, DataType.String))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:ASN:MIB {param}'.rstrip())
