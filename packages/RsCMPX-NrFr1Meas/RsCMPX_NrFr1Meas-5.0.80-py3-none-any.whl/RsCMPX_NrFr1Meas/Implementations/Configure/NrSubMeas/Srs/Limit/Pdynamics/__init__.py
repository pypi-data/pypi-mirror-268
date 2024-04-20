from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdynamicsCls:
	"""Pdynamics commands group definition. 5 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdynamics", core, parent)

	@property
	def eonPower(self):
		"""eonPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eonPower'):
			from .EonPower import EonPowerCls
			self._eonPower = EonPowerCls(self._core, self._cmd_group)
		return self._eonPower

	@property
	def ttolerance(self):
		"""ttolerance commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ttolerance'):
			from .Ttolerance import TtoleranceCls
			self._ttolerance = TtoleranceCls(self._core, self._cmd_group)
		return self._ttolerance

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:ENABle \n
		Snippet: value: bool = driver.configure.nrSubMeas.srs.limit.pdynamics.get_enable() \n
		Enables or disables the limit check for the power dynamics measurement. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:ENABle \n
		Snippet: driver.configure.nrSubMeas.srs.limit.pdynamics.set_enable(enable = False) \n
		Enables or disables the limit check for the power dynamics measurement. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:ENABle {param}')

	def get_off_power(self) -> float:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:OFFPower \n
		Snippet: value: float = driver.configure.nrSubMeas.srs.limit.pdynamics.get_off_power() \n
		Defines an upper limit for the OFF power determined with the power dynamics measurement. \n
			:return: off_power: Upper limit before adding the test tolerance
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:OFFPower?')
		return Conversions.str_to_float(response)

	def set_off_power(self, off_power: float) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:OFFPower \n
		Snippet: driver.configure.nrSubMeas.srs.limit.pdynamics.set_off_power(off_power = 1.0) \n
		Defines an upper limit for the OFF power determined with the power dynamics measurement. \n
			:param off_power: Upper limit before adding the test tolerance
		"""
		param = Conversions.decimal_value_to_str(off_power)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:OFFPower {param}')

	def clone(self) -> 'PdynamicsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PdynamicsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
