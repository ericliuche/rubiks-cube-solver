
#include <Servo.h> 
#include "Rubiks.h"
#include <string.h>

Arm arm0, arm1, arm2, arm3;
Track track0, track1, track2, track3;
Arm arms[4];
Track tracks[4];
 
void setup() 
{ 
  //initiate to place cube
  arm0.control.attach(8);
  arm0.control.write(ARM0T);
  arm1.control.attach(9);
  arm1.control.write(ARM1T);
  arm2.control.attach(2);
  arm2.control.write(ARM2T);
  arm3.control.attach(3);
  arm3.control.write(ARM3T);
  
  track0.control.attach(4);
  track0.control.write(TRACK0MIN);
  track1.control.attach(5);
  track1.control.write(TRACK1MIN);
  track2.control.attach(6);
  track2.control.write(TRACK2MIN);
  track3.control.attach(7);
  track3.control.write(TRACK3MIN);
  
  //attach all variables
  arm0.t = ARM0T;
  arm0.m = ARM0M;
  arm0.b = ARM0B;
  arm0.tm = ARM0TM;
  track0.on = TRACK0MAX;
  track0.off = TRACK0MIN;

  arm1.t = ARM1T;
  arm1.m = ARM1M;
  arm1.b = ARM1B;
  arm1.tm = ARM1TM;
  track1.on = TRACK1MAX;
  track1.off = TRACK1MIN;

  arm2.t = ARM2T;
  arm2.m = ARM2M;
  arm2.b = ARM2B;
  arm2.tm = ARM2TM;
  track2.on = TRACK2MAX;
  track2.off = TRACK2MIN;

  arm3.t = ARM3T;
  arm3.m = ARM3M;
  arm3.b = ARM3B;
  arm3.tm = ARM3TM;
  track3.on = TRACK3MAX;
  track3.off = TRACK3MIN;   
  
  //setup 
  arms[0] = arm0; arms[1] = arm1; arms[2] = arm2; arms[3] = arm3;
  tracks[0] = track0; tracks[1] = track1; tracks[2] = track2; tracks[3] = track3;
  delay(1000);
  
  
  start();
  Serial.begin(9600);
  //['X', 'B', 'LPY', 'L', 'BDF', 'L', 'BD', 'RY', 'L', 'FP', 'RDLPY', 'LD', 'FD', 'RD', 'FP', 'LD', 'BP', 'LDY', 'LD', 'B']
  int input[24] = {46, 35, 0, 32, 5, 46, 15, 32, 7, 2, 9, 10, 5, 46, 6, 11, 0, 46, 10, 33, 30, 9, 35, 6};
  for (int i = 0; i < 24; i++){
    turn(input[i]); 
  }
} 
 
 
void loop() 
{ 
//  int input;
// input = Serial.parseInt();
//  turn(input);
} 

//turns arm to position 
void Arm::turn(char turnTo)
{
  if (turnTo == TOP) {control.write(t);}
  else if (turnTo ==  BOT) {control.write(b);}
  else if (turnTo == MID) {control.write(m);}
  else if (turnTo == TM) {control.write(tm);}
}

//slides track to position
void Track::slide(char slideTo)
{
  if (slideTo == ON) {control.write(on);}
  else if (slideTo == OFF) {control.write(off);}
}


void start(void)
{
  delay(2000);
  tracks[0].slide(ON); tracks[2].slide(ON);
  delay(2000);
  tracks[1].slide(ON); tracks[3].slide(ON);
  delay(2000);
}


