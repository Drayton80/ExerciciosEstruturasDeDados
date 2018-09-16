library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_arith.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;
use STD.TEXTIO.ALL ;

entity testbench_somador_4bits is
	-- no inputs or outputs
end;

architecture sim of testbench_somador_4bits is
	component somador_4bits
		port(c0: in STD_LOGIC;
			  a, b: in STD_LOGIC_VECTOR(3 downto 0);
			  pg, gg: out STD_LOGIC;
			  s: out STD_LOGIC_VECTOR(3 downto 0));
	end component;

signal clk: STD_LOGIC;
signal c0, pg, gg: STD_LOGIC;
signal a, b, s: STD_LOGIC_VECTOR(3 downto 0);
signal pgexpected, ggexpected: STD_LOGIC;
signal sexpected: STD_LOGIC_VECTOR(3 downto 0);
constant MEMSIZE: integer := 32;
type tvarray is array (MEMSIZE downto 0) of STD_LOGIC_VECTOR (14 downto 0);
signal testvectors: tvarray;
shared variable vectornum, errors: integer;

begin
-- instantiate device under test
dut: somador_4bits port map (c0, a, b, pg, gg, s);
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
		for j in 14 downto 0 loop
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
		c0 <= testvectors (vectornum) (14);
		a(3 downto 0)  <= testvectors (vectornum) (13 downto 10);
		b(3 downto 0)  <= testvectors (vectornum) (9  downto 6);
		pgexpected <= testvectors (vectornum) (5);
		ggexpected <= testvectors (vectornum) (4);
		sexpected(3 downto 0)  <= testvectors (vectornum) (3 downto 0);
	end if;
end process;
-- check results on falling edge of clk
process (clk) is
	variable k: integer;
begin
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
			
			for k in 3 downto 0 loop
				assert s(k) = sexpected(k)
					report "Vetor deu erro n. Teste: " &integer'image(vectornum)&
							". Esperado sesp ="& STD_LOGIC'image(sexpected(k))&
							"Valor Obtido: s="& STD_LOGIC'image(s(k));
				
				if (s(k) /= sexpected(k)) then
					errors := errors + 1;
				end if;
			end loop;
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

