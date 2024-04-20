from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def read(self, mimo=repcap.Mimo.Default) -> List[int]:
		"""SCPI: READ:WLAN:MEASurement<instance>:MEValuation:SFLatness:MIMO<n>:X:AVERage \n
		Snippet: value: List[int] = driver.wlanMeas.multiEval.spectrFlatness.mimo.x.average.read(mimo = repcap.Mimo.Default) \n
		Return the subcarrier indices (x positions of the worst values) for the current, average, minimum and maximum margin
		values for true MIMO, antenna/stream number <n>. For the queries of spectrum flatness margins, see: method
		RsCMPX_WlanMeas.WlanMeas.MultiEval.SpectrFlatness.Mimo.Current.fetch etc. \n
		Suppressed linked return values: reliability \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: spec_flat_margins_segments_tx: Up to 10 comma-separated values of subcarrier indices (one index per subcarrier range from left to right) Value 1: subcarrier index of the trace margin to the upper spectrum flatness limit For bandwidths 80 MHz, the value is only relevant for the left 80 MHz segment (segment 1) . Value 2 to 5: subcarrier indices, for the trace margin to the lower spectrum flatness limit For bandwidths 80 MHz, the values are only relevant for the left 80 MHz segment (segment 1) . Value 6: subcarrier index of the trace margin to the upper spectrum flatness limit for the right 80 MHz segment (segment 2) . This index is only relevant for bandwidths 80 MHz. Value 7 to 10: subcarrier indices of the trace margins to the lower spectrum flatness limit for the right 80 MHz segment (segment 2) . Values 6 to 10 are only relevant for bandwidths 80 MHz."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:SFLatness:MIMO{mimo_cmd_val}:X:AVERage?', suppressed)
		return response

	def fetch(self, mimo=repcap.Mimo.Default) -> List[int]:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:SFLatness:MIMO<n>:X:AVERage \n
		Snippet: value: List[int] = driver.wlanMeas.multiEval.spectrFlatness.mimo.x.average.fetch(mimo = repcap.Mimo.Default) \n
		Return the subcarrier indices (x positions of the worst values) for the current, average, minimum and maximum margin
		values for true MIMO, antenna/stream number <n>. For the queries of spectrum flatness margins, see: method
		RsCMPX_WlanMeas.WlanMeas.MultiEval.SpectrFlatness.Mimo.Current.fetch etc. \n
		Suppressed linked return values: reliability \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: spec_flat_margins_segments_tx: Up to 10 comma-separated values of subcarrier indices (one index per subcarrier range from left to right) Value 1: subcarrier index of the trace margin to the upper spectrum flatness limit For bandwidths 80 MHz, the value is only relevant for the left 80 MHz segment (segment 1) . Value 2 to 5: subcarrier indices, for the trace margin to the lower spectrum flatness limit For bandwidths 80 MHz, the values are only relevant for the left 80 MHz segment (segment 1) . Value 6: subcarrier index of the trace margin to the upper spectrum flatness limit for the right 80 MHz segment (segment 2) . This index is only relevant for bandwidths 80 MHz. Value 7 to 10: subcarrier indices of the trace margins to the lower spectrum flatness limit for the right 80 MHz segment (segment 2) . Values 6 to 10 are only relevant for bandwidths 80 MHz."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:SFLatness:MIMO{mimo_cmd_val}:X:AVERage?', suppressed)
		return response
