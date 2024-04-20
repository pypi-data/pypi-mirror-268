from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	# noinspection PyTypeChecker
	def get_scenario(self) -> List[enums.GuiScenario]:
		"""SCPI: ROUTe:WLAN:MEASurement<Instance>:CATalog:SCENario \n
		Snippet: value: List[enums.GuiScenario] = driver.route.wlanMeas.catalog.get_scenario() \n
		No command help available \n
			:return: valid_gui_scenarios: No help available
		"""
		response = self._core.io.query_str('ROUTe:WLAN:MEASurement<Instance>:CATalog:SCENario?')
		return Conversions.str_to_list_enum(response, enums.GuiScenario)
