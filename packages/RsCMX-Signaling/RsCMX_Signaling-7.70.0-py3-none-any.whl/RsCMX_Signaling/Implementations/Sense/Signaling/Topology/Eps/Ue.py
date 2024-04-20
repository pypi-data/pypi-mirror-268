from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCls:
	"""Ue commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ue", core, parent)

	def get_imsi(self) -> str:
		"""SCPI: SENSe:SIGNaling:TOPology:EPS:UE:IMSI \n
		Snippet: value: str = driver.sense.signaling.topology.eps.ue.get_imsi() \n
		Queries the IMSI of the UE. \n
			:return: imsi: No help available
		"""
		response = self._core.io.query_str('SENSe:SIGNaling:TOPology:EPS:UE:IMSI?')
		return trim_str_response(response)

	def get_imei(self) -> str:
		"""SCPI: SENSe:SIGNaling:TOPology:EPS:UE:IMEI \n
		Snippet: value: str = driver.sense.signaling.topology.eps.ue.get_imei() \n
		No command help available \n
			:return: imei: No help available
		"""
		response = self._core.io.query_str('SENSe:SIGNaling:TOPology:EPS:UE:IMEI?')
		return trim_str_response(response)
