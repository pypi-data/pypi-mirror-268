from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandwidthCls:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, bandwidth: enums.Bandwidth, segmentB=repcap.SegmentB.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:BWIDth \n
		Snippet: driver.configure.wlanMeas.multiEval.listPy.segment.bandwidth.set(bandwidth = enums.Bandwidth.BW05mhz, segmentB = repcap.SegmentB.Default) \n
		Specifies the channel bandwidth for segment <no> in list mode. \n
			:param bandwidth: BW05mhz: 5 MHz BW10mhz: 10 MHz BW20mhz: 20 MHz BW40mhz: 40 MHz BW80mhz: 80 MHz BW16mhz: 160 MHz BW32mhz: 320 MHz
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.Bandwidth)
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:BWIDth {param}')

	# noinspection PyTypeChecker
	def get(self, segmentB=repcap.SegmentB.Default) -> enums.Bandwidth:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:BWIDth \n
		Snippet: value: enums.Bandwidth = driver.configure.wlanMeas.multiEval.listPy.segment.bandwidth.get(segmentB = repcap.SegmentB.Default) \n
		Specifies the channel bandwidth for segment <no> in list mode. \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: bandwidth: BW05mhz: 5 MHz BW10mhz: 10 MHz BW20mhz: 20 MHz BW40mhz: 40 MHz BW80mhz: 80 MHz BW16mhz: 160 MHz BW32mhz: 320 MHz"""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:BWIDth?')
		return Conversions.str_to_scalar_enum(response, enums.Bandwidth)
