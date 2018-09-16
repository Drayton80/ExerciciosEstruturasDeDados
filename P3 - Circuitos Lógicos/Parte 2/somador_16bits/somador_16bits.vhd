library IEEE; 
use IEEE.STD_LOGIC_1164.all;

entity somador_16bits is
	port(c0: in STD_LOGIC;
		  a, b: in STD_LOGIC_VECTOR(15 downto 0);
		  pg, gg, c16: out STD_LOGIC;
		  s: out STD_LOGIC_VECTOR(15 downto 0));
end;

architecture struct of somador_16bits is
component somador_4bits
	port(c0: in STD_LOGIC;
		  a, b: in STD_LOGIC_VECTOR(3 downto 0);
		  pg, gg: out STD_LOGIC;
		  s: out STD_LOGIC_VECTOR(3 downto 0));
end component;

component vua
	port(c0: in STD_LOGIC;
		  p, g: in STD_LOGIC_VECTOR(3 downto 0);
		  pg, gg: out STD_LOGIC;
		  c: buffer STD_LOGIC_VECTOR(4 downto 1));
end component;

signal p, g: STD_LOGIC_VECTOR(3 downto 0);
signal c: STD_LOGIC_VECTOR(4 downto 1);

begin
	adder_4bits_0: somador_4bits port map(c0  , a(3 downto 0)  , b(3 downto 0)  , p(0), g(0), s(3 downto 0)  ); 	
	adder_4bits_1: somador_4bits port map(c(1), a(7 downto 4)  , b(7 downto 4)  , p(1), g(1), s(7 downto 4)  );	
	adder_4bits_2: somador_4bits port map(c(2), a(11 downto 8) , b(11 downto 8) , p(2), g(2), s(11 downto 8) );
	adder_4bits_3: somador_4bits port map(c(3), a(15 downto 12), b(15 downto 12), p(3), g(3), s(15 downto 12));
	vua1: vua port map(c0, p, g, pg, gg, c);
	c16 <= c(4);
end;