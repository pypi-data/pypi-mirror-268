from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ThresholdsCls:
	"""Thresholds commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("thresholds", core, parent)

	def set(self, cell_name: str, ncell_name: str, threshold_low: float, threshold_high: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:NCELl:THResholds \n
		Snippet: driver.configure.signaling.lte.ncell.thresholds.set(cell_name = 'abc', ncell_name = 'abc', threshold_low = 1.0, threshold_high = 1.0) \n
		Configures reselection thresholds for an entry in the neighbor cell list of an LTE or NR cell. \n
			:param cell_name: Serving LTE or NR cell via which the neighbor cell list is broadcasted.
			:param ncell_name: Neighbor cell
			:param threshold_low: Threshold ThreshX Low ('ThreshX, LowP') .
			:param threshold_high: Threshold ThreshX High ('ThreshX, HighP') .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ncell_name', ncell_name, DataType.String), ArgSingle('threshold_low', threshold_low, DataType.Float), ArgSingle('threshold_high', threshold_high, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:NCELl:THResholds {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Threshold_Low: float: Threshold ThreshX Low ('ThreshX, LowP') .
			- Threshold_High: float: Threshold ThreshX High ('ThreshX, HighP') ."""
		__meta_args_list = [
			ArgStruct.scalar_float('Threshold_Low'),
			ArgStruct.scalar_float('Threshold_High')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Threshold_Low: float = None
			self.Threshold_High: float = None

	def get(self, cell_name: str, ncell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:NCELl:THResholds \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.ncell.thresholds.get(cell_name = 'abc', ncell_name = 'abc') \n
		Configures reselection thresholds for an entry in the neighbor cell list of an LTE or NR cell. \n
			:param cell_name: Serving LTE or NR cell via which the neighbor cell list is broadcasted.
			:param ncell_name: Neighbor cell
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ncell_name', ncell_name, DataType.String))
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:NCELl:THResholds? {param}'.rstrip(), self.__class__.GetStruct())
