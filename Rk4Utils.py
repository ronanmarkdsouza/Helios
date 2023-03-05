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

    def __init__(self, udot,vdot,wdot,rdot,qdot,pdot,phidot,thetadot,psidot,xedot,yedot,zedot):
        self.udot = udot
        self.vdot = vdot
        self.wdot = wdot
        self.rdot = rdot
        self.qdot = qdot
        self.pdot = pdot
        self.phidot = phidot
        self.thetadot = thetadot
        self.psidot = psidot
        self.xedot = xedot
        self.yedot = yedot
        self.zedot = zedot