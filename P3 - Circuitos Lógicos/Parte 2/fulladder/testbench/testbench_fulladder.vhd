library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_arith.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;
use STD.TEXTIO.ALL ;

entity testbench_fulladder is
	-- no inputs or outputs
end;

architecture sim of testbench_fulladder is
	component fulladder
		port (a, b, cin: in STD_LOGIC;
			   s: out STD_LOGIC);
	end component;

signal clk: STD_LOGIC;
signal a, b, cin, s: STD_LOGIC;					-- Definindo signals que correspondem àqueles do component que será testado
signal sexpected: STD_LOGIC;						-- Valores esperados das saídas do component, utilizados para checar se há
															--  erros na RTL Simulation, pois basta comparar as saídas expected com as
															--	 saídas reais.
constant MEMSIZE: integer := 8;					-- Número de linhas que o test vectors terá no total

-- Criando um tipo definido como um array que suporta 8 linhas cada uma com um vetor de 5 bits (número de colunas com bits
--  nos vetores de teste), é basicamente um array de 2 dimensões (2x2), em outras palavras: 
--   tipo nome_do_tipo is array (número de linhas downto 0) of vetor(número de colunas de bits do .tv)																									--
type tvarray is array (MEMSIZE downto 0) of STD_LOGIC_VECTOR (3 downto 0); 

signal testvectors: tvarray;						-- Cria um signal testvector do tipo tvarray criando na linha acima
shared variable vectornum, errors: integer;	-- Cria duas variáveis compartilhadas, acho que servem como variáveis globais.

-- A partir daqui começa a rodar o teste, como um main
begin
-- Instancia um dispositivo com o tipo de component fulladder e nome dut (device under test), basicamente é o dispositivo
--  que será testado. Ele recebe os signlas que foram criados anteriormente.
dut: fulladder port map (a, b, cin, s);
-- Gera o tempo de espera para cada transição do clock (wait for é o comando para esperar por um determinado tempo).
process begin
	clk <= '1'; wait for 15 ns;  
	clk <= '0'; wait for 10 ns;
end process;
-- at start of test, load vectors
-- and pulse reset
process is
		file tv: TEXT;					-- Cria um arquivo de nome tv e identificado como tipo texto, é o arquivo que receberá a
											--  o local do arquivo real dos test vectors
		variable i, j: integer;		-- Duas variáveis i e j do tipo integer
		variable L: line;				-- Uma varável do tipo line, vai receber provavelmente as linhas do .tv
		variable ch: character;		-- Uma varável do tipo character
	begin									-- A seguir ele lê todas as linhas do test vectors, atribuindo o valor 0 a variável i
		i := 0;													-- OBS.: em VHDL := serve para atribuição de variáveis, pois tal 
																	--  atribuição tem efeito imediatamente após a chamada.
																	
		FILE_OPEN (tv, "./example.tv", READ_MODE);	-- Abre o arquivo example.tv em modo de leitura, tv recebe o arquivo.
		while not endfile(tv) loop							-- Um loop while cuja condição de parada é o fim do arquivo tv.
			readline (tv, L);									-- Lê uma linha do arquivo tv e atribui ela a variável line L.
																	--  Creio que no readline (para que fassa sentido essa lógica e rode),
																	--  quando o comando é chamado e uma linha é lida, se ele for chamado
																	--  mais uma vez, ele lerá a próxima linha e L receberá o valor dela,
																	--  ou seja, a cada chamada de readline(tv, L), ele lê a linha 
																	--  abaixo da anterior lida, começando pela primeira de todas.
			for j in 3 downto 0 loop						-- Aqui é criado um loop que lê os 5 bits de cada linha do tv
				
				read (L, ch);									-- Aqui o read lê um caractere da linha da linha L, salva na variável
																	--  ch e, tal qual a lógico do readline, a cada chamada do read ele lê 
																	--  o caractere e passa para o próximo caractere da sequência.
																	-- OBS.: em VHDL, = significa comparação
				if (ch = '_') then							-- Se o caractere ch for igual a "_", ele apenas lê e  
					read (L, ch);								--  passa para o próximo da sequência.
				end if;
				
				if (ch = '0') then							-- Se ch foi igual a "0", o valor 0 é salvo no array testvectors na
					testvectors (i) (j) <= '0';			--  linha i e na coluna j, formando uma tabela igual a do example.tv
				else
					testvectors (i) (j) <= '1';			-- Se não, é salvo o valor 1
				end if;											
			end loop;											-- OBS.: em VHDL, <= é usado como atribuição de signals, pois tal 
																	--  atribuição tem efeito apenas no próximo ciclo (delta cycle, eu
																	--  acho que é ciclo de clock, mas não tenho certeza).
			i := i + 1;											-- Incrementa o valor de i em 1
		end loop;
		
		vectornum := 0; 					-- Atribui os valores 0 a variável vectornum e errors
		errors := 0;
		wait;									-- wait é um comando de espera incondicional que encerra o processo
