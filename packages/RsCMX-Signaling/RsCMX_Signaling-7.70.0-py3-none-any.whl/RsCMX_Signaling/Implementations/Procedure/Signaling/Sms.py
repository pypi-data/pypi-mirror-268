from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmsCls:
	"""Sms commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sms", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Address: str: Address of the originator of the message
			- Message: str: Message text
			- Type_Py: enums.Type: Optional setting parameter. Coding group GDC: general data coding DCMC: data coding / message class
			- Coding: enums.Coding: Optional setting parameter. Data coding, selecting the used character set GSM: GSM 7-bit default alphabet coding (ASCII) EIGHt: 8-bit binary data UCS2: UCS-2 16-bit coding (only for GDC, not for DCMC)
			- Class_Py: enums.Class: Optional setting parameter. Message class 0 to 3, selecting to which component of the UE the message is delivered.
			- Core_Network: enums.CoreNetwork: Optional setting parameter. Type of network delivering the message, EPS or 5G"""
		__meta_args_list = [
			ArgStruct.scalar_str('Address'),
			ArgStruct.scalar_str('Message'),
			ArgStruct.scalar_enum_optional('Type_Py', enums.Type),
			ArgStruct.scalar_enum_optional('Coding', enums.Coding),
			ArgStruct.scalar_enum_optional('Class_Py', enums.Class),
			ArgStruct.scalar_enum_optional('Core_Network', enums.CoreNetwork)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Address: str = None
			self.Message: str = None
			self.Type_Py: enums.Type = None
			self.Coding: enums.Coding = None
			self.Class_Py: enums.Class = None
			self.Core_Network: enums.CoreNetwork = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: PROCedure:SIGNaling:SMS \n
		Snippet with structure: \n
		structure = driver.procedure.signaling.sms.SetStruct() \n
		structure.Address: str = 'abc' \n
		structure.Message: str = 'abc' \n
		structure.Type_Py: enums.Type = enums.Type.DCMC \n
		structure.Coding: enums.Coding = enums.Coding.EIGHt \n
		structure.Class_Py: enums.Class = enums.Class.C0 \n
		structure.Core_Network: enums.CoreNetwork = enums.CoreNetwork.EPS \n
		driver.procedure.signaling.sms.set(structure) \n
		Sends a short message to the UE. For background information, see 3GPP TS 23.038. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'PROCedure:SIGNaling:SMS', structure)
