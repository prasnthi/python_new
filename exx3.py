try:  
    raise Exception(2000)  
except Exception as ae:  
    print "Received error:", ae.data  


