from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NbwPartsCls:
	"""NbwParts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nbwParts", core, parent)

	def set(self, no_of_bw_parts: int, carrierComponent=repcap.CarrierComponent.Nr1) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:NBWParts \n
		Snippet: driver.configure.nrSubMeas.cc.nbwParts.set(no_of_bw_parts = 1, carrierComponent = repcap.CarrierComponent.Nr1) \n
		No command help available \n
			:param no_of_bw_parts: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(no_of_bw_parts)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:NBWParts {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Nr1) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:NBWParts \n
		Snippet: value: int = driver.configure.nrSubMeas.cc.nbwParts.get(carrierComponent = repcap.CarrierComponent.Nr1) \n
		No command help available \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1
			:return: no_of_bw_parts: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:NBWParts?')
		return Conversions.str_to_int(response)
