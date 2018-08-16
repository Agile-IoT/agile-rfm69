"""
Settings below copied from RadioHead RG_RF69.h
"""
RH_RF69_DATAMODUL_DATAMODE = 0x60
RH_RF69_DATAMODUL_DATAMODE_PACKET = 0x00
RH_RF69_DATAMODUL_DATAMODE_CONT_WITH_SYNC = 0x40
RH_RF69_DATAMODUL_DATAMODE_CONT_WITHOUT_SYNC = 0x60
RH_RF69_DATAMODUL_MODULATIONTYPE = 0x18
RH_RF69_DATAMODUL_MODULATIONTYPE_FSK = 0x00
RH_RF69_DATAMODUL_MODULATIONTYPE_OOK = 0x08
RH_RF69_DATAMODUL_MODULATIONSHAPING = 0x03
RH_RF69_DATAMODUL_MODULATIONSHAPING_FSK_NONE = 0x00
RH_RF69_DATAMODUL_MODULATIONSHAPING_FSK_BT1_0 = 0x01
RH_RF69_DATAMODUL_MODULATIONSHAPING_FSK_BT0_5 = 0x02
RH_RF69_DATAMODUL_MODULATIONSHAPING_FSK_BT0_3 = 0x03
RH_RF69_DATAMODUL_MODULATIONSHAPING_OOK_NONE = 0x00
RH_RF69_DATAMODUL_MODULATIONSHAPING_OOK_BR = 0x01
RH_RF69_DATAMODUL_MODULATIONSHAPING_OOK_2BR = 0x02

CONFIG_FSK = RH_RF69_DATAMODUL_DATAMODE_PACKET | RH_RF69_DATAMODUL_MODULATIONTYPE_FSK | RH_RF69_DATAMODUL_MODULATIONSHAPING_FSK_NONE
CONFIG_GFSK = RH_RF69_DATAMODUL_DATAMODE_PACKET | RH_RF69_DATAMODUL_MODULATIONTYPE_FSK | RH_RF69_DATAMODUL_MODULATIONSHAPING_FSK_BT1_0
CONFIG_OOK = RH_RF69_DATAMODUL_DATAMODE_PACKET | RH_RF69_DATAMODUL_MODULATIONTYPE_OOK | RH_RF69_DATAMODUL_MODULATIONSHAPING_OOK_NONE
CONFIG_WHITE = 0xD0

