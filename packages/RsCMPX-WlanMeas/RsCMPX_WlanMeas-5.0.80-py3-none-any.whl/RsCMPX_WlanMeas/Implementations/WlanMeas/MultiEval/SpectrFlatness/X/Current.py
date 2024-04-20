from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self) -> List[int]:
		"""SCPI: READ:WLAN:MEASurement<instance>:MEValuation:SFLatness:X:CURRent \n
		Snippet: value: List[int] = driver.wlanMeas.multiEval.spectrFlatness.x.current.read() \n
		Return the subcarrier indices (x positions of the worst values) for the current, average, minimum and maximum margin
		values. \n
		Suppressed linked return values: reliability \n
			:return: margins: Up to 10 comma-separated values of subcarrier indices (one index per subcarrier range from left to right) Value 1: subcarrier index of the trace margin to the upper spectrum flatness limit For bandwidths 80 MHz, the value is only relevant for the left 80 MHz segment (segment 1) . Value 2 to 5: subcarrier indices, for the trace margin to the lower spectrum flatness limit For bandwidths 80 MHz, the values are only relevant for the left 80 MHz segment (segment 1) . Value 6: subcarrier index of the trace margin to the upper spectrum flatness limit for the right 80 MHz segment (segment 2) . This index is only relevant for bandwidths 80 MHz. Value 7 to 10: subcarrier indices of the trace margins to the lower spectrum flatness limit for the right 80 MHz segment (segment 2) . Values 6 to 10 are only relevant for bandwidths 80 MHz."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:SFLatness:X:CURRent?', suppressed)
		return response

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:SFLatness:X:CURRent \n
		Snippet: value: List[int] = driver.wlanMeas.multiEval.spectrFlatness.x.current.fetch() \n
		Return the subcarrier indices (x positions of the worst values) for the current, average, minimum and maximum margin
		values. \n
		Suppressed linked return values: reliability \n
			:return: margins: Up to 10 comma-separated values of subcarrier indices (one index per subcarrier range from left to right) Value 1: subcarrier index of the trace margin to the upper spectrum flatness limit For bandwidths 80 MHz, the value is only relevant for the left 80 MHz segment (segment 1) . Value 2 to 5: subcarrier indices, for the trace margin to the lower spectrum flatness limit For bandwidths 80 MHz, the values are only relevant for the left 80 MHz segment (segment 1) . Value 6: subcarrier index of the trace margin to the upper spectrum flatness limit for the right 80 MHz segment (segment 2) . This index is only relevant for bandwidths 80 MHz. Value 7 to 10: subcarrier indices of the trace margins to the lower spectrum flatness limit for the right 80 MHz segment (segment 2) . Values 6 to 10 are only relevant for bandwidths 80 MHz."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:SFLatness:X:CURRent?', suppressed)
		return response
