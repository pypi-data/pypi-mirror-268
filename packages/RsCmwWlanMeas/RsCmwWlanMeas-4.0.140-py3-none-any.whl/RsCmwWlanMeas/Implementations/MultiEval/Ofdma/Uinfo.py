from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UinfoCls:
	"""Uinfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: User, default value after init: User.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uinfo", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_user_get', 'repcap_user_set', repcap.User.Nr1)

	def repcap_user_set(self, user: repcap.User) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to User.Default
		Default value after init: User.Nr1"""
		self._cmd_group.set_repcap_enum_value(user)

	def repcap_user_get(self) -> repcap.User:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Ru_Count: int: decimal Index of RUs of all sizes (users with STA-ID 2046 are included) .
			- Ru_Index: int: decimal Index of the RUs only with the used size RUSize
			- Ru_26_Index: int: decimal Index based on RU26
			- Ru_Size: int: decimal RU size allocated by the user
			- Mcs: int: decimal Modulation and coding scheme
			- Dcm: int: decimal The value of DCM field
			- Sta_Id: int: decimal The value of STA-ID field
			- No_Of_Sts: int: decimal The value of NSTS field
			- Tx_Bf: int: decimal The value of TxBF field
			- Coding: enums.CodingType: BCC | LDPC Coding type"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Ru_Count'),
			ArgStruct.scalar_int('Ru_Index'),
			ArgStruct.scalar_int('Ru_26_Index'),
			ArgStruct.scalar_int('Ru_Size'),
			ArgStruct.scalar_int('Mcs'),
			ArgStruct.scalar_int('Dcm'),
			ArgStruct.scalar_int('Sta_Id'),
			ArgStruct.scalar_int('No_Of_Sts'),
			ArgStruct.scalar_int('Tx_Bf'),
			ArgStruct.scalar_enum('Coding', enums.CodingType)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ru_Count: int = None
			self.Ru_Index: int = None
			self.Ru_26_Index: int = None
			self.Ru_Size: int = None
			self.Mcs: int = None
			self.Dcm: int = None
			self.Sta_Id: int = None
			self.No_Of_Sts: int = None
			self.Tx_Bf: int = None
			self.Coding: enums.CodingType = None

	def fetch(self, user=repcap.User.Default) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:OFDMa:UINFo<user> \n
		Snippet: value: FetchStruct = driver.multiEval.ofdma.uinfo.fetch(user = repcap.User.Default) \n
		Queries OFDMA user-specific information signaled in a HE signal field. \n
			:param user: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Uinfo')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		user_cmd_val = self._cmd_group.get_repcap_cmd_value(user, repcap.User)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:OFDMa:UINFo{user_cmd_val}?', self.__class__.FetchStruct())

	def clone(self) -> 'UinfoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UinfoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
