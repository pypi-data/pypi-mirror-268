from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self, resourceUnit=repcap.ResourceUnit.Default) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:POWer:RUNit<ru>:CURRent \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.power.runit.current.fetch(resourceUnit = repcap.ResourceUnit.Default) \n
		Returns single power value measured for RU at all antennas (OFDMA) . \n
		Suppressed linked return values: reliability \n
			:param resourceUnit: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Runit')
			:return: power_vs_ru_all_antennas: Power vs RU for all antennas"""
		resourceUnit_cmd_val = self._cmd_group.get_repcap_cmd_value(resourceUnit, repcap.ResourceUnit)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:POWer:RUNit{resourceUnit_cmd_val}:CURRent?', suppressed)
		return response
