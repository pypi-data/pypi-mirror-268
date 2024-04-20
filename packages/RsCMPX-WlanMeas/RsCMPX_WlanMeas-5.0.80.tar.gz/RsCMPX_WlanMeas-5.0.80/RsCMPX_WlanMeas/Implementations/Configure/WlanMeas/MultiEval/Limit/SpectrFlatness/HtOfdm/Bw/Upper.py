from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UpperCls:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, upper: float, bandwidthC=repcap.BandwidthC.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:HTOFdm:BW<bandwidth>:UPPer \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.spectrFlatness.htOfdm.bw.upper.set(upper = 1.0, bandwidthC = repcap.BandwidthC.Default) \n
		Defines an upper limit for the spectrum flatness of 802.11n signals with the specified <bandwidth>. The upper limit must
		be larger than the lower limits. \n
			:param upper: No help available
			:param bandwidthC: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
		"""
		param = Conversions.decimal_value_to_str(upper)
		bandwidthC_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthC, repcap.BandwidthC)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:HTOFdm:BW{bandwidthC_cmd_val}:UPPer {param}')

	def get(self, bandwidthC=repcap.BandwidthC.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:HTOFdm:BW<bandwidth>:UPPer \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.limit.spectrFlatness.htOfdm.bw.upper.get(bandwidthC = repcap.BandwidthC.Default) \n
		Defines an upper limit for the spectrum flatness of 802.11n signals with the specified <bandwidth>. The upper limit must
		be larger than the lower limits. \n
			:param bandwidthC: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Bw')
			:return: upper: No help available"""
		bandwidthC_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthC, repcap.BandwidthC)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:HTOFdm:BW{bandwidthC_cmd_val}:UPPer?')
		return Conversions.str_to_float(response)
