#!/usr/bin/env python2
import signal

from twisted.internet import reactor, defer
from txdbus import client, objects, error
from txdbus.interface import DBusInterface, Method

import logging
from dbus_rfm_69 import *

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
th = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
th.setFormatter(formatter)
logger.addHandler(th)

@defer.inlineCallbacks
def run():
	try:
		conn = yield client.connect(reactor)
		conn.exportObject(Rfm69DBusService(PROTOCOL_PATH))
		yield conn.requestBusName(BUS_NAME)
		logger.debug("Object exported on bus name {} with path {}" \
			.format(BUS_NAME, PROTOCOL_PATH))
		
		# Register in ProtocolManager
# 		try:
# 			manager = yield conn.getRemoteObject("org.eclipse.agail.ProtocolManager",
# 												"/org/eclipse/agail/ProtocolManager")
# 			yield manager.callRemote("Add", "RFM69")
# 			logger.debug("Registered protocol with ProtocolManager")
# 		except Exception:
# 			logger.exception("Failed to register with ProtocolManager")

	except Exception:
		logger.exception("Failed to export object: ")
		reactor.stop()

def main():
	reactor.callWhenRunning(run)
	reactor.run()
	
if __name__ == '__main__':
	main()
