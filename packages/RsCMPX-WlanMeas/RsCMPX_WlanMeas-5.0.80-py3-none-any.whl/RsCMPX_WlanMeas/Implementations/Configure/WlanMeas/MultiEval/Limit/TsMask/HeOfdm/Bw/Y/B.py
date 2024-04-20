from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BCls:
	"""B commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("b", core, parent)

	def set(self, tsm_lim_yrel_lev_b: float, bandwidthD=repcap.BandwidthD.Default) -> None:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HEOFdm:BW<bandwidth>:Y:B \n
		Snippet: driver.configure.wlanMeas.multiEval.limit.tsMask.heOfdm.bw.y.b.set(tsm_lim_yrel_lev_b = 1.0, bandwidthD = repcap.BandwidthD.Default) \n
		Defines the relative spectral density limit for point B (frequency offset: 3/2*bandwidth) on the transmit spectrum mask
		for 802.11ax signals with the specified <bandwidth>. See 'Transmit spectrum mask OFDM, default masks' for background
		information. \n
			:param tsm_lim_yrel_lev_b: No help available
			:param bandwidthD: optional repeated capability selector. Default value: Bw20 (settable in the interface 'Bw')
		"""
		param = Conversions.decimal_value_to_str(tsm_lim_yrel_lev_b)
		bandwidthD_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthD, repcap.BandwidthD)
		self._core.io.write(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HEOFdm:BW{bandwidthD_cmd_val}:Y:B {param}')

	def get(self, bandwidthD=repcap.BandwidthD.Default) -> float:
		"""SCPI: CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HEOFdm:BW<bandwidth>:Y:B \n
		Snippet: value: float = driver.configure.wlanMeas.multiEval.limit.tsMask.heOfdm.bw.y.b.get(bandwidthD = repcap.BandwidthD.Default) \n
		Defines the relative spectral density limit for point B (frequency offset: 3/2*bandwidth) on the transmit spectrum mask
		for 802.11ax signals with the specified <bandwidth>. See 'Transmit spectrum mask OFDM, default masks' for background
		information. \n
			:param bandwidthD: optional repeated capability selector. Default value: Bw20 (settable in the interface 'Bw')
			:return: tsm_lim_yrel_lev_b: No help available"""
		bandwidthD_cmd_val = self._cmd_group.get_repcap_cmd_value(bandwidthD, repcap.BandwidthD)
		response = self._core.io.query_str(f'CONFigure:WLAN:MEASurement<Instance>:MEValuation:LIMit:TSMask:HEOFdm:BW{bandwidthD_cmd_val}:Y:B?')
		return Conversions.str_to_float(response)
