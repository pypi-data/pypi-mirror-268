from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	# noinspection PyTypeChecker
	def get_scenario(self) -> List[enums.GuiScenario]:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance>:CATalog:SCENario \n
		Snippet: value: List[enums.GuiScenario] = driver.route.catalog.get_scenario() \n
		Returns all scenarios possible for the instrument. \n
			:return: valid_gui_scenarios: UNDefined | SALone | CSPath | SMI4 | MIMO2x2 | MIMO4x4 | MIMO8x8 | TMIMo | SALone | CSPath | TMIMo SALone: Standalone (non-signaling) CSPath: Combined signal path (with WLAN signaling) TMIMo: True MIMO
		"""
		response = self._core.io.query_str('ROUTe:WLAN:MEASurement<Instance>:CATalog:SCENario?')
		return Conversions.str_to_list_enum(response, enums.GuiScenario)