//input char to turn cube in desired manner
void turn(int commands)
{
  int command = commands;
  switch (command){
    
    //single face turns
    case B: singleturn(B, NONE); break;
    case R: singleturn(R, NONE); break;
    case F: singleturn(F, NONE); break;
    case L: singleturn(L, NONE); break;
    case BP: singleturn(B, PRIME); break;
    case RP: singleturn(R, PRIME); break;
    case FP: singleturn(F, PRIME); break;
    case LP: singleturn(L, PRIME); break;
    case BD: singleturn(B, DOUBLE); break;
    case RD: singleturn(R, DOUBLE); break;
    case FD: singleturn(F, DOUBLE); break;
    case LD: singleturn(L, DOUBLE); break;
    
    //syncrhonized double face turns
    case BF: doubleturn(B, NONE, NONE); break;
    case BPF: doubleturn(B, PRIME, NONE); break;
    case BFP: doubleturn(B, NONE, PRIME); break;
    case BPFP: doubleturn(B, PRIME, PRIME); break;
    case BDF: doubleturn(B, DOUBLE, NONE); break;
    case BFD: doubleturn(B, NONE, DOUBLE); break;
    case BDFD: doubleturn(B, DOUBLE, DOUBLE); break;
    case BPFD: doubleturn(B, PRIME, DOUBLE); break;
    case BDFP: doubleturn(B, DOUBLE, PRIME); break;
    
    case RL: doubleturn(R, NONE, NONE); break;
    case RPL: doubleturn(R, PRIME, NONE); break;
    case RLP: doubleturn(R, NONE, PRIME); break;
    case RPLP: doubleturn(R, PRIME, PRIME); break;
    case RDL: doubleturn(R, DOUBLE, NONE); break;
    case RLD: doubleturn(R, NONE, DOUBLE); break;
    case RDLD: doubleturn(R, DOUBLE, DOUBLE); break;
    case RPLD: doubleturn(R, PRIME, DOUBLE); break;
    case RDLP: doubleturn(R, DOUBLE, PRIME); break;
    
    //single face turn with cube turn
    case RY: faceturn(R, NONE); break;
    case RDY: faceturn(R, DOUBLE); break;
    case LPY: faceturn(L, PRIME); break;
    case LDY: faceturn(L, DOUBLE); break;
    
    case BPX: faceturn(B, NONE); break;
    case BDX: faceturn(B, DOUBLE); break;
    case FX: faceturn(F, NONE); break;
    case FDX: faceturn(F, DOUBLE); break;
    
    //synchronized double face turns with cube turn
    case BPFX: doublefaceturn(B, PRIME, NONE); break;
    case BDFX: doublefaceturn(B, DOUBLE, NONE); break;
    case BDFDX: doublefaceturn(B, DOUBLE, DOUBLE); break;
    case BPFDX: doublefaceturn(B, PRIME, DOUBLE); break;
    
    case RLPY: doublefaceturn(R, NONE, PRIME); break;
    case RLDY: doublefaceturn(R, NONE, DOUBLE); break;
    case RDLDY: doublefaceturn(R, DOUBLE, DOUBLE); break;
    case RDLPY: doublefaceturn(R, DOUBLE, PRIME); break;
    
    //cube turn
    case X:cubeturn(X); break;
    case Y:cubeturn(Y); break;
    case 100: arm0.control.detach(); arm1.control.detach(); arm2.control.detach(); arm3.control.detach(); 
              track0.control.detach(); track1.control.detach(); track2.control.detach(); track3.control.detach(); break;
    
    default: break;
  }
}

void singleturn(char face, char modifier)
{  
    if (face == B || face == L) {
        if (modifier == PRIME) {modifier = NONE;}
        else if (modifier == NONE) {modifier = PRIME;}
    }    
    if (modifier == PRIME){
      tracks[face].slide(OFF);
      delay(SLIDEOFF);
      arms[face].turn(MID);
      delay(TURN);
      tracks[face].slide(ON);  
      delay(SLIDECOMP);
      arms[face].turn(TOP);
      delay(TURN);
    }
    else if (modifier == DOUBLE){
      arms[face].turn(BOT);
      delay(TURNDOUBLE);
      tracks[face].slide(OFF);
      delay(SLIDEOFF);
      arms[face].turn(TOP);
      delay(TURNDOUBLE);
      tracks[face].slide(ON);  
      delay(SLIDECOMP);
    }
    else{  
      arms[face].turn(TM);
      delay(TURN);
      tracks[face].slide(OFF);
      delay(SLIDEOFF);
      arms[face].turn(TOP);
      delay(TURN);
      tracks[face].slide(ON);  
      delay(SLIDECOMP);
    }
}

