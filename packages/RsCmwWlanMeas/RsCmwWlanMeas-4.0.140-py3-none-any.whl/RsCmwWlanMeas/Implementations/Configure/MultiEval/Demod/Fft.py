from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FftCls:
	"""Fft commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fft", core, parent)

	# noinspection PyTypeChecker
	def get_offset(self) -> enums.FftOffset:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:DEMod:FFT:OFFSet \n
		Snippet: value: enums.FftOffset = driver.configure.multiEval.demod.fft.get_offset() \n
		Sets the FFT start offset for OFDM signals. \n
			:return: offset: CENT | PEAK | AUTO CENT: Guard interval center used as start offset PEAK: Peak of fine-timing metric used to determine start offset AUTO: Automatic selection of optimal start offset
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:DEMod:FFT:OFFSet?')
		return Conversions.str_to_scalar_enum(response, enums.FftOffset)

	def set_offset(self, offset: enums.FftOffset) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:DEMod:FFT:OFFSet \n
		Snippet: driver.configure.multiEval.demod.fft.set_offset(offset = enums.FftOffset.AUTO) \n
		Sets the FFT start offset for OFDM signals. \n
			:param offset: CENT | PEAK | AUTO CENT: Guard interval center used as start offset PEAK: Peak of fine-timing metric used to determine start offset AUTO: Automatic selection of optimal start offset
		"""
		param = Conversions.enum_scalar_to_str(offset, enums.FftOffset)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:DEMod:FFT:OFFSet {param}')
