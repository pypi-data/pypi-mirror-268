from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SegmentsCls:
	"""Segments commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segments", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Obw_Values_Seg_1: List[float]: No parameter help available
			- Obw_Values_Seg_2: List[float]: No parameter help available
			- Obw_Lr_Seg_1: List[float]: No parameter help available
			- Obw_Lr_Seg_2: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Obw_Values_Seg_1', DataType.FloatList, None, False, False, 4),
			ArgStruct('Obw_Values_Seg_2', DataType.FloatList, None, False, False, 4),
			ArgStruct('Obw_Lr_Seg_1', DataType.FloatList, None, False, False, 2),
			ArgStruct('Obw_Lr_Seg_2', DataType.FloatList, None, False, False, 2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Obw_Values_Seg_1: List[float] = None
			self.Obw_Values_Seg_2: List[float] = None
			self.Obw_Lr_Seg_1: List[float] = None
			self.Obw_Lr_Seg_2: List[float] = None

	def read(self) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:SEGMents \n
		Snippet: value: ResultData = driver.multiEval.tsMask.obw.segments.read() \n
		Return the OBW results for SISO measurements and bandwidths with two segments. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:SEGMents?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:SEGMents \n
		Snippet: value: ResultData = driver.multiEval.tsMask.obw.segments.fetch() \n
		Return the OBW results for SISO measurements and bandwidths with two segments. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:SEGMents?', self.__class__.ResultData())
