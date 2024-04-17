from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Modulation_Tx: enums.ModulationTypeD: No parameter help available
			- Power_Backoff_Tx: float: No parameter help available
			- Burst_Power_Tx: float: No parameter help available
			- Peak_Power_Tx: float: No parameter help available
			- Crest_Factor_Tx: float: float Crest factor, antenna n Range: 0 dB to 60 dB, Unit: dB
			- Evm_All_Carr_Tx: float: No parameter help available
			- Evm_Data_Carr_Tx: float: No parameter help available
			- Evm_Pilot_Carr_Tx: float: No parameter help available
			- Iq_Offset_Tx: float: No parameter help available
			- Dc_Power_Tx: float: No parameter help available
			- Gain_Imbalance_Tx: float: No parameter help available
			- Quad_Error_Tx: float: No parameter help available
			- Ltf_Power_Tx: float: No parameter help available
			- Data_Power_Tx: float: No parameter help available
			- Preamble_Power_Tx: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Modulation_Tx', enums.ModulationTypeD),
			ArgStruct.scalar_float('Power_Backoff_Tx'),
			ArgStruct.scalar_float('Burst_Power_Tx'),
			ArgStruct.scalar_float('Peak_Power_Tx'),
			ArgStruct.scalar_float('Crest_Factor_Tx'),
			ArgStruct.scalar_float('Evm_All_Carr_Tx'),
			ArgStruct.scalar_float('Evm_Data_Carr_Tx'),
			ArgStruct.scalar_float('Evm_Pilot_Carr_Tx'),
			ArgStruct.scalar_float('Iq_Offset_Tx'),
			ArgStruct.scalar_float('Dc_Power_Tx'),
			ArgStruct.scalar_float('Gain_Imbalance_Tx'),
			ArgStruct.scalar_float('Quad_Error_Tx'),
			ArgStruct.scalar_float('Ltf_Power_Tx'),
			ArgStruct.scalar_float('Data_Power_Tx'),
			ArgStruct.scalar_float('Preamble_Power_Tx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Modulation_Tx: enums.ModulationTypeD = None
			self.Power_Backoff_Tx: float = None
			self.Burst_Power_Tx: float = None
			self.Peak_Power_Tx: float = None
			self.Crest_Factor_Tx: float = None
			self.Evm_All_Carr_Tx: float = None
			self.Evm_Data_Carr_Tx: float = None
			self.Evm_Pilot_Carr_Tx: float = None
			self.Iq_Offset_Tx: float = None
			self.Dc_Power_Tx: float = None
			self.Gain_Imbalance_Tx: float = None
			self.Quad_Error_Tx: float = None
			self.Ltf_Power_Tx: float = None
			self.Data_Power_Tx: float = None
			self.Preamble_Power_Tx: float = None

	def read(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<instance>:MEValuation:MODulation:MIMO<n>:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.modulation.mimo.maximum.read(mimo = repcap.Mimo.Default) \n
		Return the single value results for MIMO measurements. There are current, average, minimum, maximum and standard
		deviation results. For 80+80 MHz signals, the segment-independent values are returned. The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:MIMO{mimo_cmd_val}:MAXimum?', self.__class__.ResultData())

	def fetch(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:MODulation:MIMO<n>:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.modulation.mimo.maximum.fetch(mimo = repcap.Mimo.Default) \n
		Return the single value results for MIMO measurements. There are current, average, minimum, maximum and standard
		deviation results. For 80+80 MHz signals, the segment-independent values are returned. The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:MIMO{mimo_cmd_val}:MAXimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Modulation_Tx: enums.ResultStatus2: No parameter help available
			- Power_Backoff_Tx: enums.ResultStatus2: No parameter help available
			- Burst_Power_Tx: enums.ResultStatus2: No parameter help available
			- Peak_Power_Tx: enums.ResultStatus2: No parameter help available
			- Crest_Factor_Tx: enums.ResultStatus2: float Crest factor, antenna n Range: 0 dB to 60 dB, Unit: dB
			- Evm_All_Carr_Tx: enums.ResultStatus2: No parameter help available
			- Evm_Data_Carr_Tx: enums.ResultStatus2: No parameter help available
			- Evm_Pilot_Carr_Tx: enums.ResultStatus2: No parameter help available
			- Iq_Offset_Tx: enums.ResultStatus2: No parameter help available
			- Dc_Power_Tx: enums.ResultStatus2: No parameter help available
			- Gain_Imbalance_Tx: enums.ResultStatus2: No parameter help available
			- Quad_Error_Tx: enums.ResultStatus2: No parameter help available
			- Ltf_Power_Tx: enums.ResultStatus2: No parameter help available
			- Data_Power_Tx: enums.ResultStatus2: No parameter help available
			- Preamble_Power_Tx: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Modulation_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Power_Backoff_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Burst_Power_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Peak_Power_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Crest_Factor_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_All_Carr_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Data_Carr_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Pilot_Carr_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Offset_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dc_Power_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Gain_Imbalance_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Quad_Error_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ltf_Power_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Data_Power_Tx', enums.ResultStatus2),
			ArgStruct.scalar_enum('Preamble_Power_Tx', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Modulation_Tx: enums.ResultStatus2 = None
			self.Power_Backoff_Tx: enums.ResultStatus2 = None
			self.Burst_Power_Tx: enums.ResultStatus2 = None
			self.Peak_Power_Tx: enums.ResultStatus2 = None
			self.Crest_Factor_Tx: enums.ResultStatus2 = None
			self.Evm_All_Carr_Tx: enums.ResultStatus2 = None
			self.Evm_Data_Carr_Tx: enums.ResultStatus2 = None
			self.Evm_Pilot_Carr_Tx: enums.ResultStatus2 = None
			self.Iq_Offset_Tx: enums.ResultStatus2 = None
			self.Dc_Power_Tx: enums.ResultStatus2 = None
			self.Gain_Imbalance_Tx: enums.ResultStatus2 = None
			self.Quad_Error_Tx: enums.ResultStatus2 = None
			self.Ltf_Power_Tx: enums.ResultStatus2 = None
			self.Data_Power_Tx: enums.ResultStatus2 = None
			self.Preamble_Power_Tx: enums.ResultStatus2 = None

	def calculate(self, mimo=repcap.Mimo.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<instance>:MEValuation:MODulation:MIMO<n>:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.modulation.mimo.maximum.calculate(mimo = repcap.Mimo.Default) \n
		Return the single value results for MIMO measurements. There are current, average, minimum, maximum and standard
		deviation results. For 80+80 MHz signals, the segment-independent values are returned. The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:MIMO{mimo_cmd_val}:MAXimum?', self.__class__.CalculateStruct())
