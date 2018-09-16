library IEEE; 
use IEEE.STD_LOGIC_1164.all;

entity fulladder is
	port(a, b, cin : in STD_LOGIC;	
		  p, g, s: buffer STD_LOGIC); 
end;											

architecture synth of fulladder is 
begin
	p <= a xor b;
	g <= a and b;
	--cout <= g or (p and cin);
	s <= p xor cin;
end;