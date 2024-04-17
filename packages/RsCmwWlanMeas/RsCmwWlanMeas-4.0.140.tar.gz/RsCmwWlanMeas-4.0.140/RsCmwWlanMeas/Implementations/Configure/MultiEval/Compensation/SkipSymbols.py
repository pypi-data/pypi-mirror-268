from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SkipSymbolsCls:
	"""SkipSymbols commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("skipSymbols", core, parent)

	def set(self, skip_symbols_head: int, skip_symbols_tail: int) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:SKIPsymbols \n
		Snippet: driver.configure.multiEval.compensation.skipSymbols.set(skip_symbols_head = 1, skip_symbols_tail = 1) \n
		Defines how many head and tail symbols are excluded from OFDM modulation measurements. \n
			:param skip_symbols_head: decimal Number of heading symbols to be skipped Range: 0 Sym to 100 Sym, Unit: symbol
			:param skip_symbols_tail: decimal Number of tailing symbols to be skipped Range: 0 Sym to 100 Sym, Unit: symbol
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('skip_symbols_head', skip_symbols_head, DataType.Integer), ArgSingle('skip_symbols_tail', skip_symbols_tail, DataType.Integer))
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:SKIPsymbols {param}'.rstrip())

	# noinspection PyTypeChecker
	class SkipSymbolsStruct(StructBase):
		"""Response structure. Fields: \n
			- Skip_Symbols_Head: int: decimal Number of heading symbols to be skipped Range: 0 Sym to 100 Sym, Unit: symbol
			- Skip_Symbols_Tail: int: decimal Number of tailing symbols to be skipped Range: 0 Sym to 100 Sym, Unit: symbol"""
		__meta_args_list = [
			ArgStruct.scalar_int('Skip_Symbols_Head'),
			ArgStruct.scalar_int('Skip_Symbols_Tail')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Skip_Symbols_Head: int = None
			self.Skip_Symbols_Tail: int = None

	def get(self) -> SkipSymbolsStruct:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:SKIPsymbols \n
		Snippet: value: SkipSymbolsStruct = driver.configure.multiEval.compensation.skipSymbols.get() \n
		Defines how many head and tail symbols are excluded from OFDM modulation measurements. \n
			:return: structure: for return value, see the help for SkipSymbolsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:COMPensation:SKIPsymbols?', self.__class__.SkipSymbolsStruct())
