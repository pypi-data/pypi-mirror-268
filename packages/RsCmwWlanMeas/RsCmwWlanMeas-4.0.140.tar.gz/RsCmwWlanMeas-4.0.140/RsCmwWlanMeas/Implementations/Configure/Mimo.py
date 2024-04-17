from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	def get_no_antennas(self) -> int:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MIMO:NOANtennas \n
		Snippet: value: int = driver.configure.mimo.get_no_antennas() \n
		Sets the number of connected antennas for SISO and MIMO measurements. \n
			:return: num_of_antennas: decimal Number of antennas (1..8) , depending on receive mode
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MIMO:NOANtennas?')
		return Conversions.str_to_int(response)

	def set_no_antennas(self, num_of_antennas: int) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<instance>:MIMO:NOANtennas \n
		Snippet: driver.configure.mimo.set_no_antennas(num_of_antennas = 1) \n
		Sets the number of connected antennas for SISO and MIMO measurements. \n
			:param num_of_antennas: decimal Number of antennas (1..8) , depending on receive mode
		"""
		param = Conversions.decimal_value_to_str(num_of_antennas)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MIMO:NOANtennas {param}')
