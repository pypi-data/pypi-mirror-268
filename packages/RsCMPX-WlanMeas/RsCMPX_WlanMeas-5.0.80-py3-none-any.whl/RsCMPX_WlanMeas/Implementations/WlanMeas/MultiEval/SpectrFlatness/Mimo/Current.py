from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self, mimo=repcap.Mimo.Default) -> List[float]:
		"""SCPI: READ:WLAN:MEASurement<instance>:MEValuation:SFLatness:MIMO<n>:CURRent \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.spectrFlatness.mimo.current.read(mimo = repcap.Mimo.Default) \n
		Return the single value margins for true MIMO measurements, antenna/stream number <n>. There are current, average,
		minimum, and maximum results. A positive margin indicates a violation of the spectrum flatness limit. The respective
		trace value is located above the upper or below the lower limit line. For the queries of subcarrier indices for spectrum
		flatness margins, see: method RsCMPX_WlanMeas.WlanMeas.MultiEval.SpectrFlatness.Mimo.X.Current.fetch etc. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: spec_flat_margins_tx: Up to 10 comma-separated list of margins (one value per subcarrier range from left to right) Value 1: trace margin to the upper spectrum flatness limit For bandwidths 80 MHz, the margin is only relevant for the left 80 MHz segment (segment 1) . Value 2 to 5: trace margins to the lower spectrum flatness limit For bandwidths 80 MHz, the margins are only relevant for the left 80 MHz segment (segment 1) . Value 6: trace margin to the upper spectrum flatness limit for the right 80 MHz segment (segment 2) . This margin is only relevant for bandwidths 80 MHz. Value 7 to 10: trace margins to the lower spectrum flatness limit for the right 80 MHz segment (segment 2) . Values 6 to 10 are only relevant for bandwidths 80 MHz."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WLAN:MEASurement<Instance>:MEValuation:SFLatness:MIMO{mimo_cmd_val}:CURRent?', suppressed)
		return response

	def fetch(self, mimo=repcap.Mimo.Default) -> List[float]:
		"""SCPI: FETCh:WLAN:MEASurement<instance>:MEValuation:SFLatness:MIMO<n>:CURRent \n
		Snippet: value: List[float] = driver.wlanMeas.multiEval.spectrFlatness.mimo.current.fetch(mimo = repcap.Mimo.Default) \n
		Return the single value margins for true MIMO measurements, antenna/stream number <n>. There are current, average,
		minimum, and maximum results. A positive margin indicates a violation of the spectrum flatness limit. The respective
		trace value is located above the upper or below the lower limit line. For the queries of subcarrier indices for spectrum
		flatness margins, see: method RsCMPX_WlanMeas.WlanMeas.MultiEval.SpectrFlatness.Mimo.X.Current.fetch etc. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: spec_flat_margins_tx: Up to 10 comma-separated list of margins (one value per subcarrier range from left to right) Value 1: trace margin to the upper spectrum flatness limit For bandwidths 80 MHz, the margin is only relevant for the left 80 MHz segment (segment 1) . Value 2 to 5: trace margins to the lower spectrum flatness limit For bandwidths 80 MHz, the margins are only relevant for the left 80 MHz segment (segment 1) . Value 6: trace margin to the upper spectrum flatness limit for the right 80 MHz segment (segment 2) . This margin is only relevant for bandwidths 80 MHz. Value 7 to 10: trace margins to the lower spectrum flatness limit for the right 80 MHz segment (segment 2) . Values 6 to 10 are only relevant for bandwidths 80 MHz."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WLAN:MEASurement<Instance>:MEValuation:SFLatness:MIMO{mimo_cmd_val}:CURRent?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self, mimo=repcap.Mimo.Default) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:WLAN:MEASurement<instance>:MEValuation:SFLatness:MIMO<n>:CURRent \n
		Snippet: value: List[enums.ResultStatus2] = driver.wlanMeas.multiEval.spectrFlatness.mimo.current.calculate(mimo = repcap.Mimo.Default) \n
		Return the single value margins for true MIMO measurements, antenna/stream number <n>. There are current, average,
		minimum, and maximum results. A positive margin indicates a violation of the spectrum flatness limit. The respective
		trace value is located above the upper or below the lower limit line. For the queries of subcarrier indices for spectrum
		flatness margins, see: method RsCMPX_WlanMeas.WlanMeas.MultiEval.SpectrFlatness.Mimo.X.Current.fetch etc. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param mimo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mimo')
			:return: spec_flat_margins_tx: Up to 10 comma-separated list of margins (one value per subcarrier range from left to right) Value 1: trace margin to the upper spectrum flatness limit For bandwidths 80 MHz, the margin is only relevant for the left 80 MHz segment (segment 1) . Value 2 to 5: trace margins to the lower spectrum flatness limit For bandwidths 80 MHz, the margins are only relevant for the left 80 MHz segment (segment 1) . Value 6: trace margin to the upper spectrum flatness limit for the right 80 MHz segment (segment 2) . This margin is only relevant for bandwidths 80 MHz. Value 7 to 10: trace margins to the lower spectrum flatness limit for the right 80 MHz segment (segment 2) . Values 6 to 10 are only relevant for bandwidths 80 MHz."""
		mimo_cmd_val = self._cmd_group.get_repcap_cmd_value(mimo, repcap.Mimo)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:WLAN:MEASurement<Instance>:MEValuation:SFLatness:MIMO{mimo_cmd_val}:CURRent?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
