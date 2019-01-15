from layer2 import EchoLayer
from yowsup.layers                             import YowParallelLayer
from yowsup.layers.auth                        import YowAuthenticationProtocolLayer
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks               import YowAckProtocolLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.stacks import YowStack
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.stacks import YowStack, YOWSUP_CORE_LAYERS
from yowsup.layers.axolotl                     import AxolotlControlLayer, AxolotlSendLayer, AxolotlReceivelayer
from yowsup.env import YowsupEnv


CREDENTIALS = ("584168161470", "8DJ5dRbEvcKMdaz3iwANs/5B+GM=") # replace with your phone and password

if __name__==  "__main__":
    layers = (
        EchoLayer,
        YowParallelLayer([YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer,
                          YowAckProtocolLayer]),
        AxolotlControlLayer,
        YowParallelLayer((AxolotlSendLayer, AxolotlReceivelayer)),
    ) + YOWSUP_CORE_LAYERS

    stack = YowStack(layers)
    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)         #setting credentials
    print(YowAuthenticationProtocolLayer.PROP_CREDENTIALS)
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])    #whatsapp server address
    print(YowConstants.ENDPOINTS[0])
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)              
    print(YowCoderLayer.PROP_DOMAIN)
    print(YowConstants.DOMAIN)
    stack.setProp(YowCoderLayer.PROP_RESOURCE, YowsupEnv.getCurrent().getResource())          #info about us as WhatsApp client
    print(YowsupEnv.getCurrent().getResource())
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal
    print("hola")
    stack.loop() #this is the program mainloop