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
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:CFDistrib \n
		Snippet: driver.configure.multiEval.limit.modulation.ehtOfdm.cfoDistribution.set(cfo_percentage = 1.0, cfo_frequency = 1.0) \n
		No command help available \n
			:param cfo_percentage: (float or boolean) No help available
			:param cfo_frequency: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cfo_percentage', cfo_percentage, DataType.FloatExt), ArgSingle('cfo_frequency', cfo_frequency, DataType.Float))
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:CFDistrib {param}'.rstrip())

	# noinspection PyTypeChecker
	class CfoDistributionStruct(StructBase):
		"""Response structure. Fields: \n
			- Cfo_Percentage: float or bool: No parameter help available
			- Cfo_Frequency: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Cfo_Percentage'),
			ArgStruct.scalar_float('Cfo_Frequency')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cfo_Percentage: float or bool = None
			self.Cfo_Frequency: float = None

	def get(self) -> CfoDistributionStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:CFDistrib \n
		Snippet: value: CfoDistributionStruct = driver.configure.multiEval.limit.modulation.ehtOfdm.cfoDistribution.get() \n
		No command help available \n
			:return: structure: for return value, see the help for CfoDistributionStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:MODulation:EHTofdm:CFDistrib?', self.__class__.CfoDistributionStruct())
