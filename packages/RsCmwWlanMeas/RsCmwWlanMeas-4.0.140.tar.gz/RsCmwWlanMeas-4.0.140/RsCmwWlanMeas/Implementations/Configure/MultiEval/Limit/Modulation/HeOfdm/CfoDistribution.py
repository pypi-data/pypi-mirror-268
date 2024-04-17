from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CfoDistributionCls:
	"""CfoDistribution commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfoDistribution", core, parent)

	def set(self, cfo_percentage: float or bool, cfo_frequency: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:CFDistrib \n
		Snippet: driver.configure.multiEval.limit.modulation.heOfdm.cfoDistribution.set(cfo_percentage = 1.0, cfo_frequency = 1.0) \n
		Configure the limit of carrier frequency offset (CFO) error distribution for HE modulation measurements. Exceeding the
		limit has no impact on the stop 'On Limit Failure' condition or out-of-tolerance counter. \n
			:param cfo_percentage: (float or boolean) numeric | ON | OFF Upper limit for the tolerated CFO errors (CFO exceeding the specified CFO_Frequency) Unit: % Additional parameters: OFF | ON (disables | enables the limit check)
			:param cfo_frequency: numeric Border value defining CFO error Unit: Hz
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cfo_percentage', cfo_percentage, DataType.FloatExt), ArgSingle('cfo_frequency', cfo_frequency, DataType.Float))
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:CFDistrib {param}'.rstrip())

	# noinspection PyTypeChecker
	class CfoDistributionStruct(StructBase):
		"""Response structure. Fields: \n
			- Cfo_Percentage: float or bool: numeric | ON | OFF Upper limit for the tolerated CFO errors (CFO exceeding the specified CFO_Frequency) Unit: % Additional parameters: OFF | ON (disables | enables the limit check)
			- Cfo_Frequency: float: numeric Border value defining CFO error Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Cfo_Percentage'),
			ArgStruct.scalar_float('Cfo_Frequency')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cfo_Percentage: float or bool = None
			self.Cfo_Frequency: float = None

	def get(self) -> CfoDistributionStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:CFDistrib \n
		Snippet: value: CfoDistributionStruct = driver.configure.multiEval.limit.modulation.heOfdm.cfoDistribution.get() \n
		Configure the limit of carrier frequency offset (CFO) error distribution for HE modulation measurements. Exceeding the
		limit has no impact on the stop 'On Limit Failure' condition or out-of-tolerance counter. \n
			:return: structure: for return value, see the help for CfoDistributionStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:HEOFdm:CFDistrib?', self.__class__.CfoDistributionStruct())
