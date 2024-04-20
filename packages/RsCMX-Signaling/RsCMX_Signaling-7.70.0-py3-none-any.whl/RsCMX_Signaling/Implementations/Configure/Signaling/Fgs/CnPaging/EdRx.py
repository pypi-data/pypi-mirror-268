from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EdRxCls:
	"""EdRx commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edRx", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.EdRxMode:
		"""SCPI: [CONFigure]:SIGNaling:FGS:CNPaging:EDRX:MODE \n
		Snippet: value: enums.EdRxMode = driver.configure.signaling.fgs.cnPaging.edRx.get_mode() \n
		Selects a mode for configuration of the paging time window and of the cycle length. \n
			:return: mode: UERequested: as requested by UE USER: configured values
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:CNPaging:EDRX:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EdRxMode)

	def set_mode(self, mode: enums.EdRxMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:CNPaging:EDRX:MODE \n
		Snippet: driver.configure.signaling.fgs.cnPaging.edRx.set_mode(mode = enums.EdRxMode.UERequested) \n
		Selects a mode for configuration of the paging time window and of the cycle length. \n
			:param mode: UERequested: as requested by UE USER: configured values
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EdRxMode)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:CNPaging:EDRX:MODE {param}')

	def get_ept_window(self) -> float:
		"""SCPI: [CONFigure]:SIGNaling:FGS:CNPaging:EDRX:EPTWindow \n
		Snippet: value: float = driver.configure.signaling.fgs.cnPaging.edRx.get_ept_window() \n
		Configures the paging time window for the mode USER. \n
			:return: time_window: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:CNPaging:EDRX:EPTWindow?')
		return Conversions.str_to_float(response)

	def set_ept_window(self, time_window: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:CNPaging:EDRX:EPTWindow \n
		Snippet: driver.configure.signaling.fgs.cnPaging.edRx.set_ept_window(time_window = 1.0) \n
		Configures the paging time window for the mode USER. \n
			:param time_window: No help available
		"""
		param = Conversions.decimal_value_to_str(time_window)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:CNPaging:EDRX:EPTWindow {param}')

	def get_cycle(self) -> float:
		"""SCPI: [CONFigure]:SIGNaling:FGS:CNPaging:EDRX:CYCLe \n
		Snippet: value: float = driver.configure.signaling.fgs.cnPaging.edRx.get_cycle() \n
		Configures the eDRX cycle length for the mode USER. \n
			:return: cycle_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:CNPaging:EDRX:CYCLe?')
		return Conversions.str_to_float(response)

	def set_cycle(self, cycle_length: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:CNPaging:EDRX:CYCLe \n
		Snippet: driver.configure.signaling.fgs.cnPaging.edRx.set_cycle(cycle_length = 1.0) \n
		Configures the eDRX cycle length for the mode USER. \n
			:param cycle_length: No help available
		"""
		param = Conversions.decimal_value_to_str(cycle_length)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:CNPaging:EDRX:CYCLe {param}')
