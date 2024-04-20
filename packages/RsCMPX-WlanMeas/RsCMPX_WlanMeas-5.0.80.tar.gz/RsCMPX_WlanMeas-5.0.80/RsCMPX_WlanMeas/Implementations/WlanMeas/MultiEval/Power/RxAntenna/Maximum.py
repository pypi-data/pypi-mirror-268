from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def fetch(self, rxAntenna=repcap.RxAntenna.Default) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:POWer:RXANtenna<n>:MAXimum \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.power.rxAntenna.maximum.fetch(rxAntenna = repcap.RxAntenna.Default) \n
		Returns single power value measured at the specified antenna for all RUs (OFDMA) . \n
		Suppressed linked return values: reliability \n
			:param rxAntenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RxAntenna')
			:return: power_vs_antenna_all_rus: Power vs antenna for all RUs"""
		rxAntenna_cmd_val = self._cmd_group.get_repcap_cmd_value(rxAntenna, repcap.RxAntenna)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:POWer:RXANtenna{rxAntenna_cmd_val}:MAXimum?', suppressed)
		return response