void doubleturn(char face, char modifier1, char modifier2) //use lower face
{
  char face2 = face+2;
  if (face == B || face == L) {
    if (modifier1 == PRIME) {modifier1 = NONE;}
    else if (modifier1 == NONE) {modifier1 = PRIME;}
  }    
  if (face2  == B ||face2 == L) {
    if (modifier2 == PRIME) {modifier2 = NONE;}
    else if (modifier2 == NONE) {modifier2 = PRIME;}
  }
  if (modifier1 == DOUBLE && modifier2 == DOUBLE)  //1
  {
      arms[face].turn(BOT); arms[face2].turn(BOT); 
      delay(TURNDOUBLE);
      tracks[face].slide(OFF); tracks[face2].slide(OFF);
      delay(SLIDEOFF);
      arms[face].turn(TOP); arms[face2].turn(TOP);
      delay(TURNDOUBLE);
      tracks[face].slide(ON); tracks[face2].slide(ON);
      delay(SLIDECOMP);
  }
  else if (modifier1 == PRIME && modifier2 == PRIME) //2
  {
      tracks[face].slide(OFF); tracks[face2].slide(OFF);
      delay(SLIDEOFF);
      arms[face].turn(MID); arms[face2].turn(MID);
      delay(TURN);
      tracks[face].slide(ON); tracks[face2].slide(ON);
      delay(SLIDECOMP);
      arms[face].turn(TOP); arms[face2].turn(TOP);
      delay(TURN);
  }
  else if (modifier1 == NONE && modifier2 == NONE) //3
  {
      arms[face].turn(TM); arms[face2].turn(TM);
      delay(TURN);
      tracks[face].slide(OFF); tracks[face2].slide(OFF);
      delay(SLIDEOFF);
      arms[face].turn(TOP); arms[face2].turn(TOP);
      delay(TURN);
      tracks[face].slide(ON); tracks[face2].slide(ON);
      delay(SLIDECOMP);
  }
  else if ((modifier1 == NONE && modifier2 == PRIME)||(modifier1 == PRIME && modifier2 == NONE)) //4
  {
      if (modifier1 == PRIME) {face2-=2; face+=2;}
      arms[face].turn(TM); tracks[face2].slide(OFF);
      delay(TURN);
      tracks[face].slide(OFF); arms[face2].turn(MID);
      delay(TURN);
      arms[face].turn(TOP); tracks[face2].slide(ON);
      delay(SLIDECOMP);
      tracks[face].slide(ON); arms[face2].turn(TOP);
      delay(SLIDECOMP);
  }
  else if ((modifier1 == DOUBLE && modifier2 == NONE)||(modifier1 == NONE && modifier2 == DOUBLE))//6
  {
      if (modifier1 == NONE) {face2-=2; face +=2;}
      arms[face].turn(BOT); arms[face2].turn(TM); 
      delay(TURNDOUBLE);
      tracks[face].slide(OFF); tracks[face2].slide(OFF);
      delay(SLIDEOFF);
      arms[face].turn(TOP); arms[face2].turn(TOP);
      delay(TURNDOUBLE);
      tracks[face].slide(ON); tracks[face2].slide(ON);
      delay(SLIDECOMP);
  }
  else if ((modifier1 == DOUBLE && modifier2 == PRIME)||(modifier1 == PRIME && modifier2 == DOUBLE))  //8
  {
      if (modifier1 == PRIME) {face2-=2; face+=2;}
      arms[face].turn(BOT); tracks[face2].slide(OFF);
      delay(TURNDOUBLE);
      tracks[face].slide(OFF); arms[face2].turn(MID);
      delay(TURN);
      arms[face].turn(TOP); tracks[face2].slide(ON);
      delay(TURNDOUBLE);
      tracks[face].slide(ON); arms[face2].turn(TOP);
      delay(SLIDECOMP);
  }  
}

