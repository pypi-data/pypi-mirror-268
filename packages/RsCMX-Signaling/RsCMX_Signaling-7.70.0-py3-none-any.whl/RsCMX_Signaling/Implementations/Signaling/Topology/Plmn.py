from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlmnCls:
	"""Plmn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plmn", core, parent)

	def delete(self, name_plmn: str) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:PLMN \n
		Snippet: driver.signaling.topology.plmn.delete(name_plmn = 'abc') \n
		Deletes a PLMN. \n
			:param name_plmn: No help available
		"""
		param = Conversions.value_to_quoted_str(name_plmn)
		self._core.io.write(f'DELete:SIGNaling:TOPology:PLMN {param}')
