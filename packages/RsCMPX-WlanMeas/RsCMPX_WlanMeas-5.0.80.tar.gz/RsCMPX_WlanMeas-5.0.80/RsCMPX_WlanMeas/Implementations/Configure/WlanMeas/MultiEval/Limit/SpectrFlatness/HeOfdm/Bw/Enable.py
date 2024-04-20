from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, bandwidthD=repcap.BandwidthD.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:HEOFdm:BW<bandwidth>:ENABle \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.spectrFlatness.heOfdm.bw.enable.set(enable = False, bandwidthD = repcap.BandwidthD.Default) \n
		Enables or disables the spectrum flatness limit check for 802.11ax signals with the specified <bandwidth>. \n
			:param enable: No help available
			:param bandwidthD: optional repeated capability selector. Default value: Bw20 (settable in the interface 'Bw')
		"""
		param = Conversions.bool_to_str(enable)
		bandwidthD_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthD, repcap.BandwidthD)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:HEOFdm:BW{bandwidthD_cmd_val}:ENABle {param}')

	def get(self, bandwidthD=repcap.BandwidthD.Default) -> bool:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:HEOFdm:BW<bandwidth>:ENABle \n
		Snippet: value: bool = driver.configure.wlanMeas.multiEval.limit.spectrFlatness.heOfdm.bw.enable.get(bandwidthD = repcap.BandwidthD.Default) \n
		Enables or disables the spectrum flatness limit check for 802.11ax signals with the specified <bandwidth>. \n
			:param bandwidthD: optional repeated capability selector. Default value: Bw20 (settable in the interface 'Bw')
			:return: enable: No help available"""
		bandwidthD_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthD, repcap.BandwidthD)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:SFLatness:HEOFdm:BW{bandwidthD_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
