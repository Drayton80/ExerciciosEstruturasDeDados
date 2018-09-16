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
signal a, b, cin, s: STD_LOGIC;					-- Definindo signals que correspondem �queles do component que ser� testado
signal sexpected: STD_LOGIC;						-- Valores esperados das sa�das do component, utilizados para checar se h�
															--  erros na RTL Simulation, pois basta comparar as sa�das expected com as
															--	 sa�das reais.
constant MEMSIZE: integer := 8;					-- N�mero de linhas que o test vectors ter� no total

-- Criando um tipo definido como um array que suporta 8 linhas cada uma com um vetor de 5 bits (n�mero de colunas com bits
--  nos vetores de teste), � basicamente um array de 2 dimens�es (2x2), em outras palavras: 
--   tipo nome_do_tipo is array (n�mero de linhas downto 0) of vetor(n�mero de colunas de bits do .tv)																									--
type tvarray is array (MEMSIZE downto 0) of STD_LOGIC_VECTOR (3 downto 0); 

signal testvectors: tvarray;						-- Cria um signal testvector do tipo tvarray criando na linha acima
shared variable vectornum, errors: integer;	-- Cria duas vari�veis compartilhadas, acho que servem como vari�veis globais.

-- A partir daqui come�a a rodar o teste, como um main
begin
-- Instancia um dispositivo com o tipo de component fulladder e nome dut (device under test), basicamente � o dispositivo
--  que ser� testado. Ele recebe os signlas que foram criados anteriormente.
dut: fulladder port map (a, b, cin, s);
-- Gera o tempo de espera para cada transi��o do clock (wait for � o comando para esperar por um determinado tempo).
process begin
	clk <= '1'; wait for 15 ns;  
	clk <= '0'; wait for 10 ns;
end process;
-- at start of test, load vectors
-- and pulse reset
process is
		file tv: TEXT;					-- Cria um arquivo de nome tv e identificado como tipo texto, � o arquivo que receber� a
											--  o local do arquivo real dos test vectors
		variable i, j: integer;		-- Duas vari�veis i e j do tipo integer
		variable L: line;				-- Uma var�vel do tipo line, vai receber provavelmente as linhas do .tv
		variable ch: character;		-- Uma var�vel do tipo character
	begin									-- A seguir ele l� todas as linhas do test vectors, atribuindo o valor 0 a vari�vel i
		i := 0;													-- OBS.: em VHDL := serve para atribui��o de vari�veis, pois tal 
																	--  atribui��o tem efeito imediatamente ap�s a chamada.
																	
		FILE_OPEN (tv, "./example.tv", READ_MODE);	-- Abre o arquivo example.tv em modo de leitura, tv recebe o arquivo.
		while not endfile(tv) loop							-- Um loop while cuja condi��o de parada � o fim do arquivo tv.
			readline (tv, L);									-- L� uma linha do arquivo tv e atribui ela a vari�vel line L.
																	--  Creio que no readline (para que fassa sentido essa l�gica e rode),
																	--  quando o comando � chamado e uma linha � lida, se ele for chamado
																	--  mais uma vez, ele ler� a pr�xima linha e L receber� o valor dela,
																	--  ou seja, a cada chamada de readline(tv, L), ele l� a linha 
																	--  abaixo da anterior lida, come�ando pela primeira de todas.
			for j in 3 downto 0 loop						-- Aqui � criado um loop que l� os 5 bits de cada linha do tv
				
				read (L, ch);									-- Aqui o read l� um caractere da linha da linha L, salva na vari�vel
																	--  ch e, tal qual a l�gico do readline, a cada chamada do read ele l� 
																	--  o caractere e passa para o pr�ximo caractere da sequ�ncia.
																	-- OBS.: em VHDL, = significa compara��o
				if (ch = '_') then							-- Se o caractere ch for igual a "_", ele apenas l� e  
					read (L, ch);								--  passa para o pr�ximo da sequ�ncia.
				end if;
				
				if (ch = '0') then							-- Se ch foi igual a "0", o valor 0 � salvo no array testvectors na
					testvectors (i) (j) <= '0';			--  linha i e na coluna j, formando uma tabela igual a do example.tv
				else
					testvectors (i) (j) <= '1';			-- Se n�o, � salvo o valor 1
				end if;											
			end loop;											-- OBS.: em VHDL, <= � usado como atribui��o de signals, pois tal 
																	--  atribui��o tem efeito apenas no pr�ximo ciclo (delta cycle, eu
																	--  acho que � ciclo de clock, mas n�o tenho certeza).
			i := i + 1;											-- Incrementa o valor de i em 1
		end loop;
		
		vectornum := 0; 					-- Atribui os valores 0 a vari�vel vectornum e errors
		errors := 0;
		wait;									-- wait � um comando de espera incondicional que encerra o processo