end process;

-- Abaixo há as atribuições dos signals na subida do clock (valor de clk de 0 para 1)
process (clk) begin											-- OBS.: clk'event and clk='1' produz o mesmoe efeito que rising_edge(clk)
	if (clk'event and clk='1') then						-- A cada subida de clock é atribuído os valores salvos no array
		a <= testvectors (vectornum) (3);				--  testvectors aos signals do component, incluindo os expected, pois
		b <= testvectors (vectornum) (2);				--  a tabela é construída como um modelo de entrada e saída correta
		cin <= testvectors (vectornum) (1);
		sexpected <= testvectors (vectornum) (0);
	end if;
end process;

-- Abaixo há a checagem dos resultados na descida do clock (valor de clk de 1 para 0)
process (clk) begin
	if (clk'event and clk = '0')then
		-- As vezes é necessário um loop apenas para evitar de ficar repetindo nomes de signals que são iguais e só
		--  diferem em um número que indica o bit de saída.
		--for k in 0 to 1 loop
			-- O assert em VHDL test uma condição boolean que, se for falsa, faz com que seja impresso na tela uma
			--  mnesagem contendo o string do report.
			assert s = sexpected	
				report "Vetor deu erro n. Teste: " &integer'image(vectornum)
						&". Esperado sesp ="& STD_LOGIC'image(sexpected)&"Valor Obtido: s="
						& STD_LOGIC'image(s);
			
			-- Abaixo ele incrementa o valor da variável errors se o a saída for diferente (/=) do saídaxpected
			if (s /= sexpected) then
				errors := errors + 1;
			end if;
		--end loop;
		
		-- Ele incrementa o vectornum para que na próxima subida do clock seja pego os valores da próxima linha
		--  do array bidimensional testvectors, tal subida é representada no processo anterior
		vectornum := vectornum + 1;
		
		-- Abaixo ele checa se houveram erros, se sim ele exibe a mensagem dos erros
		if (is_x (testvectors(vectornum))) then  		-- Eu tentei pesquisar sobre o is_x, a única coisa que encontrei sobre
			if (errors = 0) then								--  é que ele apenas retorna true se o valor colocado no parametro for
				report "Just kidding --" &					--  um desses valores indefinidos: 'U', 'X', 'Z', 'W' ou '-'.
				integer'image (vectornum) &				-- Eu descobri, o is_x é usado para finalizar a simualação, pois 
				"tests completed successfully."			--  quando as linhas acabam e não há mais nada a ser lido o valor
				severity failure;								--  que começa a parecer é a alta impedância U, aí o if dá true.
			else													--  Quando se utiliza valores como X, Z, etc nos testvectors,
																	--  é preciso substituir o is_x por vectornum = MEMSIZE, para que 
				report integer'image (vectornum) &		--  a simualação não acabe parando na primeira linha em que esses 
				"tests completed, errors = " &			--  valores especiais aparecerem
				integer'image (errors)
				severity failure;
			end if;
		end if;
	end if;
	
end process;

end;
