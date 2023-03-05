class Rk4Utils():
    udot = 0
    vdot = 0
    wdot = 0
    rdot = 0
    qdot = 0
    pdot = 0
    phidot = 0
    thetadot = 0
    psidot = 0
    xedot = 0
    yedot = 0
    zedot = 0

    def __init__(self, args):
        self.udot = args[0]
        self.vdot = args[1]
        self.wdot = args[2]
        self.rdot = args[3]
        self.qdot = args[4]
        self.pdot = args[5]
        self.phidot = args[6]
        self.thetadot = args[7]
        self.psidot = args[8]
        self.xedot = args[9]
        self.yedot = args[10]
        self.zedot = args[11]