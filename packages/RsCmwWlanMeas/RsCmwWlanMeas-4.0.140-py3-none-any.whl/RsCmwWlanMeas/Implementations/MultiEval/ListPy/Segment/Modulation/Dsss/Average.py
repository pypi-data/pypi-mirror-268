from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Out_Of_Tol: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits. Range: 0 % to 100 %, Unit: %
			- Mod_Type: enums.ModulationTypeC: DBPSk1 | DQPSk2 | CCK5 | CCK11 Modulation scheme and coding rate DBPSk1: 1 Mbps DBPSK DQPSk2: 2 Mbps DQPSK CCK5: 5.5 Mbps CCK CCK11: 11 Mbps CCK
			- Plcp_Type: enums.PlcpType: SHORtplcp | LONGplcp Short or long PLCP
			- Payload_Length: int: decimal Number of bytes in the payload of the measured burst Range: 1 byte to 4095 bytes, Unit: byte
			- Burst_Power: float: float RMS power of the measured burst Range: -100 dBm to 30 dBm, Unit: dBm
			- Evm_Peak: float: float Error vector magnitude peak value Range: 0 % to 100 %, Unit: %
			- Evm_Rms: float: float Error vector magnitude RMS value Range: 0 % to 100 %, Unit: %
			- Freq_Error: float: float Center frequency error Range: -150 MHz to 150 MHz Hz
			- Clock_Error: float: float Chip clock error Range: -125 ppm to 125 ppm, Unit: ppm
			- Iq_Offset: float: float Range: -100 dB to 0 dB, Unit: dB
			- Gain_Imbalance: float: float Gain imbalance Range: -100 dB to 100 dB, Unit: dB
			- Quad_Error: float: float Quadrature error Range: -180 deg to 180 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_enum('Mod_Type', enums.ModulationTypeC),
			ArgStruct.scalar_enum('Plcp_Type', enums.PlcpType),
			ArgStruct.scalar_int('Payload_Length'),
			ArgStruct.scalar_float('Burst_Power'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Freq_Error'),
			ArgStruct.scalar_float('Clock_Error'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Gain_Imbalance'),
			ArgStruct.scalar_float('Quad_Error')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Mod_Type: enums.ModulationTypeC = None
			self.Plcp_Type: enums.PlcpType = None
			self.Payload_Length: int = None
			self.Burst_Power: float = None
			self.Evm_Peak: float = None
			self.Evm_Rms: float = None
			self.Freq_Error: float = None
			self.Clock_Error: float = None
			self.Iq_Offset: float = None
			self.Gain_Imbalance: float = None
			self.Quad_Error: float = None

	def fetch(self, segmentB=repcap.SegmentB.Default) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:MODulation:DSSS:AVERage \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.modulation.dsss.average.fetch(segmentB = repcap.SegmentB.Default) \n
		Return the current, average, minimum, maximum and standard deviation single value results for DSSS signals for segment
		<no> in list mode. \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:MODulation:DSSS:AVERage?', self.__class__.FetchStruct())