end process;

-- Abaixo h� as atribui��es dos signals na subida do clock (valor de clk de 0 para 1)
process (clk) begin											-- OBS.: clk'event and clk='1' produz o mesmoe efeito que rising_edge(clk)
	if (clk'event and clk='1') then						-- A cada subida de clock � atribu�do os valores salvos no array
		a <= testvectors (vectornum) (3);				--  testvectors aos signals do component, incluindo os expected, pois
		b <= testvectors (vectornum) (2);				--  a tabela � constru�da como um modelo de entrada e sa�da correta
		cin <= testvectors (vectornum) (1);
		sexpected <= testvectors (vectornum) (0);
	end if;
end process;

-- Abaixo h� a checagem dos resultados na descida do clock (valor de clk de 1 para 0)
process (clk) begin
	if (clk'event and clk = '0')then
		-- As vezes � necess�rio um loop apenas para evitar de ficar repetindo nomes de signals que s�o iguais e s�
		--  diferem em um n�mero que indica o bit de sa�da.
		--for k in 0 to 1 loop
			-- O assert em VHDL test uma condi��o boolean que, se for falsa, faz com que seja impresso na tela uma
			--  mnesagem contendo o string do report.
			assert s = sexpected	
				report "Vetor deu erro n. Teste: " &integer'image(vectornum)
						&". Esperado sesp ="& STD_LOGIC'image(sexpected)&"Valor Obtido: s="
						& STD_LOGIC'image(s);
			
			-- Abaixo ele incrementa o valor da vari�vel errors se o a sa�da for diferente (/=) do sa�daxpected
			if (s /= sexpected) then
				errors := errors + 1;
			end if;
		--end loop;
		
		-- Ele incrementa o vectornum para que na pr�xima subida do clock seja pego os valores da pr�xima linha
		--  do array bidimensional testvectors, tal subida � representada no processo anterior
		vectornum := vectornum + 1;
		
		-- Abaixo ele checa se houveram erros, se sim ele exibe a mensagem dos erros
		if (is_x (testvectors(vectornum))) then  		-- Eu tentei pesquisar sobre o is_x, a �nica coisa que encontrei sobre
			if (errors = 0) then								--  � que ele apenas retorna true se o valor colocado no parametro for
				report "Just kidding --" &					--  um desses valores indefinidos: 'U', 'X', 'Z', 'W' ou '-'.
				integer'image (vectornum) &				-- Eu descobri, o is_x � usado para finalizar a simuala��o, pois 
				"tests completed successfully."			--  quando as linhas acabam e n�o h� mais nada a ser lido o valor
				severity failure;								--  que come�a a parecer � a alta imped�ncia U, a� o if d� true.
			else													--  Quando se utiliza valores como X, Z, etc nos testvectors,
																	--  � preciso substituir o is_x por vectornum = MEMSIZE, para que 
				report integer'image (vectornum) &		--  a simuala��o n�o acabe parando na primeira linha em que esses 
				"tests completed, errors = " &			--  valores especiais aparecerem
				integer'image (errors)
				severity failure;
			end if;
		end if;
	end if;
	
end process;

end;
