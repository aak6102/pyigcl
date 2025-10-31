
DLL_NAME  = "ControlLib"

ctl_codes = """
    CTL_RESULT_SUCCESS = 0x00000000,
    CTL_RESULT_SUCCESS_STILL_OPEN_BY_ANOTHER_CALLER = 0x00000001,
    CTL_RESULT_ERROR_SUCCESS_END = 0x0000FFFF,
    CTL_RESULT_ERROR_GENERIC_START = 0x40000000,
    CTL_RESULT_ERROR_NOT_INITIALIZED = 0x40000001,
    CTL_RESULT_ERROR_ALREADY_INITIALIZED = 0x40000002,
    CTL_RESULT_ERROR_DEVICE_LOST = 0x40000003,
    CTL_RESULT_ERROR_OUT_OF_HOST_MEMORY = 0x40000004,
    CTL_RESULT_ERROR_OUT_OF_DEVICE_MEMORY = 0x40000005,
    CTL_RESULT_ERROR_INSUFFICIENT_PERMISSIONS = 0x40000006,
    CTL_RESULT_ERROR_NOT_AVAILABLE = 0x40000007,
    CTL_RESULT_ERROR_UNINITIALIZED = 0x40000008,
    CTL_RESULT_ERROR_UNSUPPORTED_VERSION = 0x40000009,
    CTL_RESULT_ERROR_UNSUPPORTED_FEATURE = 0x4000000A,
    CTL_RESULT_ERROR_INVALID_ARGUMENT = 0x4000000B,
    CTL_RESULT_ERROR_INVALID_API_HANDLE = 0x4000000C,
    CTL_RESULT_ERROR_INVALID_NULL_HANDLE = 0x4000000D,
    CTL_RESULT_ERROR_INVALID_NULL_POINTER = 0x4000000E,
    CTL_RESULT_ERROR_INVALID_SIZE = 0x4000000F,
    CTL_RESULT_ERROR_UNSUPPORTED_SIZE = 0x40000010,
    CTL_RESULT_ERROR_UNSUPPORTED_IMAGE_FORMAT = 0x40000011,
    CTL_RESULT_ERROR_DATA_READ = 0x40000012,
    CTL_RESULT_ERROR_DATA_WRITE = 0x40000013,
    CTL_RESULT_ERROR_DATA_NOT_FOUND = 0x40000014,
    CTL_RESULT_ERROR_NOT_IMPLEMENTED = 0x40000015,
    CTL_RESULT_ERROR_OS_CALL = 0x40000016,
    CTL_RESULT_ERROR_KMD_CALL = 0x40000017,
    CTL_RESULT_ERROR_UNLOAD = 0x40000018,
    CTL_RESULT_ERROR_ZE_LOADER = 0x40000019,
    CTL_RESULT_ERROR_INVALID_OPERATION_TYPE = 0x4000001A,
    CTL_RESULT_ERROR_NULL_OS_INTERFACE = 0x4000001B,
    CTL_RESULT_ERROR_NULL_OS_ADAPTER_HANDLE = 0x4000001C,
    CTL_RESULT_ERROR_NULL_OS_DISPLAY_OUTPUT_HANDLE = 0x4000001D,
    CTL_RESULT_ERROR_WAIT_TIMEOUT = 0x4000001E,
    CTL_RESULT_ERROR_PERSISTANCE_NOT_SUPPORTED = 0x4000001F,
    CTL_RESULT_ERROR_PLATFORM_NOT_SUPPORTED = 0x40000020,
    CTL_RESULT_ERROR_UNKNOWN_APPLICATION_UID = 0x40000021,
    CTL_RESULT_ERROR_INVALID_ENUMERATION = 0x40000022,
    CTL_RESULT_ERROR_FILE_DELETE = 0x40000023,
    CTL_RESULT_ERROR_RESET_DEVICE_REQUIRED = 0x40000024,
    CTL_RESULT_ERROR_FULL_REBOOT_REQUIRED = 0x40000025,
    CTL_RESULT_ERROR_LOAD = 0x40000026,
    CTL_RESULT_ERROR_UNKNOWN = 0x4000FFFF,
    CTL_RESULT_ERROR_RETRY_OPERATION = 0x40010000,
    CTL_RESULT_ERROR_IGSC_LOADER = 0x40010001,
    CTL_RESULT_ERROR_GENERIC_END = 0x4000FFFF,
    CTL_RESULT_ERROR_CORE_START = 0x44000000,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_NOT_SUPPORTED = 0x44000001,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_VOLTAGE_OUTSIDE_RANGE = 0x44000002,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_FREQUENCY_OUTSIDE_RANGE = 0x44000003,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_POWER_OUTSIDE_RANGE = 0x44000004,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_TEMPERATURE_OUTSIDE_RANGE = 0x44000005,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_IN_VOLTAGE_LOCKED_MODE = 0x44000006,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_RESET_REQUIRED = 0x44000007,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_WAIVER_NOT_SET = 0x44000008,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_DEPRECATED_API = 0x44000009,
    CTL_RESULT_ERROR_CORE_LED_GET_STATE_NOT_SUPPORTED_FOR_I2C_LED = 0x4400000A,
    CTL_RESULT_ERROR_CORE_LED_SET_STATE_NOT_SUPPORTED_FOR_I2C_LED = 0x4400000B,
    CTL_RESULT_ERROR_CORE_LED_TOO_FREQUENT_SET_REQUESTS = 0x4400000C,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_VRAM_MEMORY_SPEED_OUTSIDE_RANGE = 0x4400000D,
    CTL_RESULT_ERROR_CORE_OVERCLOCK_INVALID_CUSTOM_VF_CURVE = 0x4400000E,
    CTL_RESULT_ERROR_CORE_END = 0x0440FFFF,
    CTL_RESULT_ERROR_3D_START = 0x60000000,
    CTL_RESULT_ERROR_3D_END = 0x6000FFFF,
    CTL_RESULT_ERROR_MEDIA_START = 0x50000000,
    CTL_RESULT_ERROR_MEDIA_END = 0x5000FFFF,
    CTL_RESULT_ERROR_DISPLAY_START = 0x48000000,
    CTL_RESULT_ERROR_INVALID_AUX_ACCESS_FLAG = 0x48000001,
    CTL_RESULT_ERROR_INVALID_SHARPNESS_FILTER_FLAG = 0x48000002,
    CTL_RESULT_ERROR_DISPLAY_NOT_ATTACHED = 0x48000003,
    CTL_RESULT_ERROR_DISPLAY_NOT_ACTIVE = 0x48000004,
    CTL_RESULT_ERROR_INVALID_POWERFEATURE_OPTIMIZATION_FLAG = 0x48000005,
    CTL_RESULT_ERROR_INVALID_POWERSOURCE_TYPE_FOR_DPST = 0x48000006,
    CTL_RESULT_ERROR_INVALID_PIXTX_GET_CONFIG_QUERY_TYPE = 0x48000007,
    CTL_RESULT_ERROR_INVALID_PIXTX_SET_CONFIG_OPERATION_TYPE = 0x48000008,
    CTL_RESULT_ERROR_INVALID_SET_CONFIG_NUMBER_OF_SAMPLES = 0x48000009,
    CTL_RESULT_ERROR_INVALID_PIXTX_BLOCK_ID = 0x4800000A,
    CTL_RESULT_ERROR_INVALID_PIXTX_BLOCK_TYPE = 0x4800000B,
    CTL_RESULT_ERROR_INVALID_PIXTX_BLOCK_NUMBER = 0x4800000C,
    CTL_RESULT_ERROR_INSUFFICIENT_PIXTX_BLOCK_CONFIG_MEMORY = 0x4800000D,
    CTL_RESULT_ERROR_3DLUT_INVALID_PIPE = 0x4800000E,
    CTL_RESULT_ERROR_3DLUT_INVALID_DATA = 0x4800000F,
    CTL_RESULT_ERROR_3DLUT_NOT_SUPPORTED_IN_HDR = 0x48000010,
    CTL_RESULT_ERROR_3DLUT_INVALID_OPERATION = 0x48000011,
    CTL_RESULT_ERROR_3DLUT_UNSUCCESSFUL = 0x48000012,
    CTL_RESULT_ERROR_AUX_DEFER = 0x48000013,
    CTL_RESULT_ERROR_AUX_TIMEOUT = 0x48000014,
    CTL_RESULT_ERROR_AUX_INCOMPLETE_WRITE = 0x48000015,
    CTL_RESULT_ERROR_I2C_AUX_STATUS_UNKNOWN = 0x48000016,
    CTL_RESULT_ERROR_I2C_AUX_UNSUCCESSFUL = 0x48000017,
    CTL_RESULT_ERROR_LACE_INVALID_DATA_ARGUMENT_PASSED = 0x48000018,
    CTL_RESULT_ERROR_EXTERNAL_DISPLAY_ATTACHED = 0x48000019,
    CTL_RESULT_ERROR_CUSTOM_MODE_STANDARD_CUSTOM_MODE_EXISTS = 0x4800001A,
    CTL_RESULT_ERROR_CUSTOM_MODE_NON_CUSTOM_MATCHING_MODE_EXISTS = 0x4800001B,
    CTL_RESULT_ERROR_CUSTOM_MODE_INSUFFICIENT_MEMORY = 0x4800001C,
    CTL_RESULT_ERROR_ADAPTER_ALREADY_LINKED = 0x4800001D,
    CTL_RESULT_ERROR_ADAPTER_NOT_IDENTICAL = 0x4800001E,
    CTL_RESULT_ERROR_ADAPTER_NOT_SUPPORTED_ON_LDA_SECONDARY = 0x4800001F,
    CTL_RESULT_ERROR_SET_FBC_FEATURE_NOT_SUPPORTED = 0x48000020,
    CTL_RESULT_ERROR_DISPLAY_END = 0x4800FFFF,
"""

