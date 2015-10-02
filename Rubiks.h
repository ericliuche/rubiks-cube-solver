const unsigned char ARM0T = 0;
const unsigned char ARM0B = 168;
const unsigned char ARM0TM = 88;
const unsigned char ARM0M = 84;
const unsigned char TRACK0MAX = 62;
const unsigned char TRACK0MIN = 117;

const unsigned char ARM1T = 163;
const unsigned char ARM1B = 9;
const unsigned char ARM1M = 84;
const unsigned char ARM1TM = 78;
const unsigned char TRACK1MAX = 30;
const unsigned char TRACK1MIN = 86;

const unsigned char ARM2T = 180;
const unsigned char ARM2B = 14;
const unsigned char ARM2M = 97;
const unsigned char ARM2TM = 90;
const unsigned char TRACK2MAX = 75;
const unsigned char TRACK2MIN = 131;

const unsigned char ARM3T = 11;
const unsigned char ARM3B = 174;
const unsigned char ARM3M = 88;
const unsigned char ARM3TM = 93;
const unsigned char TRACK3MAX = 49;
const unsigned char TRACK3MIN = 122;

const char ON = 1;
const char OFF = 0;

const char B = 0;
const char R = 1;
const char F = 2;
const char L = 3;
const char BP = 4;
const char RP = 5;
const char FP = 6;
const char LP = 7;
const char BD = 8;
const char RD = 9;
const char FD = 10;
const char LD = 11;
    
const char BF = 12;
const char BPF = 13;
const char BFP = 14;
const char BPFP = 15;
const char BDF = 16;
const char BFD = 17;
const char BDFD = 18;
const char BPFD = 19;
const char BDFP = 20;
    
const char RL = 21;
const char RPL = 22;
const char RLP = 23;
const char RPLP = 24;
const char RDL = 25;
const char RLD = 26;
const char RDLD = 27;
const char RPLD = 28;
const char RDLP = 29;
    
const char RY = 30;
const char RDY = 31;
const char LPY = 32;
const char LDY = 33; 
    
const char BPX = 34;
const char BDX = 35;
const char FX = 36;
const char FDX = 37;
    
const char BPFX = 38;
const char BDFX = 39;
const char BDFDX = 40;
const char BPFDX = 41;
    
const char RLPY = 42;
const char RLDY = 43;
const char RDLDY = 44;
const char RDLPY = 45;
    
const char X = 46;
const char Y = 47;
const char MID = 50;
const char TOP = 51;
const char BOT = 52;
const char TM = 53;

const unsigned char PRIME = 54;
const unsigned char NONE = 55;
const unsigned char DOUBLE = 56;

//const short SLIDEOFF = 75;
//const short SLIDECOMP = 210;
//const short TURN = 320;
//const short TURNDOUBLE = 610;

const short SLIDEOFF = 150;
const short SLIDECOMP = 350;
const short TURN = 450;
const short TURNDOUBLE = 1000;

//opposite arms must spin in the same direction
//max for track is defined as position of gripping cube
//0 and 2 are opposite, 1 and 3 are opposite, labeled clockwise


#include <Servo.h> 

class Arm {
  public: 
    unsigned char t;
    unsigned char m;
    unsigned char b;
    unsigned char tm;
    Servo control;
    void turn(char turnTo);
};

class Track {
  public:
    unsigned char on;
    unsigned char off;
    Servo control;
    void slide(char slideTo);
};

