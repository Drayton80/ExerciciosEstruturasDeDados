library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_arith.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;
use STD.TEXTIO.ALL ;

entity testbench_vua is
	-- no inputs or outputs
end;

architecture sim of testbench_vua is
	component vua
		port(c0: in STD_LOGIC;
			  p, g: in STD_LOGIC_VECTOR(3 downto 0);
			  pg, gg: out STD_LOGIC;
			  c: buffer STD_LOGIC_VECTOR(4 downto 1));
	end component;

signal clk: STD_LOGIC;
signal c0, pg, gg: STD_LOGIC;
signal p, g: STD_LOGIC_VECTOR(3 downto 0);
signal c: STD_LOGIC_VECTOR(4 downto 1);
signal pgexpected, ggexpected: STD_LOGIC;
signal cexpected: STD_LOGIC_VECTOR(3 downto 1);
constant MEMSIZE: integer := 32;
type tvarray is array (MEMSIZE downto 0) of STD_LOGIC_VECTOR (13 downto 0);
signal testvectors: tvarray;
shared variable vectornum, errors: integer;

begin
-- instantiate device under test
dut: vua port map (c0, p, g, pg, gg, c);
-- generate clock
process begin
	clk <= '1'; wait for 15 ns;  
	clk <= '0'; wait for 10 ns;
end process;
-- at start of test, load vectors
-- and pulse reset
process is
file tv: TEXT;
variable i, j: integer;
variable L: line;
variable ch: character;
begin
	-- read file of test vectors
	i := 0;
	FILE_OPEN (tv, "./example.tv", READ_MODE);
	while not endfile(tv) loop
		readline (tv, L);
		for j in 13 downto 0 loop
			read (L, ch);
			
			if (ch = '_') then
				read (L, ch);
			end if;
			
			if (ch = '0') then
				testvectors (i) (j) <= '0';			
			else
				testvectors (i) (j) <= '1';
			end if;
			
		end loop;
		i := i + 1;
	end loop;
	vectornum := 0; errors := 0;
	-- reset <= '1'; wait for 27 ns; reset <= '0';
	wait;
end process;
-- apply test vectors on rising edge of clk
process (clk) begin
	if (clk'event and clk='1') then
		c0 <= testvectors (vectornum) (13);
		p(3 downto 0)  <= testvectors (vectornum) (12 downto 9);
		g(3 downto 0)  <= testvectors (vectornum) (8  downto 5);
		pgexpected <= testvectors (vectornum) (4);
		ggexpected <= testvectors (vectornum) (3);
		cexpected(3 downto 1)  <= testvectors (vectornum) (2 downto 0);
	end if;
end process;
-- check results on falling edge of clk
process (clk) begin
	if (clk'event and clk = '0')then
		--for k in 0 to 1 loop
			assert pg = pgexpected
				report "Vetor deu erro n. Teste: " &integer'image(vectornum)&
						 ". Esperado pgesp ="& STD_LOGIC'image(pgexpected)&
						 "Valor Obtido: pg="& STD_LOGIC'image(pg);
			
			if (pg /= pgexpected) then
				errors := errors + 1;
			end if;
			
			assert gg = ggexpected
				report "Vetor deu erro n. Teste: " &integer'image(vectornum)&
						 ". Esperado ggesp ="& STD_LOGIC'image(ggexpected)&
						 "Valor Obtido: gg="& STD_LOGIC'image(gg);
				
			if (gg /= ggexpected) then
				errors := errors + 1;
			end if;
			
			assert c(3) = cexpected(3)
				report "Vetor deu erro n. Teste: " &integer'image(vectornum)&
						 ". Esperado cesp3 ="& STD_LOGIC'image(cexpected(3))&
						 "Valor Obtido: c3="& STD_LOGIC'image(c(3));
				
			if (c(3) /= cexpected(3)) then
				errors := errors + 1;
			end if;
			
			assert c(2) = cexpected(2)
				report "Vetor deu erro n. Teste: " &integer'image(vectornum)&
						 ". Esperado cesp2 ="& STD_LOGIC'image(cexpected(2))&
						 "Valor Obtido: c2="& STD_LOGIC'image(c(2));
				
			if (c(2) /= cexpected(2)) then
				errors := errors + 1;
			end if;
			
			assert c(1) = cexpected(1)
				report "Vetor deu erro n. Teste: " &integer'image(vectornum)&
						 ". Esperado cesp1 ="& STD_LOGIC'image(cexpected(1))&
						 "Valor Obtido: c1="& STD_LOGIC'image(c(1));
			
			if (c(1) /= cexpected(1)) then
				errors := errors + 1;
			end if;
		--end loop;
		
		vectornum := vectornum + 1;
		if (vectornum = MEMSIZE) then
			if (errors = 0) then
				report "Just kidding --" &
				integer'image (vectornum) &
				"tests completed successfully."
				severity failure;
			else
				report integer'image (vectornum) &
				"tests completed, errors = " &
				integer'image (errors)
				severity failure;
			end if;
		end if;
	end if;
	
end process;
end;