MODEM_CONFIG_TABLE = \
{
	#  02,		03,   04,   05,   06,   19,   1a,  37
	# FSK, No Manchester, no shaping, whitening, CRC, no address filtering
	# AFC BW == RX BW == 2 x bit rate
	# Low modulation indexes of ~ 1 at slow speeds do not seem to work very well. Choose MI of 2.
	"FSK_Rb2Fd5": [CONFIG_FSK,  0x3e, 0x80, 0x00, 0x52, 0xf4, 0xf4, CONFIG_WHITE], 
	"FSK_Rb2_4Fd4_8": [CONFIG_FSK,  0x34, 0x15, 0x00, 0x4f, 0xf4, 0xf4, CONFIG_WHITE], 
	"FSK_Rb4_8Fd9_6": [CONFIG_FSK,  0x1a, 0x0b, 0x00, 0x9d, 0xf4, 0xf4, CONFIG_WHITE], 

	"FSK_Rb9_6Fd19_2": [CONFIG_FSK,  0x0d, 0x05, 0x01, 0x3b, 0xf4, 0xf4, CONFIG_WHITE], 
	"FSK_Rb19_2Fd38_4": [CONFIG_FSK,  0x06, 0x83, 0x02, 0x75, 0xf3, 0xf3, CONFIG_WHITE], 
	"FSK_Rb38_4Fd76_8": [CONFIG_FSK,  0x03, 0x41, 0x04, 0xea, 0xf2, 0xf2, CONFIG_WHITE], 

	"FSK_Rb57_6Fd120": [CONFIG_FSK,  0x02, 0x2c, 0x07, 0xae, 0xe2, 0xe2, CONFIG_WHITE], 
	"FSK_Rb125Fd125": [CONFIG_FSK,  0x01, 0x00, 0x08, 0x00, 0xe1, 0xe1, CONFIG_WHITE], 
	"FSK_Rb250Fd250": [CONFIG_FSK,  0x00, 0x80, 0x10, 0x00, 0xe0, 0xe0, CONFIG_WHITE], 
	"FSK_Rb55555Fd50": [CONFIG_FSK,  0x02, 0x40, 0x03, 0x33, 0x42, 0x42, CONFIG_WHITE], 

	#  02,		03,   04,   05,   06,   19,   1a,  37
	# GFSK (BT=1.0), No Manchester, whitening, CRC, no address filtering
	# AFC BW == RX BW == 2 x bit rate
	"GFSK_Rb2Fd5": [CONFIG_GFSK, 0x3e, 0x80, 0x00, 0x52, 0xf4, 0xf5, CONFIG_WHITE], 
	"GFSK_Rb2_4Fd4_8": [CONFIG_GFSK, 0x34, 0x15, 0x00, 0x4f, 0xf4, 0xf4, CONFIG_WHITE], 
	"GFSK_Rb4_8Fd9_6": [CONFIG_GFSK, 0x1a, 0x0b, 0x00, 0x9d, 0xf4, 0xf4, CONFIG_WHITE], 

	"GFSK_Rb9_6Fd19_2": [CONFIG_GFSK, 0x0d, 0x05, 0x01, 0x3b, 0xf4, 0xf4, CONFIG_WHITE], 
	"GFSK_Rb19_2Fd38_4": [CONFIG_GFSK, 0x06, 0x83, 0x02, 0x75, 0xf3, 0xf3, CONFIG_WHITE], 
	"GFSK_Rb38_4Fd76_8": [CONFIG_GFSK, 0x03, 0x41, 0x04, 0xea, 0xf2, 0xf2, CONFIG_WHITE], 

	"GFSK_Rb57_6Fd120": [CONFIG_GFSK, 0x02, 0x2c, 0x07, 0xae, 0xe2, 0xe2, CONFIG_WHITE], 
	"GFSK_Rb125Fd125": [CONFIG_GFSK, 0x01, 0x00, 0x08, 0x00, 0xe1, 0xe1, CONFIG_WHITE], 
	"GFSK_Rb250Fd250": [CONFIG_GFSK, 0x00, 0x80, 0x10, 0x00, 0xe0, 0xe0, CONFIG_WHITE], 
	"GFSK_Rb55555Fd50 ": [CONFIG_GFSK, 0x02, 0x40, 0x03, 0x33, 0x42, 0x42, CONFIG_WHITE], 

	#  02,		03,   04,   05,   06,   19,   1a,  37
	# OOK, No Manchester, no shaping, whitening, CRC, no address filtering
	# with the help of the SX1231 configuration program
	# AFC BW == RX BW
	# All OOK configs have the default:
	# Threshold Type": Peak
	# Peak Threshold Step": 0.5dB
	# Peak threshiold dec": ONce per chip
	# Fixed threshold": 6dB
	"OOK_Rb1Bw1": [CONFIG_OOK,  0x7d, 0x00, 0x00, 0x10, 0x88, 0x88, CONFIG_WHITE], 
	"OOK_Rb1_2Bw75": [CONFIG_OOK,  0x68, 0x2b, 0x00, 0x10, 0xf1, 0xf1, CONFIG_WHITE], 
	"OOK_Rb2_4Bw4_8": [CONFIG_OOK,  0x34, 0x15, 0x00, 0x10, 0xf5, 0xf5, CONFIG_WHITE], 
	"OOK_Rb4_8Bw9_6": [CONFIG_OOK,  0x1a, 0x0b, 0x00, 0x10, 0xf4, 0xf4, CONFIG_WHITE], 
	"OOK_Rb9_6Bw19_2": [CONFIG_OOK,  0x0d, 0x05, 0x00, 0x10, 0xf3, 0xf3, CONFIG_WHITE], 
	"OOK_Rb19_2Bw38_4": [CONFIG_OOK,  0x06, 0x83, 0x00, 0x10, 0xf2, 0xf2, CONFIG_WHITE], 
	"OOK_Rb32Bw64": [CONFIG_OOK,  0x03, 0xe8, 0x00, 0x10, 0xe2, 0xe2, CONFIG_WHITE], 

	#	"works: Rb1200 Fd 5000 bw10000, DCC 400": { CONFIG_FSK,  0x68, 0x2b, 0x00, 0x52, 0x55, 0x55, CONFIG_WHITE}, 
	#	"works 10/40/80": { CONFIG_FSK,  0x0c, 0x80, 0x02, 0x8f, 0x52, 0x52, CONFIG_WHITE}, 
	#	"works 10/40/40": { CONFIG_FSK,  0x0c, 0x80, 0x02, 0x8f, 0x53, 0x53, CONFIG_WHITE},
}

MODEM_CONFIG = "GFSK_Rb250Fd250" # <-default used in RFM69 lib but FSK_Rb55555Fd50 is better...
MODEM_KEY = "0123456789012345"

BUS_NAME = "iot.agile.Protocol"
PROTOCOL_NAME = "RFM69"
PROTOCOL_PATH = "/iot/agile/Protocol/" + PROTOCOL_NAME + "/socket0"

CHANNEL = 1
RECEIVE_TIMEOUT = 15