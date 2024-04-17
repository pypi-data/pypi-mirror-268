from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EfTapsCls:
	"""EfTaps commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("efTaps", core, parent)

	def set(self, equalizer_filter_taps_enable: bool, equalizer_filter_taps_value: int = None) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:EFTaps \n
		Snippet: driver.configure.multiEval.compensation.efTaps.set(equalizer_filter_taps_enable = False, equalizer_filter_taps_value = 1) \n
		This command is relevant for DSSS signals only. It determines if and how accurate the transmit filter is estimated. \n
			:param equalizer_filter_taps_enable: No help available
			:param equalizer_filter_taps_value: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('equalizer_filter_taps_enable', equalizer_filter_taps_enable, DataType.Boolean), ArgSingle('equalizer_filter_taps_value', equalizer_filter_taps_value, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:EFTaps {param}'.rstrip())

	# noinspection PyTypeChecker
	class EfTapsStruct(StructBase):
		"""Response structure. Fields: \n
			- Equalizer_Filter_Taps_Enable: bool: No parameter help available
			- Equalizer_Filter_Taps_Value: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Equalizer_Filter_Taps_Enable'),
			ArgStruct.scalar_int('Equalizer_Filter_Taps_Value')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Equalizer_Filter_Taps_Enable: bool = None
			self.Equalizer_Filter_Taps_Value: int = None

	def get(self) -> EfTapsStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:EFTaps \n
		Snippet: value: EfTapsStruct = driver.configure.multiEval.compensation.efTaps.get() \n
		This command is relevant for DSSS signals only. It determines if and how accurate the transmit filter is estimated. \n
			:return: structure: for return value, see the help for EfTapsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:EFTaps?', self.__class__.EfTapsStruct())
