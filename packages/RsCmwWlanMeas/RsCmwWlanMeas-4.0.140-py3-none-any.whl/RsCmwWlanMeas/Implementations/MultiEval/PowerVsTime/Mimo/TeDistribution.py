from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TeDistributionCls:
	"""TeDistribution commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("teDistribution", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Te_Percentage: float: float Percentage of TEs Unit: %
			- Te_Outside: int: decimal Number of detected TEs
			- Te_Total: int: decimal Number of measured values"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Te_Percentage'),
			ArgStruct.scalar_int('Te_Outside'),
			ArgStruct.scalar_int('Te_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Te_Percentage: float = None
			self.Te_Outside: int = None
			self.Te_Total: int = None

	def read(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:PVTime:MIMO<n>:TEDistrib \n
		Snippet: value: ResultData = driver.multiEval.powerVsTime.mimo.teDistribution.read(mimo = repcap.Mimo.Default) \n
		Return the scalar results for timing error (TE) distribution for MIMO. The commands are only supported for OFDM standards.
		Exceeding the limit has no impact on the stop 'On Limit Failure' condition or out-of-tolerance counter. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:PVTime:MIMO{mimo_cmd_val}:TEDistrib?', self.__class__.ResultData())

	def fetch(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:PVTime:MIMO<n>:TEDistrib \n
		Snippet: value: ResultData = driver.multiEval.powerVsTime.mimo.teDistribution.fetch(mimo = repcap.Mimo.Default) \n
		Return the scalar results for timing error (TE) distribution for MIMO. The commands are only supported for OFDM standards.
		Exceeding the limit has no impact on the stop 'On Limit Failure' condition or out-of-tolerance counter. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:PVTime:MIMO{mimo_cmd_val}:TEDistrib?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Te_Percentage: enums.ResultStatus2: float Percentage of TEs Unit: %
			- Te_Outside: enums.ResultStatus2: decimal Number of detected TEs
			- Te_Total: enums.ResultStatus2: decimal Number of measured values"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Te_Percentage', enums.ResultStatus2),
			ArgStruct.scalar_enum('Te_Outside', enums.ResultStatus2),
			ArgStruct.scalar_enum('Te_Total', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Te_Percentage: enums.ResultStatus2 = None
			self.Te_Outside: enums.ResultStatus2 = None
			self.Te_Total: enums.ResultStatus2 = None

	def calculate(self, mimo=repcap.Mimo.Default) -> CalculateStruct:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:PVTime:MIMO<n>:TEDistrib \n
		Snippet: value: CalculateStruct = driver.multiEval.powerVsTime.mimo.teDistribution.calculate(mimo = repcap.Mimo.Default) \n
		Return the scalar results for timing error (TE) distribution for MIMO. The commands are only supported for OFDM standards.
		Exceeding the limit has no impact on the stop 'On Limit Failure' condition or out-of-tolerance counter. \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:PVTime:MIMO{mimo_cmd_val}:TEDistrib?', self.__class__.CalculateStruct())
