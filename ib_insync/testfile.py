from ib_insync import *
import logging
import datetime
import socket
def run_test():
    util.startLoop()
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=19)
    positiondata=ib.positions()
    #for p in positiondata:
     #   print(p)
    #
    orderdata=ib.openTrades()

    for t in orderdata:
        print(t)

    # print("pause")
    # orderdata = ib.orders()
    #
    # for t in orderdata:
    #     print(t)



    tradesdata=ib.trades()


    #ib.reqExecutions()
   # for t in tradesdata:
     #    print(t)
    machine_name = socket.gethostname()
    print("Machine name:", machine_name)

    contract1 = Forex('EURUSD')
    contract2=Stock('7203','SMART','JPY')
    #ib.qualifyContracts(contract1)
    ib.qualifyContracts(contract2)

    #order1 = LimitOrder('SELL', 20000, 1.11)
    algoParams = []
    algoParams.append(TagValue("pctVol", 0.3))
    order2detail=Order(action="BUY",totalQuantity=100,orderType='LMT',lmtPrice=2300,algoStrategy='PctVol',algoParams=algoParams)
    #algoStrategy='PctVol'
    order2 =LimitOrder("BUY",100,2300,algoStrategy='PctVol',algoParams=algoParams,orderRef="IOItest",transmit=True )
    order3 = LimitOrder("BUY", 100, 2250, algoStrategy='PctVol', algoParams=algoParams,orderRef="IOItest2", transmit=False)
    order2.account="DU7226209"
    order3.account = "DU7226209"

    #account_summary=ib.accountSummary()
    #for acc in account_summary:
     #       print(acc)

    #order2 = LimitOrder(order2detail)
    #trade1=ib.placeOrder(contract1,order1)
    #ib.orderStatusEvent += orderStatusHandler
    trade2 = ib.placeOrder(contract2, order2)

    trade3 = ib.placeOrder(contract2, order3)


    #trade3 = ib.placeOrder(contract2, order3)
    ib.sleep(1)
    #trade1.log
    # portfoliodata=ib.portfolio()
    # for p in portfoliodata:
    #     print(p)

    #fillsdata = ib.fills()
    #
    # for f in fillsdata:
    #     print(f)

    a=2
    ib.disconnect()

    ib.orderStatusEvent

def orderStatusHandler(order, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld):
    print("Order Status Update:")
    print(f"Order: {order}, Status: {status}, Filled: {filled}, Remaining: {remaining}, AvgFillPrice: {avgFillPrice}")


if __name__ == '__main__':
    currentdate = datetime.datetime.now()
    logging.basicConfig(filename='C:\Work\logs\IBTest' + currentdate.strftime("%Y-%m-%d") + '.log', level=logging.INFO)
    run_test()