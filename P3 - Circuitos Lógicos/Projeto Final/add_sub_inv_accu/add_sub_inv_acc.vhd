library IEEE; 
use IEEE.STD_LOGIC_1164.all;

entity add_sub_inv_acc is
	port(a: in STD_LOGIC_VECTOR(3 downto 0);
		  sel0, sel1, clock: in STD_LOGIC;
		  cout: out STD_LOGIC;
		  s: out STD_LOGIC_VECTOR(3 downto 0));
end;

architecture struct of add_sub_inv_acc is
component somador_4bits
	port(c0: in STD_LOGIC;
		  a, b: in STD_LOGIC_VECTOR(3 downto 0);
		  pg, gg, c4: out STD_LOGIC;
		  s: out STD_LOGIC_VECTOR(3 downto 0));
end component;

component mux2
	port(d0, d1: in STD_LOGIC_VECTOR(3 downto 0);
		  s: in STD_LOGIC; 
		  y: out STD_LOGIC_VECTOR(3 downto 0));
end component;

component inverter
	port(a: in  STD_LOGIC_VECTOR(3 downto 0);
		  y: out STD_LOGIC_VECTOR(3 downto 0));
end component;

component flop
	port(clk: in  STD_LOGIC;
		  d: in  STD_LOGIC_VECTOR(3 downto 0);
		  q: out STD_LOGIC_VECTOR(3 downto 0));
end component;		  

signal ainv, amux0, amux1, yacc: STD_LOGIC_VECTOR(3 downto 0);
signal soma: STD_LOGIC_VECTOR(3 downto 0);
signal pg, gg: STD_LOGIC;

begin
	inv:  inverter port map(a, ainv);
	mux0: mux2 port map(a, ainv, sel0, amux0); 	
	mux1: mux2 port map(amux0, soma, sel1, amux1);	
	somador: somador_4bits port map(sel0, amux0, yacc, pg, gg, cout, soma);
	acc0: flop port map(clock, amux1, yacc);
	s <= amux1;
end;