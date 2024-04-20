from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VcCalibCls:
	"""VcCalib commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vcCalib", core, parent)

	def set_calibrate(self, cell_name: str) -> None:
		"""SCPI: PROCedure:SIGNaling:NRADio:CELL:VCCalib:CALibrate \n
		Snippet: driver.procedure.signaling.nradio.cell.vcCalib.set_calibrate(cell_name = 'abc') \n
		Starts the virtual cable calibration. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'PROCedure:SIGNaling:NRADio:CELL:VCCalib:CALibrate {param}')

	def set_isolation(self, cell_name: str) -> None:
		"""SCPI: PROCedure:SIGNaling:NRADio:CELL:VCCalib:ISOLation \n
		Snippet: driver.procedure.signaling.nradio.cell.vcCalib.set_isolation(cell_name = 'abc') \n
		Updates the isolation quality information without changing the calibration matrix. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'PROCedure:SIGNaling:NRADio:CELL:VCCalib:ISOLation {param}')

	def deactivate(self, cell_name: str) -> None:
		"""SCPI: PROCedure:SIGNaling:NRADio:CELL:VCCalib:DEACtivate \n
		Snippet: driver.procedure.signaling.nradio.cell.vcCalib.deactivate(cell_name = 'abc') \n
		Discards the calibration matrix. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'PROCedure:SIGNaling:NRADio:CELL:VCCalib:DEACtivate {param}')