def get_error_code_dict(codes: object) -> dict[str, int]:
    error_code_lines = codes.strip().split('\n')
    error_code_dict = {}

    for line in error_code_lines:
        line = line.strip()
        if '=' in line and '//' not in line:
            name, value = line.split('=', 1)
            name = name.strip()
            value = value.strip().rstrip(',').strip()
            if name.startswith('CTL_RESULT_'):
                error_code_dict[name] = int(value, 0)
    return error_code_dict

CTL_ERROR_CODES =  get_error_code_dict(codes=ctl_codes)

INCLUDE = """

///////////////////////////////////////////////////////////////////////////////
/// @brief ::API初始化与关闭
typedef uint32_t ctl_init_flags_t;

typedef uint32_t ctl_version_info_t;
typedef struct _ctl_application_id_t
{
    uint32_t Data1;                                 ///< [in] Data1
    uint16_t Data2;                                 ///< [in] Data2
    uint16_t Data3;                                 ///< [in] Data3
    uint8_t Data4[8];                               ///< [in] Data4

} ctl_application_id_t;
typedef struct _ctl_init_args_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    ctl_version_info_t AppVersion;                  ///< [in][release] App's IGCL version
    ctl_init_flags_t flags;                         ///< [in][release] Caller version
    ctl_version_info_t SupportedVersion;            ///< [out][release] IGCL implementation version
    ctl_application_id_t ApplicationUID;            ///< [in] Application Provided Unique ID.Application can pass all 0's as
                                                    ///< the default ID

} ctl_init_args_t;
typedef void* ctl_api_handle_t;

int __stdcall ctlInit(
    ctl_init_args_t* pInitDesc,                     ///< [in][out] App's control API version
    ctl_api_handle_t* phAPIHandle                   ///< [in][out][release] Control API handle
    );
int __stdcall ctlClose(
    ctl_api_handle_t hAPIHandle                     ///< [in][release] Control API implementation handle obtained during init
                                                    ///< call
    );

///////////////////////////////////////////////////////////////////////////////
/// @brief ::显卡适配器初始化
typedef void* ctl_device_adapter_handle_t;
int __stdcall ctlEnumerateDevices(
    ctl_api_handle_t hAPIHandle,                    ///< [in][release] Applications should pass the Control API handle returned
                                                    ///< by the CtlInit function
    uint32_t* pCount,                               ///< [in,out][release] pointer to the number of device instances. If count
                                                    ///< is zero, then the api will update the value with the total
                                                    ///< number of drivers available. If count is non-zero, then the api will
                                                    ///< only retrieve the number of drivers.
                                                    ///< If count is larger than the number of drivers available, then the api
                                                    ///< will update the value with the correct number of drivers available.
    ctl_device_adapter_handle_t* phDevices          ///< [in,out][optional][release][range(0, *pCount)] array of driver
                                                    ///< instance handles
    );

///////////////////////////////////////////////////////////////////////////////
/// @brief ::显示器初始化
typedef void* ctl_display_output_handle_t;
int __stdcall ctlEnumerateDisplayOutputs(
    ctl_device_adapter_handle_t hDeviceAdapter,     ///< [in][release] handle to control device adapter
    uint32_t* pCount,                               ///< [in,out][release] pointer to the number of display output instances.
                                                    ///< If count is zero, then the api will update the value with the total
                                                    ///< number of outputs available. If count is non-zero, then the api will
                                                    ///< only retrieve the number of outputs.
                                                    ///< If count is larger than the number of drivers available, then the api
                                                    ///< will update the value with the correct number of drivers available.
    ctl_display_output_handle_t* phDisplayOutputs   ///< [in,out][optional][release][range(0, *pCount)] array of display output
                                                    ///< instance handles
    );

///////////////////////////////////////////////////////////////////////////////
/// @brief ::AUX操作
typedef enum _ctl_operation_type_t
{
    CTL_OPERATION_TYPE_READ = 1,                    ///< Read operation
    CTL_OPERATION_TYPE_WRITE = 2,                   ///< Write operation
    CTL_OPERATION_TYPE_MAX

} ctl_operation_type_t;
typedef enum _ctl_aux_flag_t
{
    CTL_AUX_FLAG_NATIVE_AUX = (1<<0),           ///< For Native AUX operation
    CTL_AUX_FLAG_I2C_AUX = (1<<1),              ///< For I2C AUX operation
    CTL_AUX_FLAG_I2C_AUX_MOT = (1<<2),          ///< For I2C AUX MOT operation
    CTL_AUX_FLAG_MAX = 0x80000000

} ctl_aux_flag_t;
typedef struct _ctl_aux_access_args_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    ctl_operation_type_t OpType;                    ///< [in] Operation type, 1 for Read, 2 for Write, for Write operation, App
                                                    ///< needs to run with admin privileges
    ctl_aux_flag_t Flags;                          ///< [in] Aux Flags. Refer ::ctl_aux_flag_t
    uint32_t Address;                               ///< [in] Address to read or write
    uint64_t RAD;                                   ///< [in] RAD, For Future use, to be used for branch devices, Interface
                                                    ///< will be provided to get RAD
    uint32_t PortID;                                ///< [in] Port ID, For Future use, to be used for SST tiled devices
    uint32_t DataSize;                              ///< [in,out] Valid data size
    uint8_t Data[132];            ///< [in,out] Data array

} ctl_aux_access_args_t;

typedef uint32_t ctl_i2c_flags_t;
typedef struct _ctl_i2c_access_args_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    uint32_t DataSize;                              ///< [in,out] Valid data size
    uint32_t Address;                               ///< [in] Address to read or write
    ctl_operation_type_t OpType;                    ///< [in] Operation type, 1 for Read, 2 for Write, for Write operation, App
                                                    ///< needs to run with admin privileges
    uint32_t Offset;                                ///< [in] Offset
    ctl_i2c_flags_t Flags;                          ///< [in] I2C Flags. Refer ::ctl_i2c_flag_t
    uint64_t RAD;                                   ///< [in] RAD, For Future use, to be used for branch devices, Interface
                                                    ///< will be provided to get RAD
    uint8_t Data[132];            ///< [in,out] Data array

} ctl_i2c_access_args_t;

int __stdcall ctlAUXAccess(
    ctl_display_output_handle_t hDisplayOutput,     ///< [in] Handle to display output
    ctl_aux_access_args_t* pAuxAccessArgs           ///< [in,out] Aux access arguments
    );

///  ===============================================================================
///  ===============================================================================
typedef struct _ctl_generic_void_datatype_t
{
    void* pData;                                    ///< [in,out]void pointer to memory
    uint32_t size;                                  ///< [in,out]size of the allocated memory

} ctl_generic_void_datatype_t;
typedef struct _ctl_revision_datatype_t
{
    uint8_t major_version;                          ///< [in,out]Major Version
    uint8_t minor_version;                          ///< [in,out]Minor Version
    uint8_t revision_version;                       ///< [in,out]Revision Version

} ctl_revision_datatype_t;
typedef union _ctl_os_display_encoder_identifier_t
{
    uint32_t WindowsDisplayEncoderID;               ///< [out] Windows OS Display encoder ID
    ctl_generic_void_datatype_t DisplayEncoderID;   ///< [out] Display encoder ID for non-windows OS

} ctl_os_display_encoder_identifier_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief Various display types
typedef enum _ctl_display_output_types_t
{
    CTL_DISPLAY_OUTPUT_TYPES_INVALID = (1<<0),           ///< Invalid
    CTL_DISPLAY_OUTPUT_TYPES_DISPLAYPORT = (1<<1),       ///< DisplayPort
    CTL_DISPLAY_OUTPUT_TYPES_HDMI = (1<<2),             ///< HDMI
    CTL_DISPLAY_OUTPUT_TYPES_DVI = (1<<3),               ///< DVI
    CTL_DISPLAY_OUTPUT_TYPES_MIPI = (1<<4),             ///< MIPI
    CTL_DISPLAY_OUTPUT_TYPES_CRT = (1<<5),              ///< CRT
    CTL_DISPLAY_OUTPUT_TYPES_MAX

} ctl_display_output_types_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief Supported output bits per color (bpc) bitmasks
typedef uint32_t ctl_output_bpc_flags_t;
typedef enum _ctl_output_bpc_flag_t
{
    CTL_OUTPUT_BPC_FLAG_6BPC = (1<<0),          ///< [out] Is 6bpc supported
    CTL_OUTPUT_BPC_FLAG_8BPC = (1<<1),           ///< [out] Is 8bpc supported
    CTL_OUTPUT_BPC_FLAG_10BPC = (1<<2),         ///< [out] Is 10bpc supported
    CTL_OUTPUT_BPC_FLAG_12BPC = (1<<3),          ///< [out] Is 12bpc supported
    CTL_OUTPUT_BPC_FLAG_MAX = 0x80000000

} ctl_output_bpc_flag_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief Display output features. This will indicate only the high level
///        capabilities
typedef uint32_t ctl_std_display_feature_flags_t;
typedef enum _ctl_std_display_feature_flag_t
{
    CTL_STD_DISPLAY_FEATURE_FLAG_HDCP = (1<<0),  ///< [out] Is HDCP supported
    CTL_STD_DISPLAY_FEATURE_FLAG_HD_AUDIO = (1<<1),  ///< [out] Is HD Audio supported
    CTL_STD_DISPLAY_FEATURE_FLAG_PSR = (1<<2),  ///< [out] Is VESA PSR supported
    CTL_STD_DISPLAY_FEATURE_FLAG_ADAPTIVESYNC_VRR = (1<<3),  ///< [out] Is VESA Adaptive Sync or HDMI VRR supported
    CTL_STD_DISPLAY_FEATURE_FLAG_VESA_COMPRESSION = (1<<4),  ///< [out] Is display compression (VESA DSC) supported
    CTL_STD_DISPLAY_FEATURE_FLAG_HDR = (1<<5),   ///< [out] Is HDR supported
    CTL_STD_DISPLAY_FEATURE_FLAG_HDMI_QMS = (1<<6),  ///< [out] Is HDMI QMS supported
    CTL_STD_DISPLAY_FEATURE_FLAG_HDR10_PLUS_CERTIFIED = (1<<7),  ///< [out] Is HDR10+ certified
    CTL_STD_DISPLAY_FEATURE_FLAG_VESA_HDR_CERTIFIED = (1<<8),   ///< [out] Is VESA HDR certified - for future use
    CTL_STD_DISPLAY_FEATURE_FLAG_MAX = 0x80000000

} ctl_std_display_feature_flag_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief Advanced Graphics Features provided by Intel Graphics Adapter. This
///        will indicate only the high level capabilities
typedef uint32_t ctl_intel_display_feature_flags_t;
typedef enum _ctl_intel_display_feature_flag_t
{
    CTL_INTEL_DISPLAY_FEATURE_FLAG_DPST = (1<<0),    ///< [out] Is DPST supported
    CTL_INTEL_DISPLAY_FEATURE_FLAG_LACE = (1<<1),   ///< [out] Is LACE supported
    CTL_INTEL_DISPLAY_FEATURE_FLAG_DRRS = (1<<2),    ///< [out] Is DRRS supported
    CTL_INTEL_DISPLAY_FEATURE_FLAG_ARC_ADAPTIVE_SYNC_CERTIFIED = (1<<3), ///< [out] Is Intel Arc certified adaptive sync display
    CTL_INTEL_DISPLAY_FEATURE_FLAG_MAX = 0x80000000

} ctl_intel_display_feature_flag_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief Attached Display Mux Type
typedef enum _ctl_attached_display_mux_type_t
{
    CTL_ATTACHED_DISPLAY_MUX_TYPE_NATIVE = 0,       ///< [out] Native DP / HDMI
    CTL_ATTACHED_DISPLAY_MUX_TYPE_THUNDERBOLT = 1,  ///< [out] Thunderbolt
    CTL_ATTACHED_DISPLAY_MUX_TYPE_TYPE_C = 2,       ///< [out] USB Type C
    CTL_ATTACHED_DISPLAY_MUX_TYPE_USB4 = 3,         ///< [out] USB4
    CTL_ATTACHED_DISPLAY_MUX_TYPE_MAX

} ctl_attached_display_mux_type_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief Signal Standard
typedef enum _ctl_signal_standard_type_t
{
    CTL_SIGNAL_STANDARD_TYPE_UNKNOWN = 0,           ///< [out] Unknown Signal Standard
    CTL_SIGNAL_STANDARD_TYPE_CUSTOM = 1,            ///< [out] Custom added timing
    CTL_SIGNAL_STANDARD_TYPE_DMT = 2,               ///< [out] DMT timing
    CTL_SIGNAL_STANDARD_TYPE_GTF = 3,               ///< [out] GTF Timing
    CTL_SIGNAL_STANDARD_TYPE_CVT = 4,               ///< [out] CVT Timing
    CTL_SIGNAL_STANDARD_TYPE_CTA = 5,               ///< [out] CTA Timing
    CTL_SIGNAL_STANDARD_TYPE_MAX

} ctl_signal_standard_type_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief Protocol Converter Location
typedef uint32_t ctl_protocol_converter_location_flags_t;
typedef enum _ctl_protocol_converter_location_flag_t
{
    CTL_PROTOCOL_CONVERTER_LOCATION_FLAG_ONBOARD = (1<<0),   ///< [out] OnBoard Protocol Converter
    CTL_PROTOCOL_CONVERTER_LOCATION_FLAG_EXTERNAL = (1<<1),  ///< [out] External Dongle
    CTL_PROTOCOL_CONVERTER_LOCATION_FLAG_MAX = 0x80000000

} ctl_protocol_converter_location_flag_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief [out] Display Output configuration related flags which indicate how
///        the output pixel stream drive the panel
typedef uint32_t ctl_display_config_flags_t;
typedef enum _ctl_display_config_flag_t
{
    CTL_DISPLAY_CONFIG_FLAG_DISPLAY_ACTIVE = (1<<0), ,///< [out] DisplayActive 0: InActive 1: Active
    CTL_DISPLAY_CONFIG_FLAG_DISPLAY_ATTACHED = (1<<1), ,  ///< [out] DisplayAttached.This Bit indicates if any dongle/display/hub is
                                                    ///< attached to the encoder. 0: Not Attached 1: Attached
    CTL_DISPLAY_CONFIG_FLAG_IS_DONGLE_CONNECTED_TO_ENCODER = (1<<2), ,///< [out] This BIT will be set if a dongle/hub/onboard protocol converter
                                                    ///< , is attached to the encoder
    CTL_DISPLAY_CONFIG_FLAG_DITHERING_ENABLED = (1<<3), , ///< [out] This BIT will be set if dithering is enabled on the encoder
    CTL_DISPLAY_CONFIG_FLAG_MAX = 0x80000000

} ctl_display_config_flag_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief [out] Encoder configuration related flags which indicate how the
///        output pixel stream drive the panel
typedef uint32_t ctl_encoder_config_flags_t;
typedef enum _ctl_encoder_config_flag_t
{
    CTL_ENCODER_CONFIG_FLAG_INTERNAL_DISPLAY = (1<<0),  ///< [out] Internal connection or not
    CTL_ENCODER_CONFIG_FLAG_VESA_TILED_DISPLAY = (1<<1),///< [out] VESA DisplayID based tiled display which is driven by either
                                                    ///< multiple physical connections (DisplayPort SST) or virtual streams
                                                    ///< (DisplayPort MST)
    CTL_ENCODER_CONFIG_FLAG_TYPEC_CAPABLE = (1<<2), ///< [out] This is set if encoder supports type c display
    CTL_ENCODER_CONFIG_FLAG_TBT_CAPABLE = (1<<3),   ///< [out] This is set if encoder supports Thunderbolt display
    CTL_ENCODER_CONFIG_FLAG_DITHERING_SUPPORTED = (1<<4),   ///< [out] This BIT will be set if encoder supports dithering
    CTL_ENCODER_CONFIG_FLAG_VIRTUAL_DISPLAY = (1<<5),   ///< [out] This BIT will be set if this is a virtual display.Hardware based
                                                    ///< features will not be applicable to this display.For collage display
                                                    ///< this will be set for the virtual output created by driver. For split
                                                    ///< display this will be set for the virtual split displays created out of
                                                    ///< one single physical display
    CTL_ENCODER_CONFIG_FLAG_HIDDEN_DISPLAY = (1<<6),///< [out] This BIT will be set if display is hidden from OS
    CTL_ENCODER_CONFIG_FLAG_COLLAGE_DISPLAY = (1<<7),   ///< [out] This BIT will be set if this is a collage display
    CTL_ENCODER_CONFIG_FLAG_SPLIT_DISPLAY = (1<<8), ///< [out] This BIT will be set if this is a split display
    CTL_ENCODER_CONFIG_FLAG_COMPANION_DISPLAY = (1<<9), ///< [out] This BIT will be set if this is a companion display
    CTL_ENCODER_CONFIG_FLAG_MGPU_COLLAGE_DISPLAY = (1<<10), ///< [out] This BIT will be set if this is a Multi GPU collage display
    CTL_ENCODER_CONFIG_FLAG_MAX = 0x80000000

} ctl_encoder_config_flag_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief Display Timing
typedef struct _ctl_display_timing_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    uint64_t PixelClock;                            ///< [out] Pixel Clock in Hz
    uint32_t HActive;                               ///< [out] Horizontal Active
    uint32_t VActive;                               ///< [out] Vertical Active
    uint32_t HTotal;                                ///< [out] Horizontal Total
    uint32_t VTotal;                                ///< [out] Vertical Total
    uint32_t HBlank;                                ///< [out] Horizontal Blank
    uint32_t VBlank;                                ///< [out] Vertical Blank
    uint32_t HSync;                                 ///< [out] Horizontal Blank
    uint32_t VSync;                                 ///< [out] Vertical Blank
    float RefreshRate;                              ///< [out] Refresh Rate
    ctl_signal_standard_type_t SignalStandard;      ///< [out] Signal Standard
    uint8_t VicId;                                  ///< [out] VIC ID for CTA timings

} ctl_display_timing_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief This structure will contain the properties of the display currently
///        attached to the encoder.
typedef struct _ctl_display_properties_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    ctl_os_display_encoder_identifier_t Os_display_encoder_handle;  ///< [out] OS specific Display ID
    ctl_display_output_types_t Type;                ///< [out] Device Type from display HW stand point. If a DisplayPort
                                                    ///< protocol converter is involved, this will indicate it's DisplayPort.
                                                    ///< The protocol converter's output will be available from
                                                    ///< ProtocolConverterOutput field
    ctl_attached_display_mux_type_t AttachedDisplayMuxType; ///< [out] Attached Display Mux Type
    ctl_display_output_types_t ProtocolConverterOutput; ///< [out] Protocol output type which can be used if config flags indicate
                                                    ///< it's a protocol converter. If it's not a protocol converter this will
                                                    ///< be set to CTL_DISPLAY_OUTPUT_TYPES_INVALID
    ctl_revision_datatype_t SupportedSpec;          ///< [out] Supported industry spec version.
    ctl_output_bpc_flags_t SupportedOutputBPCFlags; ///< [out] Supported output bits per color. Refer ::ctl_output_bpc_flag_t.
                                                    ///< This is independent of RGB or YCbCr output.This is the max BPC
                                                    ///< supported.BPC will vary per mode based on restrictions like bandwidth
                                                    ///< and monitor support
    ctl_protocol_converter_location_flags_t ProtocolConverterType;  ///< [out] Currently Active Protocol Converter. Refer
                                                    ///< ::ctl_protocol_converter_location_flag_t
    ctl_display_config_flags_t DisplayConfigFlags;  ///< [out] Output configuration related flags which indicate how the output
                                                    ///< pixel stream drive the panel. Refer ::ctl_display_config_flag_t
    ctl_std_display_feature_flags_t FeatureEnabledFlags;///< [out] Enabled Display features.Refer ::ctl_std_display_feature_flag_t.
    ctl_std_display_feature_flags_t FeatureSupportedFlags;  ///< [out] Display Supported feature.Refer ::ctl_std_display_feature_flag_t
    ctl_intel_display_feature_flags_t AdvancedFeatureEnabledFlags;  ///< [out] Enabled advanced feature.Refer
                                                    ///< ::ctl_intel_display_feature_flag_t.
    ctl_intel_display_feature_flags_t AdvancedFeatureSupportedFlags;///< [out] Supported advanced feature.Refer
                                                    ///< ::ctl_intel_display_feature_flag_t.
    ctl_display_timing_t Display_Timing_Info;       ///< [out] Applied Timing on the Display
    uint32_t ReservedFields[16];                    ///< [out] Reserved field of 64 bytes

} ctl_display_properties_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief Adapter's display encoder properties
typedef struct _ctl_adapter_display_encoder_properties_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    ctl_os_display_encoder_identifier_t Os_display_encoder_handle;  ///< [out] OS specific Display ID
    ctl_display_output_types_t Type;                ///< [out] Device Type from display HW stand point. If a DisplayPort
                                                    ///< protocol converter is involved, this will indicate it's DisplayPort.
                                                    ///< The protocol converter's output will be available from
                                                    ///< ProtocolConverterOutput field
    bool IsOnBoardProtocolConverterOutputPresent;   ///< [out] Protocol output type which can be used if it's a protocol
                                                    ///< converter. If it's not a protocol converter this will be set to
                                                    ///< CTL_DISPLAY_OUTPUT_TYPES_INVALID
    ctl_revision_datatype_t SupportedSpec;          ///< [out] Supported industry spec version
    ctl_output_bpc_flags_t SupportedOutputBPCFlags; ///< [out] Supported output bits per color. Refer ::ctl_output_bpc_flag_t.
                                                    ///< This is independent of RGB or YCbCr output.This is the max BPC
                                                    ///< supported.BPC will vary per mode based on restrictions like bandwidth
                                                    ///< and monitor support
    ctl_encoder_config_flags_t EncoderConfigFlags;  ///< [out] Output configuration related flags which indicate how the output
                                                    ///< pixel stream drive the panel. Refer ::ctl_encoder_config_flag_t
                                                    ///< Note:
                                                    ///<    Virtual = 1: This indicates that its a software display. Hardware
                                                    ///< based features will not be applicable to this display.
                                                    ///<    Collage=1,Virtual=1: Indicates the fake display output created by
                                                    ///< driver which has the combined resolution of multiple physical displays
                                                    ///< involved in collage configuration
                                                    ///<    Collage=1,Virtual=0: Indicates the child physical displays involved
                                                    ///< in a collage configuration. These are real physical outputs
                                                    ///<    Split=1,Virtual=1  : Indicates the fake display output created by
                                                    ///< driver which occupies a portion of a real physical display
                                                    ///<    Split=1,Virtual=0  : Indicates the physical display which got split
                                                    ///< to form multiple split displays
                                                    ///<    Split=1,Collage=1  : Invalid combination
                                                    ///<    MgpuCollage=1,Collage=1,Virtual=1: Indicates the fake display
                                                    ///< output created by driver which has the combined resolution of multiple
                                                    ///< physical displays spread across multiple GPUs involved in Multi-GPU
                                                    ///< collage configuration
                                                    ///<    MgpuCollage=1,Collage=1,Virtual=0: Indicates the child physical
                                                    ///< displays involved in a Multi-GPU collage configuration. These are real
                                                    ///< physical outputs
    ctl_std_display_feature_flags_t FeatureSupportedFlags;  ///< [out] Adapter Supported feature flags. Refer
                                                    ///< ::ctl_std_display_feature_flag_t
    ctl_intel_display_feature_flags_t AdvancedFeatureSupportedFlags;///< [out] Advanced Features Supported by the Adapter. Refer
                                                    ///< ::ctl_intel_display_feature_flag_t
    uint32_t ReservedFields[16];                    ///< [out] Reserved field of 60 bytes

} ctl_adapter_display_encoder_properties_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief Get Device Properties

int __stdcall ctlGetDisplayProperties(
    ctl_display_output_handle_t hDisplayOutput,     ///< [in][release] Handle to display output
    ctl_display_properties_t* pProperties           ///< [in,out][release] Query result for display  properties
    );
///  ===============================================================================
///  ===============================================================================
typedef uint32_t ctl_power_optimization_flags_t;
typedef struct _ctl_power_optimization_caps_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    ctl_power_optimization_flags_t SupportedFeatures;   ///< [out] Supported power optimization features. Refer
                                                    ///< ::ctl_power_optimization_flag_t

} ctl_power_optimization_caps_t;
int __stdcall ctlGetPowerOptimizationCaps(
    ctl_display_output_handle_t hDisplayOutput,     ///< [in][release] Handle to display output
    ctl_power_optimization_caps_t* pPowerOptimizationCaps   ///< [in,out][release] Query result for power optimization features
    );
///  ===============================================================================
///  ===============================================================================
typedef uint32_t ctl_power_optimization_dpst_flags_t;
typedef uint32_t ctl_power_optimization_lrr_flags_t;
typedef struct _ctl_power_optimization_lrr_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    ctl_power_optimization_lrr_flags_t SupportedLRRTypes;   ///< [out] LRR type(s). Refer ::ctl_power_optimization_lrr_flag_t
    ctl_power_optimization_lrr_flags_t CurrentLRRTypes; ///< [in,out] Current enabled LRR type(s) or the LRR type(s) to set to.
                                                    ///< Refer ::ctl_power_optimization_lrr_flag_t
    bool bRequirePSRDisable;                        ///< [out] Require PSR disable for any change in the selected LRR feature.
                                                    ///< Caller can re-enable PSR once the respective LRR feature is
                                                    ///< enable/disabled. E.g. for UBRR based on platform this flag may not be
                                                    ///< set in which case caller doesn't need to do an explicit PSR disable
    uint16_t LowRR;                                 ///< [out] Lowest RR used for LRR functionality if known to source

} ctl_power_optimization_lrr_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief PSR detailed settings
typedef struct _ctl_power_optimization_psr_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    uint8_t PSRVersion;                             ///< [in,out] A value of 1 means PSR1, 2 means PSR2
    bool FullFetchUpdate;                           ///< [in,out] Full fetch and update

} ctl_power_optimization_psr_t;

///////////////////////////////////////////////////////////////////////////////
/// @brief DPST detailed settings
typedef struct _ctl_power_optimization_dpst_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    uint8_t MinLevel;                               ///< [out] Minimum supported aggressiveness level
    uint8_t MaxLevel;                               ///< [out] Maximum supported aggressiveness level
    uint8_t Level;                                  ///< [in,out] Current aggressiveness level to be set
    ctl_power_optimization_dpst_flags_t SupportedFeatures;  ///< [out] Supported features
    ctl_power_optimization_dpst_flags_t EnabledFeatures;///< [in,out] Features enabled or to be enabled. Fill only one feature for
                                                    ///< SET call

} ctl_power_optimization_dpst_t;
typedef enum _ctl_power_optimization_plan_t
{
    CTL_POWER_OPTIMIZATION_PLAN_BALANCED = 0,       ///< Balanced mode
    CTL_POWER_OPTIMIZATION_PLAN_HIGH_PERFORMANCE = 1,   ///< High Performance Mode
    CTL_POWER_OPTIMIZATION_PLAN_POWER_SAVER = 2,    ///< Power Saver Mode
    CTL_POWER_OPTIMIZATION_PLAN_MAX

} ctl_power_optimization_plan_t;
typedef uint32_t ctl_power_optimization_flags_t;
typedef union _ctl_power_optimization_feature_specific_info_t
{
    ctl_power_optimization_lrr_t LRRInfo;           ///< [out] LRR info
    ctl_power_optimization_psr_t PSRInfo;           ///< [in,out] PSR info
    ctl_power_optimization_dpst_t DPSTInfo;         ///< [in,out] DPST info

} ctl_power_optimization_feature_specific_info_t;
typedef enum _ctl_power_source_t
{
    CTL_POWER_SOURCE_AC = 0,                        ///< Power Source AC
    CTL_POWER_SOURCE_DC = 1,                        ///< Power Source DC
    CTL_POWER_SOURCE_MAX

} ctl_power_source_t;
typedef struct _ctl_power_optimization_settings_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    ctl_power_optimization_plan_t PowerOptimizationPlan;///< [in] Power optimization power plan (max power/max perf/balanced)
    ctl_power_optimization_flags_t PowerOptimizationFeature;///< [in] Power optimization feature interested in. Refer
                                                    ///< ::ctl_power_optimization_flag_t
    bool Enable;                                    ///< [in,out] Enable state
    ctl_power_optimization_feature_specific_info_t FeatureSpecificData; ///< [in,out] Data specific to the feature caller is interested in
    ctl_power_source_t PowerSource;                 ///< [in] AC/DC

} ctl_power_optimization_settings_t;
int __stdcall ctlGetPowerOptimizationSetting(
    ctl_display_output_handle_t hDisplayOutput,     ///< [in][release] Handle to display output
    ctl_power_optimization_settings_t* pPowerOptimizationSettings   ///< [in,out][release] Power optimization data to be fetched
    );
///  ===============================================================================
///  ===============================================================================

typedef enum _ctl_device_type_t
{
    CTL_DEVICE_TYPE_GRAPHICS = 1,                   ///< Graphics Device type
    CTL_DEVICE_TYPE_SYSTEM = 2,                     ///< System Device type
    CTL_DEVICE_TYPE_MAX

} ctl_device_type_t;
typedef uint32_t ctl_supported_functions_flags_t;
typedef enum _ctl_supported_functions_flag_t
{
    CTL_SUPPORTED_FUNCTIONS_FLAG_DISPLAY = (1<<0),  ///< [out] Is Display supported
    CTL_SUPPORTED_FUNCTIONS_FLAG_3D = (1<<1),   ///< [out] Is 3D supported
    CTL_SUPPORTED_FUNCTIONS_FLAG_MEDIA = (1<<2),///< [out] Is Media supported
    CTL_SUPPORTED_FUNCTIONS_FLAG_MAX = 0x80000000

} ctl_supported_functions_flag_t;

typedef struct _ctl_firmware_version_t
{
    uint64_t major_version;                         ///< [out] Major version
    uint64_t minor_version;                         ///< [out] Minor version
    uint64_t build_number;                          ///< [out] Build number

} ctl_firmware_version_t;
typedef uint32_t ctl_adapter_properties_flags_t;
typedef enum _ctl_adapter_properties_flag_t
{
    CTL_ADAPTER_PROPERTIES_FLAG_INTEGRATED = (1<<0),///< [out] Is Integrated Graphics adapter
    CTL_ADAPTER_PROPERTIES_FLAG_LDA_PRIMARY = (1<<1),   ///< [out] Is Primary (Lead) adapter in a Linked Display Adapter (LDA)
                                                    ///< chain
    CTL_ADAPTER_PROPERTIES_FLAG_LDA_SECONDARY = (1<<2), ///< [out] Is Secondary (Linked) adapter in a Linked Display Adapter (LDA)
                                                    ///< chain
    CTL_ADAPTER_PROPERTIES_FLAG_MAX = 0x80000000

} ctl_adapter_properties_flag_t;
typedef struct _ctl_adapter_bdf_t
{
    uint8_t bus;                                    ///< [out] PCI Bus Number
    uint8_t device;                                 ///< [out] PCI device number
    uint8_t function;                               ///< [out] PCI function

} ctl_adapter_bdf_t;
typedef struct _ctl_device_adapter_properties_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    void* pDeviceID;                                ///< [in,out] OS specific Device ID
    uint32_t device_id_size;                        ///< [in] size of the device ID
    ctl_device_type_t device_type;                  ///< [out] Device Type
    ctl_supported_functions_flags_t supported_subfunction_flags;///< [out] Supported functions
    uint64_t driver_version;                        ///< [out] Driver version
    ctl_firmware_version_t firmware_version;        ///< [out] Global Firmware version for discrete adapters. Not implemented
    uint32_t pci_vendor_id;                         ///< [out] PCI Vendor ID
    uint32_t pci_device_id;                         ///< [out] PCI Device ID
    uint32_t rev_id;                                ///< [out] PCI Revision ID
    uint32_t num_eus_per_sub_slice;                 ///< [out] Number of EUs per sub-slice
    uint32_t num_sub_slices_per_slice;              ///< [out] Number of sub-slices per slice
    uint32_t num_slices;                            ///< [out] Number of slices
    char name[100];             ///< [out] Device name
    ctl_adapter_properties_flags_t graphics_adapter_properties; ///< [out] Graphics Adapter Properties
    uint32_t Frequency;                             ///< [out] This represents the average frequency an end user may see in the
                                                    ///< typical gaming workload. Also referred as Graphics Clock. Supported
                                                    ///< only for Version > 0
    uint16_t pci_subsys_id;                         ///< [out] PCI SubSys ID, Supported only for Version > 1
    uint16_t pci_subsys_vendor_id;                  ///< [out] PCI SubSys Vendor ID, Supported only for Version > 1
    ctl_adapter_bdf_t adapter_bdf;                  ///< [out] Pci Bus, Device, Function. Supported only for Version > 1
    uint32_t num_xe_cores;                          ///< [out] Number of Xe Cores. Supported only for Version > 2
    char reserved[108];           ///< [out] Reserved

} ctl_device_adapter_properties_t;
int __stdcall ctlGetDeviceProperties(
    ctl_device_adapter_handle_t hDAhandle,          ///< [in][release] Handle to control device adapter
    ctl_device_adapter_properties_t* pProperties    ///< [in,out][release] Query result for device properties
    );
///  ===============================================================================
///  ===============================================================================
int __stdcall ctlSetPowerOptimizationSetting(
    ctl_display_output_handle_t hDisplayOutput,     ///< [in][release] Handle to display output
    ctl_power_optimization_settings_t* pPowerOptimizationSettings   ///< [in][release] Power optimization data to be applied
    );


///  ===============================================================================
///  ===============================================================================
typedef struct _ctl_panel_descriptor_access_args_t
{
    uint32_t Size;                                  ///< [in] size of this structure
    uint8_t Version;                                ///< [in] version of this structure
    ctl_operation_type_t OpType;                    ///< [in] Operation type, 1 for Read, 2 for Write. App needs to run with
                                                    ///< admin privileges for Write operation, Currently only Read operation is
                                                    ///< supported
    uint32_t BlockNumber;                           ///< [in] Block number, Need to provide only if acccessing EDID
    uint32_t DescriptorDataSize;                    ///< [in] Descriptor data size, Should be 0 for querying the size and
                                                    ///< should be DescriptorDataSize derived from query call otherwise
    uint8_t* pDescriptorData;                       ///< [in,out] Panel descriptor data

} ctl_panel_descriptor_access_args_t;

/// @brief Panel Descriptor Access
///
/// @details
///     - The application does EDID or Display ID access
int __stdcall ctlPanelDescriptorAccess(
    ctl_display_output_handle_t hDisplayOutput,     ///< [in] Handle to display output
    ctl_panel_descriptor_access_args_t* pPanelDescriptorAccessArgs  ///< [in,out] Panel descriptor access arguments
    );
///  ===============================================================================
///  ===============================================================================

"""
