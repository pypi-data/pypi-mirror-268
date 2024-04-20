from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NbehaviorCls:
	"""Nbehavior commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nbehavior", core, parent)

	def get_di_timer(self) -> float or bool:
		"""SCPI: [CONFigure]:SIGNaling:NBEHavior:DITimer \n
		Snippet: value: float or bool = driver.configure.signaling.nbehavior.get_di_timer() \n
		No command help available \n
			:return: timer: (float or boolean) No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:NBEHavior:DITimer?')
		return Conversions.str_to_float_or_bool(response)

	def set_di_timer(self, timer: float or bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NBEHavior:DITimer \n
		Snippet: driver.configure.signaling.nbehavior.set_di_timer(timer = 1.0) \n
		No command help available \n
			:param timer: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(timer)
		self._core.io.write(f'CONFigure:SIGNaling:NBEHavior:DITimer {param}')
