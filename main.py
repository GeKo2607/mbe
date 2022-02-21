import sys
import time
import datetime

sys.path.insert(0, "..")


from opcua import ua, Server


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://localhost:9999/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    Scanner = objects.add_object('ns=2; s="Scanner1"', "Barcodescanner Prototype")
    Matnmb = Scanner.add_variable('ns=2; s="Scanner1_Materialnumber"', "Materialnummer", 0)
    Time = Scanner.add_variable('ns=2; s="Scanner1_Datetime"', "Zeitpunkt", datetime.datetime.now())
    Station_ID = Scanner.add_variable('ns=2; s="Scanner1_Station_ID"', "Stationsnummer", 1)
    
        
    # starting!
    try:
        print("Start Server")
        server.start()
        print("Server Online")


        while True:
            Materialnummer = input()
            Matnmb.set_value(Materialnummer)
            time = datetime.datetime.now()
            Time.set_value(time)
            Stationsnummer = 1
            Station_ID.set_value(Stationsnummer)
            print("Materialnummer: " , Materialnummer, " Datum: ", time, " Stationsnummer: ", Stationsnummer)           

    finally:
    #close connection, remove subcsriptions, etc
        server.stop()
        print("Server Offline")

