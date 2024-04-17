from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LofdmCls:
	"""Lofdm commands group definition. 5 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lofdm", core, parent)

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_y'):
			from .Y import YCls
			self._y = YCls(self._core, self._cmd_group)
		return self._y

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:ENABle \n
		Snippet: value: bool = driver.configure.multiEval.limit.tsMask.lofdm.get_enable() \n
		Activates or deactivates the transmit spectrum mask, i.e. the limit check (802.11a/g, OFDM) . \n
			:return: tsm_lim_enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, tsm_lim_enable: bool) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:ENABle \n
		Snippet: driver.configure.multiEval.limit.tsMask.lofdm.set_enable(tsm_lim_enable = False) \n
		Activates or deactivates the transmit spectrum mask, i.e. the limit check (802.11a/g, OFDM) . \n
			:param tsm_lim_enable: OFF | ON
		"""
		param = Conversions.bool_to_str(tsm_lim_enable)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:LOFDm:ENABle {param}')

	def clone(self) -> 'LofdmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LofdmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
