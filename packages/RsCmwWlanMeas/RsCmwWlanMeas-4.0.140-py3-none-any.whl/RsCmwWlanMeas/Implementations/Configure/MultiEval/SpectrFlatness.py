from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrFlatnessCls:
	"""SpectrFlatness commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrFlatness", core, parent)

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.DisplayMode:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SFLatness:DMODe \n
		Snippet: value: enums.DisplayMode = driver.configure.multiEval.spectrFlatness.get_dmode() \n
		Selects the display mode of 'Spectrum Flatness' and 'Transmit Spectrum Mask' results to switch between relative and
		absolute result values (dB vs dBm) . \n
			:return: disp_mode: RELative | ABSolute
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:SFLatness:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.DisplayMode)

	def set_dmode(self, disp_mode: enums.DisplayMode) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:SFLatness:DMODe \n
		Snippet: driver.configure.multiEval.spectrFlatness.set_dmode(disp_mode = enums.DisplayMode.ABSolute) \n
		Selects the display mode of 'Spectrum Flatness' and 'Transmit Spectrum Mask' results to switch between relative and
		absolute result values (dB vs dBm) . \n
			:param disp_mode: RELative | ABSolute
		"""
		param = Conversions.enum_scalar_to_str(disp_mode, enums.DisplayMode)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:SFLatness:DMODe {param}')
