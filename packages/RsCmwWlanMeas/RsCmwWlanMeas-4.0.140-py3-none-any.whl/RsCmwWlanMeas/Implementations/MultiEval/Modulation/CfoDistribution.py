from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CfoDistributionCls:
	"""CfoDistribution commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfoDistribution", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Cfo_Percentage: float: float Percentage of CFO errors Unit: %
			- Cfo_Outside: int: decimal Number of detected CFO errors
			- Cfo_Total: int: decimal Number of measured CFOs"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Cfo_Percentage'),
			ArgStruct.scalar_int('Cfo_Outside'),
			ArgStruct.scalar_int('Cfo_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cfo_Percentage: float = None
			self.Cfo_Outside: int = None
			self.Cfo_Total: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:CFDistrib \n
		Snippet: value: ResultData = driver.multiEval.modulation.cfoDistribution.read() \n
		Return the scalar results for carrier frequency offset (CFO) error distribution. The results are only supported for 802.
		11ax. Exceeding the limit has no impact on the stop 'On Limit Failure' condition or out-of-tolerance counter. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:MODulation:CFDistrib?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:CFDistrib \n
		Snippet: value: ResultData = driver.multiEval.modulation.cfoDistribution.fetch() \n
		Return the scalar results for carrier frequency offset (CFO) error distribution. The results are only supported for 802.
		11ax. Exceeding the limit has no impact on the stop 'On Limit Failure' condition or out-of-tolerance counter. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:CFDistrib?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	def calculate(self) -> enums.ResultStatus2:
		"""SCPI: CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:CFDistrib \n
		Snippet: value: enums.ResultStatus2 = driver.multiEval.modulation.cfoDistribution.calculate() \n
		Return the scalar results for carrier frequency offset (CFO) error distribution. The results are only supported for 802.
		11ax. Exceeding the limit has no impact on the stop 'On Limit Failure' condition or out-of-tolerance counter. \n
		Use RsCmwWlanMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: cfo_percentage: float Percentage of CFO errors Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:MODulation:CFDistrib?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ResultStatus2)
