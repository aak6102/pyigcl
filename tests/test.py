from src.intel import Intel

if __name__ == '__main__':

    print('---------------controlib 初始化-------------------')
    with Intel() as ctl:
        print('api_handle initial success')

        # enumerate adapter
        adapters = ctl.EnumerateDevices()
        print(f'adapters count: {len(adapters)}')
        for i,adapter in enumerate(adapters):
            adapter_properties = ctl.GetDeviceProperties(adapter)
            print(f"adapter {i} :{adapter_properties}")

        # enumerate display
        displays = ctl.EnumerateDisplays(adapters[0])
        print(f'displays count: {len(displays)}')
        for j,display in enumerate(displays):
            display_properties = ctl.GetDisplayProperties(display)
            print(f"display {j} :{display_properties}")

        # read EDID
        edid = ctl.GetEDID(displays[0])
        print(edid.hex())

        # read DPCD register[0X400]
        data = ctl.AUXAccess(displays[0], 0x400, size = 3, data = None, OpType = ctl.CTLOpType.Read, flags = ctl.CTLAuxFlag.NATIVE_AUX)
        print(data.hex())

        # read power setting
        power_setting = ctl.Get_all_power_setting(displays[0])
        print(power_setting)
