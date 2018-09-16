library IEEE; 
use IEEE.STD_LOGIC_1164.all;

entity somador_4bits is
	port(c0: in STD_LOGIC;
		  a, b: in STD_LOGIC_VECTOR(3 downto 0);
		  pg, gg, c4: out STD_LOGIC;
		  s: out STD_LOGIC_VECTOR(3 downto 0));
end;

architecture struct of somador_4bits is
component fulladder
	port(a, b, cin : in STD_LOGIC;	
		  p, g, s: buffer STD_LOGIC);
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
	adder0: fulladder port map(a(0), b(0),  c0 , p(0), g(0), s(0)); 	-- Como tudo fora de um process funciona concorrentemente
	adder1: fulladder port map(a(1), b(1), c(1), p(1), g(1), s(1));	-- todas essas 5 linhas estão rodando ao mesmo tempo
	adder2: fulladder port map(a(2), b(2), c(2), p(2), g(2), s(2));	-- e não ocorre erros pela falta dos signals c(n) nos 
	adder3: fulladder port map(a(3), b(3), c(3), p(3), g(3), s(3));	-- na entrada do cin dos adders
	vua1:   vua port map(c0, p, g, pg, gg, c);
	c4 <= c(4);
end;