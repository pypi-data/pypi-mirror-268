from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CgroupCls:
	"""Cgroup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cgroup", core, parent)

	def set(self, network_scope: str, coding_group: enums.CodingGroup) -> None:
		"""SCPI: [CONFigure]:SIGNaling:CMAS:CGRoup \n
		Snippet: driver.configure.signaling.cmas.cgroup.set(network_scope = 'abc', coding_group = enums.CodingGroup.G7) \n
		Selects the coding group for CMAS messages. \n
			:param network_scope: No help available
			:param coding_group: G7: GSM 7-bit coding without language string G7L: GSM 7-bit coding with language string U2L: UCS-2 coding with language string
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('network_scope', network_scope, DataType.String), ArgSingle('coding_group', coding_group, DataType.Enum, enums.CodingGroup))
		self._core.io.write(f'CONFigure:SIGNaling:CMAS:CGRoup {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, network_scope: str) -> enums.CodingGroup:
		"""SCPI: [CONFigure]:SIGNaling:CMAS:CGRoup \n
		Snippet: value: enums.CodingGroup = driver.configure.signaling.cmas.cgroup.get(network_scope = 'abc') \n
		Selects the coding group for CMAS messages. \n
			:param network_scope: No help available
			:return: coding_group: G7: GSM 7-bit coding without language string G7L: GSM 7-bit coding with language string U2L: UCS-2 coding with language string"""
		param = Conversions.value_to_quoted_str(network_scope)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:CMAS:CGRoup? {param}')
		return Conversions.str_to_scalar_enum(response, enums.CodingGroup)
