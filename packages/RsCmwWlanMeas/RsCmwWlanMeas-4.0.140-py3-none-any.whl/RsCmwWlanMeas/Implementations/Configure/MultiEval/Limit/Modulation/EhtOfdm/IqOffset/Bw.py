from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwCls:
	"""Bw commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: BandwidthG, default value after init: BandwidthG.Bw5"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bw", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_bandwidthG_get', 'repcap_bandwidthG_set', repcap.BandwidthG.Bw5)

	def repcap_bandwidthG_set(self, bandwidthG: repcap.BandwidthG) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BandwidthG.Default
		Default value after init: BandwidthG.Bw5"""
		self._cmd_group.set_repcap_enum_value(bandwidthG)

	def repcap_bandwidthG_get(self) -> repcap.BandwidthG:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, offset_value_rel: float or bool, offset_value_abs: float or bool = None, bandwidthG=repcap.BandwidthG.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:IQOFfset:BW<BW> \n
		Snippet: driver.configure.multiEval.limit.modulation.ehtOfdm.iqOffset.bw.set(offset_value_rel = 1.0, offset_value_abs = 1.0, bandwidthG = repcap.BandwidthG.Default) \n
		No command help available \n
			:param offset_value_rel: (float or boolean) No help available
			:param offset_value_abs: (float or boolean) No help available
			:param bandwidthG: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('offset_value_rel', offset_value_rel, DataType.FloatExt), ArgSingle('offset_value_abs', offset_value_abs, DataType.FloatExt, None, is_optional=True))
		bandwidthG_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthG, repcap.BandwidthG)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:IQOFfset:BW{bandwidthG_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class BwStruct(StructBase):
		"""Response structure. Fields: \n
			- Offset_Value_Rel: float or bool: No parameter help available
			- Offset_Value_Abs: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Offset_Value_Rel'),
			ArgStruct.scalar_float_ext('Offset_Value_Abs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Offset_Value_Rel: float or bool = None
			self.Offset_Value_Abs: float or bool = None

	def get(self, bandwidthG=repcap.BandwidthG.Default) -> BwStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:IQOFfset:BW<BW> \n
		Snippet: value: BwStruct = driver.configure.multiEval.limit.modulation.ehtOfdm.iqOffset.bw.get(bandwidthG = repcap.BandwidthG.Default) \n
		No command help available \n
			:param bandwidthG: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: structure: for return value, see the help for BwStruct structure arguments."""
		bandwidthG_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthG, repcap.BandwidthG)
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:IQOFfset:BW{bandwidthG_cmd_val}?', self.__class__.BwStruct())

	def clone(self) -> 'BwCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BwCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
