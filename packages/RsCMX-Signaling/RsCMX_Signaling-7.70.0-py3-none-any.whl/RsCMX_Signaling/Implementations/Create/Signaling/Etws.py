from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EtwsCls:
	"""Etws commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("etws", core, parent)

	def set_secondary(self, network_scope: str) -> None:
		"""SCPI: CREate:SIGNaling:ETWS:SECondary \n
		Snippet: driver.create.signaling.etws.set_secondary(network_scope = 'abc') \n
		Creates an ETWS secondary service for all cells in a certain <NetworkScope>. Use this network scope in the other ETWS
		secondary commands. \n
			:param network_scope: Name of a PLMN or a tracking area or a cell
		"""
		param = Conversions.value_to_quoted_str(network_scope)
		self._core.io.write(f'CREate:SIGNaling:ETWS:SECondary {param}')

	def set_value(self, network_scope: str) -> None:
		"""SCPI: CREate:SIGNaling:ETWS \n
		Snippet: driver.create.signaling.etws.set_value(network_scope = 'abc') \n
		Creates an ETWS primary service for all cells in a certain <NetworkScope>. Use this network scope in the other ETWS
		primary commands. \n
			:param network_scope: Name of a PLMN or a tracking area or a cell
		"""
		param = Conversions.value_to_quoted_str(network_scope)
		self._core.io.write(f'CREate:SIGNaling:ETWS {param}')
