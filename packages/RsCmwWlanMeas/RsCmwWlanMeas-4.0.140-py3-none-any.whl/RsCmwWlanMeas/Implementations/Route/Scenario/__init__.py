from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScenarioCls:
	"""Scenario commands group definition. 6 total commands, 4 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scenario", core, parent)

	@property
	def smi(self):
		"""smi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smi'):
			from .Smi import SmiCls
			self._smi = SmiCls(self._core, self._cmd_group)
		return self._smi

	@property
	def salone(self):
		"""salone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_salone'):
			from .Salone import SaloneCls
			self._salone = SaloneCls(self._core, self._cmd_group)
		return self._salone

	@property
	def smimo(self):
		"""smimo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smimo'):
			from .Smimo import SmimoCls
			self._smimo = SmimoCls(self._core, self._cmd_group)
		return self._smimo

	@property
	def tmimo(self):
		"""tmimo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tmimo'):
			from .Tmimo import TmimoCls
			self._tmimo = TmimoCls(self._core, self._cmd_group)
		return self._tmimo

	def get_cspath(self) -> str:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: value: str = driver.route.scenario.get_cspath() \n
		Activates the combined signal path scenario and selects the controlling application. The selected application controls
		the signal routing and analyzer settings while the combined signal path scenario is active. \n
			:return: master: No help available
		"""
		response = self._core.io.query_str('ROUTe:WLAN:MEASurement<Instance>:SCENario:CSPath?')
		return trim_str_response(response)

	def set_cspath(self, master: str) -> None:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: driver.route.scenario.set_cspath(master = 'abc') \n
		Activates the combined signal path scenario and selects the controlling application. The selected application controls
		the signal routing and analyzer settings while the combined signal path scenario is active. \n
			:param master: string String parameter selecting the controlling application, e.g., 'WLAN Sig1' or 'WLAN Sig2'
		"""
		param = Conversions.value_to_quoted_str(master)
		self._core.io.write(f'ROUTe:WLAN:MEASurement<Instance>:SCENario:CSPath {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.GuiScenario:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance>:SCENario \n
		Snippet: value: enums.GuiScenario = driver.route.scenario.get_value() \n
		Returns the active scenario. \n
			:return: gui_scenario: SALone | TMIMo | CSPath SALone: Standalone (non-signaling) CSPath: Combined signal path (with WLAN signaling) TMIMo: True MIMO
		"""
		response = self._core.io.query_str('ROUTe:WLAN:MEASurement<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.GuiScenario)

	def clone(self) -> 'ScenarioCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScenarioCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
