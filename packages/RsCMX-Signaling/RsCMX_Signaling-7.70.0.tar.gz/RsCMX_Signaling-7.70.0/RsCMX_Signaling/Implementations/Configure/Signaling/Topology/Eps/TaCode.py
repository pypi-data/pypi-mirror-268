from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TaCodeCls:
	"""TaCode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("taCode", core, parent)

	def set(self, name_ta_eps: str, ta_code: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:EPS:TACode \n
		Snippet: driver.configure.signaling.topology.eps.taCode.set(name_ta_eps = 'abc', ta_code = 1) \n
		Configures the tracking area code (TAC) of an EPS tracking area. \n
			:param name_ta_eps: No help available
			:param ta_code: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_ta_eps', name_ta_eps, DataType.String), ArgSingle('ta_code', ta_code, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:EPS:TACode {param}'.rstrip())

	def get(self, name_ta_eps: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:EPS:TACode \n
		Snippet: value: int = driver.configure.signaling.topology.eps.taCode.get(name_ta_eps = 'abc') \n
		Configures the tracking area code (TAC) of an EPS tracking area. \n
			:param name_ta_eps: No help available
			:return: ta_code: No help available"""
		param = Conversions.value_to_quoted_str(name_ta_eps)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:TOPology:EPS:TACode? {param}')
		return Conversions.str_to_int(response)
