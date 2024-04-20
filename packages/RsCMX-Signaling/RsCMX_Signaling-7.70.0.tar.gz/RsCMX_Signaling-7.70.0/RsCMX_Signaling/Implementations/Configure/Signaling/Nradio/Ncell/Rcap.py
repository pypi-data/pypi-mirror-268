from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RcapCls:
	"""Rcap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rcap", core, parent)

	def set(self, cell_name: str, ncell_name: str, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:NCELl:RCAP \n
		Snippet: driver.configure.signaling.nradio.ncell.rcap.set(cell_name = 'abc', ncell_name = 'abc', enable = False) \n
		Configures 'RedCapAccessallowed-r17' for an entry in the neighbor cell list of an NR cell. \n
			:param cell_name: Serving NR cell via which the neighbor cell list is broadcasted.
			:param ncell_name: Neighbor NR cell
			:param enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ncell_name', ncell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:NCELl:RCAP {param}'.rstrip())

	def get(self, cell_name: str, ncell_name: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:NCELl:RCAP \n
		Snippet: value: bool = driver.configure.signaling.nradio.ncell.rcap.get(cell_name = 'abc', ncell_name = 'abc') \n
		Configures 'RedCapAccessallowed-r17' for an entry in the neighbor cell list of an NR cell. \n
			:param cell_name: Serving NR cell via which the neighbor cell list is broadcasted.
			:param ncell_name: Neighbor NR cell
			:return: enable: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ncell_name', ncell_name, DataType.String))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:NCELl:RCAP? {param}'.rstrip())
		return Conversions.str_to_bool(response)
