from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqualityCls:
	"""Iquality commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iquality", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, cell_name: str) -> enums.VcCalibQuantity:
		"""SCPI: FETCh:SIGNaling:NRADio:CELL:VCCalib:IQUality \n
		Snippet: value: enums.VcCalibQuantity = driver.signaling.nradio.cell.vcCalib.iquality.fetch(cell_name = 'abc') \n
		Queries the isolation quality. \n
			:param cell_name: No help available
			:return: quantity: Good, insufficient for conformance, critically low"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'FETCh:SIGNaling:NRADio:CELL:VCCalib:IQUality? {param}')
		return Conversions.str_to_scalar_enum(response, enums.VcCalibQuantity)
