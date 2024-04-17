from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


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
			- Obw_Values_Seg_1_Tx: List[float]: No parameter help available
			- Obw_Values_Seg_2_Tx: List[float]: No parameter help available
			- Obw_Leri_Seg_1_Tx: List[float]: No parameter help available
			- Obw_Leri_Seg_2_Tx: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Obw_Values_Seg_1_Tx', DataType.FloatList, None, False, False, 4),
			ArgStruct('Obw_Values_Seg_2_Tx', DataType.FloatList, None, False, False, 4),
			ArgStruct('Obw_Leri_Seg_1_Tx', DataType.FloatList, None, False, False, 2),
			ArgStruct('Obw_Leri_Seg_2_Tx', DataType.FloatList, None, False, False, 2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Obw_Values_Seg_1_Tx: List[float] = None
			self.Obw_Values_Seg_2_Tx: List[float] = None
			self.Obw_Leri_Seg_1_Tx: List[float] = None
			self.Obw_Leri_Seg_2_Tx: List[float] = None

	def read(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:MIMO<n>:SEGMents \n
		Snippet: value: ResultData = driver.multiEval.tsMask.obw.mimo.segments.read(mimo = repcap.Mimo.Default) \n
		Return the OBW results for MIMO measurements, antenna number <n>, bandwidths with two segments (80+80) . \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'READ:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:MIMO{mimo_cmd_val}:SEGMents?', self.__class__.ResultData())

	def fetch(self, mimo=repcap.Mimo.Default) -> ResultData:
		"""SCPI: FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:MIMO<n>:SEGMents \n
		Snippet: value: ResultData = driver.multiEval.tsMask.obw.mimo.segments.fetch(mimo = repcap.Mimo.Default) \n
		Return the OBW results for MIMO measurements, antenna number <n>, bandwidths with two segments (80+80) . \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		return self._core.io.query_struct(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:TSMask:OBW:MIMO{mimo_cmd_val}:SEGMents?', self.__class__.ResultData())
