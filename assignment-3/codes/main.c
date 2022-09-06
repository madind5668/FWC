#include <avr/io.h>

int main (void)
{
DDRD=DDRD|(1<<5);
unsigned char x,y,z,f;
while(1)
{
  z=PIND;
  x=0b00000100;
  y=0b00001000;
  x=x&z;
  y=y&z;
  x=x>>2;
  y=y>>3;
  f=(x&y)|(x&~y)|(~x&~y);
  f=f<<5;
  PORTD=f;
}
return 0;
}
