def smpl_rprt(smpl_vrbl):
    
    pass
def advnc_rprt(advnc_vrbl):
    pass
def data_rprt(data_vrbl):
    pass

def rprt(vrbl,chs=0):
    #The function defines
    #What type debug choose you
    if chs == "simple":
        vr_report = smpl_rprt(vrbl)
    elif chs == "avdanced":
        vr_report = advnc_rprt(vrbl)
    elif chs == "data":
        vr_report = data_rprt(vrbl)
    else:
        vr_report = smpl_rprt(vrbl)
    return print(vr_report)
