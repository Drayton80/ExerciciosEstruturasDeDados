library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_arith.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;
use STD.TEXTIO.ALL ;

entity testbench_add_sub_inv_acc is
	-- no inputs or outputs
end;

architecture test of testbench_add_sub_inv_acc is
	component add_sub_inv_acc
	port(a: in STD_LOGIC_VECTOR(3 downto 0);
		  sel0, sel1, clock: in STD_LOGIC;
		  cout: out STD_LOGIC;
		  s: out STD_LOGIC_VECTOR(3 downto 0));
	end component;

signal clk, clock: STD_LOGIC;
signal sel0, sel1, cout, coutexpected: STD_LOGIC;
signal a, s, sexpected: STD_LOGIC_VECTOR(3 downto 0);
constant MEMSIZE: integer := 64;
type tvarray is array (MEMSIZE downto 0) of STD_LOGIC_VECTOR (11 downto 0);
signal testvectors: tvarray;
shared variable vectornum, errors: integer;

begin
-- instantiate device under test
dut: add_sub_inv_acc port map (a, sel0, sel1, clock, cout, s);
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
		for j in 11 downto 0 loop
			read (L, ch);
			
			if (ch = '_') then
				read (L, ch);
			end if;
			
			if (ch = '0') then
				testvectors (i) (j) <= '0';
			end if;
			
			if (ch = '1') then
				testvectors (i) (j) <= '1';
			end if;
			
			if (ch = 'U') then
				testvectors (i) (j) <= 'U';
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
		sel0 <= testvectors (vectornum) (11);
		sel1 <= testvectors (vectornum) (10);
		a    <= testvectors (vectornum) (9 downto 6);
		sexpected <= testvectors (vectornum) (5 downto 2);
		coutexpected <= testvectors (vectornum) (1);
		clock        <= testvectors (vectornum) (0);
	end if;
end process;

-- check results on falling edge of clk
process (clk) begin
	if (clk'event and clk = '0')then
		for k in 0 to 3 loop
			if (coutexpected /= 'U') then
				assert (s(k) = sexpected(k))
					report "Vetor deu erro n. Teste: " &integer'image(vectornum)&
							 ". Esperado sesp ="& STD_LOGIC'image(sexpected(k))&
							 "Valor Obtido: s("&integer'image(k)&") ="& STD_LOGIC'image(s(k));
			
				if (s /= sexpected) then
					errors := errors + 1;
				end if;
				
				assert cout = coutexpected
					report "Vetor deu erro n. Teste: " &integer'image(vectornum)& 
							 ". Esperado coutesp ="& STD_LOGIC'image(coutexpected)& 
							 "Valor Obtido: cout="& STD_LOGIC'image(cout);
								 
				if (cout /= coutexpected) then 
					errors := errors + 1;
				end if;
			end if;
		end loop;
		
		vectornum := vectornum + 1;
		-- if (is_x (testvectors(vectornum))) then
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
