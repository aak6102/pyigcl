from cffi import FFI
from enum import IntEnum, IntFlag
from .intel_api import INCLUDE,DLL_NAME,CTL_ERROR_CODES

class Intel:

    CTL_RESULT_SUCCESS = 0

    class CTLOpType(IntFlag):
        Read = 0x1
        Write = 0x2

    class CTLAuxFlag(IntFlag):
        NATIVE_AUX = 0x1
        I2C_AUX = 0x2
        I2C_AUX_MOT = 0x4

    class PowerOptimizationFlag(IntFlag):
        FBC = 0x1
        PSR = 0x2
        DPST = 0x4
        LRR = 0x8
        LACE = 0x10

        @classmethod
        def from_string(cls, feature_str: str):
            try:
                return cls[feature_str]
            except KeyError:
                raise ValueError(f"Invalid feature name: {feature_str}")

        @classmethod
        def get_all_names(cls):
            """获取所有枚举值的名称"""
            return list(cls.__members__.keys())

    class CTLError(Exception):

        def __init__(self, code: int):
            result = IntEnum('CTLResult', CTL_ERROR_CODES)
            super().__init__(f"{result(code).name} (0x{code:08X})")

    def __init__(self, dll_path=DLL_NAME):

        self.api_handle = None
        self._allocated_pointers = [] # 管理所有需要释放的指针

        self.ffi = FFI()
        self.ffi.cdef(INCLUDE)
        try:
            self._ctl = self.ffi.dlopen(str(dll_path))
        except OSError as _e:
            raise RuntimeError(f"无法加载CTL库: {_e}")
        self.ctlInit()

    def ctlInit(self):
        # 初始化API
        init_args = self.ffi.new("ctl_init_args_t*")
        init_args.Size = self.ffi.sizeof("ctl_init_args_t")
        init_args.AppVersion = 1 << 16
        h_api_handle = self.ffi.new("ctl_api_handle_t*")
        result = self._ctl.ctlInit(init_args, h_api_handle)
        if result != self.CTL_RESULT_SUCCESS:
            raise self.CTLError(result)

        self._allocated_pointers.append(h_api_handle)
        self.api_handle = h_api_handle[0]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Close()
        return False

    def EnumerateDevices(self) -> list:
        # 枚举显卡适配器
        adapter_count = self.ffi.new("uint32_t*", 0)
        result = self._ctl.ctlEnumerateDevices(
            self.api_handle, adapter_count, self.ffi.NULL)

        if result != self.CTL_RESULT_SUCCESS :
            raise self.CTLError(result)

        if adapter_count[0] == 0:
            raise RuntimeError("没有找到适配器")

        adapter_handles = self.ffi.new("ctl_device_adapter_handle_t[]", adapter_count[0])
        result = self._ctl.ctlEnumerateDevices(
            self.api_handle, adapter_count, adapter_handles)
        self._allocated_pointers.append(adapter_handles)
        if result != self.CTL_RESULT_SUCCESS:
            raise self.CTLError(result)

        return [adapter_handles[i] for i in range(adapter_count[0])]

    def EnumerateDisplays(self, adapter) -> list:
        # 枚举显示器
        display_count = self.ffi.new("uint32_t*", 0)
        result = self._ctl.ctlEnumerateDisplayOutputs(
            adapter, display_count, self.ffi.NULL)

        if result != self.CTL_RESULT_SUCCESS:
            raise self.CTLError(result)

        if display_count[0] == 0:
            raise RuntimeError("没有找到显示器")

        display_handles = self.ffi.new("ctl_display_output_handle_t[]", display_count[0])
        result = self._ctl.ctlEnumerateDisplayOutputs(
            adapter, display_count, display_handles)
        self._allocated_pointers.append(display_handles)
        if result != self.CTL_RESULT_SUCCESS:
            raise self.CTLError(result)
        return [display_handles[i] for i in range(display_count[0])]

    def Close(self) -> int:
        """清理资源"""

        # 通过ctl释放hAPIHandle
        result = self._ctl.ctlClose(self.api_handle)
        self.api_handle = None

        # 释放ffi.new内存
        for ptr in self._allocated_pointers:
            self.ffi.release(ptr)
        self._allocated_pointers.clear()
        return result

    def AUXAccess(self, display, address:int, size:int=1, data:bytes = None, OpType:int=CTLOpType.Read,
                  flags:int=CTLAuxFlag.NATIVE_AUX) -> bytes | None:
        """AUX访问接口"""
        # 根据操作类型确定数据长度
        length = len(data) if OpType == self.CTLOpType.Write else size
        if length > 132:
            raise ValueError("数据长度超过最大限制132字节")

        # 创建FFI参数结构体
        args = self.ffi.new("ctl_aux_access_args_t*")
        args.Size = self.ffi.sizeof("ctl_aux_access_args_t")  # 结构体大小
        args.Address = address  # 目标地址
        args.Flags = flags  #
        """AUX访问接口"""
        # 根据操作类型确定数据长度
        length = len(data) if OpType == self.CTLOpType.Write else size
        if length > 132:
            raise ValueError("数据长度超过最大限制132字节")

        # 创建FFI参数结构体
        args = self.ffi.new("ctl_aux_access_args_t*")
        args.Size = self.ffi.sizeof("ctl_aux_access_args_t")  # 结构体大小
        args.Address = address  # 目标地址
        args.Flags = flags  # 操作标志位
        args.DataSize = length  # 数据长度
        args.OpType = OpType  # 操作类型

        # 读取操作预处理
        if OpType == self.CTLOpType.Read:
            data_buffer = self.ffi.buffer(args.Data, 132)
            data_buffer[:] = b'\x00' * 132
        elif OpType == self.CTLOpType.Write:
            self.ffi.memmove(args.Data, data, length)
        else:
            raise RuntimeError(f"操作类型错误，只能是1(读取)或2(写入)。当前操作类型：{OpType}")

        # 调用底层AUX访问接口
        result = self._ctl.ctlAUXAccess(display, args)
        if result != self.CTL_RESULT_SUCCESS:
            raise self.CTLError(result)

        return bytes(self.ffi.buffer(args.Data, length)) if OpType == 1 else None

    def GetDeviceProperties(self, adapter) -> dict[str, str | list[str]]:

        # 获取能力信息
        props = self.ffi.new("ctl_device_adapter_properties_t*")
        props.Size = self.ffi.sizeof("ctl_device_adapter_properties_t")
        result = self._ctl.ctlGetDeviceProperties(adapter, props)
        if result != self.CTL_RESULT_SUCCESS:
            return {}

        def parse_properties_functions(flags):
            functions = []
            if flags & (1 << 0): functions.append("Integrated Graphics adapter")
            if flags & (1 << 1): functions.append("Primary (Lead) adapter")
            if flags & (1 << 2): functions.append("Secondary (Linked) adapter")
            return functions

        driver_version = props.driver_version
        major = (driver_version >> 48) & 0xFFFF  # 前16位
        middle = (driver_version >> 32) & 0xFFFF  # 中间16位
        minor = (driver_version >> 16) & 0xFFFF  # 中间16位
        build = driver_version & 0xFFFF  # 后32位
        _properties = {
            "name": self.ffi.string(props.name).decode('utf-8', errors='ignore').strip('\x00'),
            "driver_version": f"{major}.{middle}.{minor}.{build}",
            "firmware_version": f"{props.firmware_version.major_version}.{props.firmware_version.minor_version}.{props.firmware_version.build_number}",
            "graphics_adapter_properties": parse_properties_functions(props.graphics_adapter_properties),
        }
        return _properties

    def GetEDID(self, display: object) -> bytes:
        # 获取EDID或displayID
        panel_desc_args = self.ffi.new("ctl_panel_descriptor_access_args_t*")
        panel_desc_args.Size = self.ffi.sizeof("ctl_panel_descriptor_access_args_t")
        panel_desc_args.OpType = 1  # CTL_OPERATION_TYPE_READ
        panel_desc_args.BlockNumber = 0
        panel_desc_args.DescriptorDataSize = 128
        panel_desc_args.pDescriptorData = self.ffi.new("uint8_t[]", 128)
        result = self._ctl.ctlPanelDescriptorAccess(display, panel_desc_args)
        if result != self.CTL_RESULT_SUCCESS:
            return b''
        main_block_data = bytes(self.ffi.buffer(panel_desc_args.pDescriptorData, 128))

        # 处理扩展块
        number_of_extn_blocks = panel_desc_args.pDescriptorData[126]
        ext_blocks_data = []
        if number_of_extn_blocks > 0:
            for block_index in range(number_of_extn_blocks):
                ext_block_args = self.ffi.new("ctl_panel_descriptor_access_args_t*")
                ext_block_args.Size = self.ffi.sizeof("ctl_panel_descriptor_access_args_t")
                ext_block_args.OpType = 1  # CTL_OPERATION_TYPE_READ
                ext_block_args.BlockNumber = block_index + 1
                ext_block_args.DescriptorDataSize = 128
                ext_block_args.pDescriptorData = self.ffi.new("uint8_t[]", 128)

                result = self._ctl.ctlPanelDescriptorAccess(display, ext_block_args)
                if result != self.CTL_RESULT_SUCCESS:
                    print(f"读取扩展块{block_index + 1}失败: {hex(result)}")
                    continue

                # 存储扩展块数据
                ext_block_data = bytes(self.ffi.buffer(ext_block_args.pDescriptorData, 128))
                ext_blocks_data.append({
                    "block_number": ext_block_args.BlockNumber,
                    "data": ext_block_data
                })


        complete_edid = main_block_data  # 主块数据
        for ext_block in ext_blocks_data:
            complete_edid += ext_block["data"]

        return complete_edid

    def GetDisplayProperties(self, display: object) -> dict[str, str | bool | dict[str, float]]:
        """获取显示器属性信息"""

        class DisplayConfigFlags(IntFlag):
            # 显示器配置标志
            DISPLAY_ACTIVE = 0x1  # 显示器活动
            DISPLAY_ATTACHED = 0x2  # 显示器已连接
            DONGLE_CONNECTED = 0x4  # 通过扩展坞连接
            DITHERING_ENABLED = 0x8  # 颜色抖动启用

        class DisplayOutputType(IntEnum):
            """显示器输出类型 (对应 ctl_display_output_types_t)"""
            INVALID = 0  # 无效类型
            DP = 1  # DisplayPort
            HDMI = 2  # HDMI
            DVI = 3  # DVI
            MIPI = 4  # MIPI（移动设备显示接口）
            CRT = 5  # CRT（传统阴极射线管显示器）

        props = self.ffi.new("ctl_display_properties_t*")
        props.Size = self.ffi.sizeof("ctl_display_properties_t")
        self._ctl.ctlGetDisplayProperties(display, props)

        # 解析返回数据
        timing = props.Display_Timing_Info
        timing_info = {
            'h_active': timing.HActive,
            'v_active': timing.VActive,
            'pixel_clock_mhz': timing.PixelClock / 1e6,
            'h_blank': timing.HBlank,
            'v_blank': timing.VBlank,
            'h_sync': timing.HSync,
            'v_sync': timing.VSync,
            'refresh_rate': timing.RefreshRate,
        }
        _properties = {
            'type': DisplayOutputType(props.Type).name,
            'is_active': bool(DisplayConfigFlags(props.DisplayConfigFlags) & DisplayConfigFlags.DISPLAY_ACTIVE),
            'is_attached': bool(DisplayConfigFlags(props.DisplayConfigFlags) & DisplayConfigFlags.DISPLAY_ATTACHED),
            'timing': timing_info
        }
        return _properties

    def GetPower(self, display: object, feature: str) -> bool:

        flag_value = self.PowerOptimizationFlag.from_string(feature)

        settings = self.ffi.new("ctl_power_optimization_settings_t*")
        settings.Size = self.ffi.sizeof("ctl_power_optimization_settings_t")
        settings.PowerOptimizationFeature = flag_value

        result = self._ctl.ctlGetPowerOptimizationSetting(display, settings)
        if result != self.CTL_RESULT_SUCCESS:
            raise self.CTLError(result)

        return settings.Enable

    def SetPower(self, display, feature:str, enable:bool) -> int:

        flag_value = self.PowerOptimizationFlag.from_string(feature)

        settings = self.ffi.new("ctl_power_optimization_settings_t*")
        settings.Size = self.ffi.sizeof("ctl_power_optimization_settings_t")
        settings.PowerOptimizationFeature = flag_value
        settings.Enable = enable
        return self._ctl.ctlSetPowerOptimizationSetting(display, settings)

    def Get_all_power_setting(self, display) -> dict[str, bool]:
        # 读取省功耗特性设置状态
        result = {}
        for feature in self.PowerOptimizationFlag.get_all_names():
            try:
                result[feature] = self.GetPower(display,feature)
            except Exception:
                # print(f"Failed to get power setting for {feature}: {e}")
                result[feature] = False
        return result