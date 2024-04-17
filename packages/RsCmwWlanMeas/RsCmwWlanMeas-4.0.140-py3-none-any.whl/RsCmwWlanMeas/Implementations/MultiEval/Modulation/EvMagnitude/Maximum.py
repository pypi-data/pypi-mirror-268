from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal See 'Reliability indicator'
			- Evm_All_Users_All: List[float]: No parameter help available
			- Evm_All_Users_Data: List[float]: No parameter help available
			- Evm_All_Users_Pilot: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Evm_All_Users_All', DataType.FloatList, None, False, False, 144),
			ArgStruct('Evm_All_Users_Data', DataType.FloatList, None, False, False, 144),
			ArgStruct('Evm_All_Users_Pilot', DataType.FloatList, None, False, False, 144)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Evm_All_Users_All: List[float] = None
			self.Evm_All_Users_Data: List[float] = None
			self.Evm_All_Users_Pilot: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:MODulation:EVMagnitude:MAXimum \n
		Snippet: value: FetchStruct = driver.multiEval.modulation.evMagnitude.maximum.fetch() \n
		Return the single value results per user for OFDMA SISO measurements.
		For MIMO measurements, the stream/antenna-independent values are returned. There are current, average, minimum, maximum
		and standard deviation results. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:MODulation:EVMagnitude:MAXimum?', self.__class__.FetchStruct())