void faceturn(char face, char modifier)
{
  short turndelay;
  char turnto;
  
  if (modifier == DOUBLE) {turnto = BOT; turndelay = TURNDOUBLE;}
  else {turnto = TM; turndelay = TURN;}
  
  char face1, face2, face3, face4;
  face1 = face;
  face2 = (face + 2)%4;
  face3 = (face1 +1)%4;
  face4 = (face2 +1)%4;  
  
  arms[face1].turn(turnto);
  delay(turndelay);
  tracks[face2].slide(OFF); tracks[face].slide(OFF);
  delay(SLIDECOMP);
  arms[face].turn(TOP); arms[face3].turn(MID); arms[face4].turn(MID);
  delay(turndelay);
  tracks[face2].slide(ON); tracks[face].slide(ON);
  delay(SLIDECOMP);
  tracks[face3].slide(OFF); tracks[face4].slide(OFF);
  delay(SLIDEOFF);
  arms[face3].turn(TOP); arms[face4].turn(TOP);
  delay(TURN);
  tracks[face3].slide(ON); tracks[face4].slide(ON);
  delay(SLIDECOMP);
}

void doublefaceturn(int face, int modifier1, int modifier2)
{
  char nface, nface2;
  char face2 = face+2;
  if (face == B) {nface = R;}
  else if (face == R) {nface = B;}
  nface2 = nface+2;
  
  if (face == B || face == L) {
    if (modifier1 == PRIME) {modifier1 = NONE;}
    else if (modifier1 == NONE) {modifier1 = PRIME;}
  }    
  if (face + 2  == B || face + 2 == L) {
    if (modifier2 == PRIME) {modifier2 = NONE;}
    else if (modifier2 == NONE) {modifier2 = PRIME;}
  }
  if ((modifier1 == NONE && modifier2 == NONE)||(modifier1 == DOUBLE && modifier2 == DOUBLE)) //3
  {
      short turndelay;
      char turnto;
      
      if (modifier1 == NONE) {turnto = TM; turndelay = TURN;}
      else if (modifier1 == DOUBLE) {turnto = BOT; turndelay = TURNDOUBLE;}
      arms[face].turn(turnto); arms[face2].turn(turnto);
      delay(turndelay);
      tracks[face].slide(OFF); tracks[face2].slide(OFF); 
      delay(SLIDECOMP);
      arms[face].turn(TOP); arms[face2].turn(TOP); arms[nface].turn(MID); arms[nface2].turn(MID);
      delay(turndelay);
      tracks[face].slide(ON); tracks[face2].slide(ON);
      delay(SLIDECOMP);
      tracks[nface].slide(OFF); tracks[nface2].slide(OFF);
      delay(SLIDEOFF);
      arms[nface].turn(TOP); arms[nface2].turn(TOP);
      delay(TURN);
      tracks[nface].slide(ON); tracks[nface2].slide(ON);
      delay(SLIDECOMP);
  }
  else if ((modifier1 == DOUBLE && modifier2 == NONE)||(modifier1 == NONE && modifier2 == DOUBLE)) //6
  {
      if (modifier1 == NONE) {face2 -= 2; face +=2;}
      arms[face].turn(BOT); arms[face2].turn(TM); 
      delay(TURNDOUBLE);
      tracks[face].slide(OFF); tracks[face2].slide(OFF);
      delay(SLIDECOMP);
      arms[face].turn(TOP); arms[face2].turn(TOP); arms[nface].turn(MID); arms[nface2].turn(MID);
      delay(TURNDOUBLE);
      tracks[face].slide(ON); tracks[face2].slide(ON);
      delay(SLIDECOMP);
      tracks[nface].slide(OFF); tracks[nface2].slide(OFF);
      delay(SLIDEOFF);
      arms[nface].turn(TOP); arms[nface2].turn(TOP);
      delay(TURN);
      tracks[nface].slide(ON); tracks[nface2].slide(ON);
      delay(SLIDECOMP);
  }
}

void cubeturn(int direc)
{
  boolean base;
  switch(direc){
    case(X): base = 0; break;
    case(Y): base = 1; break;
  }
  tracks[base].slide(OFF); tracks[base+2].slide(OFF);
  delay(SLIDEOFF);
  arms[!base].turn(MID); arms[!base+2].turn(MID);
  delay(TURN);
  tracks[base].slide(ON); tracks[base+2].slide(ON);
  delay(SLIDECOMP);
  tracks[!base].slide(OFF); tracks[!base+2].slide(OFF);
  delay(SLIDEOFF);
  arms[!base].turn(TOP); arms[!base+2].turn(TOP);
  delay(TURN);
  tracks[!base].slide(ON); tracks[!base+2].slide(ON);
  delay(SLIDECOMP);
}
  


