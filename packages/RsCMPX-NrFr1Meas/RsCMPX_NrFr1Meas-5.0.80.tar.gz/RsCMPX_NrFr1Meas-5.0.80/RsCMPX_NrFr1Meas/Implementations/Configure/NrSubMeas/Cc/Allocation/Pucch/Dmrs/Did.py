from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DidCls:
	"""Did commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("did", core, parent)

	def set(self, idn: int, carrierComponentFour=repcap.CarrierComponentFour.Nr1, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:DMRS:DID \n
		Snippet: driver.configure.nrSubMeas.cc.allocation.pucch.dmrs.did.set(idn = 1, carrierComponentFour = repcap.CarrierComponentFour.Nr1, allocation = repcap.Allocation.Default) \n
		Specifies the DMRS ID, for carrier <no>, allocation <a>. See also method RsCMPX_NrFr1Meas.Configure.NrSubMeas.Cc.
		Allocation.Pucch.Dmrs.Init.set. \n
			:param idn: No help available
			:param carrierComponentFour: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = Conversions.decimal_value_to_str(idn)
		carrierComponentFour_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentFour, repcap.CarrierComponentFour)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentFour_cmd_val}:ALLocation{allocation_cmd_val}:PUCCh:DMRS:DID {param}')

	def get(self, carrierComponentFour=repcap.CarrierComponentFour.Nr1, allocation=repcap.Allocation.Default) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:DMRS:DID \n
		Snippet: value: int = driver.configure.nrSubMeas.cc.allocation.pucch.dmrs.did.get(carrierComponentFour = repcap.CarrierComponentFour.Nr1, allocation = repcap.Allocation.Default) \n
		Specifies the DMRS ID, for carrier <no>, allocation <a>. See also method RsCMPX_NrFr1Meas.Configure.NrSubMeas.Cc.
		Allocation.Pucch.Dmrs.Init.set. \n
			:param carrierComponentFour: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: idn: No help available"""
		carrierComponentFour_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentFour, repcap.CarrierComponentFour)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentFour_cmd_val}:ALLocation{allocation_cmd_val}:PUCCh:DMRS:DID?')
		return Conversions.str_to_int(response)
