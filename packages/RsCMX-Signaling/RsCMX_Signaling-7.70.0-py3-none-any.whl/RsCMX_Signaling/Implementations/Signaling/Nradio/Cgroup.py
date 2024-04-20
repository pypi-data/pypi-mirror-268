from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CgroupCls:
	"""Cgroup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cgroup", core, parent)

	def delete(self, cell_group_name: str) -> None:
		"""SCPI: DELete:SIGNaling:NRADio:CGRoup \n
		Snippet: driver.signaling.nradio.cgroup.delete(cell_group_name = 'abc') \n
		Deletes an LTE or NR cell group. \n
			:param cell_group_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_group_name)
		self._core.io.write(f'DELete:SIGNaling:NRADio:CGRoup {param}')
