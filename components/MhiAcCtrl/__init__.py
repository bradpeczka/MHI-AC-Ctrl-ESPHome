import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID
from esphome.components import climate

AUTO_LOAD = ["sensor", "climate", "text_sensor", "binary_sensor"]
CONF_MHI_AC_CTRL_ID = "mhi_ac_ctrl_id"
CONF_FRAME_SIZE = 'frame_size'
CONF_ROOM_TEMP_TIMEOUT = 'room_temp_timeout'
CONF_VANES_UD = 'vanes_ud'
CONF_VANES_LR = 'vanes_lr'

mhiacctrl = cg.esphome_ns.namespace('mhiacctrl')
MhiAcCtrl = cg.global_ns.class_('MhiAcCtrl', cg.Component, climate.Climate)

CONF_MOSI_PIN = "mosi_pin"
CONF_MISO_PIN = "miso_pin"
CONF_SCLK_PIN = "sclk_pin"
CONF_CS_IN_PIN = "cs_in_pin"
CONF_CS_OUT_PIN = "cs_out_pin"

CONF_HARDWARE_SPI = "hardware_spi"

TYPES = [
    CONF_MOSI_PIN,
    CONF_MISO_PIN,
    CONF_SCLK_PIN,
    CONF_CS_IN_PIN,
    CONF_CS_OUT_PIN,
]

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(MhiAcCtrl),
    cv.Optional(CONF_FRAME_SIZE, default=20): cv.int_range(min=20, max=33),
    cv.Optional(CONF_ROOM_TEMP_TIMEOUT, default=60): cv.int_range(min=0, max=3600),
    cv.Optional(CONF_VANES_UD, default=0): cv.int_range(min=0, max=5),
    cv.Optional(CONF_VANES_LR, default=0): cv.int_range(min=0, max=8),
    cv.Optional(CONF_MOSI_PIN, default="GPIO7"): pins.gpio_input_pin_schema,
    cv.Optional(CONF_MISO_PIN, default="GPIO2"): pins.gpio_output_pin_schema,
    cv.Optional(CONF_SCLK_PIN, default="GPIO6"): pins.gpio_input_pin_schema,
    cv.Optional(CONF_CS_IN_PIN, default="GPIO10"): pins.gpio_input_pin_schema,
    cv.Optional(CONF_CS_OUT_PIN, default="GPIO9"): pins.gpio_output_pin_schema,
    cv.Optional(CONF_HARDWARE_SPI, default=True): cv.boolean,
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    cg.add(var.set_frame_size(config[CONF_FRAME_SIZE]))
    cg.add(var.set_room_temp_api_timeout(config[CONF_ROOM_TEMP_TIMEOUT]))
    cg.add(var.set_vanes(config[CONF_VANES_UD]))
    cg.add(var.set_vanesLR(config[CONF_VANES_LR]))
    cg.add(var.set_mosi_pin(CONF_MOSI_PIN))
    cg.add(var.set_miso_pin(CONF_MISO_PIN))
    cg.add(var.set_sclk_pin(CONF_SCLK_PIN))
    cg.add(var.set_cs_in_pin(CONF_CS_IN_PIN))
    cg.add(var.set_cs_out_pin(CONF_CS_OUT_PIN))
    cg.add(var.set_hardware_spi(CONF_CS_OUT_PIN))
    cg.add(var.get_binary_sensors())