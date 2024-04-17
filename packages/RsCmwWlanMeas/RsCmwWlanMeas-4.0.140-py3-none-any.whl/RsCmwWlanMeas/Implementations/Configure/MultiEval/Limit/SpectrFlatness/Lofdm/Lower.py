from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowerCls:
	"""Lower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lower", core, parent)

	def set(self, center: float, side: float) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:LOWer \n
		Snippet: driver.configure.multiEval.limit.spectrFlatness.lofdm.lower.set(center = 1.0, side = 1.0) \n
		Defines lower limits for the spectrum flatness of the center subcarriers and the side subcarriers of 802.
		11a/g OFDM signals. The lower limits must be smaller than the upper limit. \n
			:param center: numeric Range: -20 dB to 4 dB
			:param side: numeric Range: -20 dB to 4 dB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('center', center, DataType.Float), ArgSingle('side', side, DataType.Float))
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:LOWer {param}'.rstrip())

	# noinspection PyTypeChecker
	class LowerStruct(StructBase):
		"""Response structure. Fields: \n
			- Center: float: numeric Range: -20 dB to 4 dB
			- Side: float: numeric Range: -20 dB to 4 dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Center'),
			ArgStruct.scalar_float('Side')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Center: float = None
			self.Side: float = None

	def get(self) -> LowerStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:LOWer \n
		Snippet: value: LowerStruct = driver.configure.multiEval.limit.spectrFlatness.lofdm.lower.get() \n
		Defines lower limits for the spectrum flatness of the center subcarriers and the side subcarriers of 802.
		11a/g OFDM signals. The lower limits must be smaller than the upper limit. \n
			:return: structure: for return value, see the help for LowerStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:LOFDm:LOWer?', self.__class__.LowerStruct())
