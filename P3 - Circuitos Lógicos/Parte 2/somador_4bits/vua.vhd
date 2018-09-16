library IEEE; 
use IEEE.STD_LOGIC_1164.all;

entity vua is
	port(c0: in STD_LOGIC;
		  p, g: in STD_LOGIC_VECTOR(3 downto 0);
		  pg, gg: out STD_LOGIC;
		  c: buffer STD_LOGIC_VECTOR(4 downto 1));
end;

architecture synth of vua is 
begin
	pg <= p(0) and p(1) and p(2) and p(3);
	gg <= g(3) or (g(2) and p(3)) or (g(1) and p(3) and p(2))  -- Fórmulas da wikipedia que o professor nos indicou pelo SIGAA
				  or (g(0) and p(3) and p(2) and p(1));
	
	c(1) <= g(0) or (p(0) and c0);
	c(2) <= g(1) or (p(1) and c(1));
	c(3) <= g(2) or (p(2) and c(2));
	c(4) <= g(3) or (p(3) and c(3));
	
	--p <= a xor b;
	--g <= a and b;
	--cout <= g or (p and cin);
end;