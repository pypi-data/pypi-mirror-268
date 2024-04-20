from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SingleCmwCls:
	"""SingleCmw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("singleCmw", core, parent)

	# noinspection PyTypeChecker
	def get_connector(self) -> List[enums.ConnectorSwitchExt]:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:CMWS:CONNector \n
		Snippet: value: List[enums.ConnectorSwitchExt] = driver.configure.wlanMeas.multiEval.listPy.singleCmw.get_connector() \n
		No command help available \n
			:return: connectors: No help available
		"""
		response = self._core.io.query_str('CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:CMWS:CONNector?')
		return Conversions.str_to_list_enum(response, enums.ConnectorSwitchExt)

	def set_connector(self, connectors: List[enums.ConnectorSwitchExt]) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:CMWS:CONNector \n
		Snippet: driver.configure.wlanMeas.multiEval.listPy.singleCmw.set_connector(connectors = [ConnectorSwitchExt.OFF, ConnectorSwitchExt.RH8]) \n
		No command help available \n
			:param connectors: No help available
		"""
		param = Conversions.enum_list_to_str(connectors, enums.ConnectorSwitchExt)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:CMWS:CONNector {param}')
