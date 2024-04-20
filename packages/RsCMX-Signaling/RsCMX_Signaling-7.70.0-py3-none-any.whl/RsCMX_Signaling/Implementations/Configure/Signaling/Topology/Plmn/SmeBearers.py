from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmeBearersCls:
	"""SmeBearers commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smeBearers", core, parent)

	def set(self, name_plmn: str, max_15_support: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:PLMN:SMEBearers \n
		Snippet: driver.configure.signaling.topology.plmn.smeBearers.set(name_plmn = 'abc', max_15_support = False) \n
		Selects whether the network supports up to 15 EPS bearer contexts per UE (or only up to 8 EPS bearer contexts) . \n
			:param name_plmn: No help available
			:param max_15_support: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_plmn', name_plmn, DataType.String), ArgSingle('max_15_support', max_15_support, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:PLMN:SMEBearers {param}'.rstrip())

	def get(self, name_plmn: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:PLMN:SMEBearers \n
		Snippet: value: bool = driver.configure.signaling.topology.plmn.smeBearers.get(name_plmn = 'abc') \n
		Selects whether the network supports up to 15 EPS bearer contexts per UE (or only up to 8 EPS bearer contexts) . \n
			:param name_plmn: No help available
			:return: max_15_support: No help available"""
		param = Conversions.value_to_quoted_str(name_plmn)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:TOPology:PLMN:SMEBearers? {param}')
		return Conversions.str_to_bool(response)
