from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, segmentB=repcap.SegmentB.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:FREQuency \n
		Snippet: driver.configure.wlanMeas.multiEval.listPy.segment.frequency.set(frequency = 1.0, segmentB = repcap.SegmentB.Default) \n
		Specifies the center frequency of the RF analyzer for segment <no> in list mode. For the supported frequency range, see
		'Frequency ranges'. \n
			:param frequency: No help available
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:FREQuency {param}')

	def get(self, segmentB=repcap.SegmentB.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:FREQuency \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.listPy.segment.frequency.get(segmentB = repcap.SegmentB.Default) \n
		Specifies the center frequency of the RF analyzer for segment <no> in list mode. For the supported frequency range, see
		'Frequency ranges'. \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: frequency: No help available"""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)
