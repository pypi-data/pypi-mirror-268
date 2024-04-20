from __future__ import annotations


class DMAioModbusTempClientInterface:
    @staticmethod
    async def read_coils(address: int, count: int = 1, slave: int = 1) -> (list, str):
        raise NotImplementedError

    @staticmethod
    async def read_discrete_inputs(address: int, count: int = 1, slave: int = 1) -> (list, str):
        raise NotImplementedError

    @staticmethod
    async def read_holding_registers(address: int, count: int = 1, slave: int = 1) -> (list, str):
        raise NotImplementedError

    @staticmethod
    async def read_input_registers(address: int, count: int = 1, slave: int = 1) -> (list, str):
        raise NotImplementedError

    @staticmethod
    async def write_coil(address: int, value: int, slave: int = 1) -> (bool, str):
        raise NotImplementedError

    @staticmethod
    async def write_register(address: int, value: int, slave: int = 1) -> (bool, str):
        raise NotImplementedError

    @staticmethod
    async def write_coils(address: int, values: list[int] | int, slave: int = 1) -> (bool, str):
        raise NotImplementedError

    @staticmethod
    async def write_registers(address: int, values: list[int] | int, slave: int = 1) -> (bool, str):
        raise NotImplementedError
