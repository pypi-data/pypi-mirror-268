from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BtypeCls:
	"""Btype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("btype", core, parent)

	def set(self, burst_type: enums.BurstTypeB, segmentB=repcap.SegmentB.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:BTYPe \n
		Snippet: driver.configure.wlanMeas.multiEval.listPy.segment.btype.set(burst_type = enums.BurstTypeB.GREenfield, segmentB = repcap.SegmentB.Default) \n
		Specifies the burst types for standard 802.11n for segment <no> in list mode. Do not use the command for other standards. \n
			:param burst_type: MIXed: for coexistence with other standards GREenfield: incompatible with other standards
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(burst_type, enums.BurstTypeB)
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:BTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, segmentB=repcap.SegmentB.Default) -> enums.BurstTypeB:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:BTYPe \n
		Snippet: value: enums.BurstTypeB = driver.configure.wlanMeas.multiEval.listPy.segment.btype.get(segmentB = repcap.SegmentB.Default) \n
		Specifies the burst types for standard 802.11n for segment <no> in list mode. Do not use the command for other standards. \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: burst_type: MIXed: for coexistence with other standards GREenfield: incompatible with other standards"""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:BTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.BurstTypeB)
