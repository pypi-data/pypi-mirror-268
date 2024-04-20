from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectorCls:
	"""Connector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connector", core, parent)

	def set(self, connector: enums.ConnectorSwitchExt, segmentB=repcap.SegmentB.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:CMWS:CONNector \n
		Snippet: driver.configure.wlanMeas.multiEval.listPy.segment.singleCmw.connector.set(connector = enums.ConnectorSwitchExt.OFF, segmentB = repcap.SegmentB.Default) \n
		No command help available \n
			:param connector: No help available
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.ConnectorSwitchExt)
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:CMWS:CONNector {param}')

	# noinspection PyTypeChecker
	def get(self, segmentB=repcap.SegmentB.Default) -> enums.ConnectorSwitchExt:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent<segment>:CMWS:CONNector \n
		Snippet: value: enums.ConnectorSwitchExt = driver.configure.wlanMeas.multiEval.listPy.segment.singleCmw.connector.get(segmentB = repcap.SegmentB.Default) \n
		No command help available \n
			:param segmentB: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: connector: No help available"""
		segmentB_cmd_val = self._cmd_group.get_repcap_cmd_value(segmentB, repcap.SegmentB)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIST:SEGMent{segmentB_cmd_val}:CMWS:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.ConnectorSwitchExt)
