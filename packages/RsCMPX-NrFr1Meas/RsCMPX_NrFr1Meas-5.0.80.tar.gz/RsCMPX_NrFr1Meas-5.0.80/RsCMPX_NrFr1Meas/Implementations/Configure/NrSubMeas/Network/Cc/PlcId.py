from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlcIdCls:
	"""PlcId commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plcId", core, parent)

	def set(self, physical_cell_id: int, carrierComponentOne=repcap.CarrierComponentOne.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork[:CC<no>]:PLCid \n
		Snippet: driver.configure.nrSubMeas.network.cc.plcId.set(physical_cell_id = 1, carrierComponentOne = repcap.CarrierComponentOne.Default) \n
		No command help available \n
			:param physical_cell_id: No help available
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(physical_cell_id)
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:CC{carrierComponentOne_cmd_val}:PLCid {param}')

	def get(self, carrierComponentOne=repcap.CarrierComponentOne.Default) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork[:CC<no>]:PLCid \n
		Snippet: value: int = driver.configure.nrSubMeas.network.cc.plcId.get(carrierComponentOne = repcap.CarrierComponentOne.Default) \n
		No command help available \n
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: physical_cell_id: No help available"""
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:CC{carrierComponentOne_cmd_val}:PLCid?')
		return Conversions.str_to_int(response)
